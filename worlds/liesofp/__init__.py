from typing import ClassVar, Dict, Mapping, Any

from BaseClasses import Tutorial, ItemClassification as ItemClass, Item
from worlds.AutoWorld import World, WebWorld
from .ItemLists.Functionals import FUNC_ID_TO_NAME, FUNC_EAT
from .ItemLists.Keys import KEY_ID_TO_NAME, KCS_ENTRANCE_KEY
from .ItemLists.Useables import ALL_ERGO, All_THROW, All_CONSUME, ERGO_ID_TO_NAME, THROW_ID_TO_NAME, CONSUME_ID_TO_NAME
from .Groups import item_name_groups, location_name_groups

from .Options import LiesOfPOptions
from .Items import LiesOfPItem, is_progression
from . import Locations, Regions, Rules


class LiesOfPWeb(WebWorld):
    theme = "jungle"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Lies Of P for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Xtruh", "Ninjakakes"]
    )


class LiesOfPWorld(World):
    game = "Lies Of P"
    web = LiesOfPWeb()

    options_dataclass = LiesOfPOptions
    options: LiesOfPOptions

    item_name_to_id: ClassVar[Dict[str, int]] = Items.get_item_dict()
    location_name_to_id: ClassVar[Dict[str, int]] = Locations.get_location_dict()

    explicit_indirect_conditions = False

    glitches_item_name = Items.GLITCHED

    dlc_required = False

    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    def create_regions(self) -> None:
        if self.options.goal.value >= self.options.goal.option_arlecchino_short:
            self.options.dlc.value = self.options.dlc.option_enable

        regions = Regions.create_regions(self, self.options)
        Locations.create_locations(self, regions, self.options)
        self.multiworld.regions.extend(regions.values())

    def create_item(self, name: str) -> Item:
        if name == self.glitches_item_name:
            return LiesOfPItem(name, ItemClass.progression_skip_balancing, None, self.player)

        item_id = self.item_name_to_id[name]
        item_class = ItemClass.filler

        if is_progression(item_id):
            item_class = ItemClass.progression

        return LiesOfPItem(name, item_class, item_id, self.player)

    def create_items(self) -> None:
        Items.populate_item_pool(self, self.options)

    def get_filler_item_name(self) -> str:
        filler_choice = self.random.randint(0, 2)

        match filler_choice:
            case 0:
                ergo_id = self.random.choice(ALL_ERGO)
                item = ERGO_ID_TO_NAME[ergo_id]
                return item
            case 1:
                throw_id = self.random.choice(All_THROW)
                item = THROW_ID_TO_NAME[throw_id]
                return item
            case 2:
                consume_id = self.random.choice(All_CONSUME)
                item = CONSUME_ID_TO_NAME[consume_id]
                return item

    def fill_slot_data(self) -> Mapping[str, Any]:
        if self.options.dlc or self.options.dlc_items:
            self.dlc_required = True

        self.check_dlc_start_inventory()

        slot_data = {
            "ring_link": self.options.ring_link.value,
            "ring_link_ratio": self.options.ergo_to_ring_ratio.value,
            "death_link": self.options.death_link.value,
            "goal": self.options.goal.value,
            "dlc": self.options.dlc.value,
            "dlc_items": self.options.dlc_items.value,
            "require_horn": self.options.require_horn_overseer.value,
            "require_bow_minigames": self.options.require_bow_minigames.value,
            "require_grindstone_chapter4": self.options.require_grindstone_chapter4.value,
            "require_flame_grindstone_bishop": self.options.require_flame_grindstone_bishop.value,
            "require_upgrade_core_dlc_chapter2": self.options.require_upgrade_core_dlc_chapter2.value,
            "chapter6_access": self.options.chapter6_access.value,
            "quarts_combat_logic": self.options.quartz_combat_logic.value,
            "combat_logic": self.options.combat_logic.value,
            "dlc_required": self.dlc_required,
        }
        return slot_data

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player, self.options)

        if self.options.early_krat_central_station == "early_global":
            self.multiworld.early_items[self.player][KEY_ID_TO_NAME[KCS_ENTRANCE_KEY]] = 1
        elif self.options.early_krat_central_station == "early_local":
            self.multiworld.local_early_items[self.player][KEY_ID_TO_NAME[KCS_ENTRANCE_KEY]] = 1

        if self.options.early_weapon_assemble == "early_global":
            self.multiworld.early_items[self.player][FUNC_ID_TO_NAME[FUNC_EAT]] = 1
        elif self.options.early_weapon_assemble == "early_local":
            self.multiworld.local_early_items[self.player][FUNC_ID_TO_NAME[FUNC_EAT]] = 1

    def check_dlc_start_inventory(self):
        start_inventory = self.multiworld.precollected_items[self.player]

        if not self.dlc_required:
            for item in start_inventory:
                if item.code > 2000:  # Lowest DLC Item ID
                    print("DLC ITEM DETECTED")
                    self.dlc_required = True
                    return
