
from .ItemLists.Collectables import *
from .ItemLists.Keys import *
from .ItemLists.Materials import *
from .ItemLists.Useables import *
from .ItemLists.Functionals import *
from .ItemLists.Weapons import *
from .ItemLists.Parts import *
from .ItemLists.Costumes import *
from .ItemLists.Gestures import *
from .ItemLists.Amulets import *
from .LocationLists.Chapters import *

item_name_groups = {
    "Key Items":          list(KEY_ID_TO_NAME.values()) + list(DLC_KEYS_ID_TO_NAME.values()),
    "Weapons":            list(NORMAL_WPN_ID_TO_NAME.values()) + list(DLC_WPN_ID_TO_NAME.values()),
    "Special Weapons":    list(SPECIAL_WPN_ID_TO_NAME.values()) + list(DLC_SPECIAL_WPN_ID_TO_NAME.values()),
    "Amulets":            list(AMULET_ID_TO_NAME.values()) + list(DLC_AMULET_ID_TO_NAME.values()),
    "Boss Amulets":       list(BOSS_AMULET_ID_TO_NAME.values()) + list(DLC_BOSS_AMULET_ID_TO_NAME.values()),
    "Puppet Parts":       list(PARTS_ID_TO_NAME.values()) + list(DLC_PARTS_ID_TO_NAME.values()),
    "Costumes":           list(OUTFIT_ID_TO_NAME.values()) + list(ACCESSORY_ID_TO_NAME.values()) +
                          list(DLC_OUTFIT_ID_TO_NAME.values()) + list(DLC_ACCESSORY_ID_TO_NAME.values()),
    "Upgrade Materials":  list(WEAPON_MATERIALS_ID_TO_NAME.values()) + list(ARM_MATERIALS_ID_TO_NAME.values()) +
                          list(DLC_ARM_MATERIAL_ID_TO_NAME.values()) + list(PORGAN_MATERIALS_ID_TO_NAME.values()),
    "Ergo":               list(ERGO_ID_TO_NAME.values()),
    "Boss Ergo":          list(BOSS_ERGO_ID_TO_NAME.values()) + list(DLC_BOSS_ERGO_ID_TO_NAME.values()),
    "Consumables":        list(CONSUME_ID_TO_NAME.values()) + list(THROW_ID_TO_NAME.values()) +
                          list(DLC_CONSUME_ID_TO_NAME.values()),
    "Cryptic Vessels":    list(DECRYPT_ID_TO_NAME.values()) + list(DLC_CRYPTIC_ID_TO_NAME.values()),
    "Functional Items":   list(FUNC_ID_TO_NAME.values()) + list(BASIC_ID_TO_NAME.values()) + list(DLC_GRIND_ID_TO_NAME.values()),
    "Gestures":           list(GES_ID_TO_NAME.values()) + list(DLC_GES_ID_TO_NAME.values()),
    "Recollections":      list(RECOLLECTION_ID_TO_NAME.values()) + list(DLC_RECOLLECTION_ID_TO_NAME.values()),
}

