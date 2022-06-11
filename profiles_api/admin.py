from django.contrib import admin
from profiles_api.models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class ProfileApiAdmin(admin.ModelAdmin):
  pass
