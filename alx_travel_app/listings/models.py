# alx_travel_app_0x01/listings/models.py

from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    """
    Represents a travel listing (e.g., a house, apartment, or hotel room).
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.IntegerField()
    amenities = models.TextField(blank=True, help_text="Comma-separated list of amenities")
    owner = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Booking(models.Model):
    """
    Represents a booking made for a specific listing.
    """
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ['check_in_date']
        # Ensure no overlapping bookings for the same listing
        constraints = [
            models.UniqueConstraint(
                fields=['listing', 'check_in_date', 'check_out_date'],
                name='unique_booking_dates_per_listing'
            )
        ]

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.guest.username} from {self.check_in_date} to {self.check_out_date}"

