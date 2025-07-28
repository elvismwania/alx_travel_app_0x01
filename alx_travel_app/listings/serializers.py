# alx_travel_app_0x01/listings/serializers.py

from rest_framework import serializers
from .models import Listing, Booking
from django.contrib.auth.models import User

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Includes owner's username for display.
    """
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'max_guests', 'amenities', 'owner',
            'owner_username', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at'] # Owner is set automatically

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Includes listing title and guest username for display.
    """
    listing_title = serializers.ReadOnlyField(source='listing.title')
    guest_username = serializers.ReadOnlyField(source='guest.username')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'guest_username',
            'check_in_date', 'check_out_date', 'num_guests', 'total_price',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['guest', 'total_price', 'created_at', 'updated_at'] # Guest and total_price are set automatically

    def validate(self, data):
        """
        Custom validation for booking dates and number of guests.
        """
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date.")

        listing = data['listing']
        if data['num_guests'] > listing.max_guests:
            raise serializers.ValidationError(
                f"Number of guests exceeds the maximum allowed for this listing ({listing.max_guests})."
            )

        # Calculate total price based on dates and listing price_per_night
        days = (data['check_out_date'] - data['check_in_date']).days
        data['total_price'] = listing.price_per_night * days

        return data

