// Function to log messages
function log(message) {
    Chat.log(message);
}

// Function to find a Potion in the inventory and move it to the hotbar
function movePotionToHotbar() {
    var player = Player.getPlayer();
    var inventory = Player.openInventory();
    log("Searching for Potion in the inventory...");

    // Loop through inventory slots (slots 9 to 35 inclusive)
    for (var i = 9; i < 36; i++) {
        var item = inventory.getSlot(i);
        if (item && item.getName().toString().includes("Potion")) { // Adjusted for partial name matching
            log("Potion found in slot " + i + ". Moving it to the hotbar...")
            
            // Find an empty slot in the hotbar to move the potion
            for (var j = 36; j < 45; j++) {
                if (inventory.getSlot(j).isEmpty()) {
                    inventory.swapHotbar(i, j-36);
                    log("Potion moved successfully to slot " + j);
                    return true; // Potion moved successfully
                }
            }
        }
    }

    log("No Potion found in the inventory or no empty slot in the hotbar.");
    return false; // No potion found or no empty slot in the hotbar
}

movePotionToHotbar();