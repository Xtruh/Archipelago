from typing import Dict

from BaseClasses import Location, Region
from . import LiesOfPOptions
from .ItemLists.Collectables import *
from .ItemLists.Keys import *
from .ItemLists.Useables import *
from .LocationLists.Chapters import *
from ..AutoWorld import World
from ..generic.Rules import add_rule


class LiesOfPLocation(Location):
    game: str = "Lies Of P"

    def __init__(self, player, location_name, location_id, region):
        super().__init__(player, location_name, location_id, region)


def get_location_dict():
    result = {}

    for KCSId in All_KCS:
        result[KCS_ID_TO_NAME[KCSId]] = KCSId

    for KCSPId in All_KCSP:
        result[KCSP_ID_TO_NAME[KCSPId]] = KCSPId

    for HK1Id in All_HK1:
        result[HK1_ID_TO_NAME[HK1Id]] = HK1Id

    for EBId in ALL_EB:
        result[EB_ID_TO_NAME[EBId]] = EBId

    for KCHId in ALL_KCH:
        result[KCH_ID_TO_NAME[KCHId]] = KCHId

    for WUEId in ALL_WUE:
        result[WUE_ID_TO_NAME[WUEId]] = WUEId

    for VWId in ALL_VW:
        result[VW_ID_TO_NAME[VWId]] = VWId

    for MTId in ALL_MT:
        result[MT_ID_TO_NAME[MTId]] = MTId

    for POMId in ALL_POM:
        result[POM_ID_TO_NAME[POMId]] = POMId

    for SFCCId in ALL_SFCC:
        result[SFCC_ID_TO_NAME[SFCCId]] = SFCCId

    for POTPId in ALL_POTP:
        result[POTP_ID_TO_NAME[POTPId]] = POTPId

    for TSId in ALL_TS:
        result[TS_ID_TO_NAME[TSId]] = TSId

    for HBId in ALL_HB:
        result[HB_ID_TO_NAME[HBId]] = HBId

    for MDId in ALL_MD:
        result[MD_ID_TO_NAME[MDId]] = MDId

    for RISId in ALL_RIS:
        result[RIS_ID_TO_NAME[RISId]] = RISId

    for EOHEId in ALL_EOHE:
        result[EOHE_ID_TO_NAME[EOHEId]] = EOHEId

    for EOHSId in ALL_EOHS:
        result[EOHS_ID_TO_NAME[EOHSId]] = EOHSId

    for CMPId in ALL_CMP:
        result[CMP_ID_TO_NAME[CMPId]] = CMPId

    for LAId in ALL_LA:
        result[LA_ID_TO_NAME[LAId]] = LAId

    for FLAId in ALL_FLA:
        result[FLA_ID_TO_NAME[FLAId]] = FLAId

    for ULAId in ALL_ULA:
        result[ULA_ID_TO_NAME[ULAId]] = ULAId

    for GEPId in ALL_GEP:
        result[GEP_ID_TO_NAME[GEPId]] = GEPId

    for GEGId in ALL_GEG:
        result[GEG_ID_TO_NAME[GEGId]] = GEGId

    for BSId in ALL_BS:
        result[BS_ID_TO_NAME[BSId]] = BSId

    for CRId in ALL_CR:
        result[CR_ID_TO_NAME[CRId]] = CRId

    for KCS2Id in ALL_KCS2:
        result[KCS2_ID_TO_NAME[KCS2Id]] = KCS2Id

    for CSId in ALL_CS:
        result[CS_ID_TO_NAME[CSId]] = CSId

    for CKId in ALL_CK:
        result[CK_ID_TO_NAME[CKId]] = CKId

    for CSId in ALL_CS:
        result[CS_ID_TO_NAME[CSId]] = CSId

    for CKId in ALL_CK:
        result[CK_ID_TO_NAME[CKId]] = CKId

    for HCId in ALL_HC:
        result[HC_ID_TO_NAME[HCId]] = HCId

    for ROTId in ALL_ROT:
        result[ROT_ID_TO_NAME[ROTId]] = ROTId

    for BSSId in ALL_BSS:
        result[BSS_ID_TO_NAME[BSSId]] = BSSId

    for AAEId in ALL_AAE:
        result[AAE_ID_TO_NAME[AAEId]] = AAEId

    for AAOWId in ALL_AAOW:
        result[AAOW_ID_TO_NAME[AAOWId]] = AAOWId

    for AAUId in ALL_AAU:
        result[AAU_ID_TO_NAME[AAUId]] = AAUId

    for AAPId in ALL_AAP:
        result[AAP_ID_TO_NAME[AAPId]] = AAPId

    for AACGId in ALL_AACG:
        result[AACG_ID_TO_NAME[AACGId]] = AACGId

    for UTAId in ALL_UTA:
        result[UTA_ID_TO_NAME[UTAId]] = UTAId
    return result


