from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import *
from .form import ChatMessageCreateForm

@login_required
def chat_view(request):
    chatGroup = get_object_or_404(ChatGroup, group_name="public-chat")
    chatMessages = chatGroup.chat_messages.all()[:30]
    form = ChatMessageCreateForm()
    
    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chatGroup
            message.save()
            #works with htmx
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)
    
    return render(request, 'a_rtchat/chat.html', {'chat_messages' : chatMessages, 'form' : form})
