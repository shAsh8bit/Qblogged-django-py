# Generated by Django 3.2 on 2021-05-13 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussiona',
            old_name='uaer',
            new_name='user',
        ),
    ]