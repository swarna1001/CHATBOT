# Generated by Django 3.2 on 2022-05-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20220520_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
