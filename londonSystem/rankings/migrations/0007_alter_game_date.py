# Generated by Django 4.2.10 on 2024-04-12 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0006_alter_game_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
