from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import exceptions
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, View, DeleteView

from .forms import CreateResume
from .models import Resume
from .services.services import get_resume, get_resume_on_pk


class AllResume(ListView):
    context_object_name = 'resume'
    model = Resume
    template_name = 'resume/all_resume.html'

    def get_queryset(self):
        return Resume.objects.all()


class DeleteResume(DeleteView):
    context_object_name = 'resume'
    model = Resume
    template_name = 'resume/delete_resume.html'

    def get_object(self, queryset=None):
        obj = super(DeleteResume, self).get_object()
        if not obj.user == self.request.user:
            raise exceptions.PermissionDenied
        return obj

    def get_success_url(self):
        messages.success(self.request, 'OK')

        return reverse_lazy('users_resume')


class DetailResume(DetailView):
    context_object_name = 'resume'
    model = Resume
    template_name = 'resume/resume.html'


class EditResume(View):
    """Editing a resume if it exists"""
    form_class = CreateResume
    template_name = 'resume/resume-edit.html'

    def get(self, request, pk):
        resume = get_resume_on_pk(pk)
        if not resume.user == request.user:
            messages.error(request, 'access error')
            return render(request, 'resume/errors.html')
        if resume:
            form = self.form_class(instance=resume)
            return render(request, self.template_name, {'form': form})
        raise Http404

    def post(self, request, pk):
        resume = get_resume_on_pk(pk)
        if not resume:
            raise Http404
        form = self.form_class(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
        else:
            messages.error(request, 'Error')
        return redirect('edit_resume', pk=pk)


def create_resume(request):
    if request.method == 'POST':
        form = CreateResume(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'create_success')
            return redirect('users_resume')
    form = CreateResume()
    return render(request, 'resume/resume-edit.html', {'form': form})
