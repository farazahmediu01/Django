# Generated by Django 4.2.7 on 2023-12-09 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_feedback_rating_alter_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('1', 'Available'), ('0', 'Booked')], default='1', max_length=1),
        ),
    ]
