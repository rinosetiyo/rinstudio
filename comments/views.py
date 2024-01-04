from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blogApp.models import Post
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.
# def comment_post(request):
#     if request.POST:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             post = request.POST['post_id']
#             comment.post = post
#             form.save()
#     else:
#         form = CommentForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'posts/single-post.html', context)