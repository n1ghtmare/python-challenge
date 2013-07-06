import pickle

def convert_to_banner(file_name):
	file_content = open(file_name, "rb")
	list_data = pickle.load(file_content)
	output_data = ""
	for list_item in list_data:
		for k, v in list_item:
			for i in range(v):
				output_data += k
		output_data += "\n"
	return output_data

if __name__ == "__main__":
	print convert_to_banner("input.p")