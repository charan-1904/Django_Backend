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
    created_at = models.DateField(auto_now_add=True)

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
    text = models.TextField()

    def __str__(self):
        return f"Reply to {self.comment} - {self.text[:20]}"

class Blog(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to="blogs")
    tags = models.TextField(max_length=255)
    comments = models.ManyToManyField(Comment, related_name='blog_comments', blank=True)


    def __str__(self):
        return self.title


