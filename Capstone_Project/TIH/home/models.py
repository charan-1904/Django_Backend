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

class Blog(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to="blogs")
    tags = models.TextField(max_length=255)

    def __str__(self):
        return self.title
