file = open("image.png", mode="rb+")
copy_file = open("copy.png", mode="wb+")
copy_file.write(file.read())

file.close()
copy_file.close()


appended_file = open("new_file.txt", mode="a")
appended_file.write("another text\n")
appended_file.write("another text\n")
appended_file.write("another text\n")
appended_file.write("another text\n")

appended_file.close()