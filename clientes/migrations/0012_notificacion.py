# Generated by Django 4.2.7 on 2023-11-23 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_usernotificationsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('leida', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
