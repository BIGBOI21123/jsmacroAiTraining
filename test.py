for entity in World.getEntities(5):
    # Check if the entity is the player
    if not Player.getPlayer().equals(entity):
        Chat.log(entity.getType())