# Generated by Django 2.2.1 on 2019-07-31 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychotherapy', '0003_about_home_prices'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prices',
            options={'verbose_name_plural': 'Prices'},
        ),
        migrations.AlterField(
            model_name='prices',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^([+]46)(7[0236])\\s?-?\\s?(\\d{4})\\s?(\\d{3})$')]),
        ),
    ]
