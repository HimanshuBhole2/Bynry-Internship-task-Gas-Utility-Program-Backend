from django.shortcuts import render
from django.shortcuts import render, redirect


def main_home(request):
    return redirect("/services/")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)