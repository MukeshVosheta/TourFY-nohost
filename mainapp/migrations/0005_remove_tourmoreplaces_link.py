# Generated by Django 4.2.6 on 2023-10-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_tourmoreplaces_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourmoreplaces',
            name='link',
        ),
    ]
