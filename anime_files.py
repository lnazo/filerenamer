#renames anime shows
import os

# renames each file in each folder accordingly
def rename(dir_name, show_name, ep_num):
	count = int(ep_num)
	directory = dir_name.replace("\\", r"\\")
	temp = ep_num

	# look through each folder and subfolder
	for subdir, dir, files in os.walk(directory):
		# for each file in each subfolder, where files is a list of files for each subfolder
		for file in files:
			file_ext = file[len(file) - 4:len(file):1]
			file_ext = file_ext.lower()
			#if show_name in file:
			if len(temp) == 1:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - 00" + temp + file_ext))
			elif len(temp) == 2:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - 0" + temp + file_ext))
			elif len(temp) == 3:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - " + temp + file_ext))
			count+= 1
			temp = str(count)

	print("Media files renamed")

def quick_sort(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[0]
		for x in array:
			if x < pivot:
				less.append(x)
			elif x == pivot:
				equal.append(x)
			elif x > pivot:
				greater.append(x)
		return quick_sort(less) + equal + quick_sort(greater)
	else:
		return array

# gets input from user
def main():
	print("Anime Shows\n")
	dir_name = raw_input("Enter the full file directory: ")
	show_name = raw_input("Enter the name of the show: ")
	ep_num = raw_input("What number do the episodes start from?: ")

	rename(dir_name, show_name, ep_num)

main()