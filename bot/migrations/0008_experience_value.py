# Generated by Django 3.2 on 2022-07-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20220526_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]