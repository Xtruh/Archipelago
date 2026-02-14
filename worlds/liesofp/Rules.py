from BaseClasses import MultiWorld, CollectionState
from .ItemLists.Collectables import *
from .ItemLists.Costumes import *
from .ItemLists.Gestures import *
from .ItemLists.Keys import *
from .ItemLists.Useables import *
from .ItemLists.Weapons import *
from .ItemLists.Materials import *
from .LocationLists.Chapters import *
from ..generic.Rules import add_rule
from . import Items, LiesOfPOptions


def set_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    if options.goal.value == options.goal.option_king_of_puppets:
        king_of_puppets_rules(multiworld, world, player, options)
    elif options.goal.value == options.goal.option_arlecchino_short:
        arlecchino_short_rules(multiworld, world, player, options)
    elif options.goal.value == options.goal.option_arlecchino:
        arlecchino_rules(multiworld, world, player, options)
    elif (options.goal.value == options.goal.option_simon_manus_and_arlecchino or
          options.goal.value == options.goal.option_nameless_puppet_and_arlecchino):
        both_rules(multiworld, world, player, options)
    else:
        full_rules(multiworld, world, player, options)


def king_of_puppets_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.can_reach("Estella Opera House Stage", player=player)
    )

    if options.dlc_items.value == options.dlc_items.option_enable and options.dlc.value == options.dlc.option_disable:
        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Geppetto_F00], player)
    add_rule(loc, lambda state: state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1],
                                                         player=player))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    if options.dlc.value == options.dlc.option_enable:
        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Gesture_Dance], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot105], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Puppet_FlameAcrobat_Named_00], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot97], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot91], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Prize_Pinwheels_E01], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4) and
                                    state.has(DLC_GES_ID_TO_NAME[DLC_GES_DANCE], player, 1))

        if options.require_bow_minigames == options.require_bow_minigames.option_enable:
            loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot67], player)
            add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

            loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot107], player)
            add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

        if options.require_horn_overseer == options.require_horn_overseer.option_enable:
            loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1], player)
            add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

            loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_2], player)
            add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E02], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_BLOODY], player, 1) and
                                    state.can_reach_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1],
                                                             player=player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E03], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_CORRODED], player, 1) and
                                    state.can_reach_location(ARES_ID_TO_NAME[DLC_CH03_Snail_Key], player=player))

        loc = multiworld.get_location(KZ_ID_TO_NAME[DLC_CH01_ItemSpot112], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_1], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                    state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1],
                                                             player=player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_2], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                    state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1],
                                                             player=player))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot105], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_kEY_SEA_FISHERMAN], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot62], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[SHACK_KEY], player, 1))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Antonia_E04], player)
    add_rule(loc,
             lambda state: state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00],
                                                    player=player))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(TS_ID_TO_NAME[Dotted_Badman], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_OLD]))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot15], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_1], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_2], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))


def arlecchino_short_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.can_reach("Rose Garden", player=player)
    )
    loc = multiworld.get_location(HK1_ID_TO_NAME[Geppetto_F00], player)
    add_rule(loc, lambda state: state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1],
                                                         player=player))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 3))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Gesture_Dance], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Puppet_FlameAcrobat_Named_00], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot97], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot91], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Prize_Pinwheels_E01], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4) and
                                state.has(DLC_GES_ID_TO_NAME[DLC_GES_DANCE], player, 1))

    if options.require_bow_minigames == options.require_bow_minigames.option_enable:
        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot67], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot107], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

    if options.require_horn_overseer == options.require_horn_overseer.option_enable:
        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_2], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E02], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_BLOODY], player, 1) and
                                state.can_reach_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1],
                                                         player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E03], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_CORRODED], player, 1) and
                                state.can_reach_location(ARES_ID_TO_NAME[DLC_CH03_Snail_Key], player=player))

    loc = multiworld.get_location(KZ_ID_TO_NAME[DLC_CH01_ItemSpot112], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_1], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_2], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_kEY_SEA_FISHERMAN], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot62], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[SHACK_KEY], player, 1))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Antonia_E04], player)
    add_rule(loc,
             lambda state: state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00],
                                                    player=player))

    loc = multiworld.get_location(TS_ID_TO_NAME[Dotted_Badman], player)
    add_rule(loc, lambda state: can_decrypt_vessel_pre_ch09(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_OLD]))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot15], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_1], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_2], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))


