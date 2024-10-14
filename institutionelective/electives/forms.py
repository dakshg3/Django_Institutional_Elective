from django import forms

from .models import Choices, AdminLogin

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choices
        fields = [
            'usn',
            'choice1',
            'choice2',
            'choice3',
            'choice4',
            'choice5'
        ]

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminLogin
        fields = [
            'user_id',
            'user_pass'
        ] 