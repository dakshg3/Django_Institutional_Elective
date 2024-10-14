from django.contrib import admin

# Register your models here.
from .models import Choices
from .models import Options
from .models import timer
from .models import allocated

admin.site.register(Choices)
admin.site.register(Options)
admin.site.register(timer)
admin.site.register(allocated)
