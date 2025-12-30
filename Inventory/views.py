from django.shortcuts import render

def inventory_home(request):

    context = {
        "name": "Mahabi",
        "role": "employee",
        "numbers": [10, 20, 30, 40, 50],
        "age": 22,
        "city":{"MB":"Theni", "MA":"UDT"},
    }
    return render(request, 'index.html', context)
