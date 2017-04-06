from django.http import HttpResponse
from django.shortcuts import render


def chart(request):
    msg = 'My Message'
    return render(request, 'stock/chart.html', {'message': msg})


def highchart(request):
    msg = 'My Message'
    return render(request, 'stock/highchart.html', {'message': msg})


def fire(request):
    result = 'a'
    return render(request, 'stock/fire.html', {'fire': result})

