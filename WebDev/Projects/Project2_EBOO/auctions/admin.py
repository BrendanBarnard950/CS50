from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Catagories)
admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Comments)
