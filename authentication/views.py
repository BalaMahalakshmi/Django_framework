from django.shortcuts import render

def loginpage(request):

    if request.method == "POST":
        print(request.POST)
        
    return render(request, 'login.html')