from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from .models import Profile

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    return render(request, 'registration/profile.html', {'profile': profile})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('username', 'email')
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


