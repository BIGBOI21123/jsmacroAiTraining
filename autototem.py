from JsMacrosAC import *

reverse = not GlobalVars.getBoolean("autoTotemModuleState")
inv = Player.openInventory()
totem = "minecraft:totem_of_undying"
air = "minecraft:air"

def get_item_slots(searched_item):
    map = inv.getMap()
    found_slots = []
    slots = list(map.get("main")) + list(map.get("hotbar"))
    slots_set = set(slots)
    slots_set.remove(map.get("hotbar")[0])
    for slot in slots:
        if inv.getSlot(slot).getItemId() == searched_item:
            found_slots.append(slot)
    return found_slots

def log(module, setting, text):
    Chat.log(Chat.createTextBuilder()
             .append("[").withColor(0x7)
             .append(module).withColor(0x6)
             .append("]").withColor(0x7)
             .append(" ")
             .append(setting).withColor(0xd)
             .append(" ")
             .append(text).withColor(0xc)
             .build())

GlobalVars.putBoolean("autoTotemModuleState", reverse)
if reverse:
    log("Autototem", "Module", "enabled")
else:
    log("Autototem", "Module", "disabled")

def on_held_item_change(event):
    if (GlobalVars.getBoolean("autoTotemModuleState") and
        event.offHand and
        event.oldItem.getId() == totem and
        event.item.getId() == air) or len(get_item_slots(totem)) > 0:
        
        totem_slots = get_item_slots(totem)
        off_hand_slot = inv.getMap().get("offhand")
        inv.swapHotbar(totem_slots[0], off_hand_slot)
        log("Autototem", "Totem used!", f"{len(totem_slots)} remaining")

JsMacros.on("HeldItemChange", on_held_item_change)