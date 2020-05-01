# Generated by Django 2.2.5 on 2020-05-01 13:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cni', '0002_remove_profil_road'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profil',
            unique_together={('user', 'no_identity', 'birth_date')},
        ),
    ]