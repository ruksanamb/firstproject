# Generated by Django 3.2.5 on 2022-08-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_studentdetails_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='joining_date',
            field=models.DateField(null=True),
        ),
    ]
