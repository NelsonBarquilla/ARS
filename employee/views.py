from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EmployeeCreateForm, ProfileUpdateForm, EmployeeChangeForm
from web.models import Ratee, Rate, Employee
from django.db.models import Avg
from django.db.models import Q


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('first_name')
            messages.success(request, f'Account created for {username}')
            return redirect('web-home')
        else:
            messages.error(request, f'The password you have entered is not acceptable.')
    else:
        form = EmployeeCreateForm()
    return render(request, 'employee/create_employee.html', {'form': form})


@login_required
def profile(request):
    empid = request.user.empid
    quarter = Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name)
    print(str(quarter))
    if request.method == 'POST':
        u_form = EmployeeChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been updated!')
            return redirect('web-home')

    else:
        u_form = EmployeeChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 't_rate': Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name).aggregate(
        #     Avg('rate')).get('rate__avg', 0.z00),
        'q1_rate': Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name).filter
        (parentrating__quarter=1).aggregate(Avg('rate')).get('rate__avg', 0.00),
        'q2_rate': Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name).filter
        (parentrating__quarter=2).aggregate(Avg('rate')).get('rate__avg', 0.00),
        'q3_rate': Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name).filter
        (parentrating__quarter=3).aggregate(Avg('rate')).get('rate__avg', 0.00),
        'q4_rate': Ratee.objects.filter(parentrating__employee__first_name=request.user.first_name).filter
        (parentrating__quarter=4).aggregate(Avg('rate')).get('rate__avg', 0.00)
    }

    return render(request, 'employee/profile.html', context)
