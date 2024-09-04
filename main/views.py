from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245705',
        'name': 'Palastha Zhorif Kawiswara',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
