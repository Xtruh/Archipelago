from BaseClasses import MultiWorld, CollectionState
from ..generic.Rules import add_rule
from .Items import *
from .Locations import *
from .Options import EightDoorsOptions


def set_rules(multiworld: MultiWorld, world, player: int, options: EightDoorsOptions):

    goal_option = options.goal.value
    souls_needed = options.requiredfugitivesouls.value

    progressive_soul = FUGITIVE_SOUL_ID_TO_NAME[Fugitive]

    def get_soul_count(state):
        return state.count(progressive_soul, player)

    normal_goals = (0, 1, 2)

    if goal_option in normal_goals:
        multiworld.completion_condition[player] = lambda state: (
            state.can_reach("Abyss", player=player)
        )

    elif goal_option == 3:
        multiworld.completion_condition[player] = lambda state: (
            get_soul_count(state) >= souls_needed
        )

    loc = multiworld.get_location(Ch1_4_ID_TO_NAME[Ch1_4_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch1_4_ID_TO_NAME[Ch1_4_Dawn], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_Dash], player))

    loc = multiworld.get_location(Ch2_1_ID_TO_NAME[Ch2_1_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch2_2_ID_TO_NAME[Ch2_2_Soul], player)
    add_rule(loc, lambda state: (state.has(ABILITIES_ID_TO_NAME[Abl_Dash], player) and can_collect_soul(state, player)))

    loc = multiworld.get_location(Ch2_4_ID_TO_NAME[Ch2_4_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch2_5_ID_TO_NAME[Ch2_5_Dawn], player)
    add_rule(loc, lambda state: can_range_attack(state, player))

    loc = multiworld.get_location(Ch2_6_ID_TO_NAME[Ch2_6_CoinBox], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], player))

    loc = multiworld.get_location(Ch2_7_ID_TO_NAME[Ch2_7_CoinBox], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], player))

    loc = multiworld.get_location(Ch2_9_ID_TO_NAME[Ch2_9_CoinBox], player)
    add_rule(loc, lambda state: can_range_attack(state, player))

    loc = multiworld.get_location(Ch2_9_ID_TO_NAME[Ch2_9_Soul], player)
    add_rule(loc, lambda state: (can_range_attack(state, player) and can_collect_soul(state, player)))

    loc = multiworld.get_location(Ch2_10_ID_TO_NAME[Ch2_10_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch2_11_ID_TO_NAME[Ch2_11_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_1_ID_TO_NAME[Ch3_1_CoinBox], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], player))

    loc = multiworld.get_location(Ch3_1_ID_TO_NAME[Ch3_1_Dawn], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_WallHold], player))

    loc = multiworld.get_location(Ch3_3_ID_TO_NAME[Ch3_3_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_5_ID_TO_NAME[Ch3_5_CoinBox], player)
    add_rule(loc, lambda state: can_range_attack(state, player))

    loc = multiworld.get_location(Ch3_5_ID_TO_NAME[Ch3_5_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_7_ID_TO_NAME[Ch3_7_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_8_ID_TO_NAME[Ch3_8_Map], player)
    add_rule(loc, lambda state: can_range_attack(state, player))

    loc = multiworld.get_location(Ch3_9_ID_TO_NAME[Ch3_9_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_18_ID_TO_NAME[Ch3_18_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch3_18_ID_TO_NAME[Ch3_18_Soul2], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_1_ID_TO_NAME[Ch4_1_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_4_ID_TO_NAME[Ch4_4_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_9_ID_TO_NAME[Ch4_9_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_12_ID_TO_NAME[Ch4_12_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_13_ID_TO_NAME[Ch4_13_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_14_ID_TO_NAME[Ch4_14_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_6_ID_TO_NAME[Ch4_6_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_16_ID_TO_NAME[Ch4_16_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch4_16_ID_TO_NAME[Ch4_16_Soul1], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_1_ID_TO_NAME[Ch5_1_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_4_ID_TO_NAME[Ch5_4_Soul1], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_5_ID_TO_NAME[Ch5_5_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_6_ID_TO_NAME[Ch5_6_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_10_ID_TO_NAME[Ch5_10_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_13_ID_TO_NAME[Ch5_13_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch5_18_ID_TO_NAME[Ch5_18_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_2_ID_TO_NAME[Ch6_2_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player)
                                and state.has (ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1))

    loc = multiworld.get_location(Ch6_8_ID_TO_NAME[Ch6_8_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_8_ID_TO_NAME[Ch6_8_Soul1], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_6_ID_TO_NAME[Ch6_6_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_9_ID_TO_NAME[Ch6_9_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_18_ID_TO_NAME[Ch6_18_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_13_ID_TO_NAME[Ch6_13_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch6_15_ID_TO_NAME[Ch6_15_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_3_ID_TO_NAME[Ch7_3_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_16_ID_TO_NAME[Ch7_16_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player)
                                and state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1))

    loc = multiworld.get_location(Ch7_14_ID_TO_NAME[Ch7_14_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_17_ID_TO_NAME[Ch7_17_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_8_ID_TO_NAME[Ch7_8_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_9_ID_TO_NAME[Ch7_9_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch7_10_ID_TO_NAME[Ch7_10_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

    loc = multiworld.get_location(Ch2_3_ID_TO_NAME[Ch2_3_Mirror], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1)
                            and state.has(ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1)
                               and state.can_reach_location(WORKSHOP_ID_TO_NAME[Workshop_Double_Jump], player=player))

    loc = multiworld.get_location(Ch2_9_ID_TO_NAME[Ch2_9_CoinBox], player)
    add_rule(loc, lambda state: state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20)
                                and state.has(ABILITIES_ID_TO_NAME[Abl_BreakWall], world.player, 1))

    loc = multiworld.get_location(Ch3_4_ID_TO_NAME[Ch3_4_Mirror], player)
    add_rule(loc, lambda state: state.has(WEAPON_ID_TO_NAME[Wep_Umbrella], world.player, 1))

    loc = multiworld.get_location(Ch3_7_ID_TO_NAME[Ch3_7_Dawn], player)
    add_rule(loc, lambda state: state.has(ABILITIES_ID_TO_NAME[Abl_DoubleJump], world.player, 1)
                                and state.has(ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1))

    loc = multiworld.get_location(Ch3_10_ID_TO_NAME[Ch3_10_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player)
                                and state.has(ABILITIES_ID_TO_NAME[Abl_SuperJump], world.player, 1))

    loc = multiworld.get_location(Ch5_4_ID_TO_NAME[Ch5_4_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player)
                                and state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20))

    loc = multiworld.get_location(Ch2_5_ID_TO_NAME[Ch2_5_CoinBox], player)
    add_rule(loc, lambda state: state.has(CURRECY_ID_TO_NAME[Dawn_1], world.player, 20)
                                and state.has(ABILITIES_ID_TO_NAME[Abl_BreakWall], world.player, 1))

    loc = multiworld.get_location(Ch8_2_ID_TO_NAME[Ch8_2_Soul], player)
    add_rule(loc, lambda state: can_collect_soul(state, player))

def can_collect_soul(state: CollectionState, player):
    return state.has(VAL_ID_TO_NAME[Gourd], player)

def can_range_attack(state: CollectionState, player):
    return state.has(WEAPON_ID_TO_NAME[Wep_Sword], player) or state.has(WEAPON_ID_TO_NAME[Wep_Bow], player)