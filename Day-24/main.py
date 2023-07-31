# with open("my_file.txt") as file: <-- by default this is set to read only
#     contents = file.read()
#     print(contents)

#if you try to open a file that doesnt exist with "write" mode, you will create it
with open("/mnt/c/Users/Andrew/Desktop/my_file.txt", mode="r") as file: #<-- mode='w' stands for write, 'a' stands for append
     contents = file.read()
     print(contents)
