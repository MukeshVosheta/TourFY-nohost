# Generated by Django 4.2.6 on 2023-11-02 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_reviewpack'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviewpack',
            unique_together={('r_pack', 'r_user')},
        ),
    ]
