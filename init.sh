#!/bin/bash

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'satyamm1998@gmail.com', 'admin')" | python manage.py shell

# Run the Django development server
python manage.py runserver 0.0.0.0:8000

