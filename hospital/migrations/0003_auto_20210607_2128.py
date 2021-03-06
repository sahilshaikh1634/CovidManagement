# Generated by Django 2.2.10 on 2021-06-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210607_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='number',
            new_name='registration_number',
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='OCCUPIED_vaccine_slot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='total_vaccine_slot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='vaccine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hospital_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
