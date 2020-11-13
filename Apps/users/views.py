from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, logout as logoutUser, login as loginUser
from django.utils import timezone
from .models import CustomUser

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



# NECESSARY FUNCIONS

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # A backend authenticated the credentials
            loginUser(request, user)
            return render(request, 'users/index.html', {'alert_message': 'Başarılı', 'alertColor': 'successfull'})
        else:
            # No backend authenticated the credentials    
            return render(request, 'users/index.html', {'alert_message': 'Kullanıcı girişi yapılamadı Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})

def register(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password1']
                user = CustomUser.objects.create_user(username, email, password)
                return render(request, 'users/index.html', {'alert_message': 'Başarılı', 'alertColor': 'successfull'})
            else:
                return render(request, 'users/index.html', {'alert_message': 'Şifreler Eşleşmedi', 'alertColor': 'dangerr'})
        except:
            return render(request, 'users/index.html', {'alert_message': 'Bir sorun ile karşılaşıldı', 'alertColor': 'dangerr'})
    else:
        return render(request, 'users/index.html', {'alert_message': 'Bir sorun ile karşılaşıldı', 'alertColor': 'dangerr'})

def logout(request):
    logoutUser(request)
    return render(request, 'users/index.html', {'alert_message': 'Başarılı', 'alertColor': 'successfull'})
    


