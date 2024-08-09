import random

name = "Trigger Bot"  # the name of the script
enabled = GlobalVars.toggleBoolean(name)
Chat.log(
    Chat.createTextBuilder()
        .append("[")
        .withColor(0x7)
        .append(name)
        .withColor(0x5)
        .append("] ")
        .withColor(0x7)
        .append("enabled" if enabled else "disabled")
        .withColor(0xc)
        .build()
)

while GlobalVars.getBoolean(name):
    Client.waitTick(random.randint(2, 5))  # waits for a random number of ticks between 1 and 3
    try:
        if Player.getPlayer().getAttackCooldownProgress() == 1.0:
            Player.getInteractionManager().attack(Player.getInteractionManager().getTargetedEntity())
    except Exception:
        pass