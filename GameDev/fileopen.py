f = open("filey.txt.rtf", "r+")
print(f.read())
f.write("Oh hi there \n")
print(f.read())
f.close() 