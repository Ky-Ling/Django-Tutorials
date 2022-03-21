from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)


    def __str__(self) -> str:
        return f"{self.name} ({self.address})"


class Participant(models.Model):
    email = models.EmailField(unique=True)


    def __str__(self) -> str:
        return self.email



# One location can belong to many meetups but one meetup can only have one location.
# One meetup can have multiple participants, and one participant can have multiple meetups

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)


    def __str__(self) -> str:
        return f'{self.title} - {self.slug}'
