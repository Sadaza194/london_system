# Generated by Django 4.2.10 on 2024-03-22 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0003_alter_games_w_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='w_player',
            field=models.CharField(max_length=100),
        ),
    ]