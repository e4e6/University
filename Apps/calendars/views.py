from django.shortcuts import get_object_or_404, render
from .models import Event
from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers
from Apps.universities.models import University
# Create your views here.

def index(request):
    return render(request, 'calendars/index.html', {})

def getEvents(request):
    if request.is_ajax and request.method == "GET":
        month = request.GET["month"]
        year = request.GET["year"]
        universityid = request.GET["university"]
        eventList = Event.objects.filter(Q(startDate__year=year, startDate__month=month) | Q(endDate__year=year, endDate__month=month))

        if universityid != "0":
            eventList = eventList.filter(university__id = universityid)

        data = serializers.serialize('json', eventList, use_natural_foreign_keys=True)

        return JsonResponse({'eventList': data}, status = 200)
    else:
        return JsonResponse({}, status = 400)


def createevent(request, university_id):
    if request.method == 'POST':
        eventName = request.POST['eventName']
        eventColor = request.POST['eventColor']
        eventStartDate = request.POST['eventStartDate']
        eventEndDate = request.POST['eventEndDate']
        university = University.objects.get(pk=university_id)
        newEvent = Event(name=eventName,text=eventName, color=eventColor, startDate=eventStartDate, endDate=eventEndDate, university=university)
        newEvent.save()
        return render(request, 'universities/detail.html', {'university' : university, 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
        # return render(request, 'universities/detail.html', {'university' : university})
    return render(request, 'universities/detail.html', {'university' : university, 'alert_message': 'Yeni Bir Event Oluşturulamadı Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
    
