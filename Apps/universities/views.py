from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import University, Faculty, Department
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
import json
from django.db.models import Q

# Create your views here.

def index(request):
    universities = University.objects.all()
    # universities = University.objects.filter(~Q(city=''))
    universitiesForMap = serializers.serialize('json', universities)
    return render(request, 'universities/index.html', {'universities': universities, 'universitiesForMap': universitiesForMap, 'refreshMap': True})

def searchUniversityPage(request, searchText, searchCity):

    universities = University.objects.filter(name__contains=searchText)
    print(searchCity)
    if(searchCity != 'cityNull'):
        print('geldi')
        universities = universities.filter(city__iexact = searchCity)
    universitiesForMap = serializers.serialize('json', universities)
    
    return render(request, 'universities/index.html', {'universities': universities, 'universitiesForMap': universitiesForMap, 'refreshMap': False})

def searchUniversity(request):
    if request.method == 'POST':
        searchText = request.POST['searchText']
        searchCity = request.POST['city']

        if not searchText:
            return HttpResponseRedirect(reverse('universities:index'))
        return HttpResponseRedirect(reverse('universities:searchUniversityPage', args=(searchText, searchCity,)))

def detail(request, university_id):
    university = get_object_or_404(University, pk=university_id)
    return render(request, 'universities/detail.html', {'university' : university})


def editUniversity(request):
    if request.is_ajax and request.method == "POST":
        university_id = request.POST['id']
        lat = request.POST['lat']
        lng = request.POST['lng']
        text = request.POST['text']
        university = get_object_or_404(University, pk=university_id)
        university.mapShortDesc = text
        university.lat = lat
        university.lng = lng
        university.save()

        return JsonResponse({}, status = 200)
    else:
        return JsonResponse({}, status = 400)

def createUniversity(request):
    if request.user.is_superuser:
        return render(request, 'universities/createUniversity.html', {})
    else:
        return render(request, 'universities/index.html', {})

def submitcreateUniversity(request):
    if request.is_ajax and request.method == "POST":
        university_name = request.POST['university_name']
        short_description = request.POST['short_description']
        long_description = request.POST['long_description']
        student_count = request.POST['student_count']
        inter_student_count = request.POST['inter_student_count']
        uni_type = request.POST['uni_type']

        profil_photo = request.FILES['profil_photo']
        cover_photo = request.FILES['cover_photo']
        website = request.POST['website']
        instagram = request.POST['instagram']
        facebook = request.POST['facebook']
        linkedin = request.POST['linkedin']
        twitter = request.POST['twitter']
        pinterest = request.POST['pinterest']

        faculties = request.POST['faculties']
        departmentsJson = request.POST['departments']
        departments = json.loads(departmentsJson)

        createdFacultiesForthisSession = {}

        for department in departments:
            newDepartment = Department(name=department['department_name'], puanType=department['department_type'], minimumPuan=department['department_point'], minimumRanking=department['department_rank'])
            newDepartment.save()

            faculty_nameStr = department['faculty_name']

            if(faculty_nameStr not in createdFacultiesForthisSession.keys()):
                print("geldi1", faculty_nameStr)
                newFaculty = Faculty(name=faculty_nameStr)
                newFaculty.save()
                newFaculty.departmentList.add(newDepartment)
                createdFacultiesForthisSession[faculty_nameStr] = newFaculty.id
            else:
                print("geldi2", faculty_nameStr)
                existinFaculty = Faculty.objects.get(pk=createdFacultiesForthisSession[faculty_nameStr])
                existinFaculty.departmentList.add(newDepartment)
                existinFaculty.save()

        newUniversity = University(name=university_name, info=short_description, detailedInfo=long_description, numberOfLocalStudents=student_count, numberOfForeignStudents=inter_student_count,
        universityType=uni_type, website_link=website, instagram_link=instagram, facebook_link=facebook, linkedin_link=linkedin, twitter_link=twitter, pinterest_link=pinterest)
        newUniversity.save()
        
        newUniversity.profile_photo = profil_photo
        newUniversity.cover_photo = cover_photo
        newUniversity.save()

        print(createdFacultiesForthisSession)
        for value in createdFacultiesForthisSession.values():
            newUniversity.facultyList.add(Faculty.objects.get(pk=value))


    #     return HttpResponseRedirect(reverse('universities:aftercreateUniversity'))
    # return HttpResponseRedirect(reverse(('users:index')))
        context = {'alert_message': 'Üniversite Başarılı Bir Şekilde Oluşturuldu'}
        return JsonResponse(context)

    context = {'alert_message': 'Hata'}
    return JsonResponse(context)
    # return HttpResponse('None')

# def aftercreateUniversity(request):
#     print("geldi")
#     return render(request, 'users/index.html', {'alert_message': 'Üniversite Başarılı Bir Şekilde Oluşturuldu', 'alertColor': 'successfull'})



