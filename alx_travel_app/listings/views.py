# alx_travel_app_0x01/listings/views.py

from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    Provides CRUD operations for Listing model.
    """
    queryset = Listing.objects.all().select_related('owner') # Optimize with select_related for owner
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny] # For simplicity, allow any access

    def perform_create(self, serializer):
        """
        Automatically sets the owner of the listing to the current authenticated user.
        """
        # Ensure request.user is available and authenticated before setting owner
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            # Handle cases where user is not authenticated, e.g., raise an error
            # or assign a default owner if appropriate for your application logic.
            # For this task, we assume authentication is handled or AllowAny is fine.
            # If permissions.IsAuthenticated is used, this else branch won't be hit.
            raise permissions.NotAuthenticated("Authentication is required to create a listing.")

    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        """
        Retrieve all bookings for a specific listing.
        Optimized with select_related for guest and prefetch_related for listing.
        """
        listing = self.get_object()
        # Use select_related for the guest on each booking
        # Use prefetch_related if Booking had a ManyToMany relationship or reverse FKs to optimize.
        # Here, select_related('guest') is sufficient for direct FK.
        bookings = listing.bookings.all().select_related('guest').order_by('-created_at')
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    Provides CRUD operations for Booking model.
    """
    queryset = Booking.objects.all().select_related('listing', 'guest') # Optimize with select_related
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny] # For simplicity, allow any access

    def perform_create(self, serializer):
        """
        Automatically sets the guest of the booking to the current authenticated user.
        """
        if self.request.user.is_authenticated:
            serializer.save(guest=self.request.user)
        else:
            raise permissions.NotAuthenticated("Authentication is required to create a booking.")

