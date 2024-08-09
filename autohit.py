thetick = 0
name = "ToggleAttackScript"
enabled = GlobalVars.toggleBoolean(name)

# Log the script state
Chat.log(f"[{name}] {'enabled' if enabled else 'disabled'}")

# Function to check if the weapon cooldown is full
def isWeaponCooldownFull():
    return Player.getPlayer().getAttackCooldownProgress() >= 1.0

# Main loop
while GlobalVars.getBoolean(name):
    if isWeaponCooldownFull():
        Player.getPlayer().attack()
    Client.waitTick()  # wait 1 tick
    thetick = thetick + 1
    if thetick == 4800:
        thetick = 0
        Chat.say("/baltop")
