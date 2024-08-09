const name = "ToggleScript"; // the name of the script
const enabled = GlobalVars.toggleBoolean(name);

Chat.log(
    Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append(name).withColor(0x5)
        .append("] ").withColor(0x7)
        .append(enabled ? "enabled" : "disabled").withColor(0xc)
        .build()
);

function isInventoryFull() {
    const inventory = Player.openInventory();
    
    // Check slots 9 to 44 (main inventory, excluding hotbar and armor)
    for (let i = 9; i < 45; i++) {
        if (inventory.getSlot(i).isEmpty()) {
            return false;
        }
    }
    return true;
}

// Function to sell items
function sellItems() {
    Chat.say("/sell a");
    Chat.log("Inventory full, selling items!");
}

if (isInventoryFull()) {
    sellItems();
}

if (enabled) {
    JsMacros.on("SlotUpdate", JavaWrapper.methodToJava(() => {
        if (isInventoryFull()) {
            sellItems();
        }
    }));
} else {
    JsMacros.disableScriptListeners()
}