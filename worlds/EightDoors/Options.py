from dataclasses import dataclass

from Options import *


class Goal(Choice):
    """
    Choose The Goal of Your Game
    Sad: Defeat Faith
    Good: Defeat Faith with all 7 Reincarnation Flowers
    True: Defeat Faith With all Reincarnation Flowers and Mirror Pieces
    Fugitive Souls Hunt Configurable Goal
    """
    display_name = "Goal"
    option_sad = 0
    option_good = 1
    option_true = 2
    option_fugitive_souls_hunt = 3
    default = option_sad

class RequiredFugitiveSouls(Range):
    """Number of Fugitive Souls required to complete the game."""
    display_name = "Required Fugitive Souls"
    range_start = 0
    range_end = 48
    default = 20

class StartingMoney(Range):
    """Amount of starting money (Coins) to begin the game with."""
    display_name = "Starting Money"
    range_start = 0
    range_end = 1000
    default = 0

@dataclass
class EightDoorsOptions(PerGameCommonOptions):
    goal: Goal
    requiredfugitivesouls: RequiredFugitiveSouls
    startingmoney: StartingMoney

    start_inventory_from_pool: StartInventoryPool