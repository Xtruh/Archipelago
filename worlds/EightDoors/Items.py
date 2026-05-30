from BaseClasses import Item, ItemClassification as ItemClass
from . import EightDoorsOptions
from .ItemList import *
from ..AutoWorld import World

class EightDoorsItem(Item):
    game = "8Doors Arum's Afterlife Adventure"

    def __init__(self, name: str, classification: ItemClass, id: int, player):
        super().__init__(name, classification, id, player)

def get_item_dict():
    result = {}
    for weaponId in ALL_WEAPON:
        result[WEAPON_ID_TO_NAME[weaponId]] = weaponId

    for abilityId in ALL_ABILITIES:
        result[ABILITIES_ID_TO_NAME[abilityId]] = abilityId

    for currencyId in ALL_CURRENCY:
        result[CURRECY_ID_TO_NAME[currencyId]] = currencyId

    for fugitiveId in ALL_FUGITIVE_SOUL:
        result[FUGITIVE_SOUL_ID_TO_NAME[fugitiveId]] = fugitiveId

    for mapID in ALL_MAP:
        result[MAP_ID_TO_NAME[mapID]] = mapID

    for flowerID in ALL_FLOWER:
        result[FLOWER_ID_TO_NAME[flowerID]] = flowerID

    for mirrorID in ALL_MIRROR:
        result[MIRROR_ID_TO_NAME[mirrorID]] = mirrorID

    for valID in ALL_VAL:
        result[VAL_ID_TO_NAME[valID]] = valID
    return result

def populate_item_pool(world: World, options: EightDoorsOptions):

    for weaponId in ALL_WEAPON:
        weapon = EightDoorsItem(WEAPON_ID_TO_NAME[weaponId], ItemClass.progression, weaponId, world.player)

        world.multiworld.itempool.append(weapon)

    for abilityId in ALL_ABILITIES:
        ability = EightDoorsItem(ABILITIES_ID_TO_NAME[abilityId], ItemClass.progression, abilityId, world.player)

        world.multiworld.itempool.append(ability)

    for i in range (54):
        coin = EightDoorsItem(CURRECY_ID_TO_NAME[Coin_12], ItemClass.filler, Coin_12, world.player)
        world.multiworld.itempool.append(coin)

    if options.goal.value == options.goal.option_fugitive_souls_hunt:
        for i in range (48):
            soul = EightDoorsItem(FUGITIVE_SOUL_ID_TO_NAME[Fugitive], ItemClass.progression, Fugitive, world.player)

            world.multiworld.itempool.append(soul)
    else:
        for i in range (48):
            soul = EightDoorsItem(FUGITIVE_SOUL_ID_TO_NAME[Fugitive], ItemClass.filler, Fugitive, world.player)

            world.multiworld.itempool.append(soul)

    for mapId in ALL_MAP:
        map_item = EightDoorsItem(MAP_ID_TO_NAME[mapId], ItemClass.useful, mapId, world.player)

        world.multiworld.itempool.append(map_item)

    for flowerId in ALL_FLOWER:
        flower = EightDoorsItem(FLOWER_ID_TO_NAME[flowerId], ItemClass.progression, flowerId, world.player)

        world.multiworld.itempool.append(flower)

    for mirrorId in ALL_MIRROR:
        mirror = EightDoorsItem(MIRROR_ID_TO_NAME[mirrorId], ItemClass.progression, mirrorId, world.player)

        world.multiworld.itempool.append(mirror)

    val = EightDoorsItem(VAL_ID_TO_NAME[Gourd], ItemClass.progression, Gourd, world.player)
    world.multiworld.itempool.append(val)

    val = EightDoorsItem(VAL_ID_TO_NAME[NamePlate], ItemClass.filler, NamePlate, world.player)
    world.multiworld.itempool.append(val)

    val = EightDoorsItem(VAL_ID_TO_NAME[Thurible], ItemClass.filler, Thurible, world.player)
    world.multiworld.itempool.append(val)

    for i in range (37):
        dawn = EightDoorsItem(CURRECY_ID_TO_NAME[Dawn_1], ItemClass.progression, Dawn_1, world.player)
        world.multiworld.itempool.append(dawn)