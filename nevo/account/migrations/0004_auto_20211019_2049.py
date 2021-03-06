# Generated by Django 3.2.8 on 2021-10-19 15:19

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_accountuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='accountuser',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
