"""
This section is designed for massive simulation
"""

import random
import numpy as np
import RandomOrderGenerator as rog
import Aid_Function_Blocks as aid
import RMS_Construction as rms
import DML_Construction as dml
import Production_Simulation as pdc
import sys
from matplotlib import pyplot as plt


def rms_file_name_generation(rmt_module_number_list, time_span_day, order_size, order_low_mean, order_lar_mean):
    file_name = "RMS"
    # Record RMT number and module list
    file_name += "_" + str(len(rmt_module_number_list)) + "RMT"
    for machine in range(len(rmt_module_number_list)):
        file_name += "-" + str(rmt_module_number_list[machine])
    # Record order time, size, and batch size range
    file_name += "_O-T" + str(time_span_day) + "-S" + str(order_size)
    file_name += "-R" + str(order_low_mean) + "-" + str(order_lar_mean)
    file_name += ".csv"
    return file_name


print("\n\n\n")

""" -- Profit Define Section -- """
profit_gain_grade = (2.5,  2,    1.5,  1.25, 1,   0)
profit_time_grade = (2.25, 3.38, 5.06, 7.59, 11.4)

""" -- RMS Construction Section -- """
product_variant_num = 8
rmt_quantity = 3
rmt_module_pdc_t_lower = 5
rmt_module_pdc_t_higher_scale = 20
variant_reconfigure_t_lower_scale = 3
variant_reconfigure_t_higher_scale = 10
time_span_day = 365
order_low_mean = 30
order_lar_mean_scale = 30

basic_file_name = str(product_variant_num) + "-" + str(rmt_quantity) + "-" + str(rmt_module_pdc_t_lower) + "-" + \
                  str(rmt_module_pdc_t_higher_scale) + "-" + str(variant_reconfigure_t_lower_scale) + "-" + \
                  str(variant_reconfigure_t_higher_scale)

rmt_process_time_array = aid.sequence_list(rmt_quantity)
largest_product_variant = int(1)
for i in range(rmt_quantity):
    module_number = random.randint(1, product_variant_num)
    largest_product_variant *= module_number
    rmt_process_time_array[i] = [i for i in range(module_number)]
if largest_product_variant >= int(product_variant_num):
    del largest_product_variant
    pass
else:
    sys.exit("Module Number incorrect.")
rmt_module_number_list = rms.rmt_module_count(rmt_quantity, rmt_process_time_array)

for i in range(len(rmt_process_time_array)):
    module_buffer = []
    for j in range(len(rmt_process_time_array[i])):
        module_buffer.append(round(random.uniform(rmt_module_pdc_t_lower,
                                                  rmt_module_pdc_t_lower * rmt_module_pdc_t_higher_scale), 2))
    rmt_process_time_array[i] = module_buffer
variant_calling_modules = rms.variant_module_identifier(rmt_module_number_list)
variant_process_time_origin = rms.variant_total_process_time_array(rmt_process_time_array, variant_calling_modules)
'''Random pick manufacturing time'''
rms_process_time_array = rms.variant_shuffle(product_variant_num, variant_process_time_origin)
'''Reconfiguration time for each variant'''
variant_reconfigure_time_array = []
for variant in range(product_variant_num):
    variant_reconfigure_time_array.append(random.randint(variant_reconfigure_t_lower_scale,
                                                         variant_reconfigure_t_higher_scale) *
                                          rms_process_time_array[variant])
production_array = []
for i in range(product_variant_num):
    production_array.append([rms_process_time_array[i], variant_reconfigure_time_array[i]])

RMS_production_array_file_name = basic_file_name + "RMS_production_time_array.csv"
# aid.csv_export(RMS_production_array_file_name, production_array)

""" -- Order Generation Section -- """
time_span_second = time_span_day * 86400
order_lar_mean = order_low_mean * order_lar_mean_scale
order_expect_time = np.mean(rms_process_time_array) * ((order_low_mean + order_lar_mean) / 2)
order_size = int(time_span_second / order_expect_time)
order_list = rog.gen_random_order_list(order_size, time_span_second, product_variant_num,
                                       order_low_mean, order_lar_mean)
# print("Here is a random order list.")
# print(order_list)
#
# """
# RMS Production Section
# """
#
#
# production_record = pdc.rms_production(order_list, rms_process_time_array, variant_reconfigure_time_array,
#                                        profit_time_grade)
# print(production_record)
#
# """
# DML Construction Section
# """
#
# process_shrinking_ratio_lower_bond = 0.1
# process_shrinking_ratio_upper_bond = 0.5
# dml_process_time_array = dml.process_time_array(rms_process_time_array,
#                                                 process_shrinking_ratio_lower_bond, process_shrinking_ratio_upper_bond)
#
#
# """
# Data Analysis Section
# """