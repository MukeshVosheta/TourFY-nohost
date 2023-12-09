# Generated by Django 4.2.6 on 2023-10-17 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_packages_end_date_packages_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourmoreplaces',
            name='source_link',
            field=models.URLField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]