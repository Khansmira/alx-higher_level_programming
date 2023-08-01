#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    itms = 0
    for idx in range(x):
        try:
            print("{}" .format(my_list[idx]), end="")
            itms = itms + 1
        except IndexError:
            break
    print("")
    return(itms)
