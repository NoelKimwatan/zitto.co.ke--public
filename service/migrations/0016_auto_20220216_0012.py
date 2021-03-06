# Generated by Django 3.2.5 on 2022-02-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_guestorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestorder',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='guestorder',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestorder',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='guestorder',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='guestorder',
            name='identifier',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
