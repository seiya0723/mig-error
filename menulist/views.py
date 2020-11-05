from django.shortcuts import render

from django.views import View
from .models import Menu

class MenuView(View):

    def get(self, request, *args, **kwargs):

        data    = Menu.objects.order_by("category")
        context = { "data":data }

        return render(request,"menulist/index.html",context)

index   = MenuView.as_view()
