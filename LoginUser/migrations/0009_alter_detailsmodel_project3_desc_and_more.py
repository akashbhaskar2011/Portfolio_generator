# Generated by Django 4.2.6 on 2024-01-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0008_remove_detailsmodel_projects_detailsmodel_about_me_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsmodel',
            name='project3_desc',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='detailsmodel',
            name='project3_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
