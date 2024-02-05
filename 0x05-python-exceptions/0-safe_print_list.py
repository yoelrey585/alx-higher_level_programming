#!/usr/bin/python3
def safe_print_list(my_list=[], z=0):
    counter = 0
    for i in range(z):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            counter += 1
    print()
    return counter
