from django.shortcuts import redirect, render,get_object_or_404
from.models import *
from django.contrib.auth.decorators import login_required
from .form import *
# Create your views here.
@login_required
def chat_view(request):
    chatGroup=get_object_or_404(ChatGroup,group_name='public-chat')
    chatMessages=chatGroup.chat_messages.all()[:30]
    form=ChatMessageCreateForm()
    # with htmx
    if request.htmx:
        form=ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.author=request.user
            message.group=chatGroup
            message.save()
            # return redirect('home')
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)
        
    return render(request , 'a_rtchat/chat.html' , {"chatMessages" : chatMessages,"form" : form})