from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from blog.models import Blog , Reaction
from blog.serializers.serializers import BlogSerializer , ReactionSerializers

@api_view(["GET"])
def get_blogs(request):
    if request.method =="GET":
        blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    else:
        return Response({"response":"NOT FOUND"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","POST","PUT","DELETE"])
def blog_manage(request):

    if request.method == "GET":
        search_blog = request.GET.get("title")
        if not search_blog:
            return Response({"response":"Parâmetro 'title' não fornecido"}, status=status.HTTP_400_BAD_REQUEST)
        blogs = Blog.objects.filter(title=search_blog)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"BLOG CREATED SUCCESS"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        blog_id = request.data.get("id")
        try:
            update_blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"response":"Blog não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(update_blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response":"UPDATE BLOG SUCCESS"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        blog_id = request.data.get("id")
        try:
            delete_blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({"response":"Blog não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        delete_blog.delete()
        return Response({"response":"DELETE BLOG SUCCESS"}, status=status.HTTP_200_OK)


@api_view(["GET","POST","PUT","DELETE"])
def reactios_manage(request,blog_id):

    if request.method == "GET":
        reactions = Reaction.objects.filter(blog_id=blog_id)
        serializer = ReactionSerializers(reactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method =="POST":

        blog = Blog.objects.get(id=blog_id)

        try:
            reaction = request.data.get("text_reaction")
                        
            data ={
                "blog_id":blog_id,
                "reaction":reaction
            }

            serializer = ReactionSerializers(data=data)

            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Blog.DoesNotExist:
            return Response({"resquet":"NOT FOUND"},status=status.HTTP_400_BAD_REQUEST)
        
