# Generated by Django 5.0.4 on 2024-04-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeps', '0004_rename_nompeeps_nompeep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nompeep',
            name='date',
            field=models.DateField(),
        ),
    ]
