import os
import sys

data = {
    1: [2, 3],
    2: [4]
}


def my_code(data, value):
    final_list = []
    final_list.append(value)
    
    def became_final_list(data, value):
        if value in data:
            for el in data[value]:
                if el not in final_list:
                    final_list.append(el)
                    became_final_list(data, el)
        else:
            print("Bottom of recursion reached")

    became_final_list(data, value)
    return final_list


value = int(sys.argv[1])
result = my_code(data, value)
print(result)