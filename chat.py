from JsMacrosAC import *
Chat.log(FS.createFile("testFolder", "test.txt", True))
FS.open("testFolder/test.txt").write("put variable here")
Chat.log()
"""
slots = Player.openInventory().findItem("minecraft:melon_slice")

for slot in slots:
    Player.openInventory().click(slot)

wa = 10
name = "Auto Craft and Sell Melons "
enabled = GlobalVars.toggleBoolean(name)

Chat.log(Chat.createTextBuilder().append(name).withColor(0x5).append("enabled" if enabled else "disabled").withColor(0xc).build())

while GlobalVars.getBoolean(name):
    Chat.say("/shop Farming")
    Client.waitTick(wa)
    Player.openInventory().click(17)
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
    Client.waitTick(wa)
    Player.getInteractionManager().interact()
    Client.waitTick(11)
    for x in range(4):
        Player.openInventory().getRecipes(True)[0].craft(True)
        Player.openInventory().quick(0)
        Client.waitTick(2)
    Player.openInventory().close()
    Client.waitTick(4)
    Chat.say("/sellall MELON")
    Client.waitTick(6)
"""