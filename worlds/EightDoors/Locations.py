from typing import Dict
from BaseClasses import Location, Region
from .LocationLists import *
from ..AutoWorld import World

class EightDoorsLocation(Location):
    game: str = "8Doors Arum's Afterlife Adventure"

    def __init__(self, player, location_name, location_id, region):
        super().__init__(player, location_name, location_id, region)

def get_location_dict():
    result = {}

    for Ch11Id in ALL_Ch1_1:
        result[Ch1_1_ID_TO_NAME[Ch11Id]] = Ch11Id

    for Ch12Id in ALL_Ch1_2:
        result[Ch1_2_ID_TO_NAME[Ch12Id]] = Ch12Id

    for Ch13Id in ALL_Ch1_3:
        result[Ch1_3_ID_TO_NAME[Ch13Id]] = Ch13Id

    for Ch14Id in ALL_Ch1_4:
        result[Ch1_4_ID_TO_NAME[Ch14Id]] = Ch14Id

    for Ch15Id in ALL_Ch1_5:
        result[Ch1_5_ID_TO_NAME[Ch15Id]] = Ch15Id

    for Ch16Id in ALL_Ch1_6:
        result[Ch1_6_ID_TO_NAME[Ch16Id]] = Ch16Id

    for Ch16Id in ALL_Ch1_6:
        result[Ch1_6_ID_TO_NAME[Ch16Id]] = Ch16Id

    for Ch17Id in ALL_Ch1_7:
        result[Ch1_7_ID_TO_NAME[Ch17Id]] = Ch17Id

    for Ch18Id in ALL_Ch1_8:
        result[Ch1_8_ID_TO_NAME[Ch18Id]] = Ch18Id

    for DTId in ALL_IERO:
        result[IERO_ID_TO_NAME[DTId]] = DTId

    for Ch21Id in ALL_Ch2_1:
        result[Ch2_1_ID_TO_NAME[Ch21Id]] = Ch21Id

    for Ch22Id in ALL_Ch2_2:
        result[Ch2_2_ID_TO_NAME[Ch22Id]] = Ch22Id

    for Ch23Id in ALL_Ch2_3:
        result[Ch2_3_ID_TO_NAME[Ch23Id]] = Ch23Id

    for Ch24Id in ALL_Ch2_4:
        result[Ch2_4_ID_TO_NAME[Ch24Id]] = Ch24Id

    for Ch25Id in ALL_Ch2_5:
        result[Ch2_5_ID_TO_NAME[Ch25Id]] = Ch25Id

    for Ch26Id in ALL_Ch2_6:
        result[Ch2_6_ID_TO_NAME[Ch26Id]] = Ch26Id

    for Ch27Id in ALL_Ch2_7:
        result[Ch2_7_ID_TO_NAME[Ch27Id]] = Ch27Id

    for Ch28Id in ALL_Ch2_8:
        result[Ch2_8_ID_TO_NAME[Ch28Id]] = Ch28Id

    for Ch29Id in ALL_Ch2_9:
        result[Ch2_9_ID_TO_NAME[Ch29Id]] = Ch29Id

    for Ch210Id in ALL_Ch2_10:
        result[Ch2_10_ID_TO_NAME[Ch210Id]] = Ch210Id

    for Ch211Id in ALL_Ch2_11:
        result[Ch2_11_ID_TO_NAME[Ch211Id]] = Ch211Id

    for Ch212Id in ALL_Ch2_12:
        result[Ch2_12_ID_TO_NAME[Ch212Id]] = Ch212Id

    for Ch31Id in ALL_Ch3_1:
        result[Ch3_1_ID_TO_NAME[Ch31Id]] = Ch31Id

    for Ch33Id in ALL_Ch3_3:
        result[Ch3_3_ID_TO_NAME[Ch33Id]] = Ch33Id

    for Ch34Id in ALL_Ch3_4:
        result[Ch3_4_ID_TO_NAME[Ch34Id]] = Ch34Id

    for Ch35Id in ALL_Ch3_5:
        result[Ch3_5_ID_TO_NAME[Ch35Id]] = Ch35Id

    for Ch36Id in ALL_Ch3_6:
        result[Ch3_6_ID_TO_NAME[Ch36Id]] = Ch36Id

    for Ch37Id in ALL_Ch3_7:
        result[Ch3_7_ID_TO_NAME[Ch37Id]] = Ch37Id

    for Ch316Id in ALL_Ch3_16:
        result[Ch3_16_ID_TO_NAME[Ch316Id]] = Ch316Id

    for Ch38Id in ALL_Ch3_8:
        result[Ch3_8_ID_TO_NAME[Ch38Id]] = Ch38Id

    for Ch39Id in ALL_Ch3_9:
        result[Ch3_9_ID_TO_NAME[Ch39Id]] = Ch39Id

    for Ch310Id in ALL_Ch3_10:
        result[Ch3_10_ID_TO_NAME[Ch310Id]] = Ch310Id

    for Ch311Id in ALL_Ch3_11:
        result[Ch3_11_ID_TO_NAME[Ch311Id]] = Ch311Id

    for Ch313Id in ALL_Ch3_13:
        result[Ch3_13_ID_TO_NAME[Ch313Id]] = Ch313Id

    for Ch318Id in ALL_Ch3_18:
        result[Ch3_18_ID_TO_NAME[Ch318Id]] = Ch318Id

    for Ch41Id in ALL_Ch4_1:
        result[Ch4_1_ID_TO_NAME[Ch41Id]] = Ch41Id

    for CenterId in ALL_CENTER:
        result[Center_ID_TO_NAME[CenterId]] = CenterId

    for Ch43Id in ALL_Ch4_3:
        result[Ch4_3_ID_TO_NAME[Ch43Id]] = Ch43Id

    for Ch44Id in ALL_Ch4_4:
        result[Ch4_4_ID_TO_NAME[Ch44Id]] = Ch44Id

    for Ch45Id in ALL_Ch4_5:
        result[Ch4_5_ID_TO_NAME[Ch45Id]] = Ch45Id

    for Ch46Id in ALL_Ch4_6:
        result[Ch4_6_ID_TO_NAME[Ch46Id]] = Ch46Id

    for Ch47Id in ALL_Ch4_7:
        result[Ch4_7_ID_TO_NAME[Ch47Id]] = Ch47Id

    for Ch49Id in ALL_Ch4_9:
        result[Ch4_9_ID_TO_NAME[Ch49Id]] = Ch49Id

    for Ch411Id in ALL_Ch4_11:
        result[Ch4_11_ID_TO_NAME[Ch411Id]] = Ch411Id

    for Ch412Id in ALL_Ch4_12:
        result[Ch4_12_ID_TO_NAME[Ch412Id]] = Ch412Id

    for Ch413Id in ALL_Ch4_13:
        result[Ch4_13_ID_TO_NAME[Ch413Id]] = Ch413Id

    for Ch414Id in ALL_Ch4_14:
        result[Ch4_14_ID_TO_NAME[Ch414Id]] = Ch414Id

    for Ch416Id in ALL_Ch4_16:
        result[Ch4_16_ID_TO_NAME[Ch416Id]] = Ch416Id

    for Ch417Id in ALL_Ch4_17:
        result[Ch4_17_ID_TO_NAME[Ch417Id]] = Ch417Id

    for Ch420Id in ALL_Ch4_20:
        result[Ch4_20_ID_TO_NAME[Ch420Id]] = Ch420Id

    for WorkshopId in ALL_WORKSHOP:
        result[WORKSHOP_ID_TO_NAME[WorkshopId]] = WorkshopId

    for Ch52Id in ALL_Ch5_2:
        result[Ch5_2_ID_TO_NAME[Ch52Id]] = Ch52Id

    for Ch51Id in ALL_Ch5_1:
        result[Ch5_1_ID_TO_NAME[Ch51Id]] = Ch51Id

    for Ch53Id in ALL_Ch5_3:
        result[Ch5_3_ID_TO_NAME[Ch53Id]] = Ch53Id

    for Ch54Id in ALL_Ch5_4:
        result[Ch5_4_ID_TO_NAME[Ch54Id]] = Ch54Id

    for Ch55Id in ALL_Ch5_5:
        result[Ch5_5_ID_TO_NAME[Ch55Id]] = Ch55Id

    for Ch56Id in ALL_Ch5_6:
        result[Ch5_6_ID_TO_NAME[Ch56Id]] = Ch56Id

    for Ch58Id in ALL_Ch5_8:
        result[Ch5_8_ID_TO_NAME[Ch58Id]] = Ch58Id

    for Ch510Id in ALL_Ch5_10:
        result[Ch5_10_ID_TO_NAME[Ch510Id]] = Ch510Id

    for Ch511Id in ALL_Ch5_11:
        result[Ch5_11_ID_TO_NAME[Ch511Id]] = Ch511Id

    for Ch513Id in ALL_Ch5_13:
        result[Ch5_13_ID_TO_NAME[Ch513Id]] = Ch513Id

    for Ch518Id in ALL_Ch5_18:
        result[Ch5_18_ID_TO_NAME[Ch518Id]] = Ch518Id

    for Ch62Id in ALL_Ch6_2:
        result[Ch6_2_ID_TO_NAME[Ch62Id]] = Ch62Id

    for Ch63Id in ALL_Ch6_3:
        result[Ch6_3_ID_TO_NAME[Ch63Id]] = Ch63Id

    for DSId in ALL_DS:
        result[DS_ID_TO_NAME[DSId]] = DSId

    for Ch65Id in ALL_Ch6_5:
        result[Ch6_5_ID_TO_NAME[Ch65Id]] = Ch65Id

    for Ch68Id in ALL_Ch6_8:
        result[Ch6_8_ID_TO_NAME[Ch68Id]] = Ch68Id

    for Ch617Id in ALL_Ch6_17:
        result[Ch6_17_ID_TO_NAME[Ch617Id]] = Ch617Id

    for Ch618Id in ALL_Ch6_18:
        result[Ch6_18_ID_TO_NAME[Ch618Id]] = Ch618Id

    for Ch66Id in ALL_Ch6_6:
        result[Ch6_6_ID_TO_NAME[Ch66Id]] = Ch66Id

    for Ch69Id in ALL_Ch6_9:
        result[Ch6_9_ID_TO_NAME[Ch69Id]] = Ch69Id

    for Ch612Id in ALL_Ch6_12:
        result[Ch6_12_ID_TO_NAME[Ch612Id]] = Ch612Id

    for Ch613Id in ALL_Ch6_13:
        result[Ch6_13_ID_TO_NAME[Ch613Id]] = Ch613Id

    for Ch614Id in ALL_Ch6_14:
        result[Ch6_14_ID_TO_NAME[Ch614Id]] = Ch614Id

    for Ch615Id in ALL_Ch6_15:
        result[Ch6_15_ID_TO_NAME[Ch615Id]] = Ch615Id

    for CRId in ALL_CONTROLROOM:
        result[CONTROLROOM_ID_TO_NAME[CRId]] = CRId

    for Ch74Id in ALL_Ch7_4:
        result[Ch7_4_ID_TO_NAME[Ch74Id]] = Ch74Id

    for Ch73Id in ALL_Ch7_3:
        result[Ch7_3_ID_TO_NAME[Ch73Id]] = Ch73Id

    for Ch716Id in ALL_Ch7_16:
        result[Ch7_16_ID_TO_NAME[Ch716Id]] = Ch716Id

    for Ch717Id in ALL_Ch7_17:
        result[Ch7_17_ID_TO_NAME[Ch717Id]] = Ch717Id

    for Ch714Id in ALL_Ch7_14:
        result[Ch7_14_ID_TO_NAME[Ch714Id]] = Ch714Id

    for Ch76Id in ALL_Ch7_6:
        result[Ch7_6_ID_TO_NAME[Ch76Id]] = Ch76Id

    for Ch77Id in ALL_Ch7_7:
        result[Ch7_7_ID_TO_NAME[Ch77Id]] = Ch77Id

    for Ch77Id in ALL_Ch7_7:
        result[Ch7_7_ID_TO_NAME[Ch77Id]] = Ch77Id

    for Ch78Id in ALL_Ch7_8:
        result[Ch7_8_ID_TO_NAME[Ch78Id]] = Ch78Id

    for Ch79Id in ALL_Ch7_9:
        result[Ch7_9_ID_TO_NAME[Ch79Id]] = Ch79Id

    for Ch710Id in ALL_Ch7_10:
        result[Ch7_10_ID_TO_NAME[Ch710Id]] = Ch710Id

    for Ch713Id in ALL_Ch7_13:
        result[Ch7_13_ID_TO_NAME[Ch713Id]] = Ch713Id

    for Ch715Id in ALL_Ch7_15:
        result[Ch7_15_ID_TO_NAME[Ch715Id]] = Ch715Id

    for Ch817Id in ALL_Ch8_17:
        result[Ch8_17_ID_TO_NAME[Ch817Id]] = Ch817Id

    for Ch816Id in ALL_Ch8_16:
        result[Ch8_16_ID_TO_NAME[Ch816Id]] = Ch816Id

    for Ch83Id in ALL_Ch8_3:
        result[Ch8_3_ID_TO_NAME[Ch83Id]] = Ch83Id

    for Ch82Id in ALL_Ch8_2:
        result[Ch8_2_ID_TO_NAME[Ch82Id]] = Ch82Id

    for Ch85Id in ALL_Ch8_5:
        result[Ch8_5_ID_TO_NAME[Ch85Id]] = Ch85Id

    for Ch84Id in ALL_Ch8_4:
        result[Ch8_4_ID_TO_NAME[Ch84Id]] = Ch84Id

    for Ch87Id in ALL_Ch8_7:
        result[Ch8_7_ID_TO_NAME[Ch87Id]] = Ch87Id

    for Ch88Id in ALL_Ch8_8:
        result[Ch8_8_ID_TO_NAME[Ch88Id]] = Ch88Id

    for Ch86Id in ALL_Ch8_6:
        result[Ch8_6_ID_TO_NAME[Ch86Id]] = Ch86Id

    for Ch89Id in ALL_Ch8_9:
        result[Ch8_9_ID_TO_NAME[Ch89Id]] = Ch89Id

    for Ch92Id in ALL_Ch9_2:
        result[Ch9_2_ID_TO_NAME[Ch92Id]] = Ch92Id
    return result

