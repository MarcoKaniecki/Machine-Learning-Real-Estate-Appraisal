from django.contrib import admin

# Register your models here.

# import model and register with admin panel
from .models import RawAppraisalData

admin.site.register(RawAppraisalData)