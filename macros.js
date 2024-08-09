const nome = "ToggleScript"; // the name of the script
const enabled = GlobalVars.toggleBoolean(nome);

Chat.log(
    Chat.createTextBuilder()
        .append("[").withColor(0x7)
        .append(nome).withColor(0x5)
        .append("] ").withColor(0x7)
        .append(enabled ? "enabled" : "disabled").withColor(0xc)
        .build()
);

while (GlobalVars.getBoolean(nome)) {
    Chat.log("do stuff here...");
    Client.waitTick(20); // wait 1 second (synchronized to client ticks)
}