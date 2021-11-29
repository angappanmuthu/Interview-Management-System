from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([
    MobileVerification,
    EmailVerification,
    State,
    District,
    City,
    Pincode,
    User,
    PanelMember,
    PanelAdmin,
    Company,
    Post,
    Interview
    ])
