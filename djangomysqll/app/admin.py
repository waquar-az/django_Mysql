from django.contrib import admin

# Register your models here.
from .models import Customer

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['customer','address1','email','landline_no','contact_person','city','address2','mobile','gstno']
    
    
    
#admin.site.register(Customer,CustomerModelAdmin)
