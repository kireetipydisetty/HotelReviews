# Generated by Django 3.0.8 on 2020-07-11 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0006_delete_searchhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Review',
            new_name='Reviews',
        ),
    ]