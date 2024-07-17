# file = open('files/new_file.txt')
# print(file.read())
# file.close()

# files = []
# for x in range(100000000):
#     files.append(open("files/new_file.txt"))

class Context:
    def __init__(self) -> None:
        print("created")
        pass

    def __enter__(self):
        print("entered")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exited")
        pass

example_obj= Context()

with example_obj:
    print("inside with")
    pass

with open("files/new_file.txt","r+") as file:
    file.write("!2121212")
    data = file.read()
    file.close()

print(data)