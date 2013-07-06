import zipfile

def read_from_zip(file_name):
	comments = []
	file_list = zipfile.ZipFile("input.zip")
	for f in file_list.namelist():
		fc = file_list.read(file_name, "r")
		comments.append(file_list.getinfo(file_name).comment)
		seg = fc.split(' ')
		file_seg = seg[len(seg) - 1]
		if file_seg.isdigit():
			file_name = file_seg + ".txt"
		else:
			break
	return "".join(comments)

if __name__ == "__main__":
	print read_from_zip("90052.txt")