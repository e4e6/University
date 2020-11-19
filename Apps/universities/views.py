from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import University

# Create your views here.

def index(request):
    universities = University.objects.all()
    return render(request, 'universities/index.html', {'universities': universities})

def detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    return render(request, 'universities/detail.html', {'university' : university})

def createUniversity(request):
    if request.user.is_superuser:
        return render(request, 'universities/createUniversity.html', {})
    else:
        return render(request, 'universities/index.html', {})


