from typing import ClassVar, Dict, Mapping, Any

from BaseClasses import Tutorial, ItemClassification as ItemClass, Item
from worlds.AutoWorld import World, WebWorld
from .Options import EightDoorsOptions
from .Items import EightDoorsItem
from. import Items, Locations, Regions, Rules


class EightDoorsWeb(WebWorld):
    theme = "jungle"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up 8Doors for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Xtruh"]
    )

class EightDoorsWorld(World):
    game = "8Doors"
    web = EightDoorsWeb()

    options_dataclass = EightDoorsOptions
    options: EightDoorsOptions

    item_name_to_id: ClassVar[Dict[str, int]] = Items.get_item_dict()
    location_name_to_id: ClassVar[Dict[str, int]] = Locations.get_location_dict()

    explicit_indirect_conditions = False

    def create_regions(self) -> None:
        regions = Regions.create_regions(self, self.options)
        Locations.create_locations(self, regions)
        self.multiworld.regions.extend(regions.values())

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_class = ItemClass.filler
        return EightDoorsItem(name, item_class, item_id, self.player)

    def create_items(self) -> None:
        Items.populate_item_pool(self, self.options)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {
            "goal": self.options.goal.value,
            "requiredfugitivesouls": self.options.requiredfugitivesouls.value,
            "startingmoney": self.options.startingmoney.value,
        }
        return slot_data

    def set_rules(self) -> None:
        Rules.set_rules(self.multiworld, self, self.player, self.options)