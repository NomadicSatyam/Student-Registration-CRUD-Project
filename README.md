# Add This Line i docker File for make table structure and super user 

# Run makemigrations and migrate commands
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create a superuser
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'satyamm1998@gmail.com', 'admin')" | python manage.py shell


