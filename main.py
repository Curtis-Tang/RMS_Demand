"""

Coded by TJC

"""

print("---------------------------------------")
print("\nThis program is designed for researching order on reconfigurable manufacturing system.\n")
print("---------------------------------------")
print("\nNow let's set some basic parameter this RMS.\n")

import random
import numpy as np
import RandomOrderGenerator as rog
import Aid_Function_Blocks as aid
import RMS_Construction as rms
import DML_Construction as dml
import Production_Simulation as pdc


"""
Profit Define Section
"""
profit_gain_grade = (2.5,  2,    1.5,  1.25, 1,   0)
print(len(profit_gain_grade))
profit_time_grade = (2.25, 3.38, 5.06, 7.59, 11.4)

""" 
RMS Construction Section
"""
product_variant_num = aid.integer_input(input("How many kinds of product are you going to produce? \n   -> "))
print("OK. This RMS is going to handle " + str(product_variant_num) + " kinds of product.\n")

''' Reconfigurable machine tool production array definition. '''
print("Reconfigurable Machine Tools (RMT) are the key elements in RMS system.")

''' Build RMT production array '''
rmt_quantity = aid.integer_input(input("How many RMT in this RMS?\n   -> "))
print("OK. This RMS has " + str(rmt_quantity) + " RMTs.\n")
''' An empty process time matrix '''
rmt_process_time_array = rms.rmt_module_structure(product_variant_num, rmt_quantity)
rmt_module_number_list = rms.rmt_module_count(rmt_quantity, rmt_process_time_array)
# print(rmt_module_number_list)

''' Add values to process time matrix '''
print("\nNow let's define production time for each module. The unit is seconds.")
# rmt_process_time_array = rms.rmt_module_pdc_t_define_manual(rmt_process_time_array)
rmt_process_time_array = rms.rmt_module_pdc_t_define_auto(rmt_process_time_array)
# print(rmt_process_time_array)

variant_calling_modules = rms.variant_module_identifier(rmt_module_number_list)
# print(variant_calling_modules)

'''Manufacturing time for all variant'''
variant_process_time_origin = rms.variant_total_process_time_array(rmt_process_time_array, variant_calling_modules)
'''Random pick manufacturing time'''
rms_process_time_array = rms.variant_shuffle(product_variant_num, variant_process_time_origin)
print(rms_process_time_array)
'''Reconfiguration time for each variant'''
variant_reconfigure_time_array = rms.variant_reconfigure_time(len(rms_process_time_array))
print("\nRandomly assigned variant reconfiguring time.")
print(variant_reconfigure_time_array)

# largest_product_variant = rms.variant_limitation(rmt_process_time_array)
# print(largest_product_variant)

""" 
Order Generation Section
"""

time_span_day = aid.float_input(input("\nHow many days will orders pop up after RMS start working? \n   -> "))
# print(time_span_day)
time_span_second = time_span_day * 86400
# print(time_span_second)
order_size = aid.integer_input(input("How many orders could pop up during this period? \n   -> "))
print("OK. This RMS is going to handle " + str(order_size) + " orders in total.\n")

order_low_mean = aid.integer_input(input("Please enter your variant lowest mean: \n   -> "))
order_lar_mean = aid.integer_input(input("Please enter your variant largest mean: \n   -> "))
order_list = rog.gen_random_order_list(order_size, time_span_second, product_variant_num,
                                       order_low_mean, order_lar_mean)
print("Here is a random order list.")
print(order_list)

"""
RMS Production Section
"""


production_record = pdc.rms_production(order_list, rms_process_time_array, variant_reconfigure_time_array,
                                       profit_time_grade)
print(production_record)

"""
DML Construction Section
"""

process_shrinking_ratio_lower_bond = 0.1
process_shrinking_ratio_upper_bond = 0.5
dml_process_time_array = dml.process_time_array(rms_process_time_array,
                                                process_shrinking_ratio_lower_bond, process_shrinking_ratio_upper_bond)


"""
Data Analysis Section
"""
