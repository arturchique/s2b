# Generated by Django 2.2.10 on 2020-10-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0009_animal_catching_act_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='catching_act_order',
            field=models.CharField(blank=True, help_text='Акт отлова', max_length=15, null=True, verbose_name='Акт отлова'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='leaving_act_date',
            field=models.CharField(blank=True, help_text='Дата выбытия', max_length=20, null=True, verbose_name='Дата выбытия'),
        ),
    ]
