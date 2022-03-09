# Generated by Django 3.2.5 on 2021-11-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_ordertimeline_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordertimeline',
            name='status',
            field=models.CharField(choices=[('SRC', 'Ship request created'), ('SRP', 'Ship request processed'), ('PPC', 'Purchase payment completed'), ('IP', 'Item purchased'), ('ETW', 'Enroute to warehouse'), ('RAW', 'Received at warehouse'), ('BPFOS', 'Being prepared for overseas shipping'), ('DFW', 'Departed from warehouse'), ('AADSF', 'Arrived at Dubai sort facility'), ('DTDA', 'Dispatched to destination airport'), ('AADA', 'Arrived at destination airport'), ('UIC', 'Undergoing import clearance'), ('PBPFD', 'Package being prepared for delivery'), ('EDL', 'Enter delivery location'), ('SPP', 'Shipping payment pending'), ('SPC', 'Shipping payment complete'), ('RFD', 'Ready for delivery'), ('OFD', 'Out for delivery'), ('D', 'Delivered')], max_length=6),
        ),
    ]
