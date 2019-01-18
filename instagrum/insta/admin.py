from django.contrib import admin

# Register your models here.
from insta.models import MyUser, Photo

admin.site.register(MyUser)
admin.site.register(Photo)