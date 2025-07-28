alx_travel_app_0x01 - Travel App APIThis project implements a basic API for managing travel listings and bookings using Django REST Framework. It includes CRUD operations for Listing and Booking models and is documented with Swagger UI.Project Structurealx_travel_app_0x01/
├── alx_travel_app/             # Main Django project directory
│   ├── settings.py             # Project settings (DRF, drf-yasg configured)
│   ├── urls.py                 # Main URL routing (API and Swagger)
│   └── ...
└── listings/                   # Django app for listings and bookings
    ├── models.py               # Defines Listing and Booking models
    ├── serializers.py          # DRF serializers for models
    ├── views.py                # DRF ViewSets for API endpoints
    ├── urls.py                 # API URL routing for listings app
    └── ...
Setup and InstallationClone the repository:git clone https://github.com/alx-backend-python/alx_travel_app_0x01.git
cd alx_travel_app_0x01
Create a virtual environment (recommended):python3 -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate
Install dependencies:pip install Django djangorestframework drf-yasg
Apply migrations:python manage.py makemigrations listings
python manage.py migrate
Create a superuser (for admin access and API testing with authentication):python manage.py createsuperuser
Run the development server:python manage.py runserver
API EndpointsThe API endpoints are accessible under /api/.Listings:GET /api/listings/: List all listings.POST /api/listings/: Create a new listing.GET /api/listings/{id}/: Retrieve a specific listing.PUT /api/listings/{id}/: Update a specific listing.PATCH /api/listings/{id}/: Partially update a specific listing.DELETE /api/listings/{id}/: Delete a specific listing.GET /api/listings/{id}/bookings/: Retrieve all bookings for a specific listing.Bookings:GET /api/bookings/: List all bookings.POST /api/bookings/: Create a new booking.GET /api/bookings/{id}/: Retrieve a specific booking.PUT /api/bookings/{id}/: Update a specific booking.PATCH /api/bookings/{id}/: Partially update a specific booking.DELETE /api/bookings/{id}/: Delete a specific booking.API Documentation (Swagger UI / ReDoc)The API is documented using drf-yasg.Swagger UI: Access interactive documentation at http://127.0.0.1:8000/swagger/ReDoc: Access alternative documentation at http://127.0.0.1:8000/redoc/You can use these interfaces to explore endpoints, view schemas, and make test requests directly from your browser.Testing Endpoints (e.g., with Postman)Start the Django development server.Open Postman (or a similar API client).Authentication: For POST, PUT, PATCH, DELETE operations on Listing and Booking, you will need to authenticate. You can use Basic Auth with the superuser credentials you created, or log in via the Django admin (http://127.0.0.1:8000/admin/) and use session authentication (which Swagger UI supports automatically).Make requests:GET /api/listings/: To retrieve all listings.POST /api/listings/:Method: POSTHeaders: Content-Type: application/jsonBody (raw JSON):{
    "title": "Cozy Apartment in City Center",
    "description": "A beautiful apartment close to all amenities.",
    "address": "123 Main St",
    "city": "Anytown",
    "country": "USA",
    "price_per_night": "150.00",
    "max_guests": 4,
    "amenities": "WiFi, AC, Kitchen"
}
(Note: owner field is automatically set by the view based on authenticated user.)GET /api/listings/{id}/bookings/: To see bookings for a specific listing.POST /api/bookings/:Method: POSTHeaders: Content-Type: application/jsonBody (raw JSON):{
    "listing": 1,  # ID of an existing listing
    "check_in_date": "2025-08-01",
    "check_out_date": "2025-08-05",
    "num_guests": 2
}
(Note: guest and total_price are automatically set.)This setup provides a complete, runnable Django REST API with integrated Swagger documentation.
