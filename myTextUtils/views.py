from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("request : ", request)
    print(dir(request))
    print(dir(request.user))
    return HttpResponse("""<div><h1>Hello....other routes are </h1><ul><li>/home</li><li>/home/navigator</li>
    <li>/utility</li><li>/utility/remove_punc</li><li>utility/capitalize_alternate</li><li>/upload</li>
    <li>/upload/image_gallary</li>
    </ul></div>""")
