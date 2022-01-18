from django.contrib import admin


from .models import User_Info, Reservation, ErrorReport

admin.site.register(User_Info)
admin.site.register(Reservation)
admin.site.register(ErrorReport)

# Register your models here.
