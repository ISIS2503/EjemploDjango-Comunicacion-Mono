from django.contrib import admin
from .models import Variable
from .models import Measurement

# Register your models here.
admin.site.register(Variable)
admin.site.register(Measurement)
