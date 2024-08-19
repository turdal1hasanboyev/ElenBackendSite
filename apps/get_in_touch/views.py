from django.shortcuts import render, redirect

from .models import GetInTouch


def get_in_touch(request):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        GetInTouch.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        return redirect(url)
    
    return render(request, 'contact.html')
    