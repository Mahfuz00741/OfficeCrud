from django.contrib import admin
from .models import Gender, Dept, Employee

# Register your models here.
admin.site.register(Gender)


class Dept_Admin_Display(admin.ModelAdmin):
    list_display = ['name', 'active']


admin.site.register(Dept, Dept_Admin_Display)

class Emp_Admin_DIsplay(admin.ModelAdmin):
    list_display = ['code', 'name', 'mobile', 'date_of_birth', 'gender', 'dept']
admin.site.register(Employee, Emp_Admin_DIsplay)
