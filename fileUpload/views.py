from django.shortcuts import render
from .forms import ImageForm
from django.contrib import messages
from .models import ImageCollections
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def upload_image(request):
    if request.method == 'POST':
        #print("files : ", request.FILES)
        #print("other data : ", request.POST)
        formObj = ImageForm(request.POST, request.FILES)

        if formObj.is_valid():
            formObj.save()
        messages.add_message(request, messages.INFO, 'Image is uploaded successfully !!')
        return render(request, 'fileUpload/uploadPage.html',{'formObj':formObj})
    else:
        formObj = ImageForm()
        return render(request, 'fileUpload/uploadPage.html', {'formObj':formObj})

@login_required
def image_gallery(request):
    if request.method == "POST":
        #filter form to be added to filter images acc to category
        if request.POST.get('animal') == 'on':
            image_collections = ImageCollections.objects.filter(category = 'animal')
        elif request.POST.get('cars') == 'on':
            image_collections = ImageCollections.objects.filter(category = 'cars')
        elif request.POST.get('bikes') == 'on':
            image_collections = ImageCollections.objects.filter(category = 'bike')
        elif request.POST.get('scenary') == 'on':
            image_collections = ImageCollections.objects.filter(category = 'scenary')
        elif request.POST.get('river') == 'on':
            image_collections = ImageCollections.objects.filter(category = 'river')
        else:
            image_collections = ImageCollections.objects.all()
        #print('len of records : ', len(image_collections))
        return render(request, 'fileUpload/image_gallery.html', {'image_collections':image_collections})
    image_collections = ImageCollections.objects.all()
    return render(request, 'fileUpload/image_gallery.html', {'image_collections':image_collections})
