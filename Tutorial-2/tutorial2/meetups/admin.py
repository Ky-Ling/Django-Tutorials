from django.contrib import admin

from .models import Meetup, Location, Participant


# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    # Control how our meetups should be presented in the admin area and how they should behave here
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Meetup, MeetupAdmin) 
admin.site.register(Location)
admin.site.register(Participant)