def create_locations(world: World, regions: Dict[str, Region]):
    create_eightdoors_locations(world, regions)

def create_eightdoors_locations(world, regions:Dict[str, Region]):
    ch11_region = regions["Kingdom Of Yama 1"]

    for CH11Id in ALL_Ch1_1:
        loc = EightDoorsLocation(world.player, Ch1_1_ID_TO_NAME[CH11Id], CH11Id, ch11_region)
        ch11_region.locations.append(loc)

    ch12_region = regions["Kingdom Of Yama 2"]

    for CH12Id in ALL_Ch1_2:
        loc = EightDoorsLocation(world.player, Ch1_2_ID_TO_NAME[CH12Id], CH12Id, ch12_region)
        ch12_region.locations.append(loc)

    ch13_region = regions["Kingdom Of Yama 3"]

    for CH13Id in ALL_Ch1_3:
        loc = EightDoorsLocation(world.player, Ch1_3_ID_TO_NAME[CH13Id], CH13Id, ch13_region)
        ch13_region.locations.append(loc)

    ch14_region = regions["Kingdom Of Yama 4"]

    for CH14Id in ALL_Ch1_4:
        loc = EightDoorsLocation(world.player, Ch1_4_ID_TO_NAME[CH14Id], CH14Id, ch14_region)
        ch14_region.locations.append(loc)

    ch15_region = regions["Kingdom Of Yama 5"]

    for CH15Id in ALL_Ch1_5:
        loc = EightDoorsLocation(world.player, Ch1_5_ID_TO_NAME[CH15Id], CH15Id, ch15_region)
        ch15_region.locations.append(loc)

    ch16_region = regions["Kingdom Of Yama 6"]

    for CH16Id in ALL_Ch1_6:
        loc = EightDoorsLocation(world.player, Ch1_6_ID_TO_NAME[CH16Id], CH16Id, ch16_region)
        ch16_region.locations.append(loc)

    ch17_region = regions["Kingdom Of Yama 7"]

    for CH17Id in ALL_Ch1_7:
        loc = EightDoorsLocation(world.player, Ch1_7_ID_TO_NAME[CH17Id], CH17Id, ch17_region)
        ch17_region.locations.append(loc)

    ch18_region = regions["Kingdom Of Yama 8"]

    for CH18Id in ALL_Ch1_8:
        loc = EightDoorsLocation(world.player, Ch1_8_ID_TO_NAME[CH18Id], CH18Id, ch18_region)
        ch18_region.locations.append(loc)

    iero_region = regions["Death Tavern"]

    for IEROId in ALL_IERO:
        loc = EightDoorsLocation(world.player, IERO_ID_TO_NAME[IEROId], IEROId, iero_region)
        iero_region.locations.append(loc)

    ch21_region = regions["Stone Mountain 1"]

    for CH21Id in ALL_Ch2_1:
        loc = EightDoorsLocation(world.player, Ch2_1_ID_TO_NAME[CH21Id], CH21Id, ch21_region)
        ch21_region.locations.append(loc)

    ch22_region = regions["Stone Mountain 2"]

    for CH22Id in ALL_Ch2_2:
        loc = EightDoorsLocation(world.player, Ch2_2_ID_TO_NAME[CH22Id], CH22Id, ch22_region)
        ch22_region.locations.append(loc)

    ch23_region = regions["Stone Mountain 3"]

    for CH23Id in ALL_Ch2_3:
        loc = EightDoorsLocation(world.player, Ch2_3_ID_TO_NAME[CH23Id], CH23Id, ch23_region)
        ch23_region.locations.append(loc)

    ch24_region = regions["Stone Mountain 4"]

    for CH24Id in ALL_Ch2_4:
        loc = EightDoorsLocation(world.player, Ch2_4_ID_TO_NAME[CH24Id], CH24Id, ch24_region)
        ch24_region.locations.append(loc)

    ch25_region = regions["Stone Mountain 5"]

    for CH25Id in ALL_Ch2_5:
        loc = EightDoorsLocation(world.player, Ch2_5_ID_TO_NAME[CH25Id], CH25Id, ch25_region)
        ch25_region.locations.append(loc)

    ch26_region = regions["Stone Mountain 6"]

    for CH26Id in ALL_Ch2_6:
        loc = EightDoorsLocation(world.player, Ch2_6_ID_TO_NAME[CH26Id], CH26Id, ch26_region)
        ch26_region.locations.append(loc)

    ch27_region = regions["Stone Mountain 7"]

    for CH27Id in ALL_Ch2_7:
        loc = EightDoorsLocation(world.player, Ch2_7_ID_TO_NAME[CH27Id], CH27Id, ch27_region)
        ch27_region.locations.append(loc)

    ch28_region = regions["Stone Mountain 8"]

    for CH28Id in ALL_Ch2_8:
        loc = EightDoorsLocation(world.player, Ch2_8_ID_TO_NAME[CH28Id], CH28Id, ch28_region)
        ch28_region.locations.append(loc)

    ch29_region = regions["Stone Mountain 9"]

    for CH29Id in ALL_Ch2_9:
        loc = EightDoorsLocation(world.player, Ch2_9_ID_TO_NAME[CH29Id], CH29Id, ch29_region)
        ch29_region.locations.append(loc)

    ch210_region = regions["Stone Mountain 10"]

    for CH210Id in ALL_Ch2_10:
        loc = EightDoorsLocation(world.player, Ch2_10_ID_TO_NAME[CH210Id], CH210Id, ch210_region)
        ch210_region.locations.append(loc)

    ch211_region = regions["Stone Mountain 11"]

    for CH211Id in ALL_Ch2_11:
        loc = EightDoorsLocation(world.player, Ch2_11_ID_TO_NAME[CH211Id], CH211Id, ch211_region)
        ch211_region.locations.append(loc)

    ch212_region = regions["Stone Mountain 12"]

    for CH212Id in ALL_Ch2_12:
        loc = EightDoorsLocation(world.player, Ch2_12_ID_TO_NAME[CH212Id], CH212Id, ch212_region)
        ch212_region.locations.append(loc)

    ch31_region = regions["Misty Forest 1"]

    for CH31Id in ALL_Ch3_1:
        loc = EightDoorsLocation(world.player, Ch3_1_ID_TO_NAME[CH31Id], CH31Id, ch31_region)
        ch31_region.locations.append(loc)

    ch33_region = regions["Misty Forest 3"]

    for CH33Id in ALL_Ch3_3:
        loc = EightDoorsLocation(world.player, Ch3_3_ID_TO_NAME[CH33Id], CH33Id, ch33_region)
        ch33_region.locations.append(loc)

    ch34_region = regions["Misty Forest 4"]

    for CH34Id in ALL_Ch3_4:
        loc = EightDoorsLocation(world.player, Ch3_4_ID_TO_NAME[CH34Id], CH34Id, ch34_region)
        ch34_region.locations.append(loc)

    ch35_region = regions["Misty Forest 5"]

    for CH35Id in ALL_Ch3_5:
        loc = EightDoorsLocation(world.player, Ch3_5_ID_TO_NAME[CH35Id], CH35Id, ch35_region)
        ch35_region.locations.append(loc)

    ch36_region = regions["Misty Forest 6"]

    for CH36Id in ALL_Ch3_6:
        loc = EightDoorsLocation(world.player, Ch3_6_ID_TO_NAME[CH36Id], CH36Id, ch36_region)
        ch36_region.locations.append(loc)

    ch37_region = regions["Misty Forest 7"]

    for CH37Id in ALL_Ch3_7:
        loc = EightDoorsLocation(world.player, Ch3_7_ID_TO_NAME[CH37Id], CH37Id, ch37_region)
        ch37_region.locations.append(loc)

    ch316_region = regions["Misty Forest 16"]

    for CH316Id in ALL_Ch3_16:
        loc = EightDoorsLocation(world.player, Ch3_16_ID_TO_NAME[CH316Id], CH316Id, ch316_region)
        ch316_region.locations.append(loc)

    ch38_region = regions["Misty Forest 8"]

    for CH38Id in ALL_Ch3_8:
        loc = EightDoorsLocation(world.player, Ch3_8_ID_TO_NAME[CH38Id], CH38Id, ch38_region)
        ch38_region.locations.append(loc)

    ch39_region = regions["Misty Forest 9"]

    for CH39Id in ALL_Ch3_9:
        loc = EightDoorsLocation(world.player, Ch3_9_ID_TO_NAME[CH39Id], CH39Id, ch39_region)
        ch39_region.locations.append(loc)

    ch310_region = regions["Misty Forest 10"]

    for CH310Id in ALL_Ch3_10:
        loc = EightDoorsLocation(world.player, Ch3_10_ID_TO_NAME[CH310Id], CH310Id, ch310_region)
        ch310_region.locations.append(loc)

    ch311_region = regions["Misty Forest 11"]

    for CH311Id in ALL_Ch3_11:
        loc = EightDoorsLocation(world.player, Ch3_11_ID_TO_NAME[CH311Id], CH311Id, ch311_region)
        ch311_region.locations.append(loc)

    ch313_region = regions["Misty Forest 13"]

    for CH313Id in ALL_Ch3_13:
        loc = EightDoorsLocation(world.player, Ch3_13_ID_TO_NAME[CH313Id], CH313Id, ch313_region)
        ch313_region.locations.append(loc)

    ch318_region = regions["Misty Forest 18"]

    for CH318Id in ALL_Ch3_18:
        loc = EightDoorsLocation(world.player, Ch3_18_ID_TO_NAME[CH318Id], CH318Id, ch318_region)
        ch318_region.locations.append(loc)

    ch41_region = regions["Barron Grounds 1"]

    for CH41Id in ALL_Ch4_1:
        loc = EightDoorsLocation(world.player, Ch4_1_ID_TO_NAME[CH41Id], CH41Id, ch41_region)
        ch41_region.locations.append(loc)

    center_region = regions["Reincarnation Center"]

    for CenterId in ALL_CENTER:
        loc = EightDoorsLocation(world.player, Center_ID_TO_NAME[CenterId], CenterId, center_region)
        center_region.locations.append(loc)

    ch43_region = regions["Barron Grounds 3"]

    for CH43Id in ALL_Ch4_3:
        loc = EightDoorsLocation(world.player, Ch4_3_ID_TO_NAME[CH43Id], CH43Id, ch43_region)
        ch43_region.locations.append(loc)

    ch44_region = regions["Barron Grounds 4"]

    for CH44Id in ALL_Ch4_4:
        loc = EightDoorsLocation(world.player, Ch4_4_ID_TO_NAME[CH44Id], CH44Id, ch44_region)
        ch44_region.locations.append(loc)

    ch45_region = regions["Barron Grounds 5"]

    for CH45Id in ALL_Ch4_5:
        loc = EightDoorsLocation(world.player, Ch4_5_ID_TO_NAME[CH45Id], CH45Id, ch45_region)
        ch45_region.locations.append(loc)

    ch46_region = regions["Barron Grounds 6"]

    for CH46Id in ALL_Ch4_6:
        loc = EightDoorsLocation(world.player, Ch4_6_ID_TO_NAME[CH46Id], CH46Id, ch46_region)
        ch46_region.locations.append(loc)

    ch47_region = regions["Barron Grounds 7"]

    for CH47Id in ALL_Ch4_7:
        loc = EightDoorsLocation(world.player, Ch4_7_ID_TO_NAME[CH47Id], CH47Id, ch47_region)
        ch47_region.locations.append(loc)

    ch49_region = regions["Barron Grounds 9"]

    for CH49Id in ALL_Ch4_9:
        loc = EightDoorsLocation(world.player, Ch4_9_ID_TO_NAME[CH49Id], CH49Id, ch49_region)
        ch49_region.locations.append(loc)

    ch411_region = regions["Barron Grounds 11"]

    for CH411Id in ALL_Ch4_11:
        loc = EightDoorsLocation(world.player, Ch4_11_ID_TO_NAME[CH411Id], CH411Id, ch411_region)
        ch411_region.locations.append(loc)

    ch412_region = regions["Barron Grounds 12"]

    for CH412Id in ALL_Ch4_12:
        loc = EightDoorsLocation(world.player, Ch4_12_ID_TO_NAME[CH412Id], CH412Id, ch412_region)
        ch412_region.locations.append(loc)

    ch413_region = regions["Barron Grounds 13"]

    for CH413Id in ALL_Ch4_13:
        loc = EightDoorsLocation(world.player, Ch4_13_ID_TO_NAME[CH413Id], CH413Id, ch413_region)
        ch413_region.locations.append(loc)

    ch414_region = regions["Barron Grounds 14"]

    for CH414Id in ALL_Ch4_14:
        loc = EightDoorsLocation(world.player, Ch4_14_ID_TO_NAME[CH414Id], CH414Id, ch414_region)
        ch414_region.locations.append(loc)

    ch416_region = regions["Barron Grounds 16"]

    for CH416Id in ALL_Ch4_16:
        loc = EightDoorsLocation(world.player, Ch4_16_ID_TO_NAME[CH416Id], CH416Id, ch416_region)
        ch416_region.locations.append(loc)

    ch417_region = regions["Barron Grounds 17"]

    for CH417Id in ALL_Ch4_17:
        loc = EightDoorsLocation(world.player, Ch4_17_ID_TO_NAME[CH417Id], CH417Id, ch417_region)
        ch417_region.locations.append(loc)

    ch420_region = regions["Barron Grounds 20"]

    for CH420Id in ALL_Ch4_20:
        loc = EightDoorsLocation(world.player, Ch4_20_ID_TO_NAME[CH420Id], CH420Id, ch420_region)
        ch420_region.locations.append(loc)

    workshop_region = regions["Workshop"]

    for WorkshopId in ALL_WORKSHOP:
        loc = EightDoorsLocation(world.player, WORKSHOP_ID_TO_NAME[WorkshopId], WorkshopId, workshop_region)
        workshop_region.locations.append(loc)

    ch52_region = regions["Crimson Mines 2"]

    for CH52Id in ALL_Ch5_2:
        loc = EightDoorsLocation(world.player, Ch5_2_ID_TO_NAME[CH52Id], CH52Id, ch52_region)
        ch52_region.locations.append(loc)

    ch51_region = regions["Crimson Mines 1"]

    for CH51Id in ALL_Ch5_1:
        loc = EightDoorsLocation(world.player, Ch5_1_ID_TO_NAME[CH51Id], CH51Id, ch51_region)
        ch51_region.locations.append(loc)

    ch53_region = regions["Crimson Mines 3"]

    for CH53Id in ALL_Ch5_3:
        loc = EightDoorsLocation(world.player, Ch5_3_ID_TO_NAME[CH53Id], CH53Id, ch53_region)
        ch53_region.locations.append(loc)

    ch54_region = regions["Crimson Mines 4"]

    for CH54Id in ALL_Ch5_4:
        loc = EightDoorsLocation(world.player, Ch5_4_ID_TO_NAME[CH54Id], CH54Id, ch54_region)
        ch54_region.locations.append(loc)

    ch55_region = regions["Crimson Mines 5"]

    for CH55Id in ALL_Ch5_5:
        loc = EightDoorsLocation(world.player, Ch5_5_ID_TO_NAME[CH55Id], CH55Id, ch55_region)
        ch55_region.locations.append(loc)

    ch56_region = regions["Crimson Mines 6"]

    for CH56Id in ALL_Ch5_6:
        loc = EightDoorsLocation(world.player, Ch5_6_ID_TO_NAME[CH56Id], CH56Id, ch56_region)
        ch56_region.locations.append(loc)

    ch58_region = regions["Crimson Mines 8"]

    for CH58Id in ALL_Ch5_8:
        loc = EightDoorsLocation(world.player, Ch5_8_ID_TO_NAME[CH58Id], CH58Id, ch58_region)
        ch58_region.locations.append(loc)

    ch510_region = regions["Crimson Mines 10"]

    for CH510Id in ALL_Ch5_10:
        loc = EightDoorsLocation(world.player, Ch5_10_ID_TO_NAME[CH510Id], CH510Id, ch510_region)
        ch510_region.locations.append(loc)

    ch511_region = regions["Crimson Mines 11"]

    for CH511Id in ALL_Ch5_11:
        loc = EightDoorsLocation(world.player, Ch5_11_ID_TO_NAME[CH511Id], CH511Id, ch511_region)
        ch511_region.locations.append(loc)

    ch513_region = regions["Crimson Mines 13"]

    for CH513Id in ALL_Ch5_13:
        loc = EightDoorsLocation(world.player, Ch5_13_ID_TO_NAME[CH513Id], CH513Id, ch513_region)
        ch513_region.locations.append(loc)

    ch518_region = regions["Crimson Mines 18"]

    for CH518Id in ALL_Ch5_18:
        loc = EightDoorsLocation(world.player, Ch5_18_ID_TO_NAME[CH518Id], CH518Id, ch518_region)
        ch518_region.locations.append(loc)

    ch62_region = regions["Frozen Plateau 2"]

    for CH62Id in ALL_Ch6_2:
        loc = EightDoorsLocation(world.player, Ch6_2_ID_TO_NAME[CH62Id], CH62Id, ch62_region)
        ch62_region.locations.append(loc)

    ch63_region = regions["Frozen Plateau 3"]

    for CH63Id in ALL_Ch6_3:
        loc = EightDoorsLocation(world.player, Ch6_3_ID_TO_NAME[CH63Id], CH63Id, ch63_region)
        ch63_region.locations.append(loc)

    ds_region = regions["Dispatch Station"]

    for DSId in ALL_DS:
        loc = EightDoorsLocation(world.player, DS_ID_TO_NAME[DSId], DSId, ds_region)
        ds_region.locations.append(loc)

    ch65_region = regions["Frozen Plateau 5"]

    for CH65Id in ALL_Ch6_5:
        loc = EightDoorsLocation(world.player, Ch6_5_ID_TO_NAME[CH65Id], CH65Id, ch65_region)
        ch65_region.locations.append(loc)

    ch68_region = regions["Frozen Plateau 8"]

    for CH68Id in ALL_Ch6_8:
        loc = EightDoorsLocation(world.player, Ch6_8_ID_TO_NAME[CH68Id], CH68Id, ch68_region)
        ch68_region.locations.append(loc)

    ch617_region = regions["Frozen Plateau 17"]

    for CH617Id in ALL_Ch6_17:
        loc = EightDoorsLocation(world.player, Ch6_17_ID_TO_NAME[CH617Id], CH617Id, ch617_region)
        ch617_region.locations.append(loc)

    ch618_region = regions["Frozen Plateau 18"]

    for CH618Id in ALL_Ch6_18:
        loc = EightDoorsLocation(world.player, Ch6_18_ID_TO_NAME[CH618Id], CH618Id, ch618_region)
        ch618_region.locations.append(loc)

    ch66_region = regions["Frozen Plateau 6"]

    for CH66Id in ALL_Ch6_6:
        loc = EightDoorsLocation(world.player, Ch6_6_ID_TO_NAME[CH66Id], CH66Id, ch66_region)
        ch66_region.locations.append(loc)

    ch69_region = regions["Frozen Plateau 9"]

    for CH69Id in ALL_Ch6_9:
        loc = EightDoorsLocation(world.player, Ch6_9_ID_TO_NAME[CH69Id], CH69Id, ch69_region)
        ch69_region.locations.append(loc)


    ch612_region = regions["Frozen Plateau 12"]

    for CH612Id in ALL_Ch6_12:
        loc = EightDoorsLocation(world.player, Ch6_12_ID_TO_NAME[CH612Id], CH612Id, ch612_region)
        ch612_region.locations.append(loc)

    ch613_region = regions["Frozen Plateau 13"]

    for CH613Id in ALL_Ch6_13:
        loc = EightDoorsLocation(world.player, Ch6_13_ID_TO_NAME[CH613Id], CH613Id, ch613_region)
        ch613_region.locations.append(loc)

    ch614_region = regions["Frozen Plateau 14"]

    for CH614Id in ALL_Ch6_14:
        loc = EightDoorsLocation(world.player, Ch6_14_ID_TO_NAME[CH614Id], CH614Id, ch614_region)
        ch65_region.locations.append(loc)

    ch615_region = regions["Frozen Plateau 15"]

    for CH615Id in ALL_Ch6_15:
        loc = EightDoorsLocation(world.player, Ch6_15_ID_TO_NAME[CH615Id], CH615Id, ch615_region)
        ch615_region.locations.append(loc)

    cr_region = regions["Control Room"]

    for CRId in ALL_CONTROLROOM:
        loc = EightDoorsLocation(world.player, CONTROLROOM_ID_TO_NAME[CRId], CRId, cr_region)
        cr_region.locations.append(loc)

    ch74_region = regions["Underground Waterway 4"]

    for CH74Id in ALL_Ch7_4:
        loc = EightDoorsLocation(world.player, Ch7_4_ID_TO_NAME[CH74Id], CH74Id, ch74_region)
        ch74_region.locations.append(loc)

    ch73_region = regions["Underground Waterway 3"]

    for CH73Id in ALL_Ch7_3:
        loc = EightDoorsLocation(world.player, Ch7_3_ID_TO_NAME[CH73Id], CH73Id, ch73_region)
        ch73_region.locations.append(loc)

    ch716_region = regions["Underground Waterway 16"]

    for CH716Id in ALL_Ch7_16:
        loc = EightDoorsLocation(world.player, Ch7_16_ID_TO_NAME[CH716Id], CH716Id, ch716_region)
        ch716_region.locations.append(loc)

    ch717_region = regions["Underground Waterway 17"]

    for CH717Id in ALL_Ch7_17:
        loc = EightDoorsLocation(world.player, Ch7_17_ID_TO_NAME[CH717Id], CH717Id, ch717_region)
        ch717_region.locations.append(loc)

    ch714_region = regions["Underground Waterway 14"]

    for CH714Id in ALL_Ch7_14:
        loc = EightDoorsLocation(world.player, Ch7_14_ID_TO_NAME[CH714Id], CH714Id, ch714_region)
        ch714_region.locations.append(loc)

    ch76_region = regions["Underground Waterway 6"]

    for CH76Id in ALL_Ch7_6:
        loc = EightDoorsLocation(world.player, Ch7_6_ID_TO_NAME[CH76Id], CH76Id, ch76_region)
        ch76_region.locations.append(loc)

    ch77_region = regions["Underground Waterway 7"]

    for CH77Id in ALL_Ch7_7:
        loc = EightDoorsLocation(world.player, Ch7_7_ID_TO_NAME[CH77Id], CH77Id, ch77_region)
        ch77_region.locations.append(loc)

    ch78_region = regions["Underground Waterway 8"]

    for CH78Id in ALL_Ch7_8:
        loc = EightDoorsLocation(world.player, Ch7_8_ID_TO_NAME[CH78Id], CH78Id, ch78_region)
        ch78_region.locations.append(loc)

    ch79_region = regions["Underground Waterway 9"]

    for CH79Id in ALL_Ch7_9:
        loc = EightDoorsLocation(world.player, Ch7_9_ID_TO_NAME[CH79Id], CH79Id, ch79_region)
        ch79_region.locations.append(loc)

    ch710_region = regions["Underground Waterway 10"]

    for CH710Id in ALL_Ch7_10:
        loc = EightDoorsLocation(world.player, Ch7_10_ID_TO_NAME[CH710Id], CH710Id, ch710_region)
        ch710_region.locations.append(loc)

    ch713_region = regions["Underground Waterway 13"]

    for CH713Id in ALL_Ch7_13:
        loc = EightDoorsLocation(world.player, Ch7_13_ID_TO_NAME[CH713Id], CH713Id, ch713_region)
        ch713_region.locations.append(loc)

    ch715_region = regions["Underground Waterway 15"]

    for CH715Id in ALL_Ch7_15:
        loc = EightDoorsLocation(world.player, Ch7_15_ID_TO_NAME[CH715Id], CH715Id, ch715_region)
        ch715_region.locations.append(loc)

    ch817_region = regions["Land of Abundance 17"]

    for CH817Id in ALL_Ch8_17:
        loc = EightDoorsLocation(world.player, Ch8_17_ID_TO_NAME[CH817Id], CH817Id, ch817_region)
        ch817_region.locations.append(loc)

    ch816_region = regions["Land of Abundance 16"]

    for CH816Id in ALL_Ch8_16:
        loc = EightDoorsLocation(world.player, Ch8_16_ID_TO_NAME[CH816Id], CH816Id, ch816_region)
        ch816_region.locations.append(loc)

    ch83_region = regions["Land of Abundance 3"]

    for CH83Id in ALL_Ch8_3:
        loc = EightDoorsLocation(world.player, Ch8_3_ID_TO_NAME[CH83Id], CH83Id, ch83_region)
        ch83_region.locations.append(loc)

    ch82_region = regions["Land of Abundance 2"]

    for CH82Id in ALL_Ch8_2:
        loc = EightDoorsLocation(world.player, Ch8_2_ID_TO_NAME[CH82Id], CH82Id, ch82_region)
        ch82_region.locations.append(loc)

    ch85_region = regions["Land of Abundance 5"]

    for CH85Id in ALL_Ch8_5:
        loc = EightDoorsLocation(world.player, Ch8_5_ID_TO_NAME[CH85Id], CH85Id, ch85_region)
        ch85_region.locations.append(loc)

    ch84_region = regions["Land of Abundance 4"]

    for CH84Id in ALL_Ch8_4:
        loc = EightDoorsLocation(world.player, Ch8_4_ID_TO_NAME[CH84Id], CH84Id, ch84_region)
        ch84_region.locations.append(loc)

    ch87_region = regions["Land of Abundance 7"]

    for CH87Id in ALL_Ch8_7:
        loc = EightDoorsLocation(world.player, Ch8_7_ID_TO_NAME[CH87Id], CH87Id, ch87_region)
        ch87_region.locations.append(loc)

    ch88_region = regions["Land of Abundance 8"]

    for CH88Id in ALL_Ch8_8:
        loc = EightDoorsLocation(world.player, Ch8_8_ID_TO_NAME[CH88Id], CH88Id, ch88_region)
        ch88_region.locations.append(loc)

    ch86_region = regions["Land of Abundance 6"]

    for CH86Id in ALL_Ch8_6:
        loc = EightDoorsLocation(world.player, Ch8_6_ID_TO_NAME[CH86Id], CH86Id, ch86_region)
        ch86_region.locations.append(loc)

    ch89_region = regions["Land of Abundance 9"]

    for CH89Id in ALL_Ch8_9:
        loc = EightDoorsLocation(world.player, Ch8_9_ID_TO_NAME[CH89Id], CH89Id, ch89_region)
        ch89_region.locations.append(loc)

    ch92_region = regions["Abyss"]

    for CH92Id in ALL_Ch9_2:
        loc = EightDoorsLocation(world.player, Ch9_2_ID_TO_NAME[CH92Id], CH92Id, ch92_region)
        ch92_region.locations.append(loc)