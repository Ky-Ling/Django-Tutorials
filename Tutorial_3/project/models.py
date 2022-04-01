from django.db import models
import uuid


# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=200)

    # null is for database, blank is for Django
    description = models.TextField(null=True, blank=True)

    # featured_image = 
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    
    tags = models.ManyToManyField("Tag", blank=True )

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


    def __str__(self):
        return self.title



class Review(models.Model):

    VOTE_TYPE = (
        ("up", "up"),
        ("down", "down")
    )

    # on_delete = models.SET_NULL: when the parent object is deleted, the review will stay here it won't have a parent
    #   anymore.
    # 
    # on_delete = models.CASCADE:  When the project is deleted, all the reviews will be deleted too.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    
    def __str__(self) -> str:
        return self.value





class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name
