from django.shortcuts import render, redirect
from empapplication.models import Employee
from empapplication.forms import EmployeeForm


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()

    return render(request, "indexhome.html", {'form': form})


def show(request):
    employees = Employee.objects.all()
    form = EmployeeForm()
    return render(request, "show.html", {'employees': employees, 'form':form})


def update(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "update.html", {'form': form, 'employee': employee})


def delete(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    employee.delete()
    return redirect("/show")





