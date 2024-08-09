Player.getInteractionManager().interact()
Player.getPlayer().getPitch()
def on_player_join(e):
    e.closeScreen = True
    e.signText[0] = 'sand'

JsMacros.once("'SignEdit", True, on_player_join)