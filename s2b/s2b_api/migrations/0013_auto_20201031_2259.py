# Generated by Django 2.2.10 on 2020-10-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0012_auto_20201031_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='leaving_act_reason',
            field=models.CharField(blank=True, choices=[('d', 'Смерть'), ('l', 'Передача в собственность (под опеку)')], help_text='Причина выбытия', max_length=1, null=True, verbose_name='Причина выбытия'),
        ),
    ]
