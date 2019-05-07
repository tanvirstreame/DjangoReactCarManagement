# Generated by Django 2.0.5 on 2019-05-03 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0008_auto_20190503_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showroom',
            name='car',
        ),
        migrations.RemoveField(
            model_name='showroomowner',
            name='showroom',
        ),
        migrations.AddField(
            model_name='car',
            name='showroom',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='Car.ShowRoom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showroom',
            name='owner',
            field=models.ForeignKey(default=-0.1, on_delete=django.db.models.deletion.CASCADE, to='Car.ShowRoomOwner'),
            preserve_default=False,
        ),
    ]
