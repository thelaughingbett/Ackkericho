# Generated by Django 5.0.6 on 2024-07-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clergy',
            name='Image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
