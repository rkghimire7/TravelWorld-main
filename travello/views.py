from django.shortcuts import render,redirect
from .models import Destination, GuideAvailability, Booking
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required






def index(request):
    dests = Destination.objects.all()
    print(dests)
    return render(request, 'index.html', {'dests': dests})






def guide_availability(request, guide_id):
    # Get today's date to filter availability
    today = timezone.now().date()

    # Retrieve the guide's availability data with optional filters
    filter_date = request.GET.get('date', today)
    filter_available = request.GET.get('is_available', None)

    availability = GuideAvailability.objects.filter(guide_id=guide_id)

    if filter_available is not None:
        availability = availability.filter(is_available=filter_available.lower() == 'true')
    
    if filter_date:
        availability = availability.filter(date=filter_date)

    return render(request, 'guide_availability.html', {'availability': availability, 'guide_id': guide_id, 'filter_date': filter_date, 'filter_available': filter_available})



@login_required
def book_guide(request, guide_availability_id):
    # Get the guide availability instance
    availability = GuideAvailability.objects.get(id=guide_availability_id)

    # Check if the guide is available for booking
    if not availability.is_available:
        return redirect('guide_availability')  # Redirect if the guide is not available

    # Create a booking if the user is logged in
    if request.method == "POST":
        # Create a new booking
        booking = Booking.objects.create(
            guide_availability=availability,
            user=request.user,
            status='pending'
        )
        booking.save()
        return redirect('booking_confirmation', booking_id=booking.id)

    return render(request, 'book_guide.html', {'availability': availability})