# Generated by Django 3.2.13 on 2022-05-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_ordermodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
