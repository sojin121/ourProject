from django.shortcuts import render

# Create your views here.
def Main(request):
    return render(request, 'view/Main.html', {})

def Login(request):
    return render(request, 'view/Login.html', {})

def Widget(request):
    return render(request, 'pages/widgets.html', {})

def Chart(request):
    return render(request, 'pages/charts/chartjs.html', {})