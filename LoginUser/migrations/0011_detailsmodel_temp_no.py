# Generated by Django 4.2.6 on 2024-01-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginUser', '0010_alter_detailsmodel_project1_pic_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsmodel',
            name='temp_no',
            field=models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2')], default=1),
            preserve_default=False,
        ),
    ]
