from django import forms
from .models import HCTRecord, LSERecord


class HCTRecordForm(forms.ModelForm):
    class Meta:
        model = HCTRecord
        fields = ['name', 'surname', 'date_of_birth', 'sex', 'result', 'tb_tested']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class LSERecordForm(forms.ModelForm):
    class Meta:
        model = LSERecord
        fields = ['name', 'surname', 'date_of_birth', 'grade', 'sex', 'club_type']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }