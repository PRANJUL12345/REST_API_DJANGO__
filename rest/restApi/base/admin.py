from django.contrib import admin
from .models import Users

# Register your models here.
admin.site.register(Users)

### Regestring via Class


# @admin.register(YourModel1)
# class YourModel1Admin(admin.ModelAdmin):
#     # Customize how YourModel1 is displayed in the admin interface
#     list_display = ('field1', 'field2', 'field3')  # Specify fields to display
