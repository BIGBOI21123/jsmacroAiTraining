from JsMacrosAC import *
# Function to log messages
def log(message):
    Chat.log(message)

# Function to find and use a Potion of Healing in the hotbar
def useHealingPotion():
    player = Player.getPlayer()
    inventory = Player.openInventory()
    originalSlot = inventory.getSelectedHotbarSlotIndex()
    oYaw = player.getYaw()
    oPitch = player.getPitch()
    log("Original slot: " + str(originalSlot))
    log("Searching for Potion of Healing in the hotbar...")

    # Loop through hotbar slots (slots 36 to 44 inclusive)
    for i in range(36, 45):
        item = inventory.getSlot(i)
        if item and "Healing" in item.getName().toString(): # Adjusted for partial name matching
            log("Potion of Healing found in slot " + str(i) + ". Using it...")
            inventory.setSelectedHotbarSlotIndex(i-36)
            player.lookAt(player.getYaw(), 75)
            player.interact()
            Client.waitTick() # Wait for a moment to ensure the item is used
            player.lookAt(oYaw, oPitch)
            inventory.setSelectedHotbarSlotIndex(originalSlot)
            log("Potion used successfully. Switched back to original slot.")
            return True # Potion used successfully

    log("No Potion of Healing found in the hotbar.")
    return False # No potion found

# Check player health
player = Player.getPlayer()
currentHealth = player.getHealth()
maxHealth = player.getMaxHealth()
healthThreshold = maxHealth * 0.9 # Set the threshold to 90% of max health

log("Current health: " + str(currentHealth) + " / " + str(maxHealth))
log("Health threshold set to: " + str(healthThreshold))

useHealingPotion()