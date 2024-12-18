from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Signup

# Create your views here.


class About(View):
    def get(self, request):
        return render(request, 'about/about.html')

    def post(self, request):
        email = request.POST.get('email')
        about.save()
        return render(request, 'about/signup_success.html')
