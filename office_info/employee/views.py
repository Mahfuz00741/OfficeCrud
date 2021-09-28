from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Dept, Gender

# Create your views here.
class EmployeeListView(ListView):
    def get(self, request):
        dc = Dept.objects.all().count()
        el = Employee.objects.all()
        ctx = {
            'dept_count': dc,
            'employee_list': el,
        }
        return render(request, 'employee/employee_list.html', ctx)

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:all_employee')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['name', 'mobile', 'date_of_birth', 'gender']
    success_url = reverse_lazy('employee:all_employee')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:all_employee')

# view for Dept class

class DeptListView(ListView):
    model = Dept
    template_name = 'employee/dept_list.html'

class DeptCreateView(CreateView):
    model = Dept
    template_name = 'employee/dept_form.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:all_dept')

class DeptUpdateView(UpdateView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('employee:all_dept')

class DeptDeleteView(DeleteView):
    model = Dept
    fields = '__all__'
    success_url = reverse_lazy('employee:all_dept')