# Generated by Django 4.1.4 on 2023-03-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authprovider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authclient',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authprovider.authservice'),
            preserve_default=False,
        ),
    ]