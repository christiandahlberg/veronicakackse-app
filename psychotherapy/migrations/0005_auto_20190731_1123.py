# Generated by Django 2.2.1 on 2019-07-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychotherapy', '0004_auto_20190731_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': 'Home'},
        ),
        migrations.AddField(
            model_name='home',
            name='body',
            field=models.TextField(default='Type here...'),
        ),
    ]