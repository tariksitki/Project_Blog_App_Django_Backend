
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image = models.ImageField(upload_to = "blog_pics", default = "blog_pics/default.png")
#     publish_date = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#     STATUS_CHOICES = (
#         ("1", "published"),
#         ("2", "draft"),
#         ("3", "pending")
#     )

#     status = models.CharField(max_length=50, choices=STATUS_CHOICES)
#     slug = models.SlugField(null=False, unique=True)
#     user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     # likes = models.ManyToManyField(User, related_name="likes")

#     def __str__(self):
#         return self.title

#     ## ana sayfada contentin bir kismini görüntülemek icin:
#     def contentShortener(self):
#         if len(self.content) > 100:
#             return self.content[:100] + "..."
#         else:
#             return self.content

#     # reverse()¶
#     # If you need to use something similar to the url template tag in your code, Django provides the following function:

#     # reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)¶
#     # viewname can be a URL pattern name or the callable view object.

#     ## id yerine slug ile cagirma
#     def get_absolute_url(self):
#         return reverse("post_detail", kwargs={"slug" : self.slug})

#     ## slug olusturma:
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title) + str(uuid.uuid4()) ## uuid import
#         return super().save(*args, **kwargs)


        

class Post(models.Model):
    STATUS = (
        ("Published", "Published"),
        ("Draft", "Draft"),
        ("Pending", "Pending")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.CharField(max_length=200, default='https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS, max_length=10, default="Draft")
    def __str__(self):
        return self.title 





class Category(models.Model):
    CHOICES = (
        ("FullStack", "FullStack"),
        ("FrontEnd", "FrontEnd"),
        ("BackEnd", "BackEnd")
    )

    category = models.CharField(choices=CHOICES, max_length=10, default="BackEnd")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f"[ {self.category} ] POST TITLE => {self.post.title}"
        # bunun nasil göründügüne admin panelden bakabiliriz.






class Like(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"[ {self.User} ] POST TITLE => {self.Post.title}"







class Comment(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title








class PostView(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f" [ {self.timeStamp} ] POST TITLE { self.post.title }"







