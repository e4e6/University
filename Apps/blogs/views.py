from django.shortcuts import get_object_or_404, render
from .models import Post
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20]})


def createpost(request):

    if request.method == 'POST':
        textField = request.POST['textField']
        created_time = timezone.now()
        is_edited = False
        likes = 0
        newPost = Post(text=textField, created_time=created_time, is_edited=is_edited, likes=likes, owner=request.user)
        newPost.save()
        return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
    return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Yeni Bir Blog Oluşturulamadı Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})
    
def deletepost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    try:
        postText = post.text
        post.delete()
        return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Başarılı', 'alertColor': 'successfull'})
    except:
        return render(request, 'blogs/index.html', {'postList': Post.objects.order_by('-created_time')[:20], 'alert_message': 'Bloğunuz silinemedi Lütfen Tekrar deneyin', 'alertColor': 'dangerr'})

