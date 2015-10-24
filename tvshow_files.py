#renames tv shows
import os

# renames each file in each folder accordingly
def rename(dir_name, show_name, s_num, ep_num):
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
			if len(temp) == 1 and len(s_num) == 1:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - S0" + s_num + "E0" + temp + file_ext))
			elif len(temp) == 2 and len(s_num) == 1:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - S0" + s_num + "E" + temp + file_ext))
			elif len(temp) == 1 and len(s_num) == 2:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - S" + s_num + "E0" + temp + file_ext))
			elif len(temp) == 2 and len(s_num) == 2:
				os.rename(os.path.join(subdir, file),os.path.join(subdir, show_name + " - S" + s_num + "E" + temp + file_ext))
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
	print("TV Shows\n")
	dir_name = input("Enter the full file directory: ")
	show_name = input("Enter the name of the show: ")
	s_num = input("Enter the season number: ")
	ep_num = input("What number do the episodes start from?: ")

	rename(dir_name, show_name, s_num, ep_num)

main()