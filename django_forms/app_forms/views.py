from django.shortcuts import render, get_object_or_404
from .models import Cities, Brigade, Facility

def index(request):
    cities = Cities.objects.all()
    return render(request, 'app_forms/main.html', {'cities':cities})

# def getCities(request):
#     cities = Cities.objects.all()
#     return JsonResponse({'cities' : list(cities.values())})

def get_brigade(request):
    city_id = request.GET.get('city_id')
    brigades = Brigade.objects.filter(city_id = city_id).all()
    return render(request, 'app_forms/select_html_data.html' ,{'data' : brigades, 'main': 'brigade'})

def get_facility(request):
    brigade_id = request.GET.get('brigade_id')
    facilities = Facility.objects.filter(brigade_id = brigade_id)
    return render(request,'app_forms/select_html_data.html' ,{'data' : facilities, 'main': 'facility'} )

def get_info(request):
    brigade_id = request.GET.get('brigade_id')
    faclity_id = request.GET.get('facility_id')
    if(brigade_id):
        data = get_object_or_404(Brigade, pk = brigade_id)
    elif(faclity_id):
        data = get_object_or_404(Facility, pk = faclity_id)
    return render(request,'app_forms/info_block.html' ,{'data' : data} )
