from django.contrib import admin

# Register your models here.
from.models import category,product
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}

admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields ={'slug':('name',)}
    list_editable = ['price','stock','available']
    list_per_page = 20
admin.site.register(product,productAdmin)

