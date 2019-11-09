from game.newcards.discard_card import DiscardCard
from game.newcards.new_card import NewCard


class Heal(DiscardCard):
    def __init__(self):
        NewCard.__init__(self, "Heal", 3, "+ 2[Health]", "")

    def immediate_effect(self, player_that_bought_the_card, other_players):
        player_that_bought_the_card.update_health_by(2)
