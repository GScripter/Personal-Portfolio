from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from .forms import UserChangeForm, UserCreationForm

# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = (
        ("Procfile", {"fields":("photo", "name", "about", "email", "city", "cv", "linkedin", "github", "whatsapp", "telegram", "instagram",)}),
    )


