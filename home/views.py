from django.shortcuts import render

# Create your views here.

def home_page(request):
    print("about to render home page")
    return render(request, 'home/home-page.html', {})


def navigator(request):
    context_dict = {}
    return render(request, 'home/navigator.html', context_dict)
