from django.shortcuts import render


def home(request):
    return render(request, 'cabinet/vacancy-list.html')
