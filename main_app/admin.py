from django.contrib import admin

from .models import Band # IMPORT BAND MODEL FROM MODEL.PY

# Register your models here.
admin.site.register(Band) # THIS ADDS BAND MODEL TO ADMIN PANNEL 