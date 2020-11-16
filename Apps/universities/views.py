from django.shortcuts import render
from .models import University

# Create your views here.

def index(request):
    return render(request, 'universities/index.html', {})

def detail(request, university_id):
    post = get_object_or_404(University, pk=university_id)
    return render(request, 'universities/detail.html', {})

def createUniversity(request):
    if request.user.is_superuser:
        return render(request, 'universities/createUniversity.html', {})
    else:
        return render(request, 'universities/index.html', {})