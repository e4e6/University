from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout as logoutUser, login as loginUser
from django.utils import timezone
from django.views.generic.base import View
from .models import CustomUser, Subscribers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

User = get_user_model()


# NECESSARY FUNCIONS FOR VIEWS

def index(request):
    return render(request, 'users/index.html', {})


def universityList(request):
    return render(request, 'users/universityList.html', {})


def eventList(request):
    return render(request, 'users/eventList.html', {})


def profile(request):
    return render(request, 'users/profile.html', {})


def profileEdit(request):
    return render(request, 'users/profileEdit.html', {})

def sayfasifredegis(request):
    return render(request, 'users/password_change.html', {})


def passwordChangeDone(request):
    return render(request, 'users/password_change_done.html', {})

def kullanicisozlesmesi(request):
    return render(request, 'users/kullanicisozlesmesi.html', {})

def gizliliksozlesmesi(request):
    return render(request, 'users/gizliliksozlesmesi.html', {})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if not email:
            return HttpResponseRedirect(reverse('users:index'))
        return HttpResponseRedirect(reverse(('users:aftersubsribe'), args=(email,)))

def aftersubsribe(request,email):
    subcriber = Subscribers.objects.get_or_create(email=email)
    return render(request, 'users/index.html', {'alert_message': 'Abone olduğunuz için teşekkür ederiz', 'alertColor': 'successfull'})



# NECESSARY FUNCIONS

def login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])


        if user is not None:
            # A backend authenticated the credentials
            loginUser(request, user)
            return render(request, 'users/index.html', {'alert_message': 'Başarılı', 'alertColor': 'successfull'})
            
        else:
            user2 = User.objects.filter(username=request.POST['username'])
            if user2.count == 0:
                return render(request, 'users/index.html', {'alert_message': 'Kullanıcı Adı bulunamadı', 'alertColor': 'dangerr'})
            else:
                if not user2[0].is_active:
                    return render(request, 'users/index.html', {'alert_message': 'Lütfen Aktivasyon mailinden aktif hesabınızı aktif ediniz', 'alertColor': 'dangerr'})
                else:
                    return render(request, 'users/index.html', {'alert_message': 'Kullanıcı adınızla şifreniz uyuşmuyor, Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})


def register(request):
    if request.method == 'POST':
        # try:
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            user = CustomUser.objects.create_user(username, email, password)
            user.is_active = False
            user.save()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('users:activate', kwargs={
                           'uidb64': uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_subject = "hesabınızı aktifleştirin"
            email_body = user.username + '   linke tıklayınız\n' + activate_url
            emailsend = EmailMessage(
                email_subject,
                email_body,
                'portaluniversite@gmail.com',
                [user.email]
            )
            emailsend.send(fail_silently=False)
            return render(request, 'users/index.html', {'alert_message': 'Başarılı, Adresinize Aktivasyon Maili gönderilmiştir', 'alertColor': 'successfull'})
        else:
            return render(request, 'users/index.html', {'alert_message': 'Şifreler Eşleşmedi', 'alertColor': 'dangerr'})
        # except:
        # return render(request, 'users/index.html', {'alert_message': 'Bir sorun ile karşılaşıldı', 'alertColor': 'danger'})
    else:
        return render(request, 'users/index.html', {'alert_message': 'Bir sorun ile karşılaşıldı', 'alertColor': 'dangerr'})


def logout(request):
    logoutUser(request)
    return render(request, 'users/index.html', {'alert_message': 'Başarılı', 'alertColor': 'successfull'})


def password_change(request):
    
    if request.method == 'POST':
        current_user = request.user
        if check_password(request.POST['password'], current_user.password):
            if request.POST['password1'] == request.POST['password2'] :
                current_user.set_password(request.POST['password1'])
                current_user.save()
                update_session_auth_hash(request, current_user)
                #return redirect('user:password_change_done')
                return redirect('users:password_change_done')
            else: return HttpResponse("Yeni Şifreler Eşleşmedi")
        else : return HttpResponse("Şifrenizi Hatalı Girdiniz")
    else: return HttpResponse("İlginç Bir Hata")


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:

            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            #login(request, user)
            messages.success(request, ('hesabınız oluşturuldu'))
            return redirect('users:index')
        else:
            messages.warning(
                request, ('doğrulama linki geçersiz, bir ihtimal daha önce kullanıldı'))
            return redirect('users:index')
