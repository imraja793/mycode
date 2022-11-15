from sys import argv

script, filename = argv
txt = open(filename)
print(script, filename, "dikdhdihdihdiddhi")
b = input("new file name >")
txt = open(b)
print(txt.read())
txt.close()
