# Ice Cream Math
# Isaac Ingles
# CS 1400-X01 Fall 2019

tub_height = float(11)
tub_diameter = float(9.5)
scoop_diameter = float(2)

#Calculate the volumes -- divide the diameter by 2 to get the radius
tub_volume = float( ((tub_diameter /2 ) ** 2) * tub_height * 3.14)
scoop_volume = float( ((scoop_diameter /2)**2) * (4/3) * 3.14)

#Calculate the number of servings avaliable
servings = float(tub_volume / scoop_volume)

#Name and flavor
name = "Isaac Ingles"
flavor = "Chocolate"

#Output everything

print("Tub Height: ", tub_height)
print("\nTub Diameter: ", tub_diameter)
print("\nScoop diameter: ", scoop_diameter)
print("\n\nName: ", name)
print("\nFlavor: ", flavor)
print("\nVolume of Tub: ", tub_volume)
print("\nVolume of Scoop: ", scoop_volume)
print("\nServings Available", servings)
