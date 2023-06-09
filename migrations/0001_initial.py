# Generated by Django 4.1.4 on 2023-03-23 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthClient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=255)),
                ('ip_adress', models.GenericIPAddressField()),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AuthService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
