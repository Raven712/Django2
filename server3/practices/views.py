from django.shortcuts import render

# Create your views here.
def practice1(request):
  return render(request, 'practices/practice1.html')