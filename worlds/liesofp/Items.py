from BaseClasses import Item, ItemClassification as ItemClass
from . import LiesOfPOptions
from .ItemLists.Collectables import *
from .ItemLists.Keys import *
from .ItemLists.Materials import *
from .ItemLists.Useables import *
from .ItemLists.Functionals import *
from .ItemLists.Weapons import *
from .ItemLists.Parts import *
from .ItemLists.Costumes import *
from .ItemLists.Gestures import *
from .ItemLists.Legion import *
from .ItemLists.Amulets import *
from ..AutoWorld import World

GLITCHED = "Glitched Item"


class LiesOfPItem(Item):
    game = "Lies Of P"

    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)


def get_item_dict():
    result = {}
    for keyId in All_Keys:
        result[KEY_ID_TO_NAME[keyId]] = keyId

    for funcId in All_FUNC:
        result[FUNC_ID_TO_NAME[funcId]] = funcId

    for grindId in All_GRIND:
        result[GRIND_ID_TO_NAME[grindId]] = grindId

    for wishId in ALL_WISH:
        result[WISH_ID_TO_NAME[wishId]] = wishId

    for consumeId in All_CONSUME:
        result[CONSUME_ID_TO_NAME[consumeId]] = consumeId

    for throwId in All_THROW:
        result[THROW_ID_TO_NAME[throwId]] = throwId

    for ergoId in ALL_ERGO:
        result[ERGO_ID_TO_NAME[ergoId]] = ergoId

    for bossId in ALL_BOSS_ERGO:
        result[BOSS_ERGO_ID_TO_NAME[bossId]] = bossId

    for weapon_materialsId in All_WEAPON_MATERIALS:
        result[WEAPON_MATERIALS_ID_TO_NAME[weapon_materialsId]] = weapon_materialsId

    for arm_materialsId in ALL_ARM_MATERIALS:
        result[ARM_MATERIALS_ID_TO_NAME[arm_materialsId]] = arm_materialsId

    for porganId in ALL_PORGAN_MATERIALS:
        result[PORGAN_MATERIALS_ID_TO_NAME[porganId]] = porganId

    restricted_outfits = [OUTFIT_MISCHIEVOUS, OUTFIT_SIGNATURE]
    for outfitId in ALL_OUTFITS:
        if outfitId in restricted_outfits:
            continue
        result[OUTFIT_ID_TO_NAME[outfitId]] = outfitId

    restricted_accessory = [ACCESSORY_MISCHIEVOUS, ACCESSORY_VENIGNI_GLASS, ACCESSORY_PARADE]
    for accessoriesId in ALL_ACCESSORY:
        if accessoriesId in restricted_accessory:
            continue
        result[ACCESSORY_ID_TO_NAME[accessoriesId]] = accessoriesId

    for gestureId in ALL_GES:
        result[GES_ID_TO_NAME[gestureId]] = gestureId

    for normal_weaponId in ALL_NORMAL_WPN:
        result[NORMAL_WPN_ID_TO_NAME[normal_weaponId]] = normal_weaponId

    for special_weaponId in ALL_SPECIAL_WPN:
        result[SPECIAL_WPN_ID_TO_NAME[special_weaponId]] = special_weaponId

    for legionId in ALL_LEGION:
        result[LEGION_ID_TO_NAME[legionId]] = legionId

    for partId in ALL_PARTS_MATERIALS:
        result[PARTS_ID_TO_NAME[partId]] = partId

    for amuletId in ALL_AMULET:
        result[AMULET_ID_TO_NAME[amuletId]] = amuletId

    for bossAmuletId in ALL_BOSS_AMULET:
        result[BOSS_AMULET_ID_TO_NAME[bossAmuletId]] = bossAmuletId

    for crypticId in ALL_CRYPTIC:
        result[CRYPTIC_ID_TO_NAME[crypticId]] = crypticId

    return result


def populate_item_pool(world: World, options: LiesOfPOptions):
    if options.goal.value == options.goal.option_king_of_puppets:
        king_of_puppets_item_pool(world, options)
    else:
        full_item_pool(world, options)


