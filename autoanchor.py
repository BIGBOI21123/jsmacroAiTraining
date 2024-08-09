#from JsMacrosAC import *
Player.getPlayer().getVelocity()
name = "Auto Anchor"  # the name of the script
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

def Ilistener(event, ctx):
    if event.result == "SUCCESS":
        # Get the block that was interacted with
        block = event.block
        # Get the position of the block
        x, y, z = block.getX(), block.getY(), block.getZ()
    
        # Determine the position of the adjacent block based on the side of interaction
        if event.side == 0:   # Bottom
            y -= 1
        elif event.side == 1: # Top
            y += 1
        elif event.side == 2: # North
            z -= 1
        elif event.side == 3: # South
            z += 1
        elif event.side == 4: # West
            x -= 1
        elif event.side == 5: # East
            x += 1
    
        # Get the block at the new position
        adblock = World.getBlock(x, y, z)
        if adblock.getName().getString() == "Respawn Anchor":
            for i in range(36, 45):
                item = Player.openInventory().getSlot(i)
                if item and "Glowstone" in item.getName().getString():
                    orislot = Player.openInventory().getSelectedHotbarSlotIndex()
                    Player.openInventory().setSelectedHotbarSlotIndex(i-36)
                    Client.waitTick(1)
                    Player.getPlayer().tryLookAt(adblock.getBlockPos())
                    Client.waitTick()
                    Player.getInteractionManager().interact()
                    Client.waitTick(2)
                    Player.openInventory().setSelectedHotbarSlotIndex(orislot)
                    Client.waitTick(1)
                    Player.getPlayer().tryLookAt(adblock.getBlockPos())
                    Client.waitTick()
                    Player.getInteractionManager().interact()

# Register or unregister the listener for the 'InteractBlock' event based on the 'enabled' variable
if GlobalVars.getBoolean(name):
    JsMacros.on('InteractBlock', True, JavaWrapper.methodToJava(Ilistener))
else:
    JsMacros.disableScriptListeners('InteractBlock')