def arlecchino_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.can_reach("Rose Garden", player=player)
    )

    loc = multiworld.get_location(HK1_ID_TO_NAME[Geppetto_F00], player)
    add_rule(loc, lambda state: state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1],
                                                         player=player))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Gesture_Dance], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Puppet_FlameAcrobat_Named_00], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot97], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot91], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Prize_Pinwheels_E01], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4) and
                                state.has(DLC_GES_ID_TO_NAME[DLC_GES_DANCE], player, 1))

    if options.require_bow_minigames == options.require_bow_minigames.option_enable:
        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot67], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot107], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

    if options.require_horn_overseer == options.require_horn_overseer.option_enable:
        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_2], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E02], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_BLOODY], player, 1) and
                                state.can_reach_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1],
                                                         player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E03], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_CORRODED], player, 1) and
                                state.can_reach_location(ARES_ID_TO_NAME[DLC_CH03_Snail_Key], player=player))

    loc = multiworld.get_location(KZ_ID_TO_NAME[DLC_CH01_ItemSpot112], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_1], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_2], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_kEY_SEA_FISHERMAN], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot62], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[SHACK_KEY], player, 1))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Antonia_E04], player)
    add_rule(loc,
             lambda state: state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00],
                                                    player=player))

    loc = multiworld.get_location(GEG_ID_TO_NAME[Ch07_ItemSpot63], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[STATUE_KEY], player, 1))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(TS_ID_TO_NAME[Dotted_Badman], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_OLD]))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot15], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_1], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_2], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_1], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_2], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )


def both_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    multiworld.completion_condition[player] = lambda state: (
            state.can_reach("Rose Garden", player=player) and
            state.can_reach("Arche Abbey Cradle of the God", player=player)
    )

    loc = multiworld.get_location(HK1_ID_TO_NAME[Geppetto_F00], player)
    add_rule(loc, lambda state: state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1],
                                                         player=player))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Gesture_Dance], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Puppet_FlameAcrobat_Named_00], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot97], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot91], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Prize_Pinwheels_E01], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4) and
                                state.has(DLC_GES_ID_TO_NAME[DLC_GES_DANCE], player, 1))

    if options.require_bow_minigames == options.require_bow_minigames.option_enable:
        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot67], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot107], player)
        add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

    if options.require_horn_overseer == options.require_horn_overseer.option_enable:
        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_2], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E02], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_BLOODY], player, 1) and
                                state.can_reach_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1],
                                                         player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E03], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_CORRODED], player, 1) and
                                state.can_reach_location(ARES_ID_TO_NAME[DLC_CH03_Snail_Key], player=player))

    loc = multiworld.get_location(KZ_ID_TO_NAME[DLC_CH01_ItemSpot112], player)
    add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                state.has(Items.GLITCHED, player=world.player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_1], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_2], player)
    add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1], player=player))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_1], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_2], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

    loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
    add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

    loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot105], player)
    add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_kEY_SEA_FISHERMAN], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot62], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[SHACK_KEY], player, 1))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Antonia_E04], player)
    add_rule(loc,
             lambda state: state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00],
                                                    player=player))

    loc = multiworld.get_location(GEG_ID_TO_NAME[Ch07_ItemSpot63], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[STATUE_KEY], player, 1))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(TS_ID_TO_NAME[Dotted_Badman], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_OLD]))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot15], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_1], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_2], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_1], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_2], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )


