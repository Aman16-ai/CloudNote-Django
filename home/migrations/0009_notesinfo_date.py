# Generated by Django 3.1.5 on 2021-04-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_notesinfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesinfo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
