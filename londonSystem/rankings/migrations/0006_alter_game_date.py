# Generated by Django 4.2.10 on 2024-04-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0005_rename_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(),
        ),
    ]
