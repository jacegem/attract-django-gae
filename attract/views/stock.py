from django.http import HttpResponse
from django.shortcuts import render


def chart(request):
    msg = 'My Message'
    return render(request, 'chart.html', {'message': msg})