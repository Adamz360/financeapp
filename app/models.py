from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Delete")
)

# creating the model class
class posts(models.Model):
    title = models.CharField(max_length=200, unique="True")
    slug = models.SlugField(max_length=200, unique=True )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField()
    content = models.TextField()
    metatades = models.CharField(max_length=300, default="Insight")
    status = models.IntegerField(choices=STATUS, default=0)
    post_images=models.ImageField(upload_to="images")

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title
