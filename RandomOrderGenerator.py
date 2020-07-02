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
import Aid_Function_Blocks as aid


def gen_uniform(lower_bond, upper_bond):
    uniform_buffer = round(random.uniform(lower_bond, upper_bond))
    return uniform_buffer


def gen_random_order_list(order_size, time_span_second, product_variant_num, smallest_mean, largest_mean):
    variant_count = aid.zero_list(product_variant_num)
    random_order_list = []
    mean = []
    batch_size = []
    variant_record = []

    for order_seq in range(order_size):
        random_order_list.append([random.randint(0, int(time_span_second)),  # Order time
                                  random.randint(0, product_variant_num - 1)])  # Order variant

    for order in range(len(random_order_list)):
        variant_count[random_order_list[order][1]] += 1

    for variant in range(product_variant_num):
        mean.append(random.randint(smallest_mean, largest_mean))

    for variant in range(len(mean)):
        batch_size.append(np.random.poisson(mean[variant], variant_count[variant]))
    batch_size_convert = []
    for variant in range(len(batch_size)):
        batch_size_convert.append(batch_size[variant].tolist())
    batch_size = batch_size_convert
    del batch_size_convert

    for order_seq in range(order_size):
        random_order_list[order_seq].append(batch_size[random_order_list[order_seq][1]][0])
        del batch_size[random_order_list[order_seq][1]][0]
    random_order_list = sorted(random_order_list)

    for variant in range(product_variant_num):
        variant_record.append([variant_count[variant], mean[variant]])

    return random_order_list, variant_record


