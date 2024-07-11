file_text = open("new_file.txt", mode="r+")
file = open("new_file", mode="w")
file_bin = open("image.png", mode="rb")
this_file = open("files4.py","r")

# print(file.fileno())
# print(file_text.fileno())
# print(file_bin.fileno())
# print(this_file.fileno())

# print(file.readable())
# print(file_text.readable())
# print(file_bin.readable())
# print(this_file.readable())

# print(file.writable())
# print(file_text.writable())
# print(file_bin.writable())
# print(this_file.writable())

# print(file.seekable())
# print(file_text.seekable())
# print(file_bin.seekable())
# print(this_file.seekable())

# std_out = open("/dev/stdout","w")
# print(std_out.seekable())
# print(std_out.writable())
# std_out.write("some text")

# file.write("hello")
# print(file.tell())
# file.seek(0)
# print(file.tell())

# print(file_text.readline())
# print(file_text.readlines())

# file_text.writelines(["line1\n\n\n","line2"])

file_text.truncate(70)
print(file_text.read())

file.close()
file_bin.close()
file_text.close()
this_file.close()