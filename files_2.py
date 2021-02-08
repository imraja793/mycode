from sys import argv

script, filename = argv
print(f"erase filename {filename}")
print(f"if dont want to delete press CTRL-C (^C).")
print("if you want hit enter")

input("?")

print("opening the file")
target = open(filename, "w+")
print("truncating the file goodbye")
target.truncate()


line1 = input("for 1")
line2 = input("for 2")
line3 = input("for 3")

target.write(line1 + '\n')
target.write(line2 + '\n')
target.write(line3 + '\n')

print("closing time")

target.close()
