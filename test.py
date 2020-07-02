import numpy as np
import matplotlib.pyplot as plt
import DML_Construction as dml
import os
import csv
import pickle
import Aid_Function_Blocks as aid
import Production_Simulation as pdc
import Profit_Calculation as pft
import Massive_Simulation as ms
from mpl_toolkits.mplot3d import Axes3D

print("Here we are\n\n")

run_num = 5000

product_variant_num = 3
rmt_quantity = 3
rmt_module_pdc_t_lower = 5
rmt_module_pdc_t_higher_scale = 20
variant_reconfigure_t_lower_scale = 3
variant_reconfigure_t_higher_scale = 10
time_span_day = 548
order_low_mean = 30
order_lar_mean_scale = 30

dml_process_shrinking_ratio_lower_bond = 0.1
dml_process_shrinking_ratio_upper_bond = 0.5
dml_layout_change_expanding_ratio_lower_bond = 5
dml_layout_change_expanding_ratio_upper_bond = 20
dml_min_batch_expand_ratio = 2
dml_stock_batch_ratio = 2

local_dir = 'D:\\OneDrive - Cranfield University\\Works\\RMS Demand Fluctuation Research\\Data'
basic_dir = str(product_variant_num) + "-" + str(rmt_quantity) + "-" + str(rmt_module_pdc_t_lower) + "-" + \
            str(rmt_module_pdc_t_higher_scale) + "-" + str(variant_reconfigure_t_lower_scale) + "-" + \
            str(variant_reconfigure_t_higher_scale)

profit_summary = []
profit_record = []
for run_num in range(run_num):
    print(basic_dir + " Run " + str(run_num) + "\n")
    """ rms_refuse_rate - a1; dml_refuse_rate - b1; rms_final_profit - a2; dml_final_profit - b2 """
    a1, b1, a2, b2 = ms.data_generator(run_num,
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
                                       basic_dir)
    profit_record.append([a1, b1, a2, b2])
rms_profit_average, dml_profit_average, rms_refuse_average, dml_refuse_average, advance_probability = \
    pft.profit_summarising(profit_record)
profit_summary.append([basic_dir, rms_profit_average, dml_profit_average,
                       rms_refuse_average, dml_refuse_average, advance_probability])
os.chdir(local_dir)
print(profit_summary)
# aid.csv_export("Profit Summary.csv", profit_summary)
os.chdir(local_dir + "\\" + basic_dir)
aid.csv_export(basic_dir + " Profit Record.csv", profit_record)


