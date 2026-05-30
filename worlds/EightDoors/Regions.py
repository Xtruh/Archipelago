from typing import Callable, Optional, Dict

from BaseClasses import Region, Entrance
from .ItemList import *
from .Options import EightDoorsOptions



def create_regions(world, options: EightDoorsOptions):
    regions: Dict[str, Region] = \
        {
            "Menu": Region("Menu", world.player, world.multiworld),
            "Kingdom Of Yama 1": Region("Kingdom Of Yama 1", world.player, world.multiworld),
            "Kingdom Of Yama 2": Region("Kingdom Of Yama 2", world.player, world.multiworld),
            "Kingdom Of Yama 3": Region("Kingdom Of Yama 3", world.player, world.multiworld),
            "Kingdom Of Yama 4": Region("Kingdom Of Yama 4", world.player, world.multiworld),
            "Kingdom Of Yama 5": Region("Kingdom Of Yama 5", world.player, world.multiworld),
            "Kingdom Of Yama 6": Region("Kingdom Of Yama 6", world.player, world.multiworld),
            "Kingdom Of Yama 7": Region("Kingdom Of Yama 7", world.player, world.multiworld),
            "Kingdom Of Yama 8": Region("Kingdom Of Yama 8", world.player, world.multiworld),
            "Death Tavern": Region("Death Tavern", world.player, world.multiworld),
            "Stone Mountain 1": Region("Stone Mountain 1", world.player, world.multiworld),
            "Stone Mountain 2": Region("Stone Mountain 2", world.player, world.multiworld),
            "Stone Mountain 3": Region("Stone Mountain 3", world.player, world.multiworld),
            "Stone Mountain 4": Region("Stone Mountain 4", world.player, world.multiworld),
            "Stone Mountain 5": Region("Stone Mountain 5", world.player, world.multiworld),
            "Stone Mountain 6": Region("Stone Mountain 6", world.player, world.multiworld),
            "Stone Mountain 7": Region("Stone Mountain 7", world.player, world.multiworld),
            "Stone Mountain 8": Region("Stone Mountain 8", world.player, world.multiworld),
            "Stone Mountain 9": Region("Stone Mountain 9", world.player, world.multiworld),
            "Stone Mountain 10": Region("Stone Mountain 10", world.player, world.multiworld),
            "Stone Mountain 11": Region("Stone Mountain 11", world.player, world.multiworld),
            "Stone Mountain 12": Region("Stone Mountain 12", world.player, world.multiworld),
            "Misty Forest 1": Region("Misty Forest 1", world.player, world.multiworld),
            "Misty Forest 3": Region("Misty Forest 3", world.player, world.multiworld),
            "Misty Forest 4": Region("Misty Forest 4", world.player, world.multiworld),
            "Misty Forest 5": Region("Misty Forest 5", world.player, world.multiworld),
            "Misty Forest 6": Region("Misty Forest 6", world.player, world.multiworld),
            "Misty Forest 7": Region("Misty Forest 7", world.player, world.multiworld),
            "Misty Forest 8": Region("Misty Forest 8", world.player, world.multiworld),
            "Misty Forest 9": Region("Misty Forest 9", world.player, world.multiworld),
            "Misty Forest 10": Region("Misty Forest 10", world.player, world.multiworld),
            "Misty Forest 11": Region("Misty Forest 11", world.player, world.multiworld),
            "Misty Forest 13": Region("Misty Forest 13", world.player, world.multiworld),
            "Misty Forest 16": Region("Misty Forest 16", world.player, world.multiworld),
            "Misty Forest 18": Region("Misty Forest 18", world.player, world.multiworld),
            "Barron Grounds 1": Region("Barron Grounds 1", world.player, world.multiworld),
            "Reincarnation Center": Region("Reincarnation Center", world.player, world.multiworld),
            "Barron Grounds 4": Region("Barron Grounds 4", world.player, world.multiworld),
            "Barron Grounds 3": Region("Barron Grounds 3", world.player, world.multiworld),
            "Barron Grounds 5": Region("Barron Grounds 5", world.player, world.multiworld),
            "Barron Grounds 7": Region("Barron Grounds 7", world.player, world.multiworld),
            "Barron Grounds 9": Region("Barron Grounds 9", world.player, world.multiworld),
            "Barron Grounds 12": Region("Barron Grounds 12", world.player, world.multiworld),
            "Barron Grounds 13": Region("Barron Grounds 13", world.player, world.multiworld),
            "Barron Grounds 14": Region("Barron Grounds 14", world.player, world.multiworld),
            "Barron Grounds 11": Region("Barron Grounds 11", world.player, world.multiworld),
            "Barron Grounds 6": Region("Barron Grounds 6", world.player, world.multiworld),
            "Barron Grounds 16": Region("Barron Grounds 16", world.player, world.multiworld),
            "Barron Grounds 17": Region("Barron Grounds 17", world.player, world.multiworld),
            "Barron Grounds 19": Region("Barron Grounds 19", world.player, world.multiworld),
            "Barron Grounds 20": Region("Barron Grounds 20", world.player, world.multiworld),
            "Workshop": Region("Workshop", world.player, world.multiworld),
            "Crimson Mines 2": Region("Crimson Mines 2", world.player, world.multiworld),
            "Crimson Mines 1": Region("Crimson Mines 1", world.player, world.multiworld),
            "Crimson Mines 3": Region("Crimson Mines 3", world.player, world.multiworld),
            "Crimson Mines 4": Region("Crimson Mines 4", world.player, world.multiworld),
            "Crimson Mines 5": Region("Crimson Mines 5", world.player, world.multiworld),
            "Crimson Mines 6": Region("Crimson Mines 6", world.player, world.multiworld),
            "Crimson Mines 8": Region("Crimson Mines 8", world.player, world.multiworld),
            "Crimson Mines 10": Region("Crimson Mines 10", world.player, world.multiworld),
            "Crimson Mines 11": Region("Crimson Mines 11", world.player, world.multiworld),
            "Crimson Mines 13": Region("Crimson Mines 13", world.player, world.multiworld),
            "Crimson Mines 14": Region("Crimson Mines 14", world.player, world.multiworld),
            "Crimson Mines 18": Region("Crimson Mines 18", world.player, world.multiworld),
            "Frozen Plateau 2": Region("Frozen Plateau 2", world.player, world.multiworld),
            "Frozen Plateau 3": Region("Frozen Plateau 3", world.player, world.multiworld),
            "Dispatch Station": Region("Dispatch Station", world.player, world.multiworld),
            "Frozen Plateau 5": Region("Frozen Plateau 5", world.player, world.multiworld),
            "Frozen Plateau 8": Region("Frozen Plateau 8", world.player, world.multiworld),
            "Frozen Plateau 18": Region("Frozen Plateau 18", world.player, world.multiworld),
            "Frozen Plateau 17": Region("Frozen Plateau 17", world.player, world.multiworld),
            "Frozen Plateau 6": Region("Frozen Plateau 6", world.player, world.multiworld),
            "Frozen Plateau 9": Region("Frozen Plateau 9", world.player, world.multiworld),
            "Frozen Plateau 12": Region("Frozen Plateau 12", world.player, world.multiworld),
            "Frozen Plateau 13": Region("Frozen Plateau 13", world.player, world.multiworld),
            "Frozen Plateau 14": Region("Frozen Plateau 14", world.player, world.multiworld),
            "Frozen Plateau 15": Region("Frozen Plateau 15", world.player, world.multiworld),
            "Control Room": Region("Control Room", world.player, world.multiworld),
            "Underground Waterway 3": Region("Underground Waterway 3", world.player, world.multiworld),
            "Underground Waterway 4": Region("Underground Waterway 4", world.player, world.multiworld),
            "Underground Waterway 16": Region("Underground Waterway 16", world.player, world.multiworld),
            "Underground Waterway 17": Region("Underground Waterway 17", world.player, world.multiworld),
            "Underground Waterway 14": Region("Underground Waterway 14", world.player, world.multiworld),
            "Underground Waterway 6": Region("Underground Waterway 6", world.player, world.multiworld),
            "Underground Waterway 7": Region("Underground Waterway 7", world.player, world.multiworld),
            "Underground Waterway 8": Region("Underground Waterway 8", world.player, world.multiworld),
            "Underground Waterway 9": Region("Underground Waterway 9", world.player, world.multiworld),
            "Underground Waterway 10": Region("Underground Waterway 10", world.player, world.multiworld),
            "Underground Waterway 13": Region("Underground Waterway 13", world.player, world.multiworld),
            "Underground Waterway 15": Region("Underground Waterway 15", world.player, world.multiworld),
            "Land of Abundance 17": Region("Land of Abundance 17", world.player, world.multiworld),
            "Land of Abundance 16": Region("Land of Abundance 16", world.player, world.multiworld),
            "Land of Abundance 3": Region("Land of Abundance 3", world.player, world.multiworld),
            "Land of Abundance 2": Region("Land of Abundance 2", world.player, world.multiworld),
            "Land of Abundance 5": Region("Land of Abundance 5", world.player, world.multiworld),
            "Land of Abundance 4": Region("Land of Abundance 4", world.player, world.multiworld),
            "Land of Abundance 7": Region("Land of Abundance 7", world.player, world.multiworld),
            "Land of Abundance 8": Region("Land of Abundance 8", world.player, world.multiworld),
            "Land of Abundance 6": Region("Land of Abundance 6", world.player, world.multiworld),
            "Land of Abundance 9": Region("Land of Abundance 9", world.player, world.multiworld),
            "Abyss": Region("Abyss", world.player, world.multiworld),
        }

    connect(world.player, "menu-to-KOY1", regions["Menu"], regions["Kingdom Of Yama 1"])

    connect(world.player, "KOY1-to-KOY2", regions["Kingdom Of Yama 1"], regions["Kingdom Of Yama 2"],)

    connect(world.player, "KOY2-to-KOY3", regions["Kingdom Of Yama 2"], regions["Kingdom Of Yama 3"],)

    connect(world.player, "KOY3-to-KOY4", regions["Kingdom Of Yama 3"], regions["Kingdom Of Yama 4"], )

    connect(world.player, "KOY4-to-KOY5", regions["Kingdom Of Yama 4"], regions["Kingdom Of Yama 5"],
            lambda state: state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 1))

    connect(world.player, "KOY5-to-KOY6", regions["Kingdom Of Yama 5"], regions["Kingdom Of Yama 6"], )

    connect(world.player, "KOY5-to-KOY7", regions["Kingdom Of Yama 5"], regions["Kingdom Of Yama 7"], )

    connect(world.player, "KOY7-to-KOY8", regions["Kingdom Of Yama 7"], regions["Kingdom Of Yama 8"], )


    connect(world.player, "KOY8-to-DT", regions["Kingdom Of Yama 8"], regions["Death Tavern"], )

    connect(world.player, "DT-to-SM1", regions["Death Tavern"], regions["Stone Mountain 1"], )

    connect(world.player, "SM1-to-SM2", regions["Stone Mountain 1"], regions["Stone Mountain 2"], )

    connect(world.player, "SM2-to-SM3", regions["Stone Mountain 2"], regions["Stone Mountain 3"],
        lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_Dash], world.player, 1))

    connect(world.player, "SM2-to-SM4", regions["Stone Mountain 2"], regions["Stone Mountain 4"],
        lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_Dash], world.player, 1))

    connect(world.player, "SM4-to-SM5", regions["Stone Mountain 4"], regions["Stone Mountain 5"], )

    connect(world.player, "SM4-to-SM6", regions["Stone Mountain 4"], regions["Stone Mountain 6"], )

    connect(world.player, "SM6-to-SM9", regions["Stone Mountain 6"], regions["Stone Mountain 7"], )

    connect(world.player, "SM7-to-SM8", regions["Stone Mountain 7"], regions["Stone Mountain 8"], )

    connect(world.player, "SM8-to-SM9", regions["Stone Mountain 8"], regions["Stone Mountain 9"], )

    connect(world.player, "SM9-to-SM10", regions["Stone Mountain 9"], regions["Stone Mountain 10"],
        lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Sword], world.player, 1))

    connect(world.player, "SM7-to-SM11", regions["Stone Mountain 7"], regions["Stone Mountain 11"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], world.player, 1))

    connect(world.player, "SM11-to-SM12", regions["Stone Mountain 11"], regions["Stone Mountain 12"], )

    connect(world.player, "MF1-to-MF3", regions["Misty Forest 1"], regions["Misty Forest 3"], )

    connect(world.player, "MF3-to-MF4", regions["Misty Forest 3"], regions["Misty Forest 4"], )

    connect(world.player, "MF4-to-MF18", regions["Misty Forest 1"], regions["Misty Forest 3"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], world.player, 1))

    connect(world.player, "MF3-to-MF5", regions["Misty Forest 3"], regions["Misty Forest 5"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], world.player, 1))

    connect(world.player, "MF5-to-MF6", regions["Misty Forest 5"], regions["Misty Forest 6"], )

    connect(world.player, "MF6-to-MF7", regions["Misty Forest 6"], regions["Misty Forest 7"], )

    connect(world.player, "MF7-to-MF8", regions["Misty Forest 7"], regions["Misty Forest 8"], )

    connect(world.player, "MF7-to-MF16", regions["Misty Forest 7"], regions["Misty Forest 16"],
        lambda state: state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20))

    connect(world.player, "MF8-to-MF9", regions["Misty Forest 8"], regions["Misty Forest 9"], )

    connect(world.player, "MF9-to-MF10", regions["Misty Forest 9"], regions["Misty Forest 10"])

    connect(world.player, "MF10-to-MF11", regions["Misty Forest 10"], regions["Misty Forest 11"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Bow], world.player, 1))

    connect(world.player, "MF11-to-MF13", regions["Misty Forest 11"], regions["Misty Forest 13"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_Dash], world.player, 1)
                          and state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1))

    all_abilities = (
        ABILITIES_ID_TO_NAME[Abl_Dash],
        ABILITIES_ID_TO_NAME[Abl_WallHold],
        ABILITIES_ID_TO_NAME[Abl_DoubleJump],
        ABILITIES_ID_TO_NAME[Abl_SuperJump],
        ABILITIES_ID_TO_NAME[Abl_BreakWall],
        ABILITIES_ID_TO_NAME[Abl_SuperDash],
    )

    connect(world.player, "MF8-to-LOA17", regions["Misty Forest 8"], regions["Land of Abundance 17"],
        lambda state, items=all_abilities: all(state.has(i, world.player) for i in items)
                                                     and state.has(WEAPON_ID_TO_NAME[Wep_Fan], world.player, 1)
                                                     and state.has(WEAPON_ID_TO_NAME[Wep_Umbrella], world.player, 1))


    connect(world.player, "LOA17-to-LOA16", regions["Land of Abundance 17"], regions["Land of Abundance 16"])

    connect(world.player, "LOA16-to-LOA3", regions["Land of Abundance 16"], regions["Land of Abundance 3"],
        lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Bow], world.player, 1))

    connect(world.player, "LOA3-to-LOA3", regions["Land of Abundance 3"], regions["Land of Abundance 2"])

    connect(world.player, "LOA3-to-LOA5", regions["Land of Abundance 3"], regions["Land of Abundance 5"])

    connect(world.player, "LOA5-to-LOA4", regions["Land of Abundance 5"], regions["Land of Abundance 4"])

    connect(world.player, "LOA4-to-LOA7", regions["Land of Abundance 4"], regions["Land of Abundance 7"])

    connect(world.player, "LOA7-to-LOA8", regions["Land of Abundance 7"], regions["Land of Abundance 8"])

    connect(world.player, "LOA8-to-LOA6", regions["Land of Abundance 8"], regions["Land of Abundance 6"])

    connect(world.player, "LOA6-to-LOA9", regions["Land of Abundance 6"], regions["Land of Abundance 9"])

    flower_names = {FLOWER_ID_TO_NAME[f] for f in [
        Unknown_Flower, Flesh_Fresh_Flower, Whispering_Will_Flower,
        Breath_Bless_Flower, Peaceful_Presence_Flower,
        Bone_Born_Flower, Spirit_Soul_Flower
    ]}

    mirror_names = {MIRROR_ID_TO_NAME[m] for m in [
        Mirror_Shard_1, Mirror_Shard_2, Mirror_Shard_3,
        Mirror_Shard_4, Mirror_Shard_5, Mirror_Shard_6
    ]}

    if options.goal.value == options.goal.option_good:
        # Requires ALL flowers
        connect(world.player, "LOA5-to-LOA9", regions["Land of Abundance 9"], regions["Abyss"],
                lambda state: state.has_all(flower_names, world.player))

    elif options.goal.value == options.goal.option_true:
        all_reqs = flower_names | mirror_names
        connect(world.player, "LOA5-to-LOA9", regions["Land of Abundance 9"], regions["Abyss"],
                lambda state: state.has_all(all_reqs, world.player))

    else:
        connect(world.player, "LOA5-to-LOA9", regions["Land of Abundance 9"], regions["Abyss"])

    ## reverse path
    connect(world.player, "SM12-to-MF18", regions["Stone Mountain 12"], regions["Misty Forest 18"], )

    connect(world.player, "MF18-to-MF4", regions["Misty Forest 18"], regions["Misty Forest 4"], )

    connect(world.player, "MF4-to-MF3", regions["Misty Forest 4"], regions["Misty Forest 3"])

    connect(world.player, "MF3-to-MF1", regions["Misty Forest 3"], regions["Misty Forest 1"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Sword], world.player, 1))

    connect(world.player, "SM8-to-BG1", regions["Stone Mountain 8"], regions["Barron Grounds 1"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Bow], world.player, 1)
                          and state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], world.player, 1))

    connect(world.player, "BG1-to-RC", regions["Barron Grounds 1"], regions["Reincarnation Center"])

    connect(world.player, "RC-to-BG3", regions["Reincarnation Center"], regions["Barron Grounds 3"],
            lambda  state: state.has(ABILITIES_ID_TO_NAME[Abl_BreakWall], world.player, 1))

    connect(world.player, "BG3-to-BG4", regions["Barron Grounds 3"], regions["Barron Grounds 4"])

    connect(world.player, "BG4-to-BG5", regions["Barron Grounds 4"], regions["Barron Grounds 5"])

    connect(world.player, "BG5-to-BG6", regions["Barron Grounds 5"], regions["Barron Grounds 6"])

    connect(world.player, "BG6-to-BG7", regions["Barron Grounds 6"], regions["Barron Grounds 7"])

    connect(world.player, "BG7-to-BG9", regions["Barron Grounds 7"], regions["Barron Grounds 9"])

    connect(world.player, "BG9-to-BG11", regions["Barron Grounds 9"], regions["Barron Grounds 11"])

    connect(world.player, "BG11-to-BG12", regions["Barron Grounds 11"], regions["Barron Grounds 12"])

    connect(world.player, "BG12-to-BG13", regions["Barron Grounds 12"], regions["Barron Grounds 13"])

    connect(world.player, "BG13-to-BG14", regions["Barron Grounds 13"], regions["Barron Grounds 14"])

    connect(world.player, "BG14-to-BG16", regions["Barron Grounds 14"], regions["Barron Grounds 16"])

    connect(world.player, "BG16-to-BG17", regions["Barron Grounds 16"], regions["Barron Grounds 17"])

    connect(world.player, "BG17-to-BG19", regions["Barron Grounds 17"], regions["Barron Grounds 19"],
        lambda state: state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20))

    connect(world.player, "BG17-to-BG20", regions["Barron Grounds 17"], regions["Barron Grounds 20"])

    connect(world.player, "BG20-to-WORKSHOP", regions["Barron Grounds 20"], regions["Workshop"],
        lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1))

    connect(world.player, "WORKSHOP-to-CM1", regions["Workshop"], regions["Crimson Mines 1"])

    connect(world.player, "WORKSHOP-to-CM14", regions["Workshop"], regions["Crimson Mines 14"],
        lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1)
            and state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20))

    connect(world.player, "CM1-to-CM2", regions["Crimson Mines 1"], regions["Crimson Mines 2"])

    connect(world.player, "CM2-to-CM3", regions["Crimson Mines 2"], regions["Crimson Mines 3"])

    connect(world.player, "CM3-to-CM4", regions["Crimson Mines 3"], regions["Crimson Mines 4"])

    connect(world.player, "CM4-to-CM5", regions["Crimson Mines 4"], regions["Crimson Mines 5"])

    connect(world.player, "CM5-to-CM6", regions["Crimson Mines 5"], regions["Crimson Mines 6"])

    connect(world.player, "CM6-to-CM8", regions["Crimson Mines 6"], regions["Crimson Mines 8"])

    connect(world.player, "CM8-to-CM10", regions["Crimson Mines 8"], regions["Crimson Mines 10"])

    connect(world.player, "CM10-to-CM11", regions["Crimson Mines 10"], regions["Crimson Mines 11"])

    connect(world.player, "CM11-to-CM13", regions["Crimson Mines 11"], regions["Crimson Mines 13"])

    connect(world.player, "CM13-to-CM18", regions["Crimson Mines 13"], regions["Crimson Mines 18"])

    connect(world.player, "BG1-to-FP2", regions["Barron Grounds 4"], regions["Frozen Plateau 2"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Umbrella], world.player, 1)
                          and state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1))

    connect(world.player, "FP2-to-FP3", regions["Frozen Plateau 2"], regions["Frozen Plateau 3"])

    connect(world.player, "FP3-to-DS", regions["Frozen Plateau 3"], regions["Dispatch Station"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1))

    connect(world.player, "DS-to-FP5", regions["Dispatch Station"], regions["Frozen Plateau 5"])

    connect(world.player, "FP5-to-FP8", regions["Frozen Plateau 5"], regions["Frozen Plateau 8"])

    connect(world.player, "FP8-to-FP17", regions["Frozen Plateau 8"], regions["Frozen Plateau 17"])

    connect(world.player, "FP8-to-FP18", regions["Frozen Plateau 8"], regions["Frozen Plateau 18"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_SuperDash], world.player, 1))

    connect(world.player, "FP8-to-FP6", regions["Frozen Plateau 8"], regions["Frozen Plateau 6"])

    connect(world.player, "FP8-to-FP9", regions["Frozen Plateau 8"], regions["Frozen Plateau 9"])

    connect(world.player, "FP8-to-FP12", regions["Frozen Plateau 8"], regions["Frozen Plateau 12"])

    connect(world.player, "FP8-to-FP13", regions["Frozen Plateau 8"], regions["Frozen Plateau 13"])

    connect(world.player, "FP8-to-FP14", regions["Frozen Plateau 8"], regions["Frozen Plateau 14"])

    connect(world.player, "FP8-to-FP15", regions["Frozen Plateau 8"], regions["Frozen Plateau 15"])

    connect(world.player, "KOY8-to-CR", regions["Kingdom Of Yama 8"], regions["Control Room"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Lamp], world.player, 1)
                          and state.has (ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1)
                          and state.has (ABILITIES_ID_TO_NAME[Abl_Dash], world.player, 1))

    connect(world.player, "CR-to-UWW4", regions["Control Room"], regions["Underground Waterway 4"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], world.player, 1)
                          and state.has (ABILITIES_ID_TO_NAME[Abl_SuperDash], world.player, 1))

    connect(world.player, "UWW4-to-UWW3", regions["Underground Waterway 4"], regions["Underground Waterway 3"])

    connect(world.player, "UWW3-to-UWW16", regions["Underground Waterway 3"], regions["Underground Waterway 16"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Umbrella], world.player, 1))

    connect(world.player, "UWW16-to-UWW17", regions["Underground Waterway 16"], regions["Underground Waterway 17"],
            lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1))

    connect(world.player, "UWW17-to-UWW14", regions["Underground Waterway 17"], regions["Underground Waterway 14"])

    connect(world.player, "UWW14-to-UWW6", regions["Underground Waterway 14"], regions["Underground Waterway 6"])

    connect(world.player, "UWW6-to-UWW7", regions["Underground Waterway 6"], regions["Underground Waterway 7"])

    connect(world.player, "UWW7-to-UWW8", regions["Underground Waterway 7"], regions["Underground Waterway 8"])

    connect(world.player, "UWW8-to-UWW9", regions["Underground Waterway 8"], regions["Underground Waterway 9"])

    connect(world.player, "UWW9-to-UWW10", regions["Underground Waterway 9"], regions["Underground Waterway 10"])

    connect(world.player, "UWW10-to-UWW13", regions["Underground Waterway 10"], regions["Underground Waterway 13"])

    connect(world.player, "UWW13-to-UWW15", regions["Underground Waterway 13"], regions["Underground Waterway 15"],
            lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Fan], world.player, 1)
                          and state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20))

    return regions

def connect(player: int, name: str, source_region: Region, target_region: Region, rule: Optional[Callable] = None):
    connection = Entrance(player, name, source_region)

    if rule is not None:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection