# create form for user to update or edit information create form using django form 
from django.forms import ModelForm
from django import forms
from .models import Profile
from django.forms import ModelForm, FileInput, TextInput, Textarea
from django.contrib.auth.models import User

# =========== forms ===============
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': FileInput(),
            'displayname': TextInput(attrs={'placeholder': 'Add display name'}),
            'info': Textarea(attrs={'rows': 3, 'placeholder': 'Add information'})
        }
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']