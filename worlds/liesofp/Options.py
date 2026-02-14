from dataclasses import dataclass
from random import choice

from Options import PerGameCommonOptions, DeathLink, Choice, Toggle, OptionGroup, Range, StartInventoryPool


# TODO add options for NGP Amulets and Parts
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
    Nameless Puppet: Defeat Nameless Puppet (Note this can be missed if you don't reach the humanity threshold)
    Arlecchino Short: Defeat Arlecchino and the first 5 chapters of the base game
    Arlecchino: Defeat Arlecchino including the full base game
    Simon Manus and Arlecchino: Defeat both Simon Manus and Arlecchino
    Nameless Puppet and Arlecchino: Defeat both Nameless Puppet and Arlecchino (Note this can be missed if you don't reach the humanity threshold)
    """
    display_name = "Goal"
    option_king_of_puppets = 0
    option_simon_manus = 1
    option_nameless_puppet = 2
    option_arlecchino_short = 3
    option_arlecchino = 4
    option_simon_manus_and_arlecchino = 5
    option_nameless_puppet_and_arlecchino = 6
    default = option_simon_manus


class DLC(Choice):
    """
    Choose if the DLC will be enabled (Note any Arlecchino goal enables DLC by default)
    """
    display_name = "DLC"
    option_disable = 0
    option_enable = 1
    default = option_disable


class DLCItems(Choice):
    """
    Choose if the DLC items are added to the item pool(Does nothing if DLC is enabled or Arlecchino goal is set)
    Adds 5 locations on equipping Black Rabbit Brotherhood Clothes
    """
    display_name = "DLC Items"
    option_disable = 0
    option_enable = 1
    default = option_disable


class RequireHornForTwoFacedOverseer(Choice):
    """
    Enable: Daylight-Weathered Horn is required to fight Two Face Overseer
    Disable: Daylight-Weathered Horn isn't required to fight Two Face Overseer
    """
    display_name = "Require Horn for Two-Faced Overseer"
    option_disable = 0
    option_enable = 1
    default = option_disable


class RequireBowForCarnival(Choice):
    """
    Enable: Royal Horn Bow is Logically required to get some carnival mini-game checks
    Disable: May have to use consumables to complete carnival mini-games
    """
    display_name = "Require Bow For Carnival Games"
    option_disable = 0
    option_enable = 1
    default = option_disable

class RequireGrindstoneForChapter4(Choice):
    """
    choose if Grindstone is Logically required for chapter 4 to be in logic
    """
    display_name = "Require Grindstone For Chapter 4"
    option_disable = 0
    option_enable = 1
    default = option_disable

class RequireFlameGrindstoneForArcheBishop(Choice):
    """
    choose if Flame Grindstone is Logically required for Arche Bishop to be in logic
    """
    display_name = "Require Flame Grindstone For Arche Bishop"
    option_disable = 0
    option_enable = 1
    default = option_disable

class RequireUpgradeCoreForDLCChapter2(Choice):
    """
    choose if Upgrade Core is Logically required for Chapter 2 of the DLC to be in logic
    """
    display_name = "Require Upgrade Core For DLC Chapter 2"
    option_disable = 0
    option_enable = 1
    default = option_disable

class Chapter6Access(Choice):
    """
    early: Only requires Hotel access + Combat Logic Rules.
    Early_porgan: Requires Hotel access and can reach Scrapped Watchman + Combat Logic Rules.
    Vanilla: Requires access to first Black Rabbit Brotherhood fight + Combat Logic Rules
    """
    display_name = "Require P-organ For Early Chapter 6"
    option_early = 0
    option_early_porgan = 1
    option_vanilla = 3
    default = option_early_porgan

class QuartzCombatLogic(Choice):
    """
    Enable: Quartz are included in logic
    Disable: Quartz are not included in logic
    """
    display_name = "Quartz Combat Logic"
    option_enable = 0
    option_disable = 1
    default = option_enable

class CombatLogic(Choice):
    """
    Change how impactful combat logic is for your game
    """
    display_name = "Combat Logic"
    option_off = 0
    option_easy = 1
    option_normal = 2
    option_hard = 3
    default = option_normal


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
    dlc: DLC
    dlc_items: DLCItems

    require_horn_overseer: RequireHornForTwoFacedOverseer
    require_bow_minigames: RequireBowForCarnival
    require_grindstone_chapter4: RequireGrindstoneForChapter4
    require_flame_grindstone_bishop: RequireFlameGrindstoneForArcheBishop
    require_upgrade_core_dlc_chapter2: RequireUpgradeCoreForDLCChapter2
    chapter6_access: Chapter6Access
    quartz_combat_logic: QuartzCombatLogic
    combat_logic: CombatLogic
    early_krat_central_station: EarlyKratCentralStationMainEntranceKey
    early_weapon_assemble: EarlyEnigmaAssemblyTool

    shop_weapons: ShopWeapons
    boss_weapons: BossWeapons
    golden_lie: GoldenLie
    boss_amulets: BossAmulets
    additional_quartz: AdditionalQuartz

    start_inventory_from_pool: StartInventoryPool
