# Generated by Django 4.2.6 on 2023-11-05 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_reviewpack_rating_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewpack',
            name='r_upload_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
