#!/usr/bin/python3
def safe_print_list_integers(my_list=[], z=0):
    counter = 0
    for i in range(z):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            counter += 1
    print()
    return (counter)
