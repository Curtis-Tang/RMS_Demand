"""
This section contains function blocks for making main neat.
"""
import csv


def integer_input(input_num):
    # Stop until grab an integer input
    try:
        int_return = int(input_num)
        return int_return
    except Exception:
        int_return = integer_input(input("Invalid input. Please enter an integer: "))
        return int_return


def float_input(input_float):
    # Stop until grab an float input
    try:
        float_return = float(input_float)
        return float_return
    except Exception:
        float_return = float_input(input("Invalid input. Please enter a number: "))
        return float_return


def boundary_print(lower_bond, upper_bond):
    if lower_bond < upper_bond:
        print("Your lower boundary is " + str(lower_bond))
        print("Your upper boundary is " + str(upper_bond))
        print("\n")
    elif lower_bond > upper_bond:
        print("Your upper boundary is smaller than lower boundary. Swapped automatically.")
        lower_bond, upper_bond = upper_bond, lower_bond
        print("Your lower boundary is " + str(lower_bond))
        print("Your upper boundary is " + str(upper_bond))
        print("\n")
    else:
        print("Your lower boundary is identical to your upper boundary which is "
              + str(upper_bond) + ". Continue anyway.\n")
        # exit("Equal inputs. \n Please restart the program.")


def mean_print(mean):
    print("Your mean is " + str(mean))


def sequence_list(num):
    numbered_list = [i for i in range(num)]
    return numbered_list


def zero_list(num):
    numbered_list = [0 for i in range(num)]
    return numbered_list


def csv_export(file_name, rms_order):
    with open(file_name, "w", newline='') as file:
        order = csv.writer(file, delimiter=',')
        order.writerows(rms_order)


def empty_list(list_number):
    a_list = []
    for i in range(list_number):
        a_list.append([])
    return a_list


def min_location(list):
    low = list[0][0]
    location = 0
    for i in range(len(list)):
        if low > list[i][0]:
            low = list[i][0]
            location = i
    return location


def add_empty_column(a_list):
    """
    :param a_list:
    :return: a_list with an extra 0 at the end.
    """
    for i in a_list:
        i.append(0)
    return a_list
