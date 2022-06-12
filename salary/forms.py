from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from salary.models import Project, Wage, Bonus, Main


class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class WageForm(forms.ModelForm):
    class Meta:
        model = Wage
        fields = "__all__"


class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = "__all__"


class MainSearchForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by FIO..", "class": "form-control"}
        ),
    )


class BonusSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..", "class": "form-control"}
        ),
    )


class WageSearchForm(forms.Form):
    position = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by position..", "class": "form-control"}
        ),
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name..", "class": "form-control"}
        ),
    )
