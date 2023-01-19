from django.contrib import admin

from.models import cartype,Cars,Booking
# Register your models here.
admin.site.register(cartype)
admin.site.register(Cars)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','p_email','car','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
