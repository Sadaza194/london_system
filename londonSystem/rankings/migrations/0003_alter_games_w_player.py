# Generated by Django 4.2.10 on 2024-03-22 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0002_games_rename_fname_player_name_remove_player_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='w_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rankings.player'),
        ),
    ]
