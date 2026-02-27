from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context= {
        "variable1": "espresso",
        "variable2": "manchild"
    }
    messages.success(request, "This is a message from the Home Page!")
    return render(request, 'index.html', context)
    #return HttpResponse("Hello, welcome to the Home Page!")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("Hello, welcome to the About Page!")
def gadgets(request):
    return render(request, 'gadgets.html')
    #return HttpResponse("Hello, welcome to the Gadgets Page!")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email, phone= phone, desc= desc, date= datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contacts.html')