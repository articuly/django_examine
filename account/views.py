from django.shortcuts import render
from .models import UserProfile
from .forms import UserForm, UserProfileForm, RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required


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
                return JsonResponse({'result': 'fail'})
            else:
                return JsonResponse({'result': 'success'})


@login_required
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofile') else UserProfile.objects.create(
        user=request.user)
    return render(request, 'account/myself.html', {'userprofile': userprofile})


@login_required
def myself_edit(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user,
                                                                        'userprofile') else UserProfile.objects.create(
        user=request.user)
    print(userprofile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if form.is_valid() * user_form.is_valid():
            form_cd = form.cleaned_data
            user_cd = user_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.phone = form_cd['phone']
            userprofile.company = form_cd['company']
            userprofile.job = form_cd['job']
            userprofile.intro = form_cd['intro']
            try:
                request.user.save()
                userprofile.save()
            except Exception as e:
                print(str(e))
                return HttpResponse('个人信息修改失败')
            else:
                return HttpResponseRedirect('/account/myself/')
        else:
            return HttpResponse('个人信息验证不通过')
    else:
        user_form = UserForm(instance=request.user)
        form = UserProfileForm(
            initial={'phone': userprofile.phone, 'company': userprofile.company, 'job': userprofile.job,
                     'intro': userprofile.intro})
        return render(request, 'account/myself_edit.html', {'form': form, 'user_form': user_form})


@login_required
def my_image(request):
    if request.method == 'POST':
        img = request.POST['img']
        userprofile = UserProfile.objects.get(user=request.user)
        userprofile.photo = img
        try:
            userprofile.save()
        except Exception as e:
            print(str(e))
            return JsonResponse({'result': str(e)})
        else:
            return JsonResponse({'result': 'success'})
    return render(request, 'account/imagecrop.html')
