import Image

def read_image_colors(file_name):
	im = Image.open(file_name)
	pic = im.load()
	(width, height) = im.size
	colors = []
	y = height / 2
	for i in range(width /7):		
		color = pic[i * 7,y][0]
		colors.append(color)
	return colors

def decipher(items):
	message = ""
	for i in items:
		message += chr(i)
	return message

if __name__ == "__main__":
	colors = read_image_colors("oxygen.png")
	print decipher(colors)
	print decipher([105, 110, 116, 101, 103, 114, 105, 116, 121])
	