def full_rules(multiworld: MultiWorld, world, player: int, options: LiesOfPOptions):
    multiworld.completion_condition[player] = lambda state: (
        state.can_reach("Arche Abbey Cradle of the God", player=player)
    )

    if options.dlc_items.value == options.dlc_items.option_enable and options.dlc.value == options.dlc.option_disable:
        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Geppetto_F00], player)
    add_rule(loc, lambda state: state.can_reach_location(KCH_ID_TO_NAME[CH02_Puppet_Judge_Boss_00_1],
                                                         player=player))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(VW_ID_TO_NAME[Ch03_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(SFCC_ID_TO_NAME[Ch04_ItemSpot36_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    loc = multiworld.get_location(EB_ID_TO_NAME[Ch02_ItemSpot36_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED]))

    if options.dlc.value == options.dlc.option_enable:
        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Gesture_Dance], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot105], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Puppet_FlameAcrobat_Named_00], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot97], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot91], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_Prize_Pinwheels_E01], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_COIN], player, 4) and
                                    state.has(DLC_GES_ID_TO_NAME[DLC_GES_DANCE], player, 1))

        if options.require_bow_minigames == options.require_bow_minigames.option_enable:
            loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot67], player)
            add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

            loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot107], player)
            add_rule(loc, lambda state: state.has(DLC_SPECIAL_WPN_ID_TO_NAME[DLC_SPECIAL_WPN_BOW], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(CG_ID_TO_NAME[DLC_CH01_ItemSpot27_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_1], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume01_2], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PIERCING_DEATHS], player, 1))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume02], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_PREMEATING_DEATHS], player, 1))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_CH00_ItemSpot02_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(ZUF_ID_TO_NAME[DLC_CH02_ItemSpot44_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume03], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLACK_DEATHS], player, 1))

        if options.require_horn_overseer == options.require_horn_overseer.option_enable:
            loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1], player)
            add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

            loc = multiworld.get_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_2], player)
            add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                        state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E02], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_BLOODY], player, 1) and
                                    state.can_reach_location(ERZ_ID_TO_NAME[DLC_CH02_Carcass_TwoFacedWatcher_Seed_00_1],
                                                             player=player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E03], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_CORRODED], player, 1) and
                                    state.can_reach_location(ARES_ID_TO_NAME[DLC_CH03_Snail_Key], player=player))

        loc = multiworld.get_location(KZ_ID_TO_NAME[DLC_CH01_ItemSpot112], player)
        add_rule(loc, lambda state: state.has(DLC_RECOLLECTION_ID_TO_NAME[DLC_RECOLLECTION_HORN], player, 1) or
                                    state.has(Items.GLITCHED, player=world.player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_1], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                    state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1],
                                                             player=player))

        loc = multiworld.get_location(EHK_ID_TO_NAME[DLC_H_Alidoro_Code_E04_2], player)
        add_rule(loc, lambda state: state.has(DLC_CRYPTIC_ID_TO_NAME[DLC_CRYPTIC_FROSTED], player, 1) and
                                    state.can_reach_location(SC_ID_TO_NAME[DLC_CH04_Stalker_Lumacchio_01_1],
                                                             player=player))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_1], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot62_2], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_KEY_RABBIT], player, 3))

        loc = multiworld.get_location(BRB_ID_TO_NAME[DLC_BlackRabbit_Costume04], player)
        add_rule(loc, lambda state: state.has(BRB_OUTFIT_ID_TO_NAME[DLC_OUTFIT_BLAZING_DEATHS], player, 1))

        loc = multiworld.get_location(SC_ID_TO_NAME[DLC_CH04_ItemSpot105], player)
        add_rule(loc, lambda state: state.has(DLC_KEYS_ID_TO_NAME[DLC_kEY_SEA_FISHERMAN], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot62], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[SHACK_KEY], player, 1))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_1], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(KCS_ID_TO_NAME[DottedPaper_Maid_2], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED]))

    loc = multiworld.get_location(HK1_ID_TO_NAME[Antonia_E04], player)
    add_rule(loc,
             lambda state: state.can_reach_location(MD_ID_TO_NAME[CH05_Stalker_BRabbit_StrongMale_Boss_00],
                                                    player=player))

    loc = multiworld.get_location(GEG_ID_TO_NAME[Ch07_ItemSpot63], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[STATUE_KEY], player, 1))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(EOHS_ID_TO_NAME[Ch06_ItemSpot56_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(TS_ID_TO_NAME[Dotted_Badman], player)
    add_rule(loc, lambda state: can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_OLD]))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot15], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_1], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(TS_ID_TO_NAME[Ch05_ItemSpot16_2], player)
    add_rule(loc,
             lambda state:
             state.has(KEY_ID_TO_NAME[ROBBER_KEY], player, 1) and
             state.has(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], player, 1))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(KCS2_ID_TO_NAME[Ch09_ItemSpot79_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TRI_KEY], player, 4))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_1], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(AAOW_ID_TO_NAME[RiddleKing_L01_2], player)
    add_rule(loc, lambda state: state.has(KEY_ID_TO_NAME[TCO_TRI_KEY], player))

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_1], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )

    loc = multiworld.get_location(CS_ID_TO_NAME[DottedPaper_Sign_2], player)
    add_rule(loc,
             lambda state:
             can_decrypt_vessel(state, player, CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL]) and
             (
                     (
                             state.has(BOSS_ERGO_ID_TO_NAME[BOSS_ERGO_VICTOR], player) and
                             state.can_reach_location(GEG_ID_TO_NAME[CH07_Reborner_Victor_Boss_01], player=player)
                     ) or state.has(SPECIAL_WPN_ID_TO_NAME[WPN_FROZEN_FEAST], player)
             )
             )


