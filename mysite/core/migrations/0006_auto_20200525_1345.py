# Generated by Django 2.1.3 on 2020-05-25 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200525_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='pdf',
            new_name='video',
        ),
    ]