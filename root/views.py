from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'home.html')

def v1(req):
    data='django project'
    return render(req,'v1.html',{'data':data})
