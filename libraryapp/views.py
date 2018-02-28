from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class AdminDashView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'admindash.html'


class AdminCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'admincreate.html'
    form_class = StudentForm
    success_url = '/admin-dash/read/'


class AdminReadView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'adminread.html'
    model = Student
    context_object_name = 'students'


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/'
    template_name = 'admindelete.html'
    model = Student
    success_url = '/admin-dash/read/'


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'adminupdate.html'
    model = Student
    form_class = StudentForm
    success_url = '/admin-dash/read/'


class AdminLoginView(FormView):
    template_name = 'adminlogin.html'
    form_class = AdminLoginForm
    success_url = '/admin-dash/'

    def form_valid(self, form):
        u_name = form.cleaned_data['user_name']
        p_word = form.cleaned_data['password']
        user = authenticate(username=u_name, password=p_word)
        if user is not None:
            login(self.request, user)
        else:
            return HttpResponseRedirect('/')
        return super().form_valid(form)


class AdminLogoutView(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request):
        logout(request)
        HttpResponseRedirect('/adminlogin/')
