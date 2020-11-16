from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
#from University import settings 

class HomePageView(TemplateView):
    template_name = 'apptercih/home.html'

def tyt_hesaplama(request):
    eksirayersay = 000
    eksirayersoz = 000
    eksirayerest = 000
    eksirayerdil = 000
    eksirahamsay = 000
    eksirahamsoz = 000
    eksirahamest = 000
    eksirahamdil = 000
    siralamayer = 000
    siralamaham = 000
    turkceDogru = int(request.GET['turkceDogru'])
    turkceYanlis = int(request.GET['turkceYanlis'])
    turkceNet = turkceDogru - (turkceYanlis/4)

    matematikDogru = int(request.GET['matematikDogru'])
    matematikYanlis = int(request.GET['matematikYanlis'])
    matematikNet = matematikDogru - (matematikYanlis/4)

    fenDogru = int(request.GET['fenDogru'])    
    fenYanlis = int(request.GET['fenYanlis'])
    fenNet = fenDogru - (fenYanlis/4)

    sosyalDogru = int(request.GET['sosyalDogru'])
    sosyalYanlis = int(request.GET['sosyalYanlis'])
    sosyalNet = sosyalDogru - (sosyalYanlis/4)

    diplomaPuan = int(request.GET['diplomaPuan'])
    if 'gecensene' in request.GET:
        diplomaPuan=diplomaPuan/2

    # TYT için net başına puan tablosu
    # türkçe=3.24  temel matematik=3.34  fen=3.41  sosyal=3.66

    # SAY için net başına puan tablosu
    # türkçe=1.38  sosyal=1.56  temel matematik=1.43  fen=1.46  matematik=2.71  fizik=3.15  kimya=2.77  biyoloji=3.31

    # EA için net başına puan tablosu
    # türkçe=1.38  sosyal=1.55  temel matematik=1.42  fen=1.45  matematik=2.69  edebiyat=3.18  tarih1=3.54  coğrafya1=2.96

    # SÖZ için net başına puan tablosu
    # türkçe=1.35  sosyal=1.53  temel matematik=1.40  fen=1.42  edebiyat=3.12  tarih1=3.48  coğrafya1=2.91  tarih2=3.70  coğrafya2=2.60  felsefe=3.22  din=3.94

    # DİL için net başına puan tablosu
    # türkçe=1.57  sosyal=1.77  temel matematik=1.62  fen=1.65  dil=2.62

    # Örneğin 2020 SAY puanı şöyle hesaplanıyor:
    # Türkçe neti: TR, Sosyal Bilimler neti: SB, Temel Matematik neti: TM, Fen Bilimleri neti FB, Matematik neti M, Fizik neti F, Kimya neti K ve Biyoloji neti B olsun. Not ortalamanız da N olsun.
    # Y-SAY puanı = 99.135 + TR*1.38 + SB*1.56 + TM*1.43 + FB*1.46 + M*2.71 + F*3.15 + K*2.77 + B*3.31 + N*0,6
    basepuan=100
    puanham = (turkceNet*3.24)+(matematikNet*3.34)+(sosyalNet*3.66)+(fenNet*3.41)+basepuan
    puanyer = (turkceNet*3.24)+(matematikNet*3.34)+(sosyalNet*3.66)+(fenNet*3.41)+basepuan+(diplomaPuan*0.6)

    ekmatematikDogru = int(request.GET['ekmatematikDogru'])
    ekmatematikYanlis = int(request.GET['ekmatematikYanlis'])
    ekmatematikNet = ekmatematikDogru - (ekmatematikYanlis/4)

    ekfizikDogru = int(request.GET['ekfizikDogru'])
    ekfizikYanlis = int(request.GET['ekfizikYanlis'])
    ekfizikNet = ekfizikDogru - (ekfizikYanlis/4)

    ekkimyaDogru = int(request.GET['ekkimyaDogru'])
    ekkimyaYanlis = int(request.GET['ekkimyaYanlis'])
    ekkimyaNet = ekkimyaDogru - (ekkimyaYanlis/4)

    ekbiyolojiDogru = int(request.GET['ekbiyolojiDogru'])
    ekbiyolojiYanlis = int(request.GET['ekbiyolojiYanlis'])
    ekbiyolojiNet = ekbiyolojiDogru - (ekbiyolojiYanlis/4)

    ektarih1Dogru = int(request.GET['ektarih1Dogru'])
    ektarih1Yanlis = int(request.GET['ektarih1Yanlis'])
    ektarih1Net = ektarih1Dogru - (ektarih1Yanlis/4)

    ektarih2Dogru = int(request.GET['ektarih2Dogru'])
    ektarih2Yanlis = int(request.GET['ektarih2Yanlis'])
    ektarih2Net = ektarih2Dogru - (ektarih2Yanlis/4)

    ekcografya1Dogru = int(request.GET['ekcografya1Dogru'])
    ekcografya1Yanlis = int(request.GET['ekcografya1Yanlis'])
    ekcografya1Net = ekcografya1Dogru - (ekcografya1Yanlis/4)

    ekcografya2Dogru = int(request.GET['ekcografya2Dogru'])
    ekcografya2Yanlis = int(request.GET['ekcografya2Yanlis'])
    ekcografya2Net = ekcografya2Dogru - (ekcografya2Yanlis/4)

    ekedebiyatDogru = int(request.GET['ekedebiyatDogru'])
    ekedebiyatYanlis = int(request.GET['ekedebiyatYanlis'])
    ekedebiyatNet = ekedebiyatDogru - (ekedebiyatYanlis/4)

    ekfelsefeDogru = int(request.GET['ekfelsefeDogru'])
    ekfelsefeYanlis = int(request.GET['ekfelsefeYanlis'])
    ekfelsefeNet = ekfelsefeDogru - (ekfelsefeYanlis/4)

    ekdinDogru = int(request.GET['ekdinDogru'])
    ekdinYanlis = int(request.GET['ekdinYanlis'])
    ekdinNet = ekdinDogru - (ekdinYanlis/4)

    ekdilDogru = int(request.GET['ekdilDogru'])
    ekdilYanlis = int(request.GET['ekdilYanlis'])
    ekdilNet = ekdilDogru - (ekdilYanlis/4)


    
    

    # SÖZ için net başına puan tablosu
    # türkçe=1.35  sosyal=1.53  temel matematik=1.40  fen=1.42  edebiyat=3.12  tarih1=3.48  coğrafya1=2.91  tarih2=3.70  coğrafya2=2.60  felsefe=3.22  din=3.94



    ekpuanhamsay = basepuan+(turkceNet*1.38)+(sosyalNet*1.56)+(matematikNet*1.43)+(fenNet*1.46)+(ekmatematikNet*2.71)+(ekfizikNet*3.15)+(ekkimyaNet*2.77)+(ekbiyolojiNet*3.31)
    ekpuanhamsoz = basepuan+(turkceNet*1.35)+(sosyalNet*1.53)+(matematikNet*1.40)+(fenNet*1.42)+(ekedebiyatNet*3.12)+(ektarih1Net*3.48)+(ekcografya1Net*2.91)+(ektarih2Net*3.70)+(ekcografya2Net*2.60)+(ekfelsefeNet*3.22)+(ekdinNet*3.94)
    ekpuanhamest = basepuan+(sosyalNet*1.55)+(matematikNet*1.42)+(fenNet*1.45)+(ekmatematikNet*2.69)+(ekedebiyatNet*3.18)+(ektarih1Net*3.54)+(ekcografya1Net*2.96)
    ekpuanhamdil = basepuan+(sosyalNet*1.77)+(matematikNet*1.62)+(fenNet*1.65)+(ekdilNet*2.62)

    ekpuanyersay = ekpuanhamsay+(diplomaPuan*0.6)
    ekpuanyersoz = ekpuanhamsoz+(diplomaPuan*0.6)
    ekpuanyerest = ekpuanhamest+(diplomaPuan*0.6)
    ekpuanyerdil = ekpuanhamdil+(diplomaPuan*0.6)

    #tyt yer
    if puanyer>=550:
        siralamayer = 48
    elif puanyer >=530:
        siralamayer =1080
    elif puanyer >=510:
        siralamayer =4.961
    elif puanyer >=490:
        siralamayer =13.501
    elif puanyer >=470:
        siralamayer =26.999
    elif puanyer >=450:
        siralamayer =45.824
    elif puanyer >=430:
        siralamayer =69.646
    elif puanyer >=410:
        siralamayer =98.777
    elif puanyer >=390:
        siralamayer =	134.509
    elif puanyer >=370:
        siralamayer =179.581
    elif puanyer >=350:
        siralamayer =	237.601
    elif puanyer >=330:
        siralamayer =313.204
    elif puanyer >=310:
        siralamayer =413.458
    elif puanyer >=290:
        siralamayer =546.557
    elif puanyer >=270:
        siralamayer =	716.747
    elif puanyer >=250:
        siralamayer =	927.745
    elif puanyer >=230:
        siralamayer =1168283
    elif puanyer >=210:
        siralamayer =1436803
    elif puanyer >=200:
        siralamayer =1579449
    elif puanyer >=190:
        siralamayer =1699953
    elif puanyer >=170:
        siralamayer =1744928
    elif puanyer >=150:
        siralamayer =1745642

    #ekpuanyersay
    if ekpuanyersay>=550:
        eksirayersay = 150
    elif ekpuanyersay>=530:
        eksirayersay = 2846
    elif ekpuanyersay>=510:
        eksirayersay =10041
    elif ekpuanyersay>=490:
        eksirayersay =22390
    elif ekpuanyersay>=470:
        eksirayersay =37753
    elif ekpuanyersay>=450:
        eksirayersay =54534
    elif ekpuanyersay>=430:
        eksirayersay =72022
    elif ekpuanyersay>=410:
        eksirayersay =90140
    elif ekpuanyersay>=390:
        eksirayersay =109784
    elif ekpuanyersay>=370:
        eksirayersay =132428
    elif ekpuanyersay>=350:
        eksirayersay =158867
    elif ekpuanyersay>=330:
        eksirayersay =191150
    elif ekpuanyersay>=310:
        eksirayersay =230935
    elif ekpuanyersay>=290:
        eksirayersay =280599
    elif ekpuanyersay>=270:
        eksirayersay =342911
    elif ekpuanyersay>=250:
        eksirayersay =425444
    elif ekpuanyersay>=230:
        eksirayersay =538156
    elif ekpuanyersay>=210:
        eksirayersay =674050
    elif ekpuanyersay>=200:
        eksirayersay =817297
    elif ekpuanyersay>=190:
        eksirayersay =693077
    elif ekpuanyersay>=170:
        eksirayersay =693440
    elif ekpuanyersay>=150:
        eksirayersay =693440
    #söz yer
    if ekpuanyersoz>=550:
        eksirayersoz = 3
    elif ekpuanyersoz >=530:
        eksirayersoz =	29
    elif ekpuanyersoz >=510:
        eksirayersoz =	129
    elif ekpuanyersoz >=490:
        eksirayersoz =	351
    elif ekpuanyersoz >=470:
        eksirayersoz =	836
    elif ekpuanyersoz >=450:
        eksirayersoz =	1.688
    elif ekpuanyersoz >=430:
        eksirayersoz =	3.638
    elif ekpuanyersoz >=410:
        eksirayersoz =8.231
    elif ekpuanyersoz >=390:
        eksirayersoz =18.042
    elif ekpuanyersoz >=370:
        eksirayersoz =	35.288
    elif ekpuanyersoz >=350:
        eksirayersoz =64.314
    elif ekpuanyersoz >=330:
        eksirayersoz =109.421
    elif ekpuanyersoz >=310:
        eksirayersoz =	174.253
    elif ekpuanyersoz >=290:
        eksirayersoz =262.049
    elif ekpuanyersoz >=270:
        eksirayersoz =	372.563
    elif ekpuanyersoz >=250:
        eksirayersoz =503.926
    elif ekpuanyersoz >=230:
        eksirayersoz =	652.878
    elif ekpuanyersoz >=210:
        eksirayersoz=801.073
    elif ekpuanyersoz >=200:
        eksirayersoz =685.546
    elif ekpuanyersoz >=190:
        eksirayersoz =822.997
    elif ekpuanyersoz >=170:
        eksirayersoz =	823.330
    elif ekpuanyersoz >=150:
        eksirayersoz =823.330
    #esit yer
    if ekpuanyerest>=550:
        eksirayerest = 8
    elif ekpuanyerest >=530:
        eksirayerest =	102
    elif ekpuanyerest >=510:
        eksirayerest =	502
    elif ekpuanyerest >=490:
        eksirayerest =	1.332
    elif ekpuanyerest >=470:
        eksirayerest =3.125
    elif ekpuanyerest >=450:
        eksirayerest =6.368
    elif ekpuanyerest >=430:
        eksirayerest =12.290
    elif ekpuanyerest >=410:
        eksirayerest =	25.140
    elif ekpuanyerest >=390:
        eksirayerest =	50.772
    elif ekpuanyerest >=370:
        eksirayerest =87.912
    elif ekpuanyerest >=350:
        eksirayerest =132.507
    elif ekpuanyerest >=330:
        eksirayerest =185.942
    elif ekpuanyerest >=310:
        eksirayerest =	252.245
    elif ekpuanyerest >=290:
        eksirayerest =	336.637
    elif ekpuanyerest >=270:
        eksirayerest =	444.848
    elif ekpuanyerest >=250:
        eksirayerest =583.745
    elif ekpuanyerest >=230:
        eksirayerest =	761.769
    elif ekpuanyerest >=210:
        eksirayerest=	965.534
    elif ekpuanyerest >=200:
        eksirayerest =988.437
    elif ekpuanyerest >=190:
        eksirayerest =998.592
    elif ekpuanyerest >=170:
        eksirayerest =999.313
    elif ekpuanyerest >=150:
        eksirayerest =999.313
    #dil yer
    if ekpuanyerdil>=550:
        eksirayerdil = 21
    elif ekpuanyerdil >=530:
        eksirayerdil =	304
    elif ekpuanyerdil >=510:
        eksirayerdil =963
    elif ekpuanyerdil >=490:
        eksirayerdil =2.070
    elif ekpuanyerdil>=470:
        eksirayerdil =3.538
    elif ekpuanyerdil >=450:
        eksirayerdil =5.665
    elif ekpuanyerdil >=430:
        eksirayerdil =8.789
    elif ekpuanyerdil >=410:
        eksirayerdil =13.127
    elif ekpuanyerdil >=390:
        eksirayerdil =18.451
    elif ekpuanyerdil >=370:
        eksirayerdil =24.154
    elif ekpuanyerdil >=350:
        eksirayerdil =30.095
    elif ekpuanyerdil >=330:
        eksirayerdil =36.236
    elif ekpuanyerdil >=310:
        eksirayerdil =42.437
    elif ekpuanyerdil >=290:
        eksirayerdil =49.087
    elif ekpuanyerdil >=270:
        eksirayerdil =55.841
    elif ekpuanyerdil >=250:
        eksirayerdil =63.168
    elif ekpuanyerdil >=230:
        eksirayerdil =70.904
    elif ekpuanyerdil >=210:
        eksirayerdil =	77.905
    elif ekpuanyerdil >=200:
        eksirayerdil =	78.623
    elif ekpuanyerdil >=190:
        eksirayerdil =	78.952
    elif ekpuanyerdil >=170:
        eksirayerdil =	78.966
    elif ekpuanyerdil >=150:
        eksirayerdil =78.966
      #tyt ham
    if puanham>=500:
        siralamaham =5
    elif puanham>=480:
        siralamaham =	529
    elif puanham>=460:
        siralamaham =3.744
    elif puanham>=440:
        siralamaham =	11.156
    elif puanham>=420:
        siralamaham =	23.900
    elif puanham>=400:
        siralamaham =	42.803
    elif puanham>=380:
        siralamaham =	67.019
    elif puanham>=360:
        siralamaham =	96.901
    elif puanham>=340:
        siralamaham =133.808
    elif puanham>=320:
        siralamaham =181.329
    elif puanham>=300:
        siralamaham =	243.743
    elif puanham>=280:
        siralamaham =327.314
    elif puanham>=260:
        siralamaham =	442.153
    elif puanham>=240:
        siralamaham =598.087
    elif puanham>=220:
        siralamaham =797.757
    elif puanham>=200:
        siralamaham =	1042710
    elif puanham>=180:
        siralamaham =	1297656
    elif puanham>=170:
        siralamaham =1441671
    elif puanham>=150:
        siralamaham =	1745642
    elif puanham>=100:
        siralamaham =	2257671
    # say ham
    if ekpuanhamsay>=500:
        eksirahamsay=	3
    elif ekpuanhamsay>=480:
        eksirahamsay =	1.300
    elif ekpuanhamsay>=460:
        eksirahamsay =	7.126
    elif ekpuanhamsay>=440:
        eksirahamsay =18.811
    elif ekpuanhamsay>=420:
        eksirahamsay =	34.222
    elif ekpuanhamsay>=400:
        eksirahamsay =	51.511
    elif ekpuanhamsay>=380:
        eksirahamsay =	69.707
    elif ekpuanhamsay>=360:
        eksirahamsay =	88.287
    elif ekpuanhamsay>=340:
        eksirahamsay =108.399
    elif ekpuanhamsay>=320:
        eksirahamsay =	131.552
    elif ekpuanhamsay>=300:
        eksirahamsay =158.821
    elif ekpuanhamsay>=280:
        eksirahamsay =	192.294
    elif ekpuanhamsay>=260:
        eksirahamsay =233.910
    elif ekpuanhamsay>=240:
        eksirahamsay =	286.770
    elif ekpuanhamsay>=220:
        eksirahamsay =354.646
    elif ekpuanhamsay>=200:
        eksirahamsay =446.152
    elif ekpuanhamsay>=180:
        eksirahamsay =575.546
    elif ekpuanhamsay>=170:
        eksirahamsay =693.440
    elif ekpuanhamsay>=150:
        eksirahamsay =1006874
    elif ekpuanhamsay>=100:
        eksirahamsay =	1183249
    #soz ham
    if ekpuanhamsoz>=500:
        eksirahamsoz =	1
    elif ekpuanhamsoz>=480:
        eksirahamsoz =	30
    elif ekpuanhamsoz>=460:
        eksirahamsoz =	130
    elif ekpuanhamsoz>=440:
        eksirahamsoz =403
    elif ekpuanhamsoz>=420:
        eksirahamsoz =	829
    elif ekpuanhamsoz>=400:
        eksirahamsoz =	1.655
    elif ekpuanhamsoz>=380:
        eksirahamsoz =	3.732
    elif ekpuanhamsoz>=360:
        eksirahamsoz =	8.900
    elif ekpuanhamsoz>=340:
        eksirahamsoz =19.834
    elif ekpuanhamsoz>=320:
        eksirahamsoz =39.525
    elif ekpuanhamsoz>=300:
        eksirahamsoz =	72.187
    elif ekpuanhamsoz>=280:
        eksirahamsoz =	123.232
    elif ekpuanhamsoz>=260:
        eksirahamsoz =196.923
    elif ekpuanhamsoz>=240:
        eksirahamsoz =	296.595
    elif ekpuanhamsoz>=220:
        eksirahamsoz =420.915
    elif ekpuanhamsoz>=200:
        eksirahamsoz =565.738
    elif ekpuanhamsoz>=180:
        eksirahamsoz =720.759
    elif ekpuanhamsoz>=170:
        eksirahamsoz =	823.330
    elif ekpuanhamsoz>=150:
        eksirahamsoz =962.208
    elif ekpuanhamsoz>=100:
        eksirahamsoz =	991.718
    # est ham
    if ekpuanhamest>=500:
        eksirahamest =1
    elif ekpuanhamest>=480:
        eksirahamest =	67
    elif ekpuanhamest>=460:
        eksirahamest =	391
    elif ekpuanhamest>=440:
        eksirahamest =	1.148
    elif ekpuanhamest>=420:
        eksirahamest =	2.786
    elif ekpuanhamest>=400:
        eksirahamest =5.870
    elif ekpuanhamest>=380:
        eksirahamest =11.468
    elif ekpuanhamest>=360:
        eksirahamest =22.132
    elif ekpuanhamest>=340:
        eksirahamest =45.970
    elif ekpuanhamest>=320:
        eksirahamest =	83.986
    elif ekpuanhamest>=300:
        eksirahamest =	131.386
    elif ekpuanhamest>=280:
        eksirahamest =188.362
    elif ekpuanhamest>=260:
        eksirahamest =260.663
    elif ekpuanhamest>=240:
        eksirahamest =	354.428
    elif ekpuanhamest>=220:
        eksirahamest =477.282
    elif ekpuanhamest>=200:
        eksirahamest =637.942
    elif ekpuanhamest>=180:
        eksirahamest =842.438
    elif ekpuanhamest>=170:
        eksirahamest =999.313
    elif ekpuanhamest>=150:
        eksirahamest =1289718
    elif ekpuanhamest>=100:
        eksirahamest =	1364125
    #dil ham
    if ekpuanhamdil>=500:
        eksirahamdil =	5
    elif ekpuanhamdil>=480:
        eksirahamdil =	260
    elif ekpuanhamdil>=460:
        eksirahamdil =	941
    elif ekpuanhamdil>=440:
        eksirahamdil =	1.893
    elif ekpuanhamdil>=420:
        eksirahamdil =	3.289
    elif ekpuanhamdil>=400:
        eksirahamdil =	5.437
    elif ekpuanhamdil>=380:
        eksirahamdil =8.794
    elif ekpuanhamdil>=360:
        eksirahamdil =	13.558
    elif ekpuanhamdil>=340:
        eksirahamdil =19.313
    elif ekpuanhamdil>=320:
        eksirahamdil =25.321
    elif ekpuanhamdil>=300:
        eksirahamdil =	31.558
    elif ekpuanhamdil>=280:
        eksirahamdil =37.814
    elif ekpuanhamdil>=260:
        eksirahamdil =	44.214
    elif ekpuanhamdil>=240:
        eksirahamdil =	51.014
    elif ekpuanhamdil>=220:
        eksirahamdil =	58.205
    elif ekpuanhamdil>=200:
        eksirahamdil =66.022
    elif ekpuanhamdil>=180:
        eksirahamdil =	74.302
    elif ekpuanhamdil>=170:
        eksirahamdil =78.966
    elif ekpuanhamdil>=150:
        eksirahamdil =	87.206
    elif ekpuanhamdil>=100:
        eksirahamdil =	91.469
 

        





   

    return render (request,"apptercih/home.html",{'turkceNet':turkceNet,'matematikNet':matematikNet,'sosyalNet':sosyalNet,'fenNet':fenNet,
    'turkceDogru':turkceDogru,'turkceYanlis':turkceYanlis,'matematikDogru':matematikDogru,'matematikYanlis':matematikYanlis,'fenDogru':fenDogru,'fenYanlis':fenYanlis,
    'sosyalDogru':sosyalDogru,'sosyalYanlis':sosyalYanlis,'puanham':puanham,'puanyer':puanyer,'diplomaPuan':diplomaPuan,

    'ekmatematikDogru':ekmatematikDogru,'ekmatematikYanlis':ekmatematikYanlis,'ekmatematikNet':ekmatematikNet,
    'ekfizikDogru':ekfizikDogru,'ekfizikYanlis':ekfizikYanlis,'ekfizikNet':ekfizikNet,
    'ekkimyaDogru':ekkimyaDogru,'ekkimyaYanlis':ekkimyaYanlis,'ekkimyaNet':ekkimyaNet,
    'ekbiyolojiDogru':ekbiyolojiDogru,'ekbiyolojiYanlis':ekbiyolojiYanlis,'ekbiyolojiNet':ekbiyolojiNet,
    'ektarih1Dogru':ektarih1Dogru,'ektarih1Yanlis':ektarih1Yanlis,'ektarih1Net':ektarih1Net,
    'ektarih2Dogru':ektarih2Dogru,'ektarih2Yanlis':ektarih2Yanlis,'ektarih2Net':ektarih2Net,
    'ekcografya1Dogru':ekcografya1Dogru,'ekcografya1Yanlis':ekcografya1Yanlis,'ekcografya1Net':ekcografya1Net,
    'ekcografya2Dogru':ekcografya2Dogru,'ekcografya2Yanlis':ekcografya2Yanlis,'ekcografya2Net':ekcografya2Net,      
    'ekedebiyatDogru':ekedebiyatDogru,'ekedebiyatYanlis':ekedebiyatYanlis,'ekedebiyatNet':ekedebiyatNet,  
    'ekfelsefeDogru':ekfelsefeDogru,'ekfelsefeYanlis':ekfelsefeYanlis,'ekfelsefeNet':ekfelsefeNet,  
    'ekdinDogru':ekdinDogru,'ekdinYanlis':ekdinYanlis,'ekdinNet':ekdinNet,  
    'ekdilDogru':ekdilDogru,'ekdilYanlis':ekdilYanlis,'ekdilNet':ekdilNet,
    'ekpuanhamsay':ekpuanhamsay,'ekpuanhamsoz':ekpuanhamsoz,'ekpuanhamest':ekpuanhamest,'ekpuanhamdil':ekpuanhamdil,
    'ekpuanyersay':ekpuanyersay,'ekpuanyersoz':ekpuanyersoz,'ekpuanyerest':ekpuanyerest,'ekpuanyerdil':ekpuanyerdil,
    'eksirahamsay':eksirahamsay,'eksirahamsoz':eksirahamsoz,'eksirahamest':eksirahamest,'eksirahamdil':eksirahamdil,
    'eksirayersay':eksirayersay,'eksirayersoz':eksirayersoz,'eksirayerest':eksirayerest,'eksirayerdil':eksirayerdil,
    'siralamayer':siralamayer,'siralamaham':siralamaham,
    
    })
