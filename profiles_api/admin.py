from django.contrib import admin
from profiles_api import models
# Register your models here.

@admin.register(models.UserProfile)
class ProfileApiAdmin(admin.ModelAdmin):
  pass
@admin.register(models.ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
  pass
