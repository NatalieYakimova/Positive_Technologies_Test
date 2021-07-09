import json
import sys


def my_code(file):
    ter = 0

    def print_all_pairs(dict_obj, ter):
        for key, value in dict_obj.items():
            #global ter
            if isinstance(value, dict):
                for W in range(ter):
                    print("\t", end='')
                print(key, ':')
                ter+=1
                print_all_pairs(value, ter)
                ter-=1
            elif isinstance(value, list):
                for W in range(ter):
                    print("\t", end='')
                print(key, ':')
                ter+=1
                #print("\t")
                print_all_pairs_list(value, ter)
                ter -= 1
            else:
                for W in range(ter):
                    print("\t", end='')
                print(key, '::', value)

    def print_all_pairs_list(list_obj, ter):
        for value in list_obj:
            if isinstance(value, list):
                 print("\t", end='')
                 print_all_pairs_list(value, ter)
            elif isinstance(value, dict):
                 print_all_pairs(value, ter)
            else:
                for W in range(ter):
                    print("\t", end='')
                print(value)

    with open(file, "r") as read_file:
        data = json.load(read_file)
        print_all_pairs(data, ter)


file = sys.argv[1]
my_code(file)



