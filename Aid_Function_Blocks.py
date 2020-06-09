"""
This section contains function blocks for making main neat.
"""


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

# Equal to len()
# def list_count(a_list):
#     count = 0
#     for elements in a_list:
#         if elements is not None:
#             count += 1
#     return count



# Recycle bin

# Failed
# def int_compare_input_require(smaller, larger):
#     if smaller < larger:
#         return True
#     elif smaller > larger:
#         return False
#     else:
#         print("Identical input.")
#         smaller = integer_input(input("Please enter another integer: "))
#         return smaller
#         int_compare_input_require(smaller, larger)
