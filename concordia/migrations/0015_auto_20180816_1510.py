# Generated by Django 2.0.7 on 2018-08-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0014_auto_20180816_1448")]

    operations = [
        migrations.AlterField(
            model_name="pageinuse",
            name="created_on",
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name="pageinuse", name="updated_on", field=models.DateTimeField()
        ),
    ]
