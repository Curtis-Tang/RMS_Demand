"""

This program could generate essential random data for an RMS include:
    1. Orders
    2. Product manufacturing planning
    3. Factory layout based on distance between machines
orders with part kinds, mean, and frequency

"""

# Modules Import
import random
import numpy as np
from tkinter import *


def gen_uniform(lower_bond, upper_bond):
    uniform_buffer = round(random.uniform(lower_bond, upper_bond))
    return uniform_buffer


def gen_random_order_list(order_size, time_span_second, product_variant_num, smallest_mean, largest_mean):
    mean = []
    batch_size = []
    for variant in range(product_variant_num):
        mean.append(random.randint(smallest_mean, largest_mean))

    for variant in range(len(mean)):
        batch_size.append(np.random.poisson(mean[variant], order_size))

    random_order_list = []
    for order_seq in range(order_size):
        random_order_list.append([random.randint(0, int(time_span_second)),  # Order time
                                  random.randint(0, product_variant_num - 1)])  # Order variant
        random_order_list[order_seq].append(batch_size[random_order_list[order_seq][1]][order_seq])
    random_order_list = sorted(random_order_list)
    return random_order_list


