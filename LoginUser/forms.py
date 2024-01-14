from django import forms
from .models import detailsModel


class details(forms.ModelForm):
    class Meta:
        model = detailsModel
        fields = [
            'temp_no',
            'name', 'phone_number', 'email', 'age', 'github_link', 'linkedin_link',
            'facebook_link', 'insta_link', 'role', 'about_me', 'skills',
            'project1_name', 'project1_desc', 'project1_pic_link', 'project1_project_link',
            'project2_name', 'project2_desc', 'project2_pic_link', 'project2_project_link',
            'project3_name', 'project3_desc', 'project3_pic_link', 'project3_project_link',
        ]

    temp_no = forms.TypedChoiceField(
        choices=detailsModel.TemplateChoices.choices,
        coerce=int,
        widget=forms.RadioSelect
    )
