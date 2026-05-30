#Weapons


# Wep_Scythe = 1
Wep_Sword = 2
Wep_Bow = 3
Wep_Bat = 4
Wep_Umbrella = 5
Wep_Lamp = 6
Wep_Fan = 7

WEAPON_ID_TO_NAME = {
    # Wep_Scythe: "Scythe",
    Wep_Sword: "Kiddo's Sword",
    Wep_Bow: "Daredemian's Bow",
    Wep_Bat: "Bulgasari's Bat",
    Wep_Umbrella: "Red Fugituve Soul's Umbrella",
    Wep_Lamp: "Sen's Lamp",
    Wep_Fan: "Fan",
}

ALL_WEAPON = list(WEAPON_ID_TO_NAME.keys())

#Abilities
# Abl_DownJump = 105 Doesn't get removed in last region so it is probably best not to randomize it or make an option later
# Abl_Skill = 108 Don't need this it is added when we get the guard
Abl_Dash = 110
Abl_WallHold = 111
Abl_DoubleJump = 112
#Abl_UseItem = 113 Healing probably not gonna make this a item LOL
Abl_SuperJump = 117
Abl_SuperDash = 118
Abl_BreakWall = 119

ABILITIES_ID_TO_NAME = {
    Abl_Dash: "Dash",
    Abl_WallHold: "Wall Jump",
    Abl_DoubleJump: "Double Jump",
    #Abl_UseItem: "Heal",
    Abl_SuperJump: "Power Leap",
    Abl_SuperDash: "Super Wall Dash",
    Abl_BreakWall: "Throw Punch"
}

ALL_ABILITIES = list(ABILITIES_ID_TO_NAME.keys())

#Currency
Dawn_1 = 202
Coin_12 = 203
FugitiveSoulReward = 204

CURRECY_ID_TO_NAME = {
    Dawn_1: "Dawn",
    Coin_12: "12 Coins",
    FugitiveSoulReward: "Fugitive Souls Reward",
}

ALL_CURRENCY = list(CURRECY_ID_TO_NAME.keys())

#Upgrades
Potion_Upgrade_1 = 301
Potion_Upgrade_2 = 302
Potion_Upgrade_3 = 303
Potion_Upgrade_4 = 304
MaxHp_Up_1 = 401
MaxHp_Up_2 = 402
MaxHp_Up_3 = 403
MaxHp_Up_4 = 404
MaxMp_Up_1 = 501
MaxMp_Up_2 = 502
MaxMp_Up_3 = 503
MaxMp_Up_4 = 504
Respec = 601
Thurible_UP_1 = 701
Thurible_UP_2 = 702

UPGRADE_ID_TO_NAME = {
    Potion_Upgrade_1: "Hot Potion",
    Potion_Upgrade_2: "C-tamin Potion",
    Potion_Upgrade_3: "Dokaebi Potion",
    Potion_Upgrade_4: "Redfire Potion",
    MaxHp_Up_1: "Red Comma Jade",
    MaxHp_Up_2: "Red Iron Comma Jade",
    MaxHp_Up_3: "Red Steel Comma Jade",
    MaxHp_Up_4: "Red Ultimate Comma Jade",
    MaxMp_Up_1: "White Comma Jade",
    MaxMp_Up_2: "White Iron Comma Jade",
    MaxMp_Up_3: "White Steel Comma Jade",
    MaxMp_Up_4: "White Ultimate Comma Jade",
    Respec: "Root of Oblivian",
    Thurible_UP_1: "Phoenix Thurible",
    Thurible_UP_2: "Mir Thirible",
}

ALL_UPGRADE = list(UPGRADE_ID_TO_NAME.keys())

#Maps
Kingdom_Of_Yama_Map = 800
Stone_Mountain_Map = 801
Misty_Forest_Map = 802
Barron_Grounds_Map = 803
Crimson_Mines_Map = 804
Frozen_Plateau_Map = 805
Underground_Waterway_Map = 806
Land_of_Abundance_Map = 807

MAP_ID_TO_NAME = {
    Kingdom_Of_Yama_Map: "Kingdom of Yama Map",
    Stone_Mountain_Map: "Stone Mountain Map",
    Misty_Forest_Map: "Misty Forest Map",
    Barron_Grounds_Map: "Barron Grounds Map",
    Crimson_Mines_Map: "Crimson Mines Map",
    Frozen_Plateau_Map: "Frozen Plateau Map",
    Underground_Waterway_Map: "Underground Waterways Map",
    Land_of_Abundance_Map: "Land of Abundance Map"
}

ALL_MAP = list(MAP_ID_TO_NAME.keys())

NamePlate = 907
Gourd = 904
Thurible = 906

VAL_ID_TO_NAME = {
    NamePlate: "Name Plate",
    Gourd: "Gourd",
    Thurible: "Thurible"
}

ALL_VAL = list(VAL_ID_TO_NAME.keys())

Fugitive = 1000

FUGITIVE_SOUL_ID_TO_NAME = {
    Fugitive: "Fugitive Soul"
}

ALL_FUGITIVE_SOUL = list(FUGITIVE_SOUL_ID_TO_NAME.keys())

Bone_Born_Flower = 8100
Flesh_Fresh_Flower = 8101
Unknown_Flower = 8102
Breath_Bless_Flower = 8103
Spirit_Soul_Flower = 8104
Peaceful_Presence_Flower = 8105
Whispering_Will_Flower = 8106

FLOWER_ID_TO_NAME = {
    Bone_Born_Flower: "Bone Born Flower",
    Flesh_Fresh_Flower: "Flesh Fresh Flower",
    Unknown_Flower: "Unknown Flower",
    Breath_Bless_Flower: "Breath Bless Flower",
    Spirit_Soul_Flower: "Spirit Soul Flower",
    Peaceful_Presence_Flower: "Peaceful Presence Flower",
    Whispering_Will_Flower: "Whispering Will Flower",
}

ALL_FLOWER = list(FLOWER_ID_TO_NAME.keys())

Mirror_Shard_1 = 8302
Mirror_Shard_2 = 8303
Mirror_Shard_3 = 8304
Mirror_Shard_4 = 8301
Mirror_Shard_5 = 8305
Mirror_Shard_6 = 8300

MIRROR_ID_TO_NAME = {
    Mirror_Shard_1: "Barron Grounds Mirror Shard",
    Mirror_Shard_2: "Crimson Mines Mirror Shard",
    Mirror_Shard_3: "Frozen Plateau Mirror Shard",
    Mirror_Shard_4: "Misty Forest Mirror Shard",
    Mirror_Shard_5: "Underground Waterway Mirror Shard",
    Mirror_Shard_6: "Stone Mountain Mirror Shard"
}

ALL_MIRROR = list(MIRROR_ID_TO_NAME.keys())

Book_Death_1 = 8201
Book_Destiny = 8202
Book_Death_2 = 8203
Book_Path = 8204
Book_Data = 8205
Book_Sin = 8206

BOOK_ID_TO_NAME = {
    Book_Death_1: "Book: Voluntary Traveler of Death (1)",
    Book_Destiny: "Book: Destiny",
    Book_Death_2: "Book: Voluntary Traveler of Death (2)",
    Book_Path: "Book: The Path to Kkokdu",
    Book_Data : "Book: Research Data on Human Nature",
    Book_Sin: "Book: Requirement for Injecting Sin and its Effects"
}

ALL_BOOK = list(BOOK_ID_TO_NAME.keys())


