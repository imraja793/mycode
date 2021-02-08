from sys import argv
from os.path import exists

script,from_file, to_file = argv

print(f"copying from {from_file} to the file {to_file}")
in_file = open(from_file, "r")
indata = in_file.read()
print(f"the input file is {len(indata)} bytes long")
print(f"Does the output file exists{exists(to_file)}")
out_file = open(to_file, "w")
print(f"out file transferring to in file")
out_file.write(indata)
in_file.close()
out_file.close()
