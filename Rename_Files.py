import os

def rename(dir_name, show_name, ep_num):
	count = ep_num
	directory = dir_name.replace("\\", r"\\")

	for subdir, dir, files in os.walk(directory):
		for file in files:
			#print(os.path.join(subdir, file))
			#print(file)
			#print(files)
			if show_name in file:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " " + str(count) + ".mp4"))
				#os.rename(os.path.join(subdir, file),os.path.join(subdir, "One Punch Man " + str("%.2d" % count) + ".mp4"))
				count+= 1

	print("Media files renamed")

def main():
	print("File renamer\n")
	dir_name = input("Enter the full file directory: ")
	show_name = input("Enter the name of the show: ")
	ep_num = input("What episode number should it begin renaming?: ")

	rename(dir_name, show_name, ep_num)

main()