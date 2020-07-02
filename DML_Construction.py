"""
Derive a DML in this section
"""

import random
import sys
import Aid_Function_Blocks as aid


def process_time_array(rms_variant_process_time_array, shrinking_ratio_lower_bond, shrinking_ratio_upper_bond):
    for i in range(len(rms_variant_process_time_array)):
        rms_variant_process_time_array[i] *= random.uniform(shrinking_ratio_lower_bond, shrinking_ratio_upper_bond)
    return rms_variant_process_time_array


def layout_reconfiguration_time(variant_reconfigure_time_array, cfg_time_lower_bond, cfg_time_upper_bond):
    for variant in range(len(variant_reconfigure_time_array)):
        variant_reconfigure_time_array[variant] *= random.uniform(cfg_time_lower_bond, cfg_time_upper_bond)
    return variant_reconfigure_time_array


def min_batch(production_time_array, variant_reconfiguring_time, expand_ratio):
    min_batch_list = []
    try:
        for variant in range(len(production_time_array)):
            min_batch_list.append(int(variant_reconfiguring_time[variant]
                                      * expand_ratio // production_time_array[variant]))
        return min_batch_list
    except Exception:
        sys.exit("\nSome errors occurred in DML minimum batch definition.")


def pull_dml_stock_initialise(minimum_batch, stock_batch_ratio):
    """ Return standard stock level and queuing&stocking recorder """
    stock_standard = aid.empty_list(len(minimum_batch))
    for variant in range(len(minimum_batch)):
        stock_standard[variant] = minimum_batch[variant] * stock_batch_ratio

    request_stock = aid.empty_list(len(stock_standard))
    for variant in range(len(stock_standard)):
        request_stock[variant] = [0]
        request_stock[variant].append(stock_standard[variant])
    return stock_standard, request_stock


def update_variant_waiting_priority(waiting_list):
    """ Move the highest priority variant to the end """
    variant_kind = len(waiting_list)
    current_dealing_variant = aid.min_location(waiting_list)
    for variant in range(variant_kind):
        waiting_list[variant][0] -= 1
    waiting_list[current_dealing_variant][0] += variant_kind
    return waiting_list



