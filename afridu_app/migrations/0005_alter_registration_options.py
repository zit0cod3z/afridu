# Generated by Django 4.2.2 on 2024-09-04 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afridu_app', '0004_rename_attachemt_registration_attachment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ('submitted_at',)},
        ),
    ]
