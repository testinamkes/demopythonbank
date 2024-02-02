from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views import View
from django.urls import reverse
from django.contrib import messages
from .models import District, Branch

def home(request):
 return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def register_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request,user)
            return redirect(reverse('bankapp:login'))
    else:
        user_form = UserCreationForm()

    context = {
        'user_form': user_form,
    }

    return render(request, 'register.html', context)


def dashboard(request):
    districts = District.objects.all()
    branches = Branch.objects.all()

    context = {
        'districts': districts,
        'branches': branches,
    }

    return render(request, 'dashboard.html', context)

def branches(request):
    districts = District.objects.all()
    return render(request, 'branches.html', {'districts': districts})

class BranchByDistrictView(View):
    def get(self, request, district_slug):
        try:
            district = District.objects.get(slug=district_slug)
            branches = district.branch_set.all()

            context = {
                'district': district,
                'branches': branches,
            }

            return render(request, 'branches.html', context)

        except District.DoesNotExist:
            return HttpResponse("District not found", status=404)
def allbranch(request,c_slug=None):
    c_page=None
    branches=None
    if c_slug!=None:
        c_page=get_object_or_404(District,slug=c_slug)
        branches=Branch.objects.all().filter(District=c_page,available=True)
    else:
        branches=Branch.objects.all().filter(available=True)
    return render(request,"district.html",{'District':c_page,'branches':branches})


class YourDistrictView(View):
    def get(self, request, district_slug):
        district_data = f"Data for district {district_slug}"
        context = {
            'district_data': district_data,
        }
        return render(request, 'district.html', context)


def new_page(request):
    return render(request, 'new_page.html')

def registration_form(request):
    districts_list = District.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials_provide = request.POST.getlist('materials')
        messages.success(request, 'Application accepted. Thank you!')
        return redirect('bankapp:dashboard')
    context = {'districts_list': districts_list}
    return render(request, 'registration_form.html',context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('bankapp:home')

def wikipedia_page(request, district):
    wikipedia_urls = {
        'District1': 'https://en.wikipedia.org/wiki/District1',
        'District2': 'https://en.wikipedia.org/wiki/District2',
        'District3': 'https://en.wikipedia.org/wiki/District3',
        'District4': 'https://en.wikipedia.org/wiki/District4',
        'District5': 'https://en.wikipedia.org/wiki/District5',
    }
    return redirect(wikipedia_urls.get(district, '/'))

def get_branches(request):
    district_slug = request.GET.get('district')
    branches = Branch.objects.filter(district__slug=district_slug).values('slug', 'name')
    return JsonResponse(list(branches), safe=False)