from dataclasses import dataclass
from random import choice

from Options import PerGameCommonOptions, DeathLink, Choice, Toggle, OptionGroup, Range, StartInventoryPool


class RingLink(Choice):
    """
    Whether your ergo gain/loss is linked to other players.
    Off disables the feature.
    On enables the feature
    Hard enable sending and receiving more difficult ring losses
    """
    display_name = "Ring Link"
    option_off = 0
    option_on = 1
    option_hard = 2
    default = option_off


class ErgoToRingRatio(Range):
    """
    How much Ergo should be equal to one Ring in Ring Link
    """
    display_name = "Ergo to Ring Ratio"
    range_start = 1
    range_end = 100
    default = 10


class Goal(Choice):
    """
    Choose your goal for the multiworld
    King of Puppets: Defeat Romeo King of Puppets
    Simon Manus: Defeat Simon Manus
    Nameless Puppet: Defeat Nameless Puppet  (Note this can be missed if you don't reach the humanity threshold)
    """
    display_name = "Goal"
    option_king_of_puppets = 0
    option_simon_manus = 1
    option_nameless_puppet = 2
    default = option_simon_manus


class EarlyKratCentralStationMainEntranceKey(Choice):
    """
    Force Your Krat Central Station Main Entrance Key into an early sphere in your world or across all worlds.
    """
    display_name = "Early Krat Central Station Main Entrance Key"
    option_off = 0
    option_early_global = 1
    option_early_local = 2
    default = option_off


class EarlyEnigmaAssemblyTool(Choice):
    """
    Force Your Enigma Assembly Tool into an early sphere in your world or across all worlds.
    """
    display_name = "Enigma Assembly Tool"
    option_off = 0
    option_early_global = 1
    option_early_local = 2
    default = option_off


class ShopWeapons(Toggle):
    """
    Add Shop Weapons into the item pool (You can still obtain shop weapons in their respective shops)
    """
    display_name = "Shop Weapons"


class BossWeapons(Toggle):
    """
    Add Boss Weapons into the item pool (You can still obtain boss weapons via Alidoro)
    """
    display_name = "Boss Weapons"


class BossAmulets(Toggle):
    """
    Add Boss Amulets into the item pool (You can still obtain boss amulets via Alidoro)
    """
    display_name = "Boss Amulets"


class GoldenLie(Toggle):
    """
    Adds the Golden Lie into the item pool (you can still obtain it via humanity)
    """
    display_name = "Golden Lie"


class AdditionalQuartz(Range):
    """
    Add additional quarts to the item pool
    """
    display_name = "Additional Quartz"
    range_start = 0
    range_end = 35


@dataclass
class LiesOfPOptions(PerGameCommonOptions):
    death_link: DeathLink
    ring_link: RingLink
    ergo_to_ring_ratio: ErgoToRingRatio

    goal: Goal
    early_krat_central_station: EarlyKratCentralStationMainEntranceKey
    early_weapon_assemble: EarlyEnigmaAssemblyTool

    shop_weapons: ShopWeapons
    boss_weapons: BossWeapons
    golden_lie: GoldenLie
    boss_amulets: BossAmulets
    additional_quartz: AdditionalQuartz

    start_inventory_from_pool: StartInventoryPool
