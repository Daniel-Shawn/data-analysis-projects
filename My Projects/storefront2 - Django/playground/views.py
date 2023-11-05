from django.shortcuts import render


def say_hello(request):
    name_dict = {
        'name': 'Shawn'
    }
    return render(request, 'hello.html', name_dict)
