"""

Coded by TJC

"""

print("---------------------------------------")
print("\nThis program is designed for researching order on reconfigurable manufacturing system.\n")
print("---------------------------------------")
print("\nNow let's set some basic parameter this RMS.\n")

import random
import RandomOrderGenerator as rog
import Aid_Function_Blocks as aid
import RMS_Construction as rms
import numpy as np

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
variant_general_process_time_array = rms.variant_shuffle(product_variant_num, variant_process_time_origin)
print(variant_general_process_time_array)
'''Reconfiguration time for each variant'''
variant_reconfigure_time_array = rms.variant_reconfigure_time(len(variant_general_process_time_array))
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
# # RMS Summary
#
# print(order_size)
# aid.mean_print(mean)
# aid.boundary_print(order_lower_bond, order_upper_bond)

# # Manufacturing Process List
# manufacturing_process_kind = ['Cut', 'Mill', 'Bore', 'Drill', 'Turn']
# manufacturing_process_weight = [100, 50, 35, 15, 100]
#
# # order_sequence = [i for i in range(1, order_size + 1)]
# # print(order_sequence)
# # product_variant = [random.randint(1, product_variant_num) for i in range(0, order_size)]
# # print(product_variant)
# #
# # combined_order = order_sequence
# # for i in range(order_size):
# #     combined_order[i] = {'Sequence': order_sequence[i], 'Variant': product_variant[i]}
# # print(combined_order)
#
# # for i in range(10):
# #     test = RandomComponentGenerator.gen_uniform(lower_bond, upper_bond)
# #     print(test)
# #     i += 1
# #
# #
# # product_plan = random.choices(RandomComponentGenerator.manufacturing_process_kind,
# #                               RandomComponentGenerator.manufacturing_process_weight, k=10)
# # print(product_plan)

production_record = rms.rms_production(order_list, variant_general_process_time_array, variant_reconfigure_time_array)
print(production_record)


"""
Data Analysis Section
"""
