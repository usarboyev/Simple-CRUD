# Generated by Django 4.2.6 on 2023-10-07 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-id']},
        ),
    ]
