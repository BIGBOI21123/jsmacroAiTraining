Player.getPlayer().interact()
def listener(event, ctx):
    event.closeScreen = True
    event.signText[0] = 'sand'
    
JsMacros.once('SignEdit', True, JavaWrapper.methodToJava(listener))