from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Lisans42020,OnLisans2020
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'apptercihrobotu/home.html'

class LisansListView(ListView):
    model = Lisans42020
    paginate_by = 50
    template_name = 'apptercihrobotu/home.html'
    puandegeri= 1.111
    ordering = ['-EnKucukPuan']
    #Lisans42020.objects.filter().order_by('-EnKucukPuan')    #enkücük puanın clasını belirtmedim ?
    #Lisans42020.objects.filter(puandegeri > Lisans42020.EnKucukPuan).order_by('-EnKucukPuan')    #enkücük puanın clasını belirtmedim ?

class OnLisansListView(ListView):
    model = OnLisans2020
    paginate_by = 50
    template_name = 'apptercihrobotu/home.html'
    puandegeri= 1.111
    ordering = ['-EnKucukPuan']

# def secim(LisansTuru,PuanTuru,Puangirisi):
#     if(LisansTuru==2):
#         onlisanslist=OnLisansListView.objects.all()
#         onlisanslist=onlisanslist.filter(PuanTuru__exac=TYT)
#         context={object_list:onlisanslist}
#         return render()

#         #Onlisanslistview cagır

#     else if (LisansTuru==3):
#         if Puanturu==1:
#             PuanTuru="SAY"
#         else if Puanturu==2:
#             PuanTuru="SOZ"
#         else if Puanturu==3:
#             PuanTuru="EA"
#         else if Puanturu==4:
#             PuanTuru="DİL"
#         #lisanslistviewcagır
#         pass
#     #else alert secim yapmadınız uyarısı



# def index(request):
#     return render(request, 'users/index.html', {})

# def searchuni(request):
#     if request.is_ajax and  request.method == 'POST':
#         university = request.POST['university']
#         bolum = request.POST['bolum']
#         data = serializers.serialize('json', OnLisans2020.objects.all())

#         return JsonResponse({'onnn':data,}, status=200)
#     return JsonResponse({}, status=400)

def alanAzaltma(request):
    
    if request.method == 'POST':
        LisansTuru = request.POST['LisansTuru']
        PuanTuru = request.POST['PuanTuru']
        PuanGirisi =request.POST['PuanGirisi']
        #print("postları aldı",LisansTuru, PuanTuru, PuanGirisi)

    #print("if ööncesi koşu")
    if(LisansTuru=='2'):
        #print("lisansturu2 onay")
        onlisanslist=OnLisans2020.objects.all()
        onlisanslist=onlisanslist.filter(PuanTuru__exact='TYT').filter(EnKucukPuan__lte=PuanGirisi).order_by('-EnKucukPuan')
        context={'object_list':onlisanslist}
        template_name = 'apptercihrobotu/home.html'
        return render(request,template_name,context)

    elif (LisansTuru=='3'):
        #print("lisansturu3 onay")
        #print(PuanTuru)
        # if PuanTuru=='1':
        #     PuanTuru="SAY"
        #     print(PuanTuru)
        # elif PuanTuru=='2':
        #     PuanTuru="SOZ"
        # elif PuanTuru=='3':
        #     PuanTuru="EA"
        # elif PuanTuru=='4':
        #     PuanTuru="DİL"
        #lisanslistviewcagır
        #print("lisansturu4 onay")
        lisanslist=Lisans42020.objects.all()
        lisanslist=lisanslist.filter(PuanTuru__exact=PuanTuru).filter(EnKucukPuan__lte=PuanGirisi).order_by('-EnKucukPuan')
        context={'object_list':lisanslist}
        template_name = 'apptercihrobotu/home.html'
        return render(request,template_name,context)
        
    #else alert secim yapmadınız uyarısı

    return HttpResponse("İlginç Bir Hata")       

        #return HttpResponseRedirect(reverse(('apptercihrobotu:home_tercihrobotu'), args=(LisansTuru,PuanTuru,PuanGirisi)))