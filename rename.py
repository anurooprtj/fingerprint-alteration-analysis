import os

for line in open("List.txt"):
	srcFile = line[:-1]
	# print(line)

	destFile = line.replace(".BMP" , "_Real.BMP")
	# print(newLine)

	command = "mv -v " + srcFile + " " + destFile
	print(command)
	os.system(command)

