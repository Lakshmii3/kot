from game.newcards.discard_cards.victory_point_manipulation_cards.heal import Heal


def test_heal_adds_2_health(player):
    Heal().immediate_effect(player, None)
    assert player.current_health == 2


def test_heal_costs_3_energy():
    assert Heal().cost == 3
