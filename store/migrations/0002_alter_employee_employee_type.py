# Generated by Django 4.2.7 on 2023-12-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time'), ('Contract', 'Contract'), ('Temporary', 'Temporary')], max_length=20, null=True),
        ),
    ]
