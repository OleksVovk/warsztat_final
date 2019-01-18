from django.shortcuts import render

# Create your views here.
from django.views import View

from insta.models import Photo


def css(tab):
    return ["css/"+css_name+".css" for css_name in tab]


class MainPageView(View):

    def get(self, request):
        styles_tab = ["css_style", ]
        return render(request, "main.html", {"styles": css(styles_tab)})


class ShowImageView(View):
    def get(self,request):
        img = Photo.objects.all()
        for image in img:
            print(image.path)
        return render(request, "images_view.html", {"imgs": img})
