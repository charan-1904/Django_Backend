# from django.db import models
# from accounts.models import CustomUser
# import uuid

# class BaseModel(models.Model):
#     uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
#     created_at = models.DateField(auto_now_add=True)
#     # updated_at = models.DateField(auto_now_add=True)

#     class Meta:
#         abstract = True


# class Tag(models.Model):
#     name = models.TextField(max_length=255)

# class Blog(BaseModel):


#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
#     title = models.CharField(max_length=500)
#     blog_text = models.TextField()
#     main_image = models.ImageField(upload_to="blogs")
#     tags = models.TextField.ManyToManyField(Tag)

#     def __str__(self):
#         return self.title
from django.db import models
from accounts.models import CustomUser
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)  # Change this line to use DateTimeField

    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.TextField(max_length=255)


class Comment(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    # parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"
    



class Reply(BaseModel):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  

    text = models.TextField()

    def __str__(self):
        return f"Reply to {self.comment} - {self.text[:20]}"

class Blog(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.TextField(null = True)
    upload_image = models.ImageField(upload_to="blogs", null=True, blank=True)
    # video = models.FileField(upload_to="blogs", null=True, blank=True)
    tags = models.TextField(max_length=255)
    comments = models.ManyToManyField(Comment, related_name='blog_comments', blank=True)
    # votes = models.IntegerField(null = True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


