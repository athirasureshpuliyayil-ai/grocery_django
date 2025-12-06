from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# 🧍 User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """Ensure the email gets saved to the User model."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# 🧑‍💼 User Profile Edit Form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'border p-2 w-full rounded',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border p-2 w-full rounded',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border p-2 w-full rounded',
                'placeholder': 'Email Address'
            }),
        }


# 🛒 Checkout Form
class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded',
            'placeholder': 'Full Name'
        })
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border p-2 w-full rounded',
            'placeholder': 'Delivery Address',
            'rows': 3
        })
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded',
            'placeholder': 'City'
        })
    )
    postal_code = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'border p-2 w-full rounded',
            'placeholder': 'Postal Code'
        })
    )
