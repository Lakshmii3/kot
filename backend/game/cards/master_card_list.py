# Energy Manipulation Cards
from game.cards.discard_cards.energy_manipulation_cards.energize import Energize

# Health Manipulation cards
from game.cards.discard_cards.health_manipulation_cards.fire_blast import FireBlast
from game.cards.discard_cards.health_manipulation_cards.high_altitude_bombing import HighAltitudeBombing

# Multi-Manipulation Cards
from game.cards.discard_cards.multi_manipulation_cards.gas_refinery import GasRefinery
from game.cards.discard_cards.multi_manipulation_cards.jet_fighters import JetFighters

# Victory Point Manipulation Cards
from game.cards.discard_cards.victory_point_manipulation_cards.apartment_building import ApartmentBuilding
from game.cards.discard_cards.victory_point_manipulation_cards.commuter_train import CommuterTrain
from game.cards.discard_cards.victory_point_manipulation_cards.corner_store import CornerStore
from game.cards.discard_cards.victory_point_manipulation_cards.evacuation_orders import EvacuationOrders
from game.cards.discard_cards.victory_point_manipulation_cards.skyscraper import Skyscraper


def get_all_cards():
    """
    Serves as the master list of all cards to add to the deck.

    Create lists to reflect package structure and add individual cards to each list.
    If a new list is created extend it onto the full_list_of_cards
    """
    energy_manipulation_cards = [Energize()]

    health_manipulation_cards = [FireBlast(), HighAltitudeBombing()]

    multi_manipulation_cards = [GasRefinery(), JetFighters()]

    victory_point_manipulation_cards = [ApartmentBuilding(), CommuterTrain(), CornerStore(),
                                        EvacuationOrders(), Skyscraper()]

    full_list_of_cards = []
    full_list_of_cards.extend(energy_manipulation_cards)
    full_list_of_cards.extend(health_manipulation_cards)
    full_list_of_cards.extend(multi_manipulation_cards)
    full_list_of_cards.extend(victory_point_manipulation_cards)

    return full_list_of_cards
