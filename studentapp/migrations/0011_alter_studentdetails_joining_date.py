# Generated by Django 4.1 on 2022-08-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0010_alter_studentdetails_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='joining_date',
            field=models.DateField(null=True),
        ),
    ]
