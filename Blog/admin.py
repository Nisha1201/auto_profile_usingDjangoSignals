from django.contrib import admin
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
     list_display=("id","image","place","user","father_name","mother_name","city","dob")
# admin.site.register(Profile,ProfileAdmin)


# Register your models here.

