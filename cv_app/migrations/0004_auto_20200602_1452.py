# Generated by Django 2.2.8 on 2020-06-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0003_auto_20200602_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
