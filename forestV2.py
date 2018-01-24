from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 6
y = 5
z = 28
wood = 17
leaves = 18

mc.setBlocks(x , y+5, z, wood)
mc.setBlocks(x+5 , 10 , z, leaves)
#def growTree(x, y, z):
