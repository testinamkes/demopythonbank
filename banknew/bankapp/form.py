from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms



def register_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        registration_form = RegistrationForm(request.POST)

        if user_form.is_valid() and registration_form.is_valid():
            user = user_form.save()
            name = registration_form.cleaned_data.get('name')
            dob = registration_form.cleaned_data.get('dob')
            age = registration_form.cleaned_data.get('age')
            gender = registration_form.cleaned_data.get('gender')
            phone_number = registration_form.cleaned_data.get('phone_number')
            email = registration_form.cleaned_data.get('email')
            address = registration_form.cleaned_data.get('address')
            district = registration_form.cleaned_data.get('district')
            branch = registration_form.cleaned_data.get('branch')
            account_type = registration_form.cleaned_data.get('account_type')
            materials_provided = registration_form.cleaned_data.get('materials_provided')
            print(f"Registration Data: {name}, {dob}, {age}, {gender}, {phone_number}, {email}, {address}, {district}, {branch}, {account_type}, {materials_provided}")
            return redirect('login')
    else:
        user_form = UserCreationForm()
        registration_form = RegistrationForm()

    context = {
        'user_form': user_form,
        'registration_form': registration_form,
    }

    return render(request, 'register.html', context)

from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.CharField(max_length=100)
    branch = forms.CharField(max_length=100)
    account_type = forms.ChoiceField(choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')],
        widget=forms.CheckboxSelectMultiple
    )
