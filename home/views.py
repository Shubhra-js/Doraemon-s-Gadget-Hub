from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context= {
        "variable1": "espresso",
        "variable2": "manchild"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("Hello, welcome to the Home Page!")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("Hello, welcome to the About Page!")
def gadgets(request):
    return render(request, 'gadgets.html')
    #return HttpResponse("Hello, welcome to the Gadgets Page!")
def contact(request):
    return render(request, 'contacts.html')