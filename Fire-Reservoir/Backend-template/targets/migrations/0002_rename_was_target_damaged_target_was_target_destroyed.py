# Generated by Django 4.2.6 on 2023-10-16 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='was_target_damaged',
            new_name='was_target_destroyed',
        ),
    ]
