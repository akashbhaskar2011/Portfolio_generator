# Generated by Django 4.2.6 on 2024-01-11 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0005_remove_detailsmodel_about_remove_detailsmodel_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='project_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoginUser.detailsmodel')),
            ],
        ),
    ]
