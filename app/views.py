from django.shortcuts import render

# Create your views here.
def operation(request):
    return render(request,'operation.html')
