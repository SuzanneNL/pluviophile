from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile.html"
