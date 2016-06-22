from os import listdir, getcwd, rename

files_to_rename = listdir(getcwd())
array_len = files_to_rename.__len__()
i=0
for file in files_to_rename:
	dst = str(array_len-i)+"_"+file[4:]
	rename(file, dst)
	i+=1