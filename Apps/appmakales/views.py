from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Makale
from django.contrib.auth import get_user_model
User = get_user_model()
#from .models import Post

# Create your views here.


# def makale_home(request):
#     return render(request, 'appmakales/makale_home.html', {'postList': Post.objects.order_by('-created_time')[:20]})


# def create_makale(request):

#     if request.method == 'POST':
#         textField = request.POST['textField']
#         created_time = timezone.now()
#         is_edited = False
#         likes = 0
#         newMakale = Post(text=textField, created_time=created_time, is_edited=is_edited, likes=likes, owner=request.user)
#         newMakale.save()
#         return render(request, 'appmakales/makale_home.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
#     return render(request, 'appmakales/makale_home.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Yeni Bir Blog Oluşturulamadı Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
    
    
# def deletepost(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)

#     if(post.owner.id == request.user.id):
#         try:
#             postText = post.text
#             post.delete()
#             return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
#         except:
#             return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Bloğunuz silinemedi Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
#     else:
#         return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Sadece kendi blogunuzu silebilirsiniz', 'alertColor': 'dangerr'})


# def editpost(request):
#     # request should be ajax and method should be POST.
#     if request.is_ajax and request.method == "POST":
#         dataList = request.body.decode('utf-8').split('&')
#         post_id= 0
#         post_text= ""
#         for item in dataList:
#             value = item.split('=')
#             if(value[0] == 'post_id'):
#                 post_id = value[1]
#             elif(value[0] == 'post_text'):
#                 post_text = value[1]
#             else:
#                 continue

#         post = get_object_or_404(Post, pk=post_id)
#         if(post.owner.id == request.user.id):
#             post.text = post_text
#             post.save()
#             return JsonResponse({'alert_message': 'Başarılı', 'alertColor': 'successfull'}, status = 200)
#         else:
#             return JsonResponse({'alert_message': 'Sizin bu blogu silmeye yetkiniz yok', 'alertColor': 'dangerr'}, status = 400)

#     return JsonResponse({'alert_message': 'Bir hata ile karşılaşıldı', 'alertColor': 'dangerr'}, status = 400)




################


class MakaleListView(ListView):
    model = Makale
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    #queryset = Post.objects.order_by('-created_on')

    template_name = 'appmakales/makale_home.html'

class MakaleDetailView(DetailView):
    model = Makale
    template_name = 'appmakales/makale_detail.html'

class MakaleCreateView(CreateView): # new
    model = Makale
    template_name = 'appmakales/makale_new.html'
    fields = ['title', 'body']
    #Makale.author = User
    #fields = ['title', 'author', 'body']
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)

class MakaleUpdateView(UpdateView): # new
    model = Makale
    template_name = 'appmakales/makale_edit.html'
    fields = ['title', 'body']  

class MakaleDeleteView(DeleteView): # new
    model = Makale
    template_name = 'appmakales/makale_delete.html'
    success_url = reverse_lazy('appmakales:makale_home')