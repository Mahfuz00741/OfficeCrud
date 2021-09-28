from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('', views.EmployeeListView.as_view(), name = 'all_employee'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name = 'employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name = 'employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name = 'employee_delete'),

    path('dept/all/', views.DeptListView.as_view(), name = 'all_dept'),
    path('dept/create/', views.DeptCreateView.as_view(), name = 'dept_create'),
    path('dept/<int:pk>/update/', views.DeptUpdateView.as_view(), name = 'dept_update'),
    path('dept/<int:pk>/delete/', views.DeptDeleteView.as_view(), name = 'dept_delete'),

]