def weapon_level(state: CollectionState, player, level: int) -> bool:
    level_to_normal_amount = {
        # Level: [Hidden, Crescent, Half, Full]
        1: [1, 0, 0, 0],
        2: [3, 0, 0, 0],
        3: [7, 0, 0, 0],
        4: [7, 1, 0, 0],
        5: [7, 3, 0, 0],
        6: [7, 7, 0, 0],
        7: [7, 7, 1, 0],
        8: [7, 7, 3, 0],
        9: [7, 7, 7, 0],
        10: [7, 7, 7, 1],
    }
    level_to_special_amount = {
        # Level: [Dark, Full]
        0: [0, 0],
        1: [1, 0],
        2: [3, 0],
        3: [7, 0],
        4: [7, 1],
        5: [7, 3],
    }
    boss_ergo = list(BOSS_ERGO_ID_TO_NAME.values()) and list(DLC_BOSS_ERGO_ID_TO_NAME.values())
    special_weapons = list(SPECIAL_WPN_ID_TO_NAME.values()) and list(DLC_SPECIAL_WPN_ID_TO_NAME.values())
    has_special = (
            (
                    state.has_any(boss_ergo, player) and
                    state.can_reach_region("St.Frangelico Cathedral Chapel", player)
            ) or state.has_any(special_weapons, player)
    )

    normal_amount = level_to_normal_amount[level]
    has_normal_level = (
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE], player, normal_amount[0]) and
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE2], player, normal_amount[1]) and
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE3], player, normal_amount[2]) and
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE4], player, normal_amount[3])
    )

    special_amount = level_to_special_amount[level // 2]
    has_special_level = (
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_SPECIAL_WPN_UPGRADE], player, special_amount[0]) and
            state.has(WEAPON_MATERIALS_ID_TO_NAME[MAT_SPECIAL_WPN_UPGRADE2], player, special_amount[1])
    )

    return (has_normal_level or (has_special and has_special_level)) or state.has(Items.GLITCHED, player)


def can_decrypt_vessel(state: CollectionState, player, vessel) -> bool:
    can_decrypt = \
        (
                state.can_reach_location(VW_ID_TO_NAME[CH03_Puppet_FireStoker_Named_01_1], player=player) or
                state.can_reach_location(CK_ID_TO_NAME[CH09_Carcass_GraveKeeper_Seed_00_1], player=player)
        )

    return can_decrypt and state.has(vessel, player)


def can_decrypt_vessel_pre_ch09(state: CollectionState, player, vessel) -> bool:
    can_decrypt = state.can_reach_location(VW_ID_TO_NAME[CH03_Puppet_FireStoker_Named_01_1], player=player)
    return can_decrypt and state.has(vessel, player)
