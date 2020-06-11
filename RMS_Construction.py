"""
Construct an RMS in this section
"""

import Aid_Function_Blocks as aid
import random
import numpy as np
import sys


def rmt_module_count(rmt_quantity, rmt_group):
    rmt_module_number_list = []
    for i in range(rmt_quantity):
        rmt_module_number_list.append(len(rmt_group[i]))
    return rmt_module_number_list


def rmt_module_structure(product_variant_num, rmt_quantity):
    print("Reconfigurable modules are the souls of RMTs.")
    rmt_process_time_array = aid.sequence_list(rmt_quantity)
    largest_product_variant = int(1)
    for i in range(rmt_quantity):
        module_number = aid.integer_input(input("How many module does the #" + str(i + 1) + " RMT have?\n   -> "))
        largest_product_variant *= module_number
        rmt_process_time_array[i] = [i for i in range(module_number)]
    if largest_product_variant >= int(product_variant_num):
        return rmt_process_time_array
    else:
        print("Your modules are not sufficient to produce " + str(product_variant_num) +
              "kinds of products. Please try again.")
        rmt_process_time_array = rmt_module_structure(product_variant_num, rmt_quantity)
        return rmt_process_time_array


def rmt_module_pdc_t_define_manual(rmt_process_time_array):
    for i in range(len(rmt_process_time_array)):
        module_buffer = []
        for j in range(len(rmt_process_time_array[i])):
            print("How many second will machine #" + str(i + 1) + " module #" + str(j + 1) + " cost?")
            module_buffer.append(float(aid.float_input(input("   -> "))))
        rmt_process_time_array[i] = module_buffer
    return rmt_process_time_array


def rmt_module_pdc_t_define_auto(rmt_process_time_array):
    for i in range(len(rmt_process_time_array)):
        module_buffer = []
        for j in range(len(rmt_process_time_array[i])):
            module_buffer.append(round(random.uniform(2, 12), 2))
        rmt_process_time_array[i] = module_buffer
    return rmt_process_time_array


def variant_limitation(module_array):
    largest_product_variant = 1
    for i in range(len(module_array)):
        largest_product_variant *= len(module_array[i])
    return largest_product_variant


def rmt_correction(module_list):
    module_correction_array = []
    module_length = len(module_list)
    for machine_num in range(1, module_length):
        module_correction_array.append(np.prod(module_list[machine_num:module_length]))
    module_correction_array.append(0)
    return module_correction_array


def last_seq(variant_seq, module_list):
    return variant_seq % module_list[len(module_list) - 1]


def current_machine_module_seq(variant_seq, module_list, module_correction, append_list):
    machine_num = len(append_list)
    total_rmt_num = len(module_list)
    for i in range(machine_num):
        variant_seq -= append_list[i] * module_correction[i]
    variant_seq //= (np.prod(module_list[machine_num + 1:total_rmt_num]))
    return variant_seq


def variant_module_identifier(module_list):
    module_correction = rmt_correction(module_list)
    variant_calling_modules = []
    for x in range(np.prod(module_list)):
        current_variant_module_identity = []
        for i in range(len(module_list) - 1):
            current_module_number = current_machine_module_seq(x, module_list, module_correction,
                                                               current_variant_module_identity)
            current_variant_module_identity.append(current_module_number)
        current_variant_module_identity.append(last_seq(x, module_list))
        variant_calling_modules.append(current_variant_module_identity)
    return variant_calling_modules


def variant_total_process_time_array(rmt_process_time_array, variant_calling_modules):
    variant_process_time_array = []
    for variant in range(len(variant_calling_modules)):
        variant_total_process_time = 0
        for machine_num in range(len(variant_calling_modules[variant])):
            module_num = variant_calling_modules[variant][machine_num]
            variant_total_process_time += rmt_process_time_array[machine_num][module_num]
        variant_process_time_array.append(variant_total_process_time)
    return variant_process_time_array


def variant_shuffle(product_variant_num, variant_general_process_time_array):
    if product_variant_num == len(variant_general_process_time_array):
        print("Your product variant reached RMS maximum customisation. Please check the production time list.")
        return variant_general_process_time_array
    elif product_variant_num > len(variant_general_process_time_array):
        sys.exit("\n\nThe product variant exceed the RMS capacity. \nThis error should not appear here. "
                 "\nCheck 'rmt_module_structure' function in RMS_Construction.py\nProgram terminated.")
    else:
        random.shuffle(variant_general_process_time_array)
        variant_process_time_array = variant_general_process_time_array[:product_variant_num]
        print("Your have " + str(product_variant_num) + " kinds of product.\nThis RMS can handle up to "
              + str(len(variant_general_process_time_array)) + " product variants.\n"
                                                               "Assigned variant production time randomly.")
        return variant_process_time_array


def variant_reconfigure_time(variant_num):
    variant_reconfigure_time_array = []
    for variant in range(variant_num):
        variant_reconfigure_time_array.append(random.randint(30, 300))
    return variant_reconfigure_time_array



