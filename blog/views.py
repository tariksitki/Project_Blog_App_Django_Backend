from django.shortcuts import redirect, render
from .forms import NewPostForm, CategoryForm
from .models import Post, Like, Comment, PostView, Category

# Create your views here.


def postListView(request):
    return render(request, "blog/post_list.html")




def post_List(request):
    posts = Post.objects.all()
    # print(posts)
    for post in posts:
        # print(post.id)
        ## Önemli: asagida filter icinde yazdigimiz kriterler, model deki class larin attribute larindan geliyor. Karismasin diye kimini kücük kimini büyük yaptik models de tanimlama yaparken.
        post.likeCount = Like.objects.filter(Post = post.id).count()
        post.viewCount = PostView.objects.filter(post = post.id).count()
        post.commentCount = Comment.objects.filter(post_id = post.id).count()
        # Note: Burada olusturdugumuz 3 degisken db de olusmaz. Bunlar sadece fonksiyonel olarak kullanilirlar.
        
    context = {
        "posts" : posts
    }

    return render(request, "blog/post_list.html", context) 













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







## Önemli: post_update  func icerisine gelen id;  urls.py da belirlemis oldugumuz url den gelir. orada <int:id> seklinde buraya id göndermesi yapariz. request in post oldugunu ise template deki form un methodundan belirliyoruz.

def post_update(request, id):
    post = Post.objects.get(id = id)
    postCategory = Category.objects.get(post = post)
    formPost = NewPostForm(instance=post)
    formCategory = CategoryForm(instance=postCategory)

    if request.method == "POST":
        formPost = NewPostForm(request.POST, request.FILES, instance=post)
        formCategory = CategoryForm(request.POST, instance=postCategory)

        if formPost.is_valid() and formCategory.is_valid():
            formPost.save()
            formCategory.save()
            return redirect("home")

    context = {
        "formPost" : formPost,
        "formCategory" : formCategory
    }

    return render(request, "blog/post_update.html", context)











def post_delete(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        post.delete()
        return redirect("home")

    context = {
        "post" : post
    }

    return render(request, "blog/post_delete.html", context)
