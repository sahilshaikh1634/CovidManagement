# Generated by Django 2.2.10 on 2021-06-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20210607_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospitalstuff',
            options={'verbose_name': 'HospitalStuff', 'verbose_name_plural': 'HospitalStuffs'},
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='VACANT_icu_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='VACANT_oxygen_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='VACANT_regural_beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hospitalstuff',
            name='VACANT_vaccine_slot',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hospital_profile',
            field=models.BooleanField(default=True),
        ),
    ]