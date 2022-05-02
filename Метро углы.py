import pyperclip

########################################################################

block_down  = "minecraft:waxed_cut_copper" #из чего пол 
block_wall  = "minecraft:white_stained_glass" #из чего стены 
block_light = "minecraft:lantern" #из чего свет 
block_red   = "minecraft:redstone_block" #из чего редстоун
block_air   = "minecraft:air" #из чего воздух
block_rail  = "minecraft:rail" #из чего рельсы

x = 47 #координаты начальной точки
y =  110
z = 12

########################################################################


p1 = str('summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:\'gamerule commandBlockOutput false\'},')
p2 = " "
p3 = str('{id:command_block_minecart,Command:\'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}\'},{id:command_block_minecart,Command:\'kill @e[type=command_block_minecart,distance=..1]\'}]}]}]}')


p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x-2) +" "+ str(y) +" "+ str(z-2)+ " "+ str(x+2) +" "+ str(y) +" "+ str(z+2) +" "+ block_down + '\'},')
p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x-2) +" "+ str(y+1) +" "+ str(z-2)+ " "+ str(x+2) +" "+ str(y+6) +" "+ str(z+2) +" "+ block_wall + '\'},')
p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x-1) +" "+ str(y+1) +" "+ str(z-1)+ " "+ str(x+1) +" "+ str(y+5) +" "+ str(z+1) +" "+ block_air + '\'},')
p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y+5) +" "+ str(z)+ " "+ str(x) +" "+ str(y+5) +" "+ str(z) +" "+ block_light + '\'},')  
p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x-1) +" "+ str(y+1) +" "+ str(z)+ " "+ str(x+1) +" "+ str(y+1) +" "+ str(z) +" "+ block_rail + '\'},')    
p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x) +" "+ str(y+1) +" "+ str(z-1)+ " "+ str(x) +" "+ str(y+1) +" "+ str(z+1) +" "+ block_rail + '\'},')     


pyperclip.copy(p1 + p2 + p3)
print ('Код скопирован в буфер обмена')
