from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('frontend/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')


@login_required
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "user_profile.html", {"first_name": request.user.first_name})
    else:
        redirect('/users/login')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
