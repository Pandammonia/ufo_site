# Generated by Django 4.0.5 on 2022-06-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_blogpost_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
