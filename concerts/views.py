from django.shortcuts import render
from .models import Concert

def concert_list(request):
    concerts = Concert.objects.all().order_by('date')
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})
