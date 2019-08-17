import os
count = 100

for item in range(1, count+1):
	# srcFile = "Real/" + str(item) +"__" + "*.BMP"
	srcFile = "Altered/Altered-Easy/" + str(item) +"__" + "*.BMP"
	# print(srcFile)
	destFile = "sampleData/"

	command = "cp -v " + srcFile + " " + destFile
	print(command)
	os.system(command)
