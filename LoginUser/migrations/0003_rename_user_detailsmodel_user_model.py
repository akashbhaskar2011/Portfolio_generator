# Generated by Django 4.2.6 on 2024-01-10 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0002_detailsmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailsmodel',
            old_name='user',
            new_name='user_model',
        ),
    ]
