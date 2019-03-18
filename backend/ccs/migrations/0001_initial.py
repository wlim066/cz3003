# Generated by Django 2.1.1 on 2019-03-18 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_person_name', models.CharField(max_length=20)),
                ('report_person_phone', models.CharField(max_length=12)),
                ('report_person_location', models.CharField(max_length=200)),
                ('incident_location', models.CharField(max_length=200)),
                ('incident_type', models.CharField(choices=[('dengue', 'Dengue'), ('haze', 'Haze')], default='dengue', max_length=10)),
                ('incident_assistanceRequired', models.CharField(choices=[('emergencyAmbulance', 'Emergency Ambulance'), ('rescueEvacuation', 'Rescue Evacuation')], default='emergencyAmbulance', max_length=20)),
                ('incident_status', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending', max_length=20)),
                ('key_indicator_numOfInjured', models.IntegerField(blank=True, null=True)),
                ('key_indicator_numOfdeaths', models.IntegerField(blank=True, null=True)),
                ('key_indicator_estimateStartingTime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('record_id',),
            },
        ),
    ]