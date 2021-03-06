# Generated by Django 2.2.10 on 2021-06-07 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(blank=True, max_length=16)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hp_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.RemoveField(
            model_name='hospitalstuff',
            name='verify',
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='docter_details',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='OCCUPIED_icu_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='OCCUPIED_oxygen_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='OCCUPIED_regural_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='icu_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='oxygen_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalstuff',
            name='regural_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='HospitalProfile',
        ),
    ]
