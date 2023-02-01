from django.shortcuts import render,HttpResponse
from django import forms
from yunfeng.utils.encrypt import md5
from firstapp.models import UserInfo
class LoginForm(forms.Form):
    id = forms.IntegerField(label='学号',widget=forms.TextInput,required=True)
    password = forms.CharField(label='密码',widget=forms.PasswordInput,required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

def login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_object = UserInfo.objects.filter(**form.cleaned_data).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        return HttpResponse("登陆成功")
        request.session["info"] = {'id': user_object.id}
        #return redirect(请假网页)
    return render(request,'login.html',{'form':form})

