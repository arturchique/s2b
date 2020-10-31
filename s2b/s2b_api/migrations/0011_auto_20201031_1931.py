# Generated by Django 2.2.10 on 2020-10-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0010_auto_20201031_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animal_id',
            field=models.CharField(help_text='Идентификационная метка', max_length=50, null=True, unique=True, verbose_name='Идентификационная метка'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='birth_date',
            field=models.CharField(help_text='Возраст, дата рождения', max_length=23, verbose_name='Возраст, дата рождения'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='medical_checkup_date',
            field=models.CharField(blank=True, help_text='Дата медосмотра', max_length=23, null=True, verbose_name='Дата медосмотра'),
        ),
    ]