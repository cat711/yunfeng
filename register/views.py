from django.shortcuts import render
from firstapp.models import UserInfo, YunDingInfo
from django import forms
from django.contrib import messages

# 邀请码
CODE = '1111'
# 邀请码长度
CODE_LEN = 4


# Create your views here.

##注册表单
class RegisterForm(forms.Form):
    # ID
    user_id = forms.CharField(min_length=10, required=True)
    # 邀请码
    invitation_code = forms.CharField(min_length=CODE_LEN, max_length=CODE_LEN, required=True)
    # 用户名
    user_name = forms.CharField(min_length=2, required=True)
    # 方向
    direction = forms.CharField(min_length=2, required=True)
    # 期数
    phase_num = forms.CharField(min_length=2, required=True)
    # 密码
    password = forms.CharField(min_length=6, max_length=12, required=True)
    # 重复密码
    confirm_password = forms.CharField(min_length=6, max_length=12, required=True)


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', context={'form': form})

    if request.method == 'POST':
        # 使用自定义注册表单
        form = RegisterForm(request.POST)

        # 判断表单验证是否通过
        if form.is_valid():
            user_id = form.cleaned_data.get('user_id')
            invitation_code = form.cleaned_data.get('invitation_code')
            user_name = form.cleaned_data.get('user_name')
            direction = form.cleaned_data.get('direction')
            phase_num = form.cleaned_data.get('phase_num')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            """
            判断是否在云顶书院
            测试时将其注释掉
            """
            if not YunDingInfo.objects.filter(id=user_id, user_name=user_name).first():
                messages.error(request, '你未在云顶书院！')
                return render(request, 'register.html', context={'form': form})

            # 判断邀请码是否正确
            if invitation_code != CODE:
                messages.error(request, '邀请码错误！')
                return render(request, 'register.html', context={'form': form})

            # 判断学号ID是否重复或不满足条件
            if UserInfo.objects.filter(id=user_id).first():
                messages.error(request, '学号重复！')
                return render(request, 'register.html', context={'form': form})
            if len(user_id) != 10:
                messages.error(request, '学号为10位数字！')
                return render(request, 'register.html', context={'form': form})

            UserInfo.objects.create(id=user_id, user_name=user_name, phase_num=phase_num, direction=direction,
                                    password=password)
            return render(request, 'index.html')
        else:
            return render(request, 'register.html', context={'form': form})
