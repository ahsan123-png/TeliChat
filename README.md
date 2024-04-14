HTNL Folder stucture
a_user
      |-templates
                |-a_user
                        |-profile.html
                        |-profile_delete.html
                        |-profile_eidt.html
                        |-profile_settings.html
a_home
a_rtchat
        |-templates
                  |-a_rtchat
                            |-chat_message.html
                            |-chat.html
                            |-partial
                                    |-chat_message_p.html
telicat
media
static
template
        |-base.html
        |-home.html
        |-allauth
                |-layout
                        |- base.html
        |-includes
                  |- header.html
                  |- message.html
        |-layouts
                |- blank.html
                |-box.html
        |-partials
                  |- email_form.html
        
  CODE EXPLAINATIONS APPS WISE
  a_user app
  view.py
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import *
from .form import ChatMessageCreateForm

@login_required
def chat_view(request):

This section imports necessary modules and decorators, such as render, get_object_or_404, and login_required. It also imports models and forms specific to your application.

chatGroup = get_object_or_404(ChatGroup, group_name="public-chat")
chatMessages = chatGroup.chat_messages.all()[:30]
form = ChatMessageCreateForm()

Here, you're retrieving a chat group named "public-chat" and fetching its latest 30 chat messages. Additionally, you're initializing a form for creating new chat messages.

  if request.htmx:
      form = ChatMessageCreateForm(request.POST)
      if form.is_valid:
This part checks if the request is made using htmx. If so, it populates the form with POST data and validates it.

  message = form.save(commit=False)
  message.author = request.user
  message.group = chatGroup
  message.save()
When the form is valid, it saves the new chat message. The message is associated with the current user (author) and the chat group it belongs to.

context = {
    'message' : message,
    'user' : request.user
}
return render(request, 'a_rtchat/partials/chat_message_p.html', context)
This part prepares a context containing the newly created message and the current user. It then renders a partial template (chat_message_p.html) with this context.

return render(request, 'a_rtchat/chat.html', {'chat_messages' : chatMessages, 'form' : form})
Finally, this line renders the main chat page (chat.html) with the fetched chat messages and the chat message creation form.
========================================================================================================================================
Signals.py

from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.models import EmailAddress

@receiver(post_save, sender=User)       
def user_postsave(sender, instance, created, **kwargs):
"This part sets up signals for handling user creation and updating."


user = instance

# add profile if user is created
if created:
    Profile.objects.create(
        user = user,
    )
else:
If a new user is created, a corresponding profile object is created. Otherwise, if the user is being updated, the signal checks for changes in email addresses.

# update allauth emailaddress if exists 
try:
    email_address = EmailAddress.objects.get_primary(user)
    if email_address.email != user.email:
        email_address.email = user.email
        email_address.verified = False
        email_address.save()
except:

This block updates the associated email address if it exists and if it has been changed.

  # if allauth emailaddress doesn't exist create one
  EmailAddress.objects.create(
      user = user,
      email = user.email, 
      primary = True,
      verified = False
            )
If there's no associated email address (likely during initial creation), a new EmailAddress instance is created for the user.
============================================================================================================================
*models.py
