def full_item_pool(world: World, options: LiesOfPOptions):
    item_count = 0
    location_count = sum(1 for e in world.get_locations())

    key = LiesOfPItem(KEY_ID_TO_NAME[KCS_ENTRANCE_KEY], ItemClass.progression, KCS_ENTRANCE_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[KCH_KEY], ItemClass.progression, KCH_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[KCH_COURTYARD_KEY], ItemClass.progression, KCH_COURTYARD_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[SHACK_KEY], ItemClass.progression, SHACK_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ROSA_KEY], ItemClass.progression, ROSA_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ARCADE_FLOOR_KEY], ItemClass.progression, ARCADE_FLOOR_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ARCADE_UNDERGROUND_KEY], ItemClass.progression, ARCADE_UNDERGROUND_KEY,
                      world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[STATUE_KEY], ItemClass.progression, STATUE_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ROBBER_KEY], ItemClass.progression, ROBBER_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ALCHEMIST_BADGE], ItemClass.progression, ALCHEMIST_BADGE, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[TCO_TRI_KEY], ItemClass.progression, TCO_TRI_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[PASSAGE_KEY], ItemClass.progression, PASSAGE_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    eat = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_EAT], ItemClass.useful, FUNC_EAT, world.player)

    world.multiworld.itempool.append(eat)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED], ItemClass.progression, CRYPTIC_CRAFTED, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED], ItemClass.progression, CRYPTIC_JEWELED, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], ItemClass.progression, CRYPTIC_OLD, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_MECHANICAL], ItemClass.progression, CRYPTIC_MECHANICAL,
                          world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_BOX], ItemClass.progression, FUNC_BOX, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_STURDY_BOX], ItemClass.progression, FUNC_STURDY_BOX, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_SPECIAL_BOX], ItemClass.progression, FUNC_SPECIAL_BOX, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_FANCY_VC], ItemClass.progression, FUNC_FANCY_VC, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_INCREADIBLE_VC], ItemClass.progression, FUNC_INCREADIBLE_VC, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_GREAT_VC], ItemClass.progression, FUNC_GREAT_VC, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    grind = LiesOfPItem(GRIND_ID_TO_NAME[GRIND_FLAME], ItemClass.useful, GRIND_FLAME, world.player)

    world.multiworld.itempool.append(grind)
    item_count += 1

    arm = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_FIRE], ItemClass.useful, MAT_FIRE, world.player)

    world.multiworld.itempool.append(arm)
    item_count += 1

    arm = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ELEC], ItemClass.useful, MAT_ELEC, world.player)

    world.multiworld.itempool.append(arm)
    item_count += 1

    for i in range(4):
        plug = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ARM_UNLOCK], ItemClass.useful, MAT_ARM_UNLOCK, world.player)

        world.multiworld.itempool.append(plug)
        item_count += 1

    for i in range(39):
        caliber = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ARM_UPGRADE], ItemClass.useful,
                              MAT_ARM_UPGRADE, world.player)

        world.multiworld.itempool.append(caliber)
        item_count += 1

    for i in range(4):
        key = LiesOfPItem(KEY_ID_TO_NAME[TRI_KEY], ItemClass.progression, TRI_KEY, world.player)

        world.multiworld.itempool.append(key)
        item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[RAIL_KEY], ItemClass.progression, RAIL_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    for i in range(28):
        hidden_moon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE], ItemClass.progression,
                                        MAT_WPN_UPGRADE, world.player)

        world.multiworld.itempool.append(hidden_moon_stone)
        item_count += 1

    for i in range(22):
        crescent_moon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE2], ItemClass.progression,
                                          MAT_WPN_UPGRADE2, world.player)

        world.multiworld.itempool.append(crescent_moon_stone)
        item_count += 1

    for i in range(24):
        half_moon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE3], ItemClass.progression,
                                      MAT_WPN_UPGRADE3, world.player)

        world.multiworld.itempool.append(half_moon_stone)
        item_count += 1

    for i in range(6):
        fullmoon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE4], ItemClass.progression,
                                     MAT_WPN_UPGRADE4, world.player)

        world.multiworld.itempool.append(fullmoon_stone)
        item_count += 1

    for i in range(22):
        dark_cov_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_SPECIAL_WPN_UPGRADE], ItemClass.progression,
                                     MAT_SPECIAL_WPN_UPGRADE, world.player)

        world.multiworld.itempool.append(dark_cov_stone)
        item_count += 1

    for i in range(5):
        full_cov_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_SPECIAL_WPN_UPGRADE2], ItemClass.progression,
                                     MAT_SPECIAL_WPN_UPGRADE2, world.player)
        world.multiworld.itempool.append(full_cov_stone)
        item_count += 1

    for i in range(25 + options.additional_quartz.value):
        quartz = LiesOfPItem(PORGAN_MATERIALS_ID_TO_NAME[MAT_PORGAN], ItemClass.progression, MAT_PORGAN, world.player)

        world.multiworld.itempool.append(quartz)
        item_count += 1

    for i in range(4):
        adv_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_ADV_CRANK], ItemClass.useful,
                                MAT_ADV_CRANK, world.player)

        world.multiworld.itempool.append(adv_crank)
        item_count += 1

    for i in range(7):
        bal_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_BAL_CRANK], ItemClass.useful,
                                MAT_BAL_CRANK, world.player)

        world.multiworld.itempool.append(bal_crank)
        item_count += 1

    for i in range(4):
        mot_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_MOT_CRANK], ItemClass.useful,
                                MAT_MOT_CRANK, world.player)

        world.multiworld.itempool.append(mot_crank)
        item_count += 1

    for i in range(4):
        tech_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_TECH_CRANK], ItemClass.useful,
                                 MAT_TECH_CRANK, world.player)

        world.multiworld.itempool.append(tech_crank)
        item_count += 1

    shop_weapons = [
        WPN_PUPPET_SABER, WPN_WINTERY_RAPIER, WPN_GREATSWORD_OF_FATE, WPN_ELECTRIC_COILSTICK, WPN_BRAMBLE_CURVED_SWORD,
        WPN_TYRANT_MURDERERS_DAGGER, WPN_CIRCULAR_ELECTRIC_CHAINSAW, WPN_PISTOL_ROCK_DRILL, WPN_MILITARY_SHOVEL,
        WPN_CARCASS_CRYSTAL_AXE
    ]
    for weaponId in ALL_NORMAL_WPN:
        if weaponId in shop_weapons and not options.shop_weapons:
            continue
        weapon_item = LiesOfPItem(NORMAL_WPN_ID_TO_NAME[weaponId], ItemClass.useful, weaponId, world.player)

        world.multiworld.itempool.append(weapon_item)
        item_count += 1

    for bossId in ALL_BOSS_ERGO:
        boss_item = LiesOfPItem(BOSS_ERGO_ID_TO_NAME[bossId], ItemClass.progression, bossId, world.player)

        world.multiworld.itempool.append(boss_item)
        item_count += 1

    if options.boss_weapons:
        for specialId in ALL_SPECIAL_WPN:
            if specialId == WPN_GOLDEN_LIE and not options.golden_lie:
                continue

            special_item = LiesOfPItem(SPECIAL_WPN_ID_TO_NAME[specialId], ItemClass.progression,
                                       specialId, world.player)

            world.multiworld.itempool.append(special_item)
            item_count += 1
    else:
        glaive_item = LiesOfPItem(SPECIAL_WPN_ID_TO_NAME[WPN_DRAGON_GLAIVE], ItemClass.progression, WPN_DRAGON_GLAIVE,
                                  world.player)

        world.multiworld.itempool.append(glaive_item)
        item_count += 1

    default_parts = [PARTS_BASIC_FRAME, PARTS_BASIC_CART, PARTS_BASIC_CONV, PARTS_BASIC_LINER]
    for partId in ALL_PARTS_MATERIALS:

        if partId in default_parts:
            continue

        part_item = LiesOfPItem(PARTS_ID_TO_NAME[partId], ItemClass.useful, partId, world.player)

        world.multiworld.itempool.append(part_item)
        item_count += 1

    for amuletId in ALL_AMULET:
        amulet_item = LiesOfPItem(AMULET_ID_TO_NAME[amuletId], ItemClass.useful, amuletId, world.player)

        world.multiworld.itempool.append(amulet_item)
        item_count += 1

    if options.boss_amulets:
        for bossAmuletId in ALL_BOSS_AMULET:
            boss_amulet_item = LiesOfPItem(BOSS_AMULET_ID_TO_NAME[bossAmuletId], ItemClass.useful, bossAmuletId,
                                           world.player)

            world.multiworld.itempool.append(boss_amulet_item)
            item_count += 1

    restricted_outfits = [OUTFIT_MISCHIEVOUS, OUTFIT_SIGNATURE]
    for outfitId in ALL_OUTFITS:
        if outfitId in restricted_outfits:
            continue

        outfit_item = LiesOfPItem(OUTFIT_ID_TO_NAME[outfitId], ItemClass.filler, outfitId, world.player)

        world.multiworld.itempool.append(outfit_item)
        item_count += 1

    restricted_accessory = [ACCESSORY_MISCHIEVOUS, ACCESSORY_VENIGNI_GLASS, ACCESSORY_PARADE]
    for accessoryId in ALL_ACCESSORY:
        if accessoryId in restricted_accessory:
            continue

        accessory_item = LiesOfPItem(ACCESSORY_ID_TO_NAME[accessoryId], ItemClass.filler, accessoryId, world.player)

        world.multiworld.itempool.append(accessory_item)
        item_count += 1

    filler = location_count - item_count
    add_filler(world, options, filler)


