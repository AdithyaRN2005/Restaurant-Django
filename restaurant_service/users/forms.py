from django import forms
from .models import UserProfile, Address



class CheckOutForm(forms.ModelForm):
    address_id = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'email')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['address_id'].queryset = Address.objects.filter(user_profile=user)
            
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'email')

class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('name','type','housename','place','postoffice','pincode','district','state','mob')

