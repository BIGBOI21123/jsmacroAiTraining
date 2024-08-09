wa = 6
name = "Auto Craft and Sell Melons "
enabled = GlobalVars.toggleBoolean(name)

Chat.log(Chat.createTextBuilder().append(name).withColor(0x5).append("enabled" if enabled else "disabled").withColor(0xc).build())

while GlobalVars.getBoolean(name):
    Chat.say("/shop Gear")
    Client.waitTick(wa)
    Player.openInventory().click(14)
    Client.waitTick(wa)
    Player.openInventory().click(31)
    Client.waitTick(wa)
    Player.openInventory().click(25)
    for x in range(3):
        Client.waitTick(3)
        Player.openInventory().click(23)
    Client.waitTick(wa)
    Player.openInventory().click(13)
    Client.waitTick(3)
    Player.openInventory().close()
    Client.waitTick(4)
    Chat.say("/sellall ENDER_PEARL")
    Client.waitTick(6)