def create_locations(world: World, regions: Dict[str, Region], options: LiesOfPOptions):
    kcs_region = regions["Krat Central Station"]

    for KCSId in All_KCS:
        loc = LiesOfPLocation(world.player, KCS_ID_TO_NAME[KCSId], KCSId, kcs_region)
        kcs_region.locations.append(loc)

    kcsp_region = regions["Krat Central Station Plaza"]

    for KCSPId in All_KCSP:
        loc = LiesOfPLocation(world.player, KCSP_ID_TO_NAME[KCSPId], KCSPId, kcsp_region)
        kcsp_region.locations.append(loc)

    hk1_region = regions["Hotel Krat"]

    for HK1Id in All_HK1:
        loc = LiesOfPLocation(world.player, HK1_ID_TO_NAME[HK1Id], HK1Id, hk1_region)
        hk1_region.locations.append(loc)

    eb_region = regions["Elysion Boulevard"]
    for EBId in ALL_EB:
        loc = LiesOfPLocation(world.player, EB_ID_TO_NAME[EBId], EBId, eb_region)
        eb_region.locations.append(loc)

    kch_region = regions["Krat City Hall"]
    for KCHId in ALL_KCH:
        loc = LiesOfPLocation(world.player, KCH_ID_TO_NAME[KCHId], KCHId, kch_region)
        kch_region.locations.append(loc)

    wue_region = regions["Workshop Union Entrance"]
    for WUEId in ALL_WUE:
        loc = LiesOfPLocation(world.player, WUE_ID_TO_NAME[WUEId], WUEId, wue_region)
        wue_region.locations.append(loc)

    vw_region = regions["Venigni Works"]
    for VWId in ALL_VW:
        loc = LiesOfPLocation(world.player, VW_ID_TO_NAME[VWId], VWId, vw_region)
        vw_region.locations.append(loc)

    mt_region = regions["Moonlight Town"]
    for MTId in ALL_MT:
        loc = LiesOfPLocation(world.player, MT_ID_TO_NAME[MTId], MTId, mt_region)
        mt_region.locations.append(loc)

    pom_region = regions["Path of Misery"]
    for POMId in ALL_POM:
        loc = LiesOfPLocation(world.player, POM_ID_TO_NAME[POMId], POMId, pom_region)
        pom_region.locations.append(loc)

    sfcc_region = regions["St.Frangelico Cathedral Chapel"]
    for SFCCId in ALL_SFCC:
        loc = LiesOfPLocation(world.player, SFCC_ID_TO_NAME[SFCCId], SFCCId, sfcc_region)
        sfcc_region.locations.append(loc)

    potp_region = regions["Path of the Pilgrim"]
    for POTPId in ALL_POTP:
        loc = LiesOfPLocation(world.player, POTP_ID_TO_NAME[POTPId], POTPId, potp_region)
        potp_region.locations.append(loc)

    ts_region = regions["Tomb Slums"]
    for TSId in ALL_TS:
        loc = LiesOfPLocation(world.player, TS_ID_TO_NAME[TSId], TSId, ts_region)
        ts_region.locations.append(loc)

    hb_region = regions["Hobbler's Bridge"]
    for HBId in ALL_HB:
        loc = LiesOfPLocation(world.player, HB_ID_TO_NAME[HBId], HBId, hb_region)
        hb_region.locations.append(loc)

    md_region = regions["Malum District"]
    for MDId in ALL_MD:
        loc = LiesOfPLocation(world.player, MD_ID_TO_NAME[MDId], MDId, md_region)
        md_region.locations.append(loc)

    ris_region = regions["Rosa Isabelle Street"]
    for RISId in ALL_RIS:
        loc = LiesOfPLocation(world.player, RIS_ID_TO_NAME[RISId], RISId, ris_region)
        ris_region.locations.append(loc)

    eohe_region = regions["Estella Opera House Entrance"]
    for EOHEId in ALL_EOHE:
        loc = LiesOfPLocation(world.player, EOHE_ID_TO_NAME[EOHEId], EOHEId, eohe_region)
        eohe_region.locations.append(loc)

    eohs_region = regions["Estella Opera House Stage"]
    for EOHSId in ALL_EOHS:
        loc = LiesOfPLocation(world.player, EOHS_ID_TO_NAME[EOHSId], EOHSId, eohs_region)
        eohs_region.locations.append(loc)

    if options.goal.value == options.goal.option_king_of_puppets:
        return

    cmp_region = regions["Charity Market Path"]
    for CMPId in ALL_CMP:
        loc = LiesOfPLocation(world.player, CMP_ID_TO_NAME[CMPId], CMPId, cmp_region)
        cmp_region.locations.append(loc)

    la_region = regions["Lorenzini Arcade"]
    for LAId in ALL_LA:
        loc = LiesOfPLocation(world.player, LA_ID_TO_NAME[LAId], LAId, la_region)
        la_region.locations.append(loc)

    fla_region = regions["First Floor Lorenzini Arcade"]
    for FLAId in ALL_FLA:
        loc = LiesOfPLocation(world.player, FLA_ID_TO_NAME[FLAId], FLAId, fla_region)
        fla_region.locations.append(loc)

    ula_region = regions["Underground Lorenzini Arcade"]
    for ULAId in ALL_ULA:
        loc = LiesOfPLocation(world.player, ULA_ID_TO_NAME[ULAId], ULAId, ula_region)
        ula_region.locations.append(loc)

    gep_region = regions["Grand Exhibition Plaza"]
    for GEPId in ALL_GEP:
        loc = LiesOfPLocation(world.player, GEP_ID_TO_NAME[GEPId], GEPId, gep_region)
        gep_region.locations.append(loc)

    geg_region = regions["Grand Exhibition Gallery"]
    for GEGId in ALL_GEG:
        loc = LiesOfPLocation(world.player, GEG_ID_TO_NAME[GEGId], GEGId, geg_region)
        geg_region.locations.append(loc)

    bs_region = regions["Baron Swamp"]
    for BSId in ALL_BS:
        loc = LiesOfPLocation(world.player, BS_ID_TO_NAME[BSId], BSId, bs_region)
        bs_region.locations.append(loc)

    cr_region = regions["Closed Railway"]
    for CRId in ALL_CR:
        loc = LiesOfPLocation(world.player, CR_ID_TO_NAME[CRId], CRId, cr_region)
        cr_region.locations.append(loc)

    kcs2_region = regions["Krat Central Station Revisit"]
    for KCS2Id in ALL_KCS2:
        loc = LiesOfPLocation(world.player, KCS2_ID_TO_NAME[KCS2Id], KCS2Id, kcs2_region)
        kcs2_region.locations.append(loc)

    cs_region = regions["Collapsed Street"]
    for CSId in ALL_CS:
        loc = LiesOfPLocation(world.player, CS_ID_TO_NAME[CSId], CSId, cs_region)
        cs_region.locations.append(loc)

    ck_region = regions["Collapsing Krat"]
    for CKId in ALL_CK:
        loc = LiesOfPLocation(world.player, CK_ID_TO_NAME[CKId], CKId, ck_region)
        ck_region.locations.append(loc)

    hc_region = regions["Hermit's Cave"]
    for HCId in ALL_HC:
        loc = LiesOfPLocation(world.player, HC_ID_TO_NAME[HCId], HCId, hc_region)
        hc_region.locations.append(loc)

    rot_region = regions["Relic of Trismegistus"]
    for ROTId in ALL_ROT:
        loc = LiesOfPLocation(world.player, ROT_ID_TO_NAME[ROTId], ROTId, rot_region)
        rot_region.locations.append(loc)

    bss_region = regions["Black Seaside"]
    for BSSId in ALL_BSS:
        loc = LiesOfPLocation(world.player, BSS_ID_TO_NAME[BSSId], BSSId, bss_region)
        bss_region.locations.append(loc)

    aae_region = regions["Arche Abbey Entrance"]
    for AAEId in ALL_AAE:
        loc = LiesOfPLocation(world.player, AAE_ID_TO_NAME[AAEId], AAEId, aae_region)
        aae_region.locations.append(loc)

    aaow_region = regions["Arche Abbey Outer Wall"]
    for AAOWId in ALL_AAOW:
        loc = LiesOfPLocation(world.player, AAOW_ID_TO_NAME[AAOWId], AAOWId, aaow_region)
        aaow_region.locations.append(loc)

    aau_region = regions["Arche Abbey Upper"]
    for AAUId in ALL_AAU:
        loc = LiesOfPLocation(world.player, AAU_ID_TO_NAME[AAUId], AAUId, aau_region)
        aau_region.locations.append(loc)

    aap_region = regions["Arche Abbey Passageway"]
    for AAPId in ALL_AAP:
        loc = LiesOfPLocation(world.player, AAP_ID_TO_NAME[AAPId], AAPId, aap_region)
        aap_region.locations.append(loc)

    aacg_region = regions["Arche Abbey Cradle of the God"]
    for AACGId in ALL_AACG:
        loc = LiesOfPLocation(world.player, AACG_ID_TO_NAME[AACGId], AACGId, aacg_region)
        aacg_region.locations.append(loc)

    if options.goal.value == options.goal.option_simon_manus:
        return

    uta_region = regions["Under the Abyss"]
    for UTAId in ALL_UTA:
        loc = LiesOfPLocation(world.player, UTA_ID_TO_NAME[UTAId], UTAId, uta_region)
        uta_region.locations.append(loc)