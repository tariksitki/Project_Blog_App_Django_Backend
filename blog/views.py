from django.shortcuts import redirect, render
from .forms import NewPostForm, CategoryForm
from .models import Post, Like, Comment, PostView

# Create your views here.


def postListView(request):
    return render(request, "blog/post_list.html")




def post_List(request):
    print(Like.Post)
    posts = Post.objects.all()
    for post in posts:
        # print(post.id)
        ## Önemli: asagida filter icinde yazdigimiz kriterler, model deki class larin attribute larindan geliyor. Karismasin diye kimini kücük kimini büyük yaptik models de tanimlama yaparken.
        post.likeCount = Like.objects.filter(Post = post.id)
        post.viewCount = PostView.objects.filter(post = post.id)
        post.commentCount = Comment.objects.filter()


    return render(request, "blog/post_list.html") 













def new_post(request):
    formPost = NewPostForm()
    formCategory = CategoryForm()

    if request.method == "POST":
        formPost = NewPostForm(request.POST, request.FILES)
        formCategory = CategoryForm(request.POST)

        if formPost.is_valid() and formCategory.is_valid():
            post = formPost.save(commit=False)
            post.user = request.user
            post.save()
            category = formCategory.save(commit=False)
            category.post = post 
            category.save()

            return redirect("home")

    context = {
        "formPost" : formPost,
        "formCategory" : formCategory
    }
    return render(request, "blog/post_create.html", context)

    ## eger render yazmayi unutursak; su hatayi aliriz:
    # AttributeError 'tuple' object has no attribute 'get'