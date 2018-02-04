from django.shortcuts import render

def index(request):
    return render(request, 'about/home.html')

def contact(request):
    return render(request, 'about/basic.html', {'about_me':
            ['If you would like to contact me, feel free to email or call me at:',
            'concox@uw.edu',
            '253.282.1606']
        })
