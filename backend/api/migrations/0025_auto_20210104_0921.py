# Generated by Django 2.2.13 on 2021-01-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_scrimmage_map_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrimmage',
            name='map_ids',
            field=models.TextField(null=True),
        ),
    ]
