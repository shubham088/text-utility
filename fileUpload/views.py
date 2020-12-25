from django.shortcuts import render
from .forms import ImageForm
from django.contrib import messages
from .models import ImageCollections

# Create your views here.


def upload_image(request):
    if request.method == 'POST':
        print("files : ", request.FILES)
        print("other data : ", request.POST)
        formObj = ImageForm(request.POST, request.FILES)

        if formObj.is_valid():
            formObj.save()
        messages.add_message(request, messages.INFO, 'Image is uploaded successfully !!')
        return render(request, 'fileUpload/uploadPage.html',{'formObj':formObj})
    else:
        formObj = ImageForm()
        return render(request, 'fileUpload/uploadPage.html', {'formObj':formObj})

    
def image_gallery(request):
    #if request.method == "POST":
        ##filter form to be added to filter images acc to category
    
    image_collections = ImageCollections.objects.all()
    print('len of records : ', len(image_collections))
    return render(request, 'fileUpload/image_gallery.html', {'image_collections':image_collections})
