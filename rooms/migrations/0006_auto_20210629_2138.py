# Generated by Django 2.2.5 on 2021-06-29 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210619_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to=settings.AUTH_USER_MODEL),
        ),
    ]
