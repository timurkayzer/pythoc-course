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


def unzip_list(zipped_list: list):
    # Пишите ваш код здесь
    
    pass

print("2".split("|"))