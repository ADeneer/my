from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





class ShowProjectView(ListView):
    model = Project
    template_name = 'blog/home.html'
    context_object_name = 'project'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowProjectView, self).get_context_data(**kwards)
        ctx['title'] = 'Портфолио'
        return ctx


class UserAllProjectView(ListView):
    model = Project
    template_name = 'blog/user_project.html'
    context_object_name = 'project'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllProjectView, self).get_context_data(**kwards)
        ctx['title'] = f"Проекты пользователя {self.kwargs.get('username')}"
        return ctx


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'blog/project_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):
        ctx = super(ProjectDetailView, self).get_context_data(**kwards)
        ctx['title'] = Project.objects.get(pk=self.kwargs['pk'])
        return ctx

class UpdateProjectView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    template_name = 'blog/create_project.html'

    fields = ['title', 'text', 'role', 'img', 'img1', 'img2', 'img3', 'img4']

    def get_context_data(self, **kwards):
        ctx = super(UpdateProjectView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление проекта'
        ctx['btn_text'] = 'Обновить проект'
        return ctx

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True

        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteProjectView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    template_name = 'blog/delete-project.html'

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True

class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'blog/create_project.html'

    fields = ['title', 'img', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateProjectView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление проекта'
        ctx['btn_text'] = 'Добавить проект'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def resume(request):
    return render(request, 'blog/resume.html', {'title': 'Бутин Александр Александрович'})
