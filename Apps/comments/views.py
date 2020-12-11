from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20]})


def createpost(request):
    if request.method == 'POST':
        textField = request.POST['textField']
        created_time = timezone.now()
        is_edited = False
        likes = 0
        newPost = Post(text=textField, created_time=created_time, is_edited=is_edited, likes=likes, owner=request.user)
        newPost.save()
        return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
    return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Yeni Bir Blog Oluşturulamadı Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
    
    
def deletepost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if(post.owner.id == request.user.id):
        try:
            postText = post.text
            post.delete()
            return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
        except:
            return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Bloğunuz silinemedi Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
    else:
        return render(request, 'comments/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Sadece kendi blogunuzu silebilirsiniz', 'alertColor': 'dangerr'})


def editpost(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        dataList = request.body.decode('utf-8').split('&')
        post_id= 0
        post_text= ""
        for item in dataList:
            value = item.split('=')
            if(value[0] == 'post_id'):
                post_id = value[1]
            elif(value[0] == 'post_text'):
                post_text = value[1]
            else:
                continue

        post = get_object_or_404(Post, pk=post_id)
        if(post.owner.id == request.user.id):
            post.text = post_text
            post.save()
            return JsonResponse({'alert_message': 'Başarılı', 'alertColor': 'successfull'}, status = 200)
        else:
            return JsonResponse({'alert_message': 'Sizin bu blogu silmeye yetkiniz yok', 'alertColor': 'dangerr'}, status = 400)

    return JsonResponse({'alert_message': 'Bir hata ile karşılaşıldı', 'alertColor': 'dangerr'}, status = 400)







    
