from django.shortcuts import render


def handler404(request, exception):
    """ Page Not Found """
    return render(request, "404.html")


def handler500(request):
    """ Internal Server Error """
    return render(request, "500.html")
       