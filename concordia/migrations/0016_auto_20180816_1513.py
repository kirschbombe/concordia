# Generated by Django 2.0.7 on 2018-08-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0015_auto_20180816_1510")]

    operations = [
        migrations.AlterField(
            model_name="pageinuse",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="pageinuse",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
