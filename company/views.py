from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from company.forms import FormCreateCompany
from vacancy.servises.servises import get_my_company


class CreateMyCompany(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Creating a company from form."""
    permission_required = (
        'company.add_company', 'company.change_company',
        'delete_company', 'company.view_company'
    )
    form_class = FormCreateCompany
    template_name = 'cabinet/company-edit.html'

    def get(self, request):
        company = get_my_company(request)

        if not company:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

        form = self.form_class(instance=company)
        context = {
            'form': form,
            'logo': company.logo
        }
        return render(request, self.template_name, context)

    def post(self, request):
        company = get_my_company(request)
        if company:
            form = self.form_class(
                request.POST, request.FILES, instance=company
            )
        else:
            form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            messages.success(request, 'Отлично')
            return redirect('create_company')
        return render(request, self.template_name, {'form': form})
