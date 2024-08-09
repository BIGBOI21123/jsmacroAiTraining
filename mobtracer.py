name = "Tracers"  # the name of the script
enabled = GlobalVars.toggleBoolean(name)

# Create a list to hold the Draw3D objects
d3d_objects = []
entity_names = ["minecraft:falling_block"]

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
    mobsnearme = World.getEntities()

    for entity in mobsnearme:
        # Check if the entity is the player
        if not Player.getPlayer().equals(entity) and entity.getType() in entity_names:
        #if not Player.getPlayer().equals(entity):
            entity.setGlowing(True)
            entity.setGlowingColor(0x00FFFF)
            d3d = Hud.createDraw3D()
            d3d.entityTraceLineBuilder().color(0x00FFFF).buildAndAdd(entity)
            d3d.register()
            # Add the Draw3D object to the list
            d3d_objects.append(d3d)

    Client.waitTick(5) #How often to check for new entities

# When the script is toggled off, unregister all tracer lines
Hud.clearDraw3Ds()
for entity in World.getEntities():
    entity.resetGlowing()