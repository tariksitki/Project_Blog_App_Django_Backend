from django.shortcuts import render

# Create your views here.


def postListView(request):
    return render(request, "blog/post_list.html")