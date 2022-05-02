import pyperclip

########################################################################

block_down  = "minecraft:waxed_cut_copper" #из чего пол
block_wall  = "minecraft:white_stained_glass" #из чего стены
block_light = "minecraft:lantern" #из чего свет 
block_red   = "minecraft:redstone_block" #из чего редстоун
block_air   = "minecraft:air" #из чего воздух
block_rail   = "minecraft:powered_rail" #из чего рельсы

x1 = 47 #координаты начальной точки
y =  102
z1 = 37

facing = "north" #east west north south - направление движения

l = 15 #длинна метро (до примерно 250-270 блоков за раз)

########################################################################

p1 = str('summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:\'gamerule commandBlockOutput false\'},')
p2 = " "
p3 = str('{id:command_block_minecart,Command:\'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}\'},{id:command_block_minecart,Command:\'kill @e[type=command_block_minecart,distance=..1]\'}]}]}]}')


if facing == "east" or facing == "west":
    
    if facing == "east":
        x2 = x1+l
        z2 = z1
    elif facing == "west":
        x2 = x1-l
        z2 = z1
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y) +" "+ str(z1-2)+ " "+ str(x2) +" "+ str(y) +" "+ str(z1+2) +" "+ block_down + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y) +" "+ str(z1) +" "+ block_red + '\'},')

    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+1) +" "+ str(z1-2)+ " "+ str(x2) +" "+ str(y+4) +" "+ str(z1+2) +" "+ block_wall + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+5) +" "+ str(z1-1)+ " "+ str(x2) +" "+ str(y+5) +" "+ str(z1+1) +" "+ block_wall + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+6) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+6) +" "+ str(z1) +" "+ block_wall + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+1) +" "+ str(z1-1)+ " "+ str(x2) +" "+ str(y+4) +" "+ str(z1+1) +" "+ block_air + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+1) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+1) +" "+ str(z1) +" "+ block_rail + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+5) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+5) +" "+ str(z1) +" "+ block_light + '\'},')
    
    
    
    
else:
    if facing == "north":
        x2 = x1
        z2 = z1-l
    elif facing == "south":
        x2 = x1
        z2 = z1+l
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1-2) +" "+ str(y) +" "+ str(z1)+ " "+ str(x1+2) +" "+ str(y) +" "+ str(z2) +" "+ block_down + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y) +" "+ str(z2) +" "+ block_red + '\'},')

    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1-2) +" "+ str(y+1) +" "+ str(z1)+ " "+ str(x1+2) +" "+ str(y+4) +" "+ str(z2) +" "+ block_wall + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1-1) +" "+ str(y+5) +" "+ str(z1)+ " "+ str(x2+1) +" "+ str(y+5) +" "+ str(z2) +" "+ block_wall + '\'},')
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+6) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+6) +" "+ str(z2) +" "+ block_wall + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1-1) +" "+ str(y+1) +" "+ str(z1)+ " "+ str(x2+1) +" "+ str(y+4) +" "+ str(z2) +" "+ block_air + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+1) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+1) +" "+ str(z2) +" "+ block_rail + '\'},')
    
    p2 += str('{id:command_block_minecart,Command:\'' +'fill '+ str(x1) +" "+ str(y+5) +" "+ str(z1)+ " "+ str(x2) +" "+ str(y+5) +" "+ str(z2) +" "+ block_light + '\'},')
    
  
pyperclip.copy(p1 + p2 + p3)
print ('Код скопирован в буфер обмена')
