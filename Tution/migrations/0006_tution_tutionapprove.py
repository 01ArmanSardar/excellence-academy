# Generated by Django 5.1.1 on 2024-09-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tution', '0005_tution_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tution',
            name='TutionApprove',
            field=models.BooleanField(default=False),
        ),
    ]
