from django.db import models

from django.contrib.auth.models import User
class detailsModel(models.Model):
    class TemplateChoices(models.IntegerChoices):
        CHOICE_1 = 1, 'Choice 1'
        CHOICE_2 = 2, 'Choice 2'

    user_model = models.ForeignKey(User, on_delete=models.CASCADE)
    temp_no = models.IntegerField(choices=TemplateChoices.choices)

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email=models.EmailField(blank=True)
    age = models.IntegerField()
    github_link=models.URLField(blank=True, null=True)
    linkedin_link=models.URLField(blank=True, null=True)
    facebook_link=models.URLField(blank=True, null=True)
    insta_link=models.URLField(blank=True, null=True)
    role=models.CharField(max_length=100,default='')
    about_me=models.CharField(max_length=120,default='')
    skills=models.CharField(max_length=20,default='')
    project1_name=models.CharField(max_length=100,default='')
    project1_desc=models.CharField(max_length=100,default='')
    project1_pic_link=models.URLField(null=True)
    project1_project_link=models.URLField(null=True)

    project2_name = models.CharField(max_length=100,default='')
    project2_desc = models.CharField(max_length=100,default='')
    project2_pic_link = models.URLField(null=True)
    project2_project_link = models.URLField(null=True)

    project3_name = models.CharField(max_length=100,blank=True,default='')
    project3_desc = models.CharField(max_length=100,blank=True,default='')
    project3_pic_link = models.URLField(blank=True, null=True)
    project3_project_link = models.URLField(blank=True, null=True)