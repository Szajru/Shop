# Generated by Django 4.1 on 2022-10-07 09:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0025_useracivity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAcivity',
            new_name='UserActivity',
        ),
    ]