def king_of_puppets_item_pool(world: World, options: LiesOfPOptions):
    item_count = 0
    location_count = sum(1 for e in world.get_locations())

    key = LiesOfPItem(KEY_ID_TO_NAME[KCS_ENTRANCE_KEY], ItemClass.progression, KCS_ENTRANCE_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[KCH_KEY], ItemClass.progression, KCH_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[KCH_COURTYARD_KEY], ItemClass.progression, KCH_COURTYARD_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[SHACK_KEY], ItemClass.progression, SHACK_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ROSA_KEY], ItemClass.progression, ROSA_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[ROBBER_KEY], ItemClass.progression, ROBBER_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    eat = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_EAT], ItemClass.useful, FUNC_EAT, world.player)

    world.multiworld.itempool.append(eat)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_CRAFTED], ItemClass.progression, CRYPTIC_CRAFTED, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_JEWELED], ItemClass.progression, CRYPTIC_JEWELED, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    cryptic = LiesOfPItem(CRYPTIC_ID_TO_NAME[CRYPTIC_OLD], ItemClass.progression, CRYPTIC_OLD, world.player)

    world.multiworld.itempool.append(cryptic)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_BOX], ItemClass.progression, FUNC_BOX, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    box = LiesOfPItem(FUNC_ID_TO_NAME[FUNC_INCREADIBLE_VC], ItemClass.progression, FUNC_INCREADIBLE_VC, world.player)

    world.multiworld.itempool.append(box)
    item_count += 1

    grind = LiesOfPItem(GRIND_ID_TO_NAME[GRIND_FLAME], ItemClass.useful, GRIND_FLAME, world.player)

    world.multiworld.itempool.append(grind)
    item_count += 1

    arm = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_FIRE], ItemClass.useful, MAT_FIRE, world.player)

    world.multiworld.itempool.append(arm)
    item_count += 1

    arm = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ELEC], ItemClass.useful, MAT_ELEC, world.player)

    world.multiworld.itempool.append(arm)
    item_count += 1

    for i in range(2):
        plug = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ARM_UNLOCK], ItemClass.useful, MAT_ARM_UNLOCK, world.player)

        world.multiworld.itempool.append(plug)
        item_count += 1

    for i in range(5):
        caliber = LiesOfPItem(ARM_MATERIALS_ID_TO_NAME[MAT_ARM_UPGRADE], ItemClass.useful,
                              MAT_ARM_UPGRADE, world.player)

        world.multiworld.itempool.append(caliber)
        item_count += 1

    for i in range(3):
        key = LiesOfPItem(KEY_ID_TO_NAME[TRI_KEY], ItemClass.progression, TRI_KEY, world.player)

        world.multiworld.itempool.append(key)
        item_count += 1

    key = LiesOfPItem(KEY_ID_TO_NAME[RAIL_KEY], ItemClass.progression, RAIL_KEY, world.player)

    world.multiworld.itempool.append(key)
    item_count += 1

    for i in range(22):
        hidden_moon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE], ItemClass.progression,
                                        MAT_WPN_UPGRADE, world.player)

        world.multiworld.itempool.append(hidden_moon_stone)
        item_count += 1

    for i in range(10):
        crescent_moon_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_WPN_UPGRADE2], ItemClass.progression,
                                          MAT_WPN_UPGRADE2, world.player)

        world.multiworld.itempool.append(crescent_moon_stone)
        item_count += 1

    for i in range(5):
        dark_cov_stone = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_SPECIAL_WPN_UPGRADE], ItemClass.progression,
                                     MAT_SPECIAL_WPN_UPGRADE, world.player)

        world.multiworld.itempool.append(dark_cov_stone)
        item_count += 1

    for i in range(11 + options.additional_quartz.value):
        quartz = LiesOfPItem(PORGAN_MATERIALS_ID_TO_NAME[MAT_PORGAN], ItemClass.progression, MAT_PORGAN, world.player)

        world.multiworld.itempool.append(quartz)
        item_count += 1

    for i in range(2):
        adv_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_ADV_CRANK], ItemClass.useful,
                                MAT_ADV_CRANK, world.player)

        world.multiworld.itempool.append(adv_crank)
        item_count += 1

    for i in range(1):
        bal_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_BAL_CRANK], ItemClass.useful,
                                MAT_BAL_CRANK, world.player)

        world.multiworld.itempool.append(bal_crank)
        item_count += 1

    for i in range(2):
        mot_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_MOT_CRANK], ItemClass.useful,
                                MAT_MOT_CRANK, world.player)

        world.multiworld.itempool.append(mot_crank)
        item_count += 1

    for i in range(2):
        tech_crank = LiesOfPItem(WEAPON_MATERIALS_ID_TO_NAME[MAT_TECH_CRANK], ItemClass.useful,
                                 MAT_TECH_CRANK, world.player)

        world.multiworld.itempool.append(tech_crank)
        item_count += 1

    shop_weapons = [
        WPN_PUPPET_SABER, WPN_WINTERY_RAPIER, WPN_GREATSWORD_OF_FATE, WPN_ELECTRIC_COILSTICK, WPN_BRAMBLE_CURVED_SWORD,
        WPN_TYRANT_MURDERERS_DAGGER, WPN_CIRCULAR_ELECTRIC_CHAINSAW, WPN_PISTOL_ROCK_DRILL, WPN_MILITARY_SHOVEL,
        WPN_CARCASS_CRYSTAL_AXE
    ]
    # weapon_pool = [item for item in ALL_NORMAL_WPN if not (item in shop_weapons)]
    # if options.shop_weapons:
    #     weapon_pool += shop_weapons
    # if options.boss_weapons:
    #     weapon_pool += [item for item in ALL_SPECIAL_WPN if not item == WPN_GOLDEN_LIE]
    # if options.golden_lie:
    #     weapon_pool.append(WPN_GOLDEN_LIE)
    # for i in range(15):
    #     weapon_id = world.random.choice(weapon_pool)
    #     item = None
    #     if weapon_id in ALL_SPECIAL_WPN:
    #         item = LiesOfPItem(SPECIAL_WPN_ID_TO_NAME[weapon_id], ItemClass.progression, weapon_id, world.player)
    #     item = LiesOfPItem(NORMAL_WPN_ID_TO_NAME[weapon_id], ItemClass.useful, weapon_id, world.player)
    #     world.multiworld.itempool.append(item)
    #     item_count += 1
    #     weapon_pool.remove(weapon_id)

    for weaponId in ALL_NORMAL_WPN:
        if weaponId in shop_weapons and not options.shop_weapons:
            continue
        weapon_item = LiesOfPItem(NORMAL_WPN_ID_TO_NAME[weaponId], ItemClass.useful, weaponId, world.player)

        world.multiworld.itempool.append(weapon_item)
        item_count += 1

    if options.boss_weapons:
        for specialId in ALL_SPECIAL_WPN:
            if specialId == WPN_GOLDEN_LIE and not options.golden_lie:
                continue

            special_item = LiesOfPItem(SPECIAL_WPN_ID_TO_NAME[specialId], ItemClass.progression,
                                       specialId, world.player)

            world.multiworld.itempool.append(special_item)
            item_count += 1
    else:
        glaive_item = LiesOfPItem(SPECIAL_WPN_ID_TO_NAME[WPN_DRAGON_GLAIVE], ItemClass.progression, WPN_DRAGON_GLAIVE,
                                  world.player)

        world.multiworld.itempool.append(glaive_item)
        item_count += 1

    for bossId in ALL_BOSS_ERGO:

        boss_item = LiesOfPItem(BOSS_ERGO_ID_TO_NAME[bossId], ItemClass.progression, bossId, world.player)

        world.multiworld.itempool.append(boss_item)
        item_count += 1

    default_parts = [PARTS_BASIC_FRAME, PARTS_BASIC_CART, PARTS_BASIC_CONV, PARTS_BASIC_LINER]
    for partId in ALL_PARTS_MATERIALS:

        if partId in default_parts:
            continue

        part_item = LiesOfPItem(PARTS_ID_TO_NAME[partId], ItemClass.useful, partId, world.player)

        world.multiworld.itempool.append(part_item)
        item_count += 1

    for amuletId in ALL_AMULET:
        amulet_item = LiesOfPItem(AMULET_ID_TO_NAME[amuletId], ItemClass.useful, amuletId, world.player)

        world.multiworld.itempool.append(amulet_item)
        item_count += 1

    if options.boss_amulets:
        for bossAmuletId in ALL_BOSS_AMULET:
            boss_amulet_item = LiesOfPItem(BOSS_AMULET_ID_TO_NAME[bossAmuletId], ItemClass.useful, bossAmuletId,
                                           world.player)

            world.multiworld.itempool.append(boss_amulet_item)
            item_count += 1

    restricted_outfits = [OUTFIT_MISCHIEVOUS, OUTFIT_SIGNATURE]
    for outfitId in ALL_OUTFITS:
        if outfitId in restricted_outfits:
            continue

        outfit_item = LiesOfPItem(OUTFIT_ID_TO_NAME[outfitId], ItemClass.filler, outfitId, world.player)

        world.multiworld.itempool.append(outfit_item)
        item_count += 1

    restricted_accessory = [ACCESSORY_MISCHIEVOUS, ACCESSORY_VENIGNI_GLASS, ACCESSORY_PARADE]
    for accessoryId in ALL_ACCESSORY:
        if accessoryId in restricted_accessory:
            continue

        accessory_item = LiesOfPItem(ACCESSORY_ID_TO_NAME[accessoryId], ItemClass.filler, accessoryId, world.player)

        world.multiworld.itempool.append(accessory_item)
        item_count += 1

    filler = location_count - item_count
    add_filler(world, options, filler)


def add_filler(world: World, options: LiesOfPOptions, filler):
    print(filler)  # TODO REMOVE PRINT

    for i in range(filler):

        filler_choice = world.random.randint(0, 2)

        match filler_choice:
            case 0:
                ergo_id = world.random.choice(ALL_ERGO)
                item = (LiesOfPItem(ERGO_ID_TO_NAME[ergo_id], ItemClass.filler, ergo_id, world.player))
                world.multiworld.itempool.append(item)
            case 1:
                throw_id = world.random.choice(All_THROW)
                item = (LiesOfPItem(THROW_ID_TO_NAME[throw_id], ItemClass.filler, throw_id, world.player))
                world.multiworld.itempool.append(item)
            case 2:
                consume_id = world.random.choice(All_CONSUME)
                item = (LiesOfPItem(CONSUME_ID_TO_NAME[consume_id], ItemClass.filler, consume_id, world.player))
                world.multiworld.itempool.append(item)
