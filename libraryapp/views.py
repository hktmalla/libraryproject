from django.views.generic import *
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class AdminDashView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'student/admindash.html'


class AdminHomeView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'student/adminhome.html'


class AdminCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'student/admincreate.html'
    form_class = StudentForm
    success_url = '/admin-dash/read/'

# Book views are defined here


class AdminBookView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'book/adminbooklist.html'
    model = Book
    context_object_name = 'books'


class AdminAddBookView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'book/adminaddbook.html'
    form_class = BookForm
    success_url = '/admin-dash/book'


class AdminBookDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'book/adminbookdelete.html'
    queryset = Book.objects.all()
    model = Book
    success_url = '/admin-dash/book/'


class AdminBookUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'book/adminbookupdate.html'
    queryset = Book.objects.all()
    modal = Book
    form_class = BookForm
    success_url = '/admin-dash/book/'


class AdminReadView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'student/adminread.html'
    model = Student
    context_object_name = 'students'


class AdminDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    template_name = 'student/admindelete.html'
    model = Student
    success_url = '/admin-dash/read/'


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'student/adminupdate.html'
    model = Student
    form_class = StudentForm
    success_url = '/admin-dash/read/'


class AdminLoginView(FormView):
    template_name = 'student/adminlogin.html'
    form_class = AdminLoginForm
    success_url = '/'

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
    login_url = '/login/'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')


class AdminIssueCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'issue/adminissue.html'
    form_class = IssueForm
    success_url = '/admin-dash/issue-read/'


class AdminIssueListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'issue/adminissuelist.html'
    queryset = Issue.objects.all()
    context_object_name = 'issues'
