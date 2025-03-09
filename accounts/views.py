from django.shortcuts import render
from accounts.forms import UserRegisterForm, ProfileForm
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.



def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page or any other page


class RegisterView(CreateView):
    form_class = UserRegisterForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request,  self.object)
        return reverse_lazy('project_list')

@login_required()
def edit_profile(request):
    if request.method == 'POST':
        form= ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form= ProfileForm(instance=request.user)
        return render(request, 'profile.html', {
            'form': form
        })


