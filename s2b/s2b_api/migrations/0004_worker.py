# Generated by Django 2.2.10 on 2020-10-31 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s2b_api', '0003_auto_20201031_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, choices=[('s', 'Супер Админ'), ('d', 'Работник Департамента'), ('a', 'Администратор приюта'), ('w', 'Работник приюта')], help_text='Должность', max_length=1, null=True, verbose_name='Должность')),
                ('shelter', models.ForeignKey(blank=True, help_text='Приют', on_delete=django.db.models.deletion.CASCADE, to='s2b_api.Shelter', verbose_name='Приют')),
                ('user', models.OneToOneField(help_text='Пользователь', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
