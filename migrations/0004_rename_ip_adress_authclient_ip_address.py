# Generated by Django 4.1.4 on 2023-03-23 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authprovider', '0003_alter_authclient_client_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authclient',
            old_name='ip_adress',
            new_name='ip_address',
        ),
    ]
