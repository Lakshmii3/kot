# Generated by Django 2.2.6 on 2019-10-14 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_details', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dice1', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice1_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('Dice2', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice2_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('Dice3', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice3_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('Dice4', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice4_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('Dice5', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice5_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('Dice6', models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Two'), ('4', 'Energy'), ('5', 'Attack'), ('6', 'Heal')], max_length=1)),
                ('dice6_selected', models.CharField(choices=[('Y', 'Selected'), ('N', 'Not-Selected')], max_length=1)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('is_winner', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('I', 'In-Progress')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('user_monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.Monster')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('T', 'In-Tokyo'), ('O', 'Outside-Tokyo')], max_length=1)),
                ('victory_points', models.IntegerField()),
                ('energy_cube', models.IntegerField()),
                ('life_points', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.Card')),
                ('dice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.Dice')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.User')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.User'),
        ),
        migrations.AddField(
            model_name='dice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kot.User'),
        ),
    ]
