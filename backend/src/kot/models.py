from django.db import models


# Create your models here.
class User(models.Model):
    monster_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateTimeField()


class Dice(models.Model):
    DICE_VALUE = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Two'),
        ('4', 'Energy'),
        ('5', 'Attack'),
        ('6', 'Heal'),
    )
    DICE_SELECTED = (
        ('Y', 'Selected'),
        ('N', 'Not-Selected'),
    )
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dice1 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice1_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice2 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice2_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice3 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice3_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice4 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice4_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice5 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice5_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    dice6 = models.CharField(max_length=1, choices=DICE_VALUE)
    dice6_selected = models.CharField(max_length=1, choices=DICE_SELECTED)
    date_created = models.DateTimeField()


class Game(models.Model):
    GAME_RESULT = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('I', 'In-Progress'),
    )
    # game_id = models.IntegerField(primary_key=True)
    # should cascade be applied below.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_winner = models.CharField(max_length=1, choices=GAME_RESULT)
    num_players = models.IntegerField()
    player_position = models.IntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()


class Play(models.Model):
    MONSTER_POSITION = (
        ('T', 'In-Tokyo'),
        ('O', 'Outside-Tokyo'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    dice = models.ForeignKey(Dice, on_delete=models.CASCADE)
    card_purchased = models.CharField(max_length=30)
    card_used = models.CharField(max_length=30)
    location = models.CharField(max_length=1, choices=MONSTER_POSITION)
    victory_points = models.IntegerField()
    energy_cubes = models.IntegerField()
    life_points = models.IntegerField()
    date_created = models.DateTimeField()