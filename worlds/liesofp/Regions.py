from typing import Callable, Optional, Dict

from BaseClasses import Region, Entrance
from .ItemLists.Functionals import *

from .ItemLists.Keys import *
from .ItemLists.Materials import *
from .LocationLists.Chapters import *
from .Rules import weapon_level

from . import Items, LiesOfPOptions


def create_regions(world, options: LiesOfPOptions):
    regions: Dict[str, Region] = \
        {
            "Menu": Region("Menu", world.player, world.multiworld),
            "Krat Central Station": Region("Krat Central Station", world.player, world.multiworld),
            "Krat Central Station Plaza": Region("Krat Central Station Plaza", world.player, world.multiworld),
            "Hotel Krat": Region("Hotel Krat", world.player, world.multiworld),
            "Elysion Boulevard": Region("Elysion Boulevard", world.player, world.multiworld),
            "Krat City Hall": Region("Krat City Hall", world.player, world.multiworld),
            "Workshop Union Entrance": Region("Workshop Union Entrance", world.player, world.multiworld),
            "Venigni Works": Region("Venigni Works", world.player, world.multiworld),
            "Moonlight Town": Region("Moonlight Town", world.player, world.multiworld),
            "Path of Misery": Region("Path of Misery", world.player, world.multiworld),
            "St.Frangelico Cathedral Chapel": Region("St.Frangelico Cathedral Chapel", world.player, world.multiworld),
            "Path of the Pilgrim": Region("Path of the Pilgrim", world.player, world.multiworld),
            "Tomb Slums": Region("Tomb Slums", world.player, world.multiworld),
            "Hobbler's Bridge": Region("Hobbler's Bridge", world.player, world.multiworld),
            "Malum District": Region("Malum District", world.player, world.multiworld),
            "Rosa Isabelle Street": Region("Rosa Isabelle Street", world.player, world.multiworld),
            "Estella Opera House Entrance": Region("Estella Opera House Entrance", world.player, world.multiworld),
            "Estella Opera House Stage": Region("Estella Opera House Stage", world.player, world.multiworld),
            "Charity Market Path": Region("Charity Market Path", world.player, world.multiworld),
            "Lorenzini Arcade": Region("Lorenzini Arcade", world.player, world.multiworld),
            "First Floor Lorenzini Arcade": Region("First Floor Lorenzini Arcade", world.player, world.multiworld),
            "Underground Lorenzini Arcade": Region("Underground Lorenzini Arcade", world.player, world.multiworld),
            "Grand Exhibition Plaza": Region("Grand Exhibition Plaza", world.player, world.multiworld),
            "Grand Exhibition Gallery": Region("Grand Exhibition Gallery", world.player, world.multiworld),
            "Baron Swamp": Region("Baron Swamp", world.player, world.multiworld),
            "Closed Railway": Region("Closed Railway", world.player, world.multiworld),
            "Krat Central Station Revisit": Region("Krat Central Station Revisit", world.player, world.multiworld),
            "Collapsed Street": Region("Collapsed Street", world.player, world.multiworld),
            "Collapsing Krat": Region("Collapsing Krat", world.player, world.multiworld),
            "Hermit's Cave": Region("Hermit's Cave", world.player, world.multiworld),
            "Relic of Trismegistus": Region("Relic of Trismegistus", world.player, world.multiworld),
            "Black Seaside": Region("Black Seaside", world.player, world.multiworld),
            "Arche Abbey Entrance": Region("Arche Abbey Entrance", world.player, world.multiworld),
            "Arche Abbey Outer Wall": Region("Arche Abbey Outer Wall", world.player, world.multiworld),
            "Arche Abbey Upper": Region("Arche Abbey Upper", world.player, world.multiworld),
            "Arche Abbey Passageway": Region("Arche Abbey Passageway", world.player, world.multiworld),
            "Arche Abbey Cradle of the God": Region("Arche Abbey Cradle of the God", world.player, world.multiworld),
            "Under the Abyss": Region("Under the Abyss", world.player, world.multiworld)
        }

    connect(world.player, "menu-to-KCS", regions["Menu"], regions["Krat Central Station"])

    key_item_name = KEY_ID_TO_NAME[KCS_ENTRANCE_KEY]
    connect(world.player, "KCS-to-KCSP", regions["Krat Central Station"], regions["Krat Central Station Plaza"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    connect(world.player, "KCSP-to-HK", regions["Krat Central Station Plaza"], regions["Hotel Krat"])

    connect(world.player, "HK-to-EB", regions["Hotel Krat"], regions["Elysion Boulevard"],
            lambda state: weapon_level(state, world.player, 1))

    key_item_name = KEY_ID_TO_NAME[KCH_KEY]
    connect(world.player, "EB-to-KCH", regions["Elysion Boulevard"], regions["Krat City Hall"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    key_item_name = KEY_ID_TO_NAME[KCH_COURTYARD_KEY]
    connect(world.player, "KCH-to-WUE", regions["Krat City Hall"], regions["Workshop Union Entrance"],
            lambda state, ki=key_item_name:
            state.has(ki, world.player) and weapon_level(state, world.player, 2))

    connect(world.player, "WUE-to-VW", regions["Workshop Union Entrance"], regions["Venigni Works"])

    connect(world.player, "VW-to-MT", regions["Venigni Works"], regions["Moonlight Town"])

    key_item_name = KEY_ID_TO_NAME[RAIL_KEY]
    connect(world.player, "MT-to-POM", regions["Moonlight Town"], regions["Path of Misery"],
            lambda state, ki=key_item_name:
            state.has(ki, world.player) and weapon_level(state, world.player, 3))

    connect(world.player, "POM-to-SFCC", regions["Path of Misery"], regions["St.Frangelico Cathedral Chapel"])

    connect(world.player, "SFCC-to-POTP", regions["St.Frangelico Cathedral Chapel"], regions["Path of the Pilgrim"],
            lambda state: weapon_level(state, world.player, 4))

    connect(world.player, "POTP-to-TS", regions["Path of the Pilgrim"], regions["Tomb Slums"])

    connect(world.player, "TS-to-HB", regions["Tomb Slums"], regions["Hobbler's Bridge"])

    connect(world.player, "HB-to-MD", regions["Hobbler's Bridge"], regions["Malum District"])

    key_item_name = KEY_ID_TO_NAME[ROSA_KEY]
    if options.chapter6_access == options.chapter6_access.option_early:
        connect(world.player, "HK-to-RIS", regions["Hotel Krat"], regions["Rosa Isabelle Street"],
                lambda state, ki=key_item_name:
                state.has(ki, world.player) and (weapon_level(state, world.player, 5)or
                        state.has(Items.GLITCHED, player=world.player)))

    elif options.chapter6_access == options.chapter6_access.option_early_porgan:
        connect(world.player, "HK-to-RIS", regions["Hotel Krat"], regions["Rosa Isabelle Street"],
                lambda state, ki=key_item_name:
                state.has(ki, world.player) and (weapon_level(state, world.player, 5)) and
                (
                    state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1], player=world.player) or
                    state.has(Items.GLITCHED, player=world.player)
                ))
    else:
        connect(world.player, "HK-to-RIS", regions["Hotel Krat"], regions["Rosa Isabelle Street"],
                lambda state, ki=key_item_name:
                state.has(ki, world.player) and (weapon_level(state, world.player, 5)) and
                (
                    state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00], player=world.player) or
                    state.has(Items.GLITCHED, player=world.player)
                ))

    connect(world.player, "RIS-to-EOHE", regions["Rosa Isabelle Street"], regions["Estella Opera House Entrance"])

    connect(world.player, "EOHE-to-EOHS", regions["Estella Opera House Entrance"], regions["Estella Opera House Stage"])

    connect(world.player, "EOHS-to-CMP", regions["Estella Opera House Stage"], regions["Charity Market Path"],
            lambda state: weapon_level(state, world.player, 6))

    connect(world.player, "CMP-to-LA", regions["Charity Market Path"], regions["Lorenzini Arcade"])

    key_item_name = KEY_ID_TO_NAME[ARCADE_FLOOR_KEY]
    connect(world.player, "LA-to-FLA", regions["Lorenzini Arcade"], regions["First Floor Lorenzini Arcade"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    key_item_name = KEY_ID_TO_NAME[ARCADE_UNDERGROUND_KEY]
    connect(world.player, "FLA-to-ULA", regions["First Floor Lorenzini Arcade"],
            regions["Underground Lorenzini Arcade"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    connect(world.player, "ULA-to-GEP", regions["Underground Lorenzini Arcade"], regions["Grand Exhibition Plaza"])

    connect(world.player, "GEP-to-GEG", regions["Grand Exhibition Plaza"], regions["Grand Exhibition Gallery"])

    connect(world.player, "GEG-to-BS", regions["Grand Exhibition Gallery"], regions["Baron Swamp"],
            lambda state: weapon_level(state, world.player, 7))

    connect(world.player, "BS-to-CR", regions["Baron Swamp"], regions["Closed Railway"],
            lambda state: weapon_level(state, world.player, 8))

    connect(world.player, "CR-to-KCS2", regions["Closed Railway"], regions["Krat Central Station Revisit"])

    connect(world.player, "KCS2-to-CS", regions["Krat Central Station Revisit"], regions["Collapsed Street"])

    connect(world.player, "CS-to-CK", regions["Krat Central Station Revisit"], regions["Collapsing Krat"])

    # todo change this to cryptic vessel when shops get randomized
    box_items_name = (FUNC_ID_TO_NAME[FUNC_BOX], FUNC_ID_TO_NAME[FUNC_STURDY_BOX], FUNC_ID_TO_NAME[FUNC_SPECIAL_BOX])
    connect(world.player, "BS-to-HC", regions["Baron Swamp"], regions["Hermit's Cave"],
            lambda state, bi=box_items_name:
            state.has_all(bi, world.player) and
            (
                    state.can_reach_location(VW_ID_TO_NAME[CH03_Puppet_FireStoker_Named_01_1], player=world.player) or
                    state.can_reach_location(CK_ID_TO_NAME[CH09_Carcass_GraveKeeper_Seed_00_1], player=world.player)
            ))

    connect(world.player, "CK-to-ROT", regions["Collapsing Krat"], regions["Relic of Trismegistus"],
            lambda state: weapon_level(state, world.player, 9))

    connect(world.player, "ROT-to-BSS", regions["Relic of Trismegistus"], regions["Black Seaside"])

    key_item_name = KEY_ID_TO_NAME[ALCHEMIST_BADGE]
    connect(world.player, "BSS-to-AAE", regions["Black Seaside"], regions["Arche Abbey Entrance"],
            lambda state, ki=key_item_name: state.has(ki, world.player))

    connect(world.player, "AAE-to-AAOW", regions["Arche Abbey Entrance"], regions["Arche Abbey Outer Wall"])

    connect(world.player, "AAOW-to-AAU", regions["Arche Abbey Outer Wall"], regions["Arche Abbey Upper"])

    key_item_name = KEY_ID_TO_NAME[PASSAGE_KEY]
    connect(world.player, "AAU-to-AAP", regions["Arche Abbey Upper"], regions["Arche Abbey Passageway"],
            lambda state, ki=key_item_name: state.has(ki, world.player) and weapon_level(state, world.player, 10))

    connect(world.player, "AAP-to-AACG", regions["Arche Abbey Passageway"], regions["Arche Abbey Cradle of the God"])

    connect(world.player, "AACG-to-UTA", regions["Arche Abbey Cradle of the God"], regions["Under the Abyss"])
    return regions


def connect(player: int, name: str, source_region: Region, target_region: Region, rule: Optional[Callable] = None):
    connection = Entrance(player, name, source_region)

    if rule is not None:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection
