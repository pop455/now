# Generated by Django 3.2.13 on 2022-05-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_rename_phonenumber_ordermodel_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='branch',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='subbranch',
            new_name='state',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='street',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]