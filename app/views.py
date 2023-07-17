from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'Hai Harshad How are you'}
    return render(request,'usdf.html',d)
