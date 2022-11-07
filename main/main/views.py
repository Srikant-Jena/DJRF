from django.http import HttpResponse,JsonResponse




def home_page(request):
    print("Home page requested")
    friends=[
        'Bapi',
        'srikant',
        'Mamoon',
    ]
    return JsonResponse(friends,safe = False)