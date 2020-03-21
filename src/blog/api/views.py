from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerialize


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogPostSerialize(blog_post)
        return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to edit this post"})

    if request.method == 'PUT':
        serializer = BlogPostSerialize(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to delete this post"})

    if request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["falure"] = "delete failed"

        return Response(data=data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_blog_view(request):
    account = request.user
    blog_post = BlogPost(author=account)

    if request.method == "POST":
        serializer = BlogPostSerialize(blog_post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)