# Generated by Django 3.2.5 on 2022-01-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_ordertimeline_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertimeline',
            name='arrived_at_us_sort_facility',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
