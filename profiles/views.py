from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    template = 'HTML here'
    return render(request,template,context)