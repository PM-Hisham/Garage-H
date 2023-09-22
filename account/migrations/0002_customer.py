# Generated by Django 4.2.4 on 2023-09-01 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectservice', models.CharField(choices=[('periodic service', 'periodic service'), ('wheel allignment', 'wheel allignment'), ('car polish and waxing', 'car polish and waxing'), ('car wash', 'car wash')], default='car wash', max_length=300)),
                ('date', models.DateField()),
                ('timeslot', models.CharField(choices=[('8:00 am - 10:00 am', '8:00 am - 10:00 am'), ('10:00 am - 12:00 pm', '10:00 am - 12:00 pm'), ('12:00 am - 2:00 pm', '12:00 am - 2:00 pm'), ('3:00 am - 5:00 pm', '3:00 am - 5:00 pm'), ('5:00 am - 7:00 pm', '5:00 am - 7:00 pm')], default='8:00 am - 10:00 am', max_length=300)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
