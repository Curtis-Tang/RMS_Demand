"""
This section is designed for massive simulation
"""

import Aid_Function_Blocks as aid


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


for i in range(5):
    pass
    # aid.csv_export()


rms_feature_summary = [[],[]]
rms_feature_summary[0] = []
rms_feature_summary[1] = []

aid.csv_export("test.csv", rms_feature_summary)