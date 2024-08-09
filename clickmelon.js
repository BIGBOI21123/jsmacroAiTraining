let slots = Player.openInventory().findItem("minecraft:melon_slice");

slots.forEach(function(slot) {
    Player.openInventory().click(slot);
    Client.waitTick(2)
});