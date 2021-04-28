from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ProfileForm
from .models import Profile
from forum.models import Thread, Comment
from blog.models import BlogPost
from donation.models import Donation


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['threads_by_user'] = \
            Thread.objects.filter(creator=profile.user)
        context['comments_by_user'] = \
            Comment.objects.filter(creator=profile.user)
        return context


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    success_message = "Your profile was updated successfully"
    template_name = "profiles/edit_profile.html"

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    # Source for redirecting: StackOverFlow. See README file under 'Sources'.
    def handle_no_permission(self):
        return redirect('error')


@login_required
def account(request):
    template = 'profiles/account.html'
    donations = Donation.objects.all().order_by('-date')
    donations_by_user = \
        Donation.objects.filter(donor=request.user).order_by('-date')
    context = {
        'donations': donations,
        'donations_by_user': donations_by_user,
        'blogposts': BlogPost.objects.all()
    }
    return render(request, template, context)


def error(request):
    return render(request, 'profiles/error.html')
