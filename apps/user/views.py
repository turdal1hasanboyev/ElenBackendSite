from django.shortcuts import render

from .models import User


def about(request):
    user = User.objects.get(id=1)

    return render(request, 'about.html', {"user": user})
