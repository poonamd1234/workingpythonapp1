from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Chat
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from cryptography.fernet import Fernet

key = '84mZqDjCLLFHzTcSBITkW3Ut3NB-GWp0qmUhQNt6mXs='

f = Fernet(key)

encrypted_data = b'gAAAAABlvJekXsimw1sgMoLuR962cFIf7iXA208ZjaCS9xMcVnl3963FAc4Jz0H5ZaaetEF44ADGKdFznq-OcsIAAfvVwBD4vmKFDsR9Ygovh8mHUKnls2pi6wqHPSNxzo-pDMojw4w5oHpdNamCXXFaUHx1hprz7g=='

decrypted_data = f.decrypt(encrypted_data)


openai.api_key = decrypted_data.decode()

def ask_openai(message):
    reponse = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content": "You are a helpful assistant"},
            {"role": "user", "content":message},
        ]
    )
    answer = reponse.choices[0].message.content.strip()
    return answer

# Create your views here.
@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)
    if request.method == 'POST':
        message = request.POST.get('message')
        reponse = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=reponse, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message':message, 'response':reponse})
    return render(request, 'chatbot.html', {'chats': chats})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid Username or Password'
            return render(request, 'login.html', {'error_message':error_message})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_msg = 'Error in Creating Account'
                return render (request, 'register.html', {'error_message': error_msg})
        else:
            error_msg = 'Password don\'t match'
            return render (request, 'register.html', {'error_message': error_msg})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect ('custom_login')



