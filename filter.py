from PIL import Image, ImageDraw  

fil = int(input('Фильтр (от 1 до 4): ')) 
im = Image.open("gopher.jpg")
draw = ImageDraw.Draw(im) 
x, y = im.size 	
pixels = im.load()

if (fil == 1):
	for i in range(x):
		for j in range(y):
			a = pixels[i, j][0]
			b = pixels[i, j][1]
			c = pixels[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))

if (fil == 2):
	dep = int(input("Введите глубину сепии: "))
	for i in range(x):
		for j in range(y):
			r, g, b = pixels[i, j]
			mid = (r + g + b) // 3
			r, g, b = mid + dep * 2, mid + dep, mid
			pixels[i, j] = r, g, b



im.show()