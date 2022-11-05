# @Sheeye
# Date = 03.11.2022

import random

# Brain
# [0][0] - Output
# [0][1-4] - base
# [1] - Dist mult
# [2] - Plane changes Mult
# [3] - Time multi


brain = [[[0 for x in range(5)]for y in range(4)]for z in range(200)]
testor = ["LOT",6955,2,1070]

def randomize(offset,howmany):
    for specimen in range(howmany):
        for x in range(4):
            for y in range(4):
                brain[specimen+offset][x][y] = random.uniform(-500,500)
        brain[specimen][0][0] = 0


randomize(0,200)
f = open("airlines.txt", "r")
arr = f.readlines()
arr.pop(0)

for generation in range(1000):
    for specimen in range(200):
        for x in arr:
            x=x.replace("\n","")
            divided = x.split(";")
            price=1
            for z in range(3):
                price*=brain[specimen][0][z+1]
            for z in range(2):
                priceaddon = 1
                for y in range(4):
                    priceaddon *= brain[specimen][z+1][y] * int(divided[z+1])
                price+=priceaddon
            if specimen==0:
                print("My guess : ",price,"  Real price : ",int(divided[4]))
            co = price-int(divided[4])
            co=co*co
            brain[specimen][0][0]+=co
    brain.sort(key=lambda x:x[0][0])
    print("\nGENERATION ",generation)
    print("Score (bigger=worse) : ",brain[0][0][0])
    for x in range(20):
        brain[x][0][0]=0
        for y in range(4):
            for z in range(4):
                brain[20+x][y][z]=(brain[x][y][z]+brain[random.randint(0,20)][y][z])/2*random.uniform(0.95,1.05)
                brain[40 + x][y][z] = (brain[x][y][z] + brain[random.randint(0,20)][y][z]) / 2 * random.uniform(0.95, 1.05)
        brain[x][0][0] = 0
        brain[20+x][0][0] = 0
        brain[40+x][0][0] = 0
    for toto in range(4):
        for okk in range(20):
            for y in range(4):
                for z in range(4):
                    brain[60 + okk + toto * 20][y][z] = brain[okk][y][z]
                    c = random.randint(0, 100)
                    if c > 90:
                        brain[60 + okk + toto * 20][y][z] = brain[okk][y][z] * random.uniform(0.5, 2.05)
                    if c > 95:
                        brain[60 + okk + toto * 20][y][z] = brain[okk][y][z] * random.uniform(0.75, 1.25)
                    brain[60 + okk + toto * 20][0][0] = 0
    randomize(140,60)
print(brain[0])
print("DONE:")
price = 1
for z in range(3):
    price *= brain[0][0][z + 1]
for z in range(2):
    priceaddon = 1
    for y in range(4):
        priceaddon *= brain[0][z + 1][y] * int(testor[z + 1])
    price += priceaddon
print(price)