const reverse = !GlobalVars.getBoolean("autoTotemModuleState");
const inv = Player.openInventory()
const totem = "minecraft:totem_of_undying"
const air = "minecraft:air"
function getItemSlots(searchedItem) {
    const map = inv.getMap();
    var foundSlots = []
    const slots = Array.from(map.get("main")).concat(Array.from(map.get("hotbar")));
    var slotsSet = new Set(slots);
    slotsSet.delete(map.get("hotbar")[0])
    for (const slot of slots) {
        if (inv.getSlot(slot).getItemId() == searchedItem) {
            foundSlots.push(slot)
        }
    }
    return foundSlots
}
function log(Module, setting, text) {
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7).append(Module).withColor(0x6).append("]").withColor(0x7).append(" ").append(setting).withColor(0xd).append(" ").append(text).withColor(0xc).build());
    }
GlobalVars.putBoolean("autoTotemModuleState", reverse);
if (reverse) {
    log("Autototem","Module","enabled")
} else {
    log("Autototem","Module","disabled")
}
JsMacros.on("HeldItemChange", JavaWrapper.methodToJava((event) => {
    if (GlobalVars.getBoolean("autoTotemModuleState") && event.offHand && event.oldItem.getId() == totem && event.item.getId() == air || !!getItemSlots(totem).length) {
        let totemSlots = getItemSlots(totem)    
        let offHandSlot = inv.getMap().get("offhand")
        inv.swapHotbar(totemSlots[0],offHandSlot)
        log("Autototem","Totem used!", totemSlots.length+" remaining")
    }
}))