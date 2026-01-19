from django.shortcuts import render, get_object_or_404, redirect
from .models import GroupMessage, ChatGroup
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageCreateForm


@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="Public Chat")
    chat_messages =  chat_group.chat_messages.all()[:30]
    form = ChatMessageCreateForm()
        
    if request.method == 'POST':
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            if request.htmx:
                return render(request, 'chat/partials/message.html', {'message': message})
            return redirect('home_chat')


    return render(request, 'chat/chat.html', {'chat_messages': chat_messages, 'form': form})