// Function to log messages
function log(message) {
    Chat.log(message);
}

// Function to find and use a Potion of Healing in the hotbar
function useHealingPotion() {
    var player = Player.getPlayer();
    var inventory = Player.openInventory();
    var originalSlot = inventory.getSelectedHotbarSlotIndex();
    log("Original slot: " + originalSlot);
    
    log("Searching for Potion of Healing in the hotbar...");

    // Loop through hotbar slots (slots 36 to 44 inclusive)
    for (var i = 36; i <= 44; i++) {
        log(i)
        var item = inventory.getSlot(i);
        log(item.getName())
        if (item && item.getName().toString().includes("Healing")) { // Adjusted for partial name matching
            log("Potion of Healing found in slot " + i + ". Using it...");
            inventory.swapHotbar(inventory.getSlots('hotbar').indexOf(i));
            player.useItem();
            Time.sleep(1000); // Wait for a moment to ensure the item is used
            i inventory.swapHotbar(inventory.getSlots('hotbar').indexOf(original));
            log("Potion used successfully. Switched back to original slot.");
            return true; // Potion used successfully
        }
    }
    log("No Potion of Healing found in the hotbar.");
    return false; // No potion found
}

// Check player health
var player = Player.getPlayer();
var currentHealth = player.getHealth();
var maxHealth = player.getMaxHealth();
var healthThreshold = maxHealth * 0.9; // Set the threshold to 90% of max health

log("Current health: " + currentHealth + " / " + maxHealth);
log("Health threshold set to: " + healthThreshold);

useHealingPotion();