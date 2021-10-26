from PIL import Image
import numpy as np
import random


# p-norm formula
vector_norm = lambda r,g,b,p: abs((r**p + g**p + b**p) ** (1 / p))
p = 2

def matrix_one_norm(arr):
    x = []
    for j in range(len(arr[0])):
        x.append(0)
        for i in range(len(arr)):
            r,g,b, a = arr[i][j]
            x[-1] += vector_norm(r,g,b,p)
    return max(x)




def matrix_max_norm(arr):
    return max(
        map(lambda x:
        sum(map(lambda y: vector_norm(y[0],y[1],y[2],p), x)), arr)
    )

# 'pretaken' images of glasses filled with liquids
images = [
    'water_glass.png',
    'coffee_glass.png',
    'fanta_glass.png'
]

# predefined lists of liquids by their norms

liquids_one_norm = {
    'water': 58742,
    'fanta': 84801,
    'coffee': 113951
}

liquids_max_norm = {
    'water': 59600,
    'fanta': 35641,
    'coffee': 41874
}

chooose = int(input("Choose from 1 to 3: "))
if chooose == 1:
    image = Image.open(images[0])
if chooose == 2:
    image = Image.open(images[1])
if chooose == 3:
    image = Image.open(images[2])
# image = Image.open(random.choice(images))
arr = np.array(image)
image.show()


# setting the boundaries of the glass (precalculated)
left = 175
right = 330
up = 50
down = 355



# calculating the percentage of fill
liquid_height = 0
mid = (right + left) // 2

for i in range(down-1, up-1, -1):
    if arr[i][mid][3] == 0:
        break
    liquid_height += 1


fill = liquid_height / (down - up) * 100
print(fill, 'percents filled')

# part of matrix fully filled with liquid
liquid_arr = list(map(lambda x: x[left:right], arr[down-liquid_height:down]))
# calculating norms respectively
liquid_one_norm = matrix_one_norm(liquid_arr)
liquid_max_norm = matrix_max_norm(liquid_arr)

print('one-norm:', liquid_one_norm)
print('max-norm:', liquid_max_norm)



# detecting the liquid by the min absolute difference of the calculated and predefined norms
print('it is', min(map(lambda x: (x[0], abs(liquid_one_norm - x[1])), liquids_one_norm.items()), key = lambda x: x[1])[0], 'according to one-norm')

print('it is' ,min(map(lambda x: (x[0], abs(liquid_max_norm - x[1])), liquids_max_norm.items()), key = lambda x: x[1])[0], 'according to max-norm')
