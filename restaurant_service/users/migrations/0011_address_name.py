# Generated by Django 5.0.6 on 2024-07-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_userprofile_address_remove_userprofile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(default='Not specified', max_length=50),
            preserve_default=False,
        ),
    ]
