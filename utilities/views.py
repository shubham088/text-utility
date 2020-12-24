from django.shortcuts import render

# Create your views here.

def text_utilities(request):
    context_dict = {}
    return render(request, 'utilities/utility_home.html', context_dict)


def remove_punctuations(request):
    if request.method == 'GET':
        text_to_analyze = request.GET.get('text', 'default')
        print("this is the text to analyze : ", text_to_analyze)
    if request.method == 'POST':
        text_to_analyze = request.POST.get('text', 'default')
        print("this is the text to analyze : ", text_to_analyze)

    list_of_punctuations = ['.',',', '\'','?', ';','!',':','-','\"']
    analyzed_text = ""
    for char in text_to_analyze:
        if char not in list_of_punctuations:
            analyzed_text = analyzed_text + char
    context_dict  = {"analyzed_text":analyzed_text, "text_to_analyze":text_to_analyze}
    return render(request, 'utilities/remove_punctuation.html', context_dict)


def capitalize_alternate(request):
    if request.method == 'GET':
        text_to_analyze = request.GET.get('text', 'default')
        print("this is the text to analyze : ", text_to_analyze)
    if request.method == 'POST':
        text_to_analyze = request.POST.get('text', 'default')
        print("this is the text to analyze : ", text_to_analyze)

    analyzed_text = ""
    for x in range(0, len(text_to_analyze)):
        if x%2 == 0:
            print(text_to_analyze[x])
            analyzed_text = analyzed_text + text_to_analyze[x].upper()
        else:
            print(text_to_analyze[x])
            analyzed_text = analyzed_text + text_to_analyze[x]

    context_dict  = {"analyzed_text":analyzed_text, "text_to_analyze":text_to_analyze}
    return render(request, 'utilities/capitalize_alt.html', context_dict)
