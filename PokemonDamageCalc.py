#damage
Level = 12
Power = 110
D = 80
A = 75

#Modifier
Target = 1
Weather = 1.5
Badge = 1
Critical = random.randint(2,1)
Random Number = round(random.uniform(0.05 , 1.00)2)
STAB = 1
Type = 1
other = 1

Modifier = round(Target * Weather * Badge * Critical * Random_Number * STAB * Type* other)
Damage = round((((((2*Level1)/5)+2)*Power*A/D)/50)+2)+Modifier

print("Target: ", Target)
print("Weather: ", Weather)
print("Badge: ", Badge)
print("Critical: ", Critical)
print("Random: ", Random_Number)
print("STAB: ", STAB)
print("Type: ", Type)
print("other: ", other)
print("Modifier: ", Modifier)
print("Raichu Deals: ",Damage,  "to pikachu " )

Recoil_Dam = round(Damge*0.50 )
Recoil = random.randint(1,600)
if Recoil_Dam
    print("As well as Pikachu is recoiling ")
else:
    print("However, Pikachu is not recoiling ")