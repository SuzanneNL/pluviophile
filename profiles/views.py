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
    """
    This renders a profile page. Login is required.
    """
    model = Profile
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        """
        This adds the threads and comments that were created by the user to the
        context of the template.
        """
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['threads_by_user'] = \
            Thread.objects.filter(creator=profile.user)
        context['comments_by_user'] = \
            Comment.objects.filter(creator=profile.user)
        return context


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, UpdateView):
    """
    This renders a page with a form for editing a profile, which can only be
    accessed by registered users. This view inherits from UpdateView, which
    handles the updating of the profile. After the update, a success message
    appears.
    """
    model = Profile
    form_class = ProfileForm
    success_message = "Your profile was updated successfully"
    template_name = "profiles/edit_profile.html"

    def test_func(self):
        """
        This makes sure only the user connected to the profile and superusers
        can edit the profile.
        """
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    # Source for redirecting: StackOverFlow. See README file under 'Sources'.
    def handle_no_permission(self):
        """
        Other users get redirected to the error page, when trying to access the
        edit profile page.
        """
        return redirect('error')


@login_required
def account(request):
    """
    This renders the account page for the logged in user. Therefore, login is
    required. Donations by all users and donarions by the logged in user are
    added to context. Also, blogposts are added to the context.
    """
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
    """
    This renders an error page.
    """
    return render(request, 'profiles/error.html')
