# Generated by Django 2.2.10 on 2020-10-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0005_worker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sterilization_date',
            field=models.CharField(help_text='Дата стериллизации', max_length=40, null=True, verbose_name='Дата стериллизации'),
        ),
    ]
