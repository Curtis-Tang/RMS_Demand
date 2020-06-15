"""
Derive a DML in this section
"""

import random


def process_time_array(rms_variant_process_time_array, shrinking_ratio_lower_bond, shrinking_ratio_upper_bond):
    for i in range(len(rms_variant_process_time_array)):
        rms_variant_process_time_array[i] *= random.uniform(shrinking_ratio_lower_bond, shrinking_ratio_upper_bond)
    return rms_variant_process_time_array


def layout_reconfiguration_time(dml_process_time_array, cfg_time_lower_bond, cfg_time_upper_bond):
    for i in range(len(dml_process_time_array)):
        dml_process_time_array[i] = random.uniform(cfg_time_lower_bond, cfg_time_upper_bond)
    return dml_process_time_array
