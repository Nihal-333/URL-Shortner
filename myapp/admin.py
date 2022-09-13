from django.contrib import admin

# Register your models here.
#from myapp.models import LongToShort
from .models import LongToShort

admin.site.register(LongToShort)
