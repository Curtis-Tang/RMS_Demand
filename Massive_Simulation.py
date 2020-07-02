"""
This section is designed for massive simulation
"""

import random
import math
import numpy as np
import os
import sys
import copy
import Aid_Function_Blocks as aid
import RandomOrderGenerator as rog
import RMS_Construction as rms
import DML_Construction as dml
import Production_Simulation as pdc
import Profit_Calculation as pft


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


def data_generator(run_num,
                   product_variant_num,
                   rmt_quantity,
                   rmt_module_pdc_t_lower,
                   rmt_module_pdc_t_higher_scale,
                   variant_reconfigure_t_lower_scale,
                   variant_reconfigure_t_higher_scale,
                   time_span_day,
                   order_low_mean,
                   order_lar_mean_scale,

                   dml_process_shrinking_ratio_lower_bond,
                   dml_process_shrinking_ratio_upper_bond,
                   dml_layout_change_expanding_ratio_lower_bond,
                   dml_layout_change_expanding_ratio_upper_bond,
                   dml_min_batch_expand_ratio,
                   dml_stock_batch_ratio,
                   local_dir,
                   basic_dir):
    """
    This section is designed for massive simulation
    """

    """ -- Profit Define Section -- """
    profit_gain_grade = (2.5, 2, 1.5, 1.25, 1)
    profit_time_grade = (2.25, 3.38, 5.06, 7.59, 11.4)

    """ -- RMS Construction Section -- """
    file_dir = "-Run_" + str(run_num)
    basic_file_name = basic_dir + file_dir

    os.chdir(local_dir)
    try:
        os.mkdir(basic_dir)
        os.chdir(local_dir + "\\" + basic_dir)
    except:
        os.chdir(local_dir + "\\" + basic_dir)
    try:
        os.mkdir(basic_dir + file_dir)
        os.chdir(local_dir + "\\" + basic_dir + "\\" + basic_dir + file_dir)
    except:
        os.chdir(local_dir + "\\" + basic_dir + "\\" + basic_dir + file_dir)

    rmt_process_time_array = aid.sequence_list(rmt_quantity)
    largest_product_variant = int(1)
    for i in range(rmt_quantity):
        module_number = math.ceil(pow(product_variant_num, 1 / rmt_quantity))
        # module_number = random.randint(1, product_variant_num)
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

    """ -- Order Generation Section -- """
    time_span_second = time_span_day * 86400
    order_lar_mean = order_low_mean * order_lar_mean_scale
    order_expect_time = np.mean(rms_process_time_array) * ((order_low_mean + order_lar_mean) / 2)
    order_size = int(time_span_second / order_expect_time)
    order_list_original, variant_record = \
        rog.gen_random_order_list(order_size, time_span_second, product_variant_num, order_low_mean, order_lar_mean)
    basic_order_name = basic_file_name + "_Order_Original.csv"
    aid.csv_export(basic_order_name, order_list_original)

    for i in range(product_variant_num):
        variant_record[i].append(rms_process_time_array[i])
        variant_record[i].append(variant_reconfigure_time_array[i])

    variant_record_name = basic_file_name + "_Variant_Mean_Production.csv"
    aid.csv_export(variant_record_name, variant_record)

    """ -- RMS Production Section -- """
    rms_production_record = copy.deepcopy(order_list_original)
    rms_production_record = \
        pdc.rms_production(rms_production_record, rms_process_time_array,
                           variant_reconfigure_time_array, profit_time_grade)
    rms_production_record_name = basic_file_name + "_RMS_Production_Record.csv"
    aid.csv_export(rms_production_record_name, rms_production_record)

    """ -- DML Construction Section -- """

    dml_process_time_array = \
        dml.process_time_array(rms_process_time_array,
                               dml_process_shrinking_ratio_lower_bond, dml_process_shrinking_ratio_upper_bond)
    dml_layout_change_time = \
        dml.layout_reconfiguration_time(variant_reconfigure_time_array,
                                        dml_layout_change_expanding_ratio_lower_bond,
                                        dml_layout_change_expanding_ratio_upper_bond)
    dml_production_record = copy.deepcopy(order_list_original)
    dml_production_record, state_record = \
        pdc.dml_pull_production(dml_production_record, dml_process_time_array, dml_layout_change_time,
                                profit_time_grade, dml_min_batch_expand_ratio, dml_stock_batch_ratio)

    dml_production_record_name = basic_file_name + "_DML_Production_Record.csv"
    aid.csv_export(dml_production_record_name, dml_production_record)
    aid.csv_export(basic_file_name + "_DML_state_record.csv", state_record)

    """ -- Data Analysis Section -- """
    # RMS Profit Calculation
    rms_final_profit, rms_refuse_rate = \
        pft.profit_calculation(rms_production_record, time_span_second, profit_gain_grade, rms_process_time_array)

    # DML Profit Calculation
    dml_final_profit, dml_refuse_rate = \
        pft.profit_calculation(dml_production_record, time_span_second, profit_gain_grade, rms_process_time_array)

    configure_record = [
        ["Product Variant Number", product_variant_num],
        ["RMT Number", rmt_quantity],
        ["Lowest Module Production Time", rmt_module_pdc_t_lower],
        ["Highest Module Production Time", rmt_module_pdc_t_lower * rmt_module_pdc_t_higher_scale],
        ["Lowest RMS Reconfiguring Time", rmt_module_pdc_t_lower * variant_reconfigure_t_lower_scale],
        ["Highest RMS Reconfiguring Time",
         rmt_module_pdc_t_lower * rmt_module_pdc_t_higher_scale * variant_reconfigure_t_higher_scale],
        ["Simulation time", time_span_day],
        ["order_low_mean", order_low_mean],
        ["order_up_mean", order_low_mean * order_lar_mean_scale],
        ["dml_process_shrinking_ratio_lower_bond", dml_process_shrinking_ratio_lower_bond],
        ["dml_process_shrinking_ratio_upper_bond", dml_process_shrinking_ratio_upper_bond],
        ["dml_layout_change_expanding_ratio_lower_bond", dml_layout_change_expanding_ratio_lower_bond],
        ["dml_layout_change_expanding_ratio_upper_bond", dml_layout_change_expanding_ratio_upper_bond],
        ["dml_min_batch_expand_ratio", dml_min_batch_expand_ratio],
        ["dml_stock_batch_ratio", dml_stock_batch_ratio],
        [],
        ["RMS Refuse Rate", rms_refuse_rate],
        ["DML Refuse Rate", dml_refuse_rate],
        ["RMS Profit", rms_final_profit],
        ["DML Profit", dml_final_profit]
    ]
    # aid.csv_export(basic_file_name + "_Configure_Record.csv", configure_record)
    return rms_refuse_rate, dml_refuse_rate, rms_final_profit, dml_final_profit
