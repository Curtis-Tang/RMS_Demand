"""
Discrete Event Simulating RMS and DML
"""


def production_time_calculation(last_variant, variant, batch_size, production_time_array, variant_reconfiguring_time):
    if last_variant == variant:
        return batch_size * production_time_array[variant]
    else:
        return batch_size * production_time_array[variant] + variant_reconfiguring_time[variant]


def rms_production(order_list, production_time_array, variant_reconfiguring_time, profit_time_grade):
    remaining_production_time = 0
    last_variant = 0
    refused_order = 0
    # print(production_time_array)
    # print(variant_reconfiguring_time)
    for order in range(len(order_list)):
        order_production_time = production_time_calculation(last_variant, order_list[order][1], order_list[order][2],
                                                            production_time_array, variant_reconfiguring_time)
        order_list[order].append(order_production_time)
        # order_list[order].append(order_production_time * 7.59)
        # Record current order actual finish time
        if order == 0:
            order_list[order].append(order_list[0][0] + order_production_time)
            order_list[order].append(18)
        else:
            if order_list[order][0] >= order_list[order - 1][4]:
                order_list[order].append(order_list[order][0] + order_production_time)
                order_list[order].append(18)
            else:
                current_order_finish_time = order_list[order - 1][4] + order_production_time
                if current_order_finish_time - order_list[order][0] <= profit_time_grade[0] * order_production_time:
                    order_list[order].append(current_order_finish_time)
                    order_list[order].append(4)
                elif current_order_finish_time - order_list[order][0] <= profit_time_grade[1] * order_production_time:
                    order_list[order].append(current_order_finish_time)
                    order_list[order].append(3)
                elif current_order_finish_time - order_list[order][0] <= profit_time_grade[2] * order_production_time:
                    order_list[order].append(current_order_finish_time)
                    order_list[order].append(2)
                elif current_order_finish_time - order_list[order][0] <= profit_time_grade[3] * order_production_time:
                    order_list[order].append(current_order_finish_time)
                    order_list[order].append(1)
                else:
                    order_list[order].append(order_list[order - 1][4])
                    order_list[order].append(0)
                    refused_order += 1

    print("\nRefuse rate is " + str(refused_order / len(order_list) * 100) + "%.")
    return order_list