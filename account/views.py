from django.shortcuts import render
from .models import UserProfile
from .forms import UserForm, UserProfileForm, RegistrationForm
from django.http import HttpResponse


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            try:
                user.save()
            except Exception as e:
                print(str(e))
                return HttpResponse('<h1>对不起，注册失败。</h1>')
            else:
                return HttpResponse('<h1>恭喜，注册成功。点击<a href="/account/login/">这里</a>登陆。</h1>')
