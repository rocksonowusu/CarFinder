from django.shortcuts import get_object_or_404, render
from .models import Car

# Create your views here.
def home(request):
    return render(request, 'cars/home.html')

def recommend(request):
    return render(request, 'cars/recommend.html')

def results(request):
    if request.method == 'POST':
        budget = int(request.POST.get('budget'))
        purpose = request.POST.get('purpose')
        car_type = request.POST.get('car_type')

        #Filter cars based on criteria
        cars = Car.objects.filter(
            price__lte=budget,
            purpose=purpose,
            car_type=car_type
        )

        context = {
            "cars":cars,
            "budget":budget,
            "purpose":purpose,
            "car_type":car_type,
        }
        return render(request, 'cars/results.html', context)
    
    return render(request, 'cars/recommend.html')

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {"car":car}
    return render(request, 'cars/car_detail.html', context)


def upcoming_features(request):
    return render(request, 'cars/upcoming_features.html')