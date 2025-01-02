from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# this part is added later


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Destination(models.Model):

    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Guide(models.Model):
    CIVILITY_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
    ]

    civility = models.CharField(max_length=10, choices=CIVILITY_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100)
    city_or_region = models.CharField(max_length=100)
    mother_tongue = models.CharField(max_length=50)
    tour_languages = models.TextField(help_text="Comma-separated list of languages")
    presentation = models.TextField()
    photo = models.ImageField(upload_to="pics/")
    certified_guide = models.BooleanField(default=False)
    guide_card = models.FileField(upload_to="pics/", blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.country})"



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    




# Define the GuideAvailability model
class GuideAvailability(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.guide.name} - {self.date}'

class Booking(models.Model):
    guide_availability = models.ForeignKey(GuideAvailability, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Booking for {self.guide_availability.guide.first_name} on {self.guide_availability.date}"