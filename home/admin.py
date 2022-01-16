from django.contrib import admin


from .models import User, Reservation

admin.site.register(User)
admin.site.register(Reservation)
# Register your models here.
