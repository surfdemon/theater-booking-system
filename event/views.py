from django.shortcuts import render
from django.views import View

# Create your views here.


class EventHome(View):
    def get(self, request):
        return render(request, 'event/home.html')