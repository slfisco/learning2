import os

print(os.getcwd())
os.chdir(r"C:\Users\sfisco\Documents")

file = open("antibody notes.txt")
print(file.read())
print(os.getcwd())
