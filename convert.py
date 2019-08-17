import os

for line in open("convertList.txt"):
	srcFile = line[:-1]
	# print(line)

	destFile = line.replace(".BMP" , ".pgm")
	# print(newLine)

	command1 = "convert " + srcFile + " " + destFile
	print(command1)

	command2 = "rm -vf " + srcFile
	print(command2)

	os.system(command1)
	os.system(command2)


