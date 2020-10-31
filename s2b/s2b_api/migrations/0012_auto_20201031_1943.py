# Generated by Django 2.2.10 on 2020-10-31 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0011_auto_20201031_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='catching_act',
            field=models.CharField(blank=True, help_text='Акт отлова', max_length=40, null=True, verbose_name='Акт отлова'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='catching_act_date',
            field=models.CharField(blank=True, help_text='Дата отлова', max_length=40, null=True, verbose_name='Дата отлова'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='catching_act_order',
            field=models.CharField(blank=True, help_text='Акт отлова', max_length=40, null=True, verbose_name='Акт отлова'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='catching_address',
            field=models.CharField(blank=True, help_text='Адрес места отлова', max_length=40, null=True, verbose_name='Адрес места отлова'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='entrance_act',
            field=models.CharField(help_text='Акт о поступлении', max_length=40, null=True, verbose_name='Акт о поступлении'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='leaving_act',
            field=models.CharField(blank=True, help_text='Акт о выбытии', max_length=40, null=True, verbose_name='Акт о выбытии'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='leaving_act_date',
            field=models.CharField(blank=True, help_text='Дата выбытия', max_length=40, null=True, verbose_name='Дата выбытия'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='legal_entity',
            field=models.CharField(blank=True, help_text='Юридическое лицо', max_length=40, null=True, verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='owner_name',
            field=models.CharField(blank=True, help_text='ФИО опекунов', max_length=40, null=True, verbose_name='ФИО опекунов'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='person_owner_name',
            field=models.CharField(blank=True, help_text='ФИО физического лица', max_length=40, null=True, verbose_name='ФИО физического лица'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='region',
            field=models.CharField(help_text='Административный округ', max_length=40, null=True, verbose_name='Административный округ'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.FloatField(help_text='Вес', max_length=8, verbose_name='Вес'),
        ),
    ]
