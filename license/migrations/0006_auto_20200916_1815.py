# Generated by Django 3.1.1 on 2020-09-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0005_auto_20200916_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_type',
            field=models.CharField(choices=[('0', 'Javascript_sdk'), ('1', 'Ios_sdk'), ('2', 'Android_sdk')], max_length=1),
        ),
        migrations.AlterField(
            model_name='license',
            name='package',
            field=models.CharField(choices=[('0', 'Production'), ('0', 'Evaluation')], max_length=1),
        ),
    ]
