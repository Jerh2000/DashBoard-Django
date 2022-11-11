from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import EducationLevel, Flights, Birth
from .forms import BirthForm,EducationLevelForm,FlightForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    customer = User.objects.filter(groups=2)
    birth = Birth.objects.all()
    educationlevel_year = EducationLevel.objects.values('year').annotate(dcount=Sum('cantidad')).order_by('year')
    educationlevel_level = EducationLevel.objects.values('nivel').annotate(dcount=Sum('cantidad')).order_by('nivel')

    flights_yearc = Flights.objects.values('year').annotate(dcount=Sum('cantidad')).order_by('year')
    flights_city = Flights.objects.values('city').annotate(dcount=Sum('cantidad')).order_by('city')

    births_year = Birth.objects.values('year').annotate(dcount = Sum('cantidad')).order_by('year');
    birth_gender = Birth.objects.values('gender').annotate(dcount = Sum('cantidad')).order_by('gender');
    
    birth_count = birth.count()
    
    customer_count = customer.count()

    context = {
        'birth': birth,
        'educationlevel_year' : educationlevel_year,
        'educationlevel_level' : educationlevel_level,
        'flights_yearc' : flights_yearc,
        'flights_city' : flights_city,
        'births_year' : births_year,
        'birth_gender' :birth_gender,
        'birth_count': birth_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def educationlevel(request):
    level = EducationLevel.objects.all()

    if request.method == 'POST':
        form = EducationLevelForm(request.POST)
        if  form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('year')
            messages.success(request,f'{product_name} added')
            return redirect('dashboard-educationlevel')
    else:
        form = EducationLevelForm()
    context = {
        'level': level,
        'form': form
    }
    return render(request,'dashboard/educationlevel.html',context)


@login_required(login_url='user-login')
def educationlevel_edit(request, pk):
    item = EducationLevel.objects.get(id=pk)
    if request.method == 'POST':
        form = EducationLevelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-educationlevel-edit')
    else:
        form = EducationLevelForm(request.POST, instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/educationlevel_edit.html', context)

@login_required(login_url='user-login')
def educationlevel_delete(request, pk):
    item = EducationLevel.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-educationlevel')
    context = {
        'item': item
    }
    return render(request, 'dashboard/educationlevel_delete.html', context)


def flights(request):
    flights = Flights.objects.all()

    if request.method == 'POST':
        form = FlightForm(request.POST)
        if  form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('year')
            messages.success(request,f'{product_name} added')
            return redirect('dashboard-flights')
    else:
        form = FlightForm()
    context = {
        'flights': flights,
        'form': form
    }
    return render(request,'dashboard/flights.html',context)


@login_required(login_url='user-login')
def flights_edit(request, pk):
    item = Flights.objects.get(id=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-flights')
    else:
        form = FlightForm(request.POST, instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/flights_edit.html', context)

@login_required(login_url='user-login')
def flights_delete(request, pk):
    item = Flights.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-flights')
    context = {
        'item': item
    }
    return render(request, 'dashboard/flights_delete.html', context)

#################################################################################

@login_required(login_url='user-login')
def births(request):
    birth = Birth.objects.all()
    birth_count = birth.count()
    if request.method == 'POST':
        form = BirthForm(request.POST)
        if form.is_valid():
            form.save()
            birth_year = form.cleaned_data.get('year')
            messages.success(request, f'{birth_year} has been added')
            return redirect('dashboard-births')
    else:
        form = BirthForm()
    context = {
        'birth': birth,
        'form': form,
        'birth_count': birth_count,
    }
    return render(request, 'dashboard/birth.html', context)


@login_required(login_url='user-login')
def education_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/education_detail.html', context)


@login_required(login_url='user-login')
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    
    context = {
        'customer': customer,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/customers_detail.html', context)


@login_required(login_url='user-login')
def birth_edit(request, pk):
    item = Birth.objects.get(id=pk)
    if request.method == 'POST':
        form = BirthForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-births')
    else:
        form = BirthForm(request.POST, instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/birth_edit.html', context)



@login_required(login_url='user-login')
def birth_delete(request, pk):
    item = Birth.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-births')
    context = {
        'item': item
    }
    return render(request, 'dashboard/births_delete.html', context)

