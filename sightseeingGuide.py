from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"Bedroom" : (76,1,-61)}

choice = ""
while choice != "exit":
    choice = input("Bedroom")
    if choice in places:
        location=places["Bedroom"]
        x,y,z=location[0],location[1],location[2]
        mc.player.setTilePos(x,y,z)