location_name_groups = {
    "Krat Central Station" :[name for name in KCS_ID_TO_NAME.values()],
    "Krat Central Station Plaza" :[name for name in KCSP_ID_TO_NAME.values()],
    "Hotel Krat" :[name for name in HK1_ID_TO_NAME.values()],
    "Elysion Boulevard" :[name for name in EB_ID_TO_NAME.values()],
    "Krat City Hall" :[name for name in KCH_ID_TO_NAME.values()],
    "Workshop Union Entrance" :[name for name in WUE_ID_TO_NAME.values()],
    "Venigni Works" :[name for name in VW_ID_TO_NAME.values()],
    "Moonlight Town" :[name for name in MT_ID_TO_NAME.values()],
    "Path of Misery" :[name for name in POM_ID_TO_NAME.values()],
    "St.Frangelico Cathedral Chapel" :[name for name in SFCC_ID_TO_NAME.values()],
    "Path of the Pilgrim" :[name for name in POTP_ID_TO_NAME.values()],
    "Tomb Slums" :[name for name in TS_ID_TO_NAME.values()],
    "Hobbler's Bridge" :[name for name in HB_ID_TO_NAME.values()],
    "Malum District" :[name for name in MD_ID_TO_NAME.values()],
    "Rosa Isabelle Street" :[name for name in RIS_ID_TO_NAME.values()],
    "Estella Opera House Entrance" :[name for name in EOHE_ID_TO_NAME.values()],
    "Estella Opera House Stage" :[name for name in EOHS_ID_TO_NAME.values()],
    "Charity Market Path":[name for name in CMP_ID_TO_NAME.values()],
    "Lorenzini Arcade" :[name for name in LA_ID_TO_NAME.values()],
    "First Floor Lorenzini Arcade" :[name for name in FLA_ID_TO_NAME.values()],
    "Underground Lorenzini Arcade" :[name for name in ULA_ID_TO_NAME.values()],
    "Grand Exhibition Plaza" :[name for name in GEP_ID_TO_NAME.values()],
    "Grand Exhibition Gallery" :[name for name in GEG_ID_TO_NAME.values()],
    "Baron Swamp" :[name for name in BS_ID_TO_NAME.values()],
    "Closed Railway" :[name for name in CR_ID_TO_NAME.values()],
    "Krat Central Station Revisit" :[name for name in KCS2_ID_TO_NAME.values()],
    "Collapsed Street" :[name for name in CS_ID_TO_NAME.values()],
    "Collapsing Krat" :[name for name in CK_ID_TO_NAME.values()],
    "Hermit's Cave" :[name for name in HC_ID_TO_NAME.values()],
    "Relic of Trismegistus" :[name for name in ROT_ID_TO_NAME.values()],
    "Black Seaside" :[name for name in BSS_ID_TO_NAME.values()],
    "Arche Abbey Entrance" :[name for name in AAE_ID_TO_NAME.values()],
    "Arche Abbey Outer Wall" :[name for name in AAOW_ID_TO_NAME.values()],
    "Arche Abbey Upper" :[name for name in AAU_ID_TO_NAME.values()],
    "Arche Abbey Passageway" :[name for name in AAP_ID_TO_NAME.values()],
    "Arche Abbey Cradle of the God" :[name for name in AACG_ID_TO_NAME.values()],
    "Under the Abyss" :[name for name in UTA_ID_TO_NAME.values()],
    "Strange Forest" :[name for name in SF_ID_TO_NAME.values()],
    "Krat Zoo" :[name for name in KZ_ID_TO_NAME.values()],
    "Savanna Experience Center" :[name for name in SEC_ID_TO_NAME.values()],
    "Greenhouse Interior" :[name for name in GI_ID_TO_NAME.values()],
    "Carnival Garden" :[name for name in CG_ID_TO_NAME.values()],
    "Black Rabbit Brotherhood" :[name for name in BRB_ID_TO_NAME.values()],
    "Zoo Tram Station" :[name for name in ZTS_ID_TO_NAME.values()],
    "Eventide Hotel Krat" :[name for name in EHK_ID_TO_NAME.values()],
    "Zelator Underground Facility" :[name for name in ZUF_ID_TO_NAME.values()],
    "Zelator Underground Facility Unfrozen" :[name for name in ZUFU_ID_TO_NAME.values()],
    "Elixir Research Zone" :[name for name in ERZ_ID_TO_NAME.values()],
    "Ancient Ruins Excavation Site" :[name for name in ARES_ID_TO_NAME.values()],
    "Secret Ruins" :[name for name in SR_ID_TO_NAME.values()],
    "Abandoned Excavation Campsite" :[name for name in AEC_ID_TO_NAME.values()],
    "Sea Cliffs" :[name for name in SC_ID_TO_NAME.values()],
    "Pleroma Forest Cave" :[name for name in PFC_ID_TO_NAME.values()],
    "Rose Estate" :[name for name in RE_ID_TO_NAME.values()],
    "Rose Garden" :[name for name in RG_ID_TO_NAME.values()],
}