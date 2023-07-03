# %%writefile HW1Q3.py
# Your code for Question 3 in this cell
# After you finish writing your code and check that it is working correctly,
# uncomment the first line and run your code so that it genrates HW1Q3.py file
from math import *

radius = float(input('Enter radius of the cylinder: '))
if radius > 0:
    liquidLevel = float(input('Enter liquid level : '))
    if liquidLevel > 0 and liquidLevel > radius:
        coneVolume = 1 / 3 * (pi * (radius ** 2) * radius)
        cylinderVolume = (pi * (radius ** 2) * 2 * radius)
        totalVolume = coneVolume + cylinderVolume
        liquidVolume = coneVolume + (pi * (radius ** 2) * (liquidLevel - radius))
        if liquidVolume > totalVolume:

            print('Tank is overfilled')
        else:
            print(f'Total volume of liquid = {"%.2f" % liquidVolume}')
    elif liquidLevel > 0 and liquidLevel < radius:
        liquidVolume = (1 / 3) * (pi * (liquidLevel ** 2) * (liquidLevel))
        print(f'Total volume of liquid = {"%.2f" % liquidVolume}')
    else:
        print('Liquid level must be positive')
else:
    print('Radius must be positive')
