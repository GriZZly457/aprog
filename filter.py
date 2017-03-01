from PIL import Image, ImageDraw  
import random


fil = int(input('Фильтр (от 1 до 4): ')) 
im = Image.open("uzbagoisya.jpg")
draw = ImageDraw.Draw(im) 
x, y = im.size 	
pixels = im.load()


if fil == 1:
	for i in range(x):
		for j in range(y):
			a = pixels[i, j][0]
			b = pixels[i, j][1]
			c = pixels[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))


if fil == 2:
	dep = int(input("Введите глубину сепии: "))
	for i in range(x):
		for j in range(y):
			r, g, b = pixels[i, j]
			mid = (r + g + b) // 3
			r, g, b = mid + dep * 2, mid + dep, mid
			pixels[i, j] = r, g, b


if fil == 3:
	f = int(input('Введите любое число:'))
	for i in range(x):
		for j in range(y):
			a = pixels[i, j][0]
			b = pixels[i, j][1]
			c = pixels[i, j][2]
			S = a + b + c
			if (S > (((255 + f) // 2) * 3)):
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))


if fil == 4:
	f = int(input('Введите любое число:'))
	for i in range(x):
		for j in range(y):
			rand = random.randint(-f, f)
			a = pixels[i, j][0] + rand
			b = pixels[i, j][1] + rand
			c = pixels[i, j][2] + rand
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))

im.show()