from django.shortcuts import render

def home(reqeust):
    return render(reqeust, 'index.html')
