def reverse_number_part(numtype: str, num_str: str):
    res = ""
    met_int = False
    for i in range(len(num_str) - 1, -1, -1):
        if numtype == "float" and not met_int:
            if num_str[i] == "0": 
                continue
            elif num_str[i] != "0":
                met_int = True 
        res += num_str[i]
    return res


def reverse_number(number):
    # Напишите ваш код здесь
    num_str = str(number)
    multiplier = 1
    result = None
    
    if number < 0:
        num_str = num_str[1:]
        multiplier = -1
    
    if type(number) == float:
        int_part, float_part = num_str.split('.')
        result = float(reverse_number_part("int",int_part) + "." + reverse_number_part("float", float_part))
        
    elif type(number) == int:
        result = int(reverse_number_part("int",num_str))

    return result*multiplier

# print(reverse_number(1000011))
# print(reverse_number(1000001.0011101))


def running_sum(some_list: list):
    if type(some_list) != list:
        return "Это не список"
    if len(some_list) <= 1:
        return some_list
    res = []
    for i in range(len(some_list)):
        if type(some_list[i]) not in [int,float]:
            return "Плохой список"
        if i == 0:
            res.append(some_list[0])
        else:
            res.append(some_list[i] + res[i-1])
    return res

# print(running_sum([1,2,3,4,5]))


def unzip_list(zipped_list: list[str]) -> list[int]:
    res = []
    for item in zipped_list:
        splitted = item.split('|')
        if(len(splitted) == 1):
            res.append(int(item))
        else:
            for i in range(int(splitted[0])):
                res.append(int(splitted[1]))
    return res

# print("2".split("|"))

def zip_list(some_list: list):
    # Пипите код здесь
    pass

# print(zip_list([0,1,1,1,2,3,3,4,4,4,4]))

def c_crypt(msg: str, shift: int, alph: str) -> str:
    
    if shift == 0:
        return msg
    
    RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    EN = "abcdefghijklmnopqrstuvwxyz"
    
    if alph == 'ru':
        alphabet = RU 
    else:
        alphabet = EN 
        
    shift = shift%len(alphabet)
    
    if shift < 0:
        alphabet = alphabet[-shift:] + alphabet[0:-shift]
    else:
        alphabet = alphabet[0:-shift] + alphabet[-shift:]
    
    print(alphabet)
    
    trans_table = str.maketrans(alphabet)
    
    return msg.translate(trans_table)

print(c_crypt("aaafvdfddfdf",5,"en"))