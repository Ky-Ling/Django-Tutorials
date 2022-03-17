from django.contrib import admin

from .models import Meetup


# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    # Control how our meetups should be presented in the admin area and how they should behave here
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Meetup, MeetupAdmin) 

