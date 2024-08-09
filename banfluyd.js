JsMacros.on('PlayerJoin',JavaWrapper.methodToJava((e) => {
    txt = e.player.getName()
    
    if (txt == "Fluyd") {
        Chat.log("/banip "+txt+" 7d pls no unban yourself - ev")
    }
}));