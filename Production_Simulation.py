"""
Discrete Event Simulating RMS and DML
"""

import sys
import Aid_Function_Blocks as aid
import DML_Construction as dml


def production_time_calculation(last_variant, variant, batch_size, production_time_array, variant_reconfiguring_time):
    if last_variant == variant:
        return batch_size * production_time_array[variant]
    else:
        return batch_size * production_time_array[variant] + variant_reconfiguring_time[variant]


def order_queue_production_check(stock_standard, request_stock, min_batch):
    """ Abandoned """
    for variant in range(len(stock_standard)):
        request = request_stock[variant][0]
        if request + stock_standard[variant] - request_stock[variant][1] >= min_batch[variant]:
            return True
    return False


def order_queue_prior_variant(order_queue, stock_standard, request_stock, min_batch):
    """ Return the first variant in queue achieved manufacturing minimum batch.
    Return false when there is not queuing order trigger manufacturing process.
    """
    for variant_in_queue in range(len(order_queue)):
        variant = order_queue[variant_in_queue][1]
        request = request_stock[variant][0]
        if request + stock_standard[variant] - request_stock[variant][1] < min_batch[variant]:
            pass
        else:
            return variant
    return False


def rms_production(order_list, production_time_array, variant_reconfiguring_time, profit_time_grade):
    # remaining_production_time = 0
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
            order_list[order].append(4)
        else:
            if order_list[order][0] >= order_list[order - 1][4]:
                order_list[order].append(order_list[order][0] + order_production_time)
                order_list[order].append(4)
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


def dml_pull_production(order_list, production_time_array, variant_reconfiguring_time, profit_time_grade,
                        min_batch_expand_ratio, stock_batch_ratio):
    min_batch = dml.min_batch(production_time_array, variant_reconfiguring_time, min_batch_expand_ratio)
    stock_standard, request_stock = dml.pull_dml_stock_initialise(min_batch, stock_batch_ratio)
    order_queue = []
    #  Machine state contains [current variant configure, system free up time point]
    system_state = [0, 0]
    system_idle_time = 0

    # print(min_batch)
    # print("Stock standards are ", stock_standard)
    # print(request_stock)
    for order in range(len(order_list)):
        """ Test Section """
        # print("Step " + str(order))
        # print(request_stock)
        # print(order_queue)
        # print(system_state)
        # print(system_idle_time)
        order_variant = order_list[order][1]
        """ Check system availability before dealing the current order"""
        if system_state[1] < order_list[order][0]:

            # When order in queue worth dealing
            while dealing_variant := order_queue_prior_variant(order_queue, stock_standard, request_stock, min_batch):
                # Extra the first 'worth-dealing' queues from
                dealing_queue, order_queue = go_production(dealing_variant, order_queue)
                system_state[1] += variant_reconfiguring_time[dealing_variant]
                # Update current variant and add layout adjustment time to the system state
                system_state[0] = dealing_variant
                system_state[1] += variant_reconfiguring_time[dealing_variant]
                for dealing_orders in range(len(dealing_queue)):
                    # Calculate the current order finish time, update system state and record deliver time
                    production_time = production_time_calculation(dealing_variant, dealing_variant,
                                                                  dealing_queue[dealing_orders][2],
                                                                  production_time_array, variant_reconfiguring_time)
                    #  Theory production time
                    # order_list[dealing_queue[dealing_orders][1]][3] = production_time
                    system_state[1] += production_time
                    # Actual deliver time
                    order_list[dealing_queue[dealing_orders][1]][4] = \
                        system_state[1]
                    # Record lead time
                    order_list[dealing_queue[dealing_orders][1]][6] = \
                        system_state[1] - order_list[dealing_queue[dealing_orders][1]][0]
                del dealing_queue
                # Replenish the stocks
                # A logic breach here if a same variant order come but it should not effect the result significant
                system_state[1] += production_time_calculation(dealing_variant, dealing_variant,
                                                               stock_standard[dealing_variant]
                                                               - request_stock[dealing_variant][1],
                                                               production_time_array, variant_reconfiguring_time)
                request_stock[dealing_variant] = [0, stock_standard[dealing_variant]]
                print(request_stock)
                # Stop dealing order queue when new order come in before finish
                if system_state[1] > order_list[order][0]:
                    break
                # Exit if there is not worth dealing variant
                if not order_queue_prior_variant(order_queue, stock_standard, request_stock, min_batch):
                    break

        if system_state[1] < order_list[order][0]:
            # Record idle time when system finished all previous order. Update system free-up time point.
            system_idle_time += order_list[order][0] - system_state[1]
            system_state[1] = order_list[order][0]

        """ Current order volume interact with accumulate request(s) and stock """
        # When stock can satisfy current order request
        if order_list[order][2] <= request_stock[order_variant][1]:
            # Remove stock
            request_stock[order_variant][1] -= order_list[order][2]
            # Record theory production time - P3
            production_time = production_time_calculation(order_variant, order_variant,
                                                          order_list[order][2],
                                                          production_time_array, variant_reconfiguring_time)
            order_list[order].append(production_time)
            # Actual finish time equals to order arrive time - P4
            order_list[order].append(order_list[order][0])
            # Profit grade occupation - P5
            order_list[order].append(-1)
            # Lead time equals to 0 - P6
            order_list[order].append(0)
            # Insert to a queue if configure is match
            if order_variant == system_state[0]:
                system_delay = production_time
                system_state[1] += system_delay
                order_queue = queue_delay(order_queue, system_delay)
                order_queue, request_stock = queue_exit(order_queue, request_stock)

        # When stock is insufficient
        else:
            # Record theoretical production time - P3
            production_time = production_time_calculation(order_variant, order_variant,
                                                          order_list[order][2],
                                                          production_time_array, variant_reconfiguring_time)
            order_list[order].append(production_time)
            # Actual finish time pending - P4
            order_list[order].append(-1)
            # Profit grade occupation - P5
            order_list[order].append(-1)
            # Lead time pending - P6
            order_list[order].append(-1)
            # Insert to a queue if configure is correct
            if order_variant == system_state[0]:
                system_delay = production_time
                system_state[1] += system_delay
                order_queue = queue_delay(order_queue, system_delay)
                order_queue, request_stock = queue_exit(order_queue, request_stock)
            else:
                """ If the order could possibly finish before latest deadline, add current order 
                to queue with [
                1: order number, 
                2: variant, 
                3: batch size, 
                4: best estimation, and 
                5: worst estimation]."""
                best_estimation = system_state[1] + production_time
                worst_estimation = order_list[order][0] \
                                   + variant_reconfiguring_time[order_variant] \
                                   + request_stock[order_variant][0] * production_time_array[order_variant] \
                                   + production_time * profit_time_grade[-1]
                if system_state[1] <= worst_estimation:
                    order_queue.append([order, order_variant, order_list[order][2], best_estimation, worst_estimation])
    # print("The system idled " + str(system_idle_time) + " seconds")
    # aid.csv_export("Queue.csv", order_queue)
    print(order_queue)
    return order_list


def dml_push_production(order_list, production_time_array, variant_reconfiguring_time, profit_time_grade,
                        min_batch_expand_ratio, stock_batch_ratio):
    pass


def go_production(variant, queue):
    next_variant_orders = []
    for queue_order in range(len(queue) - 1, -1, -1):
        if queue[queue_order][1] == variant:
            next_variant_orders.append(queue[queue_order])
            del (queue[queue_order])
        else:
            pass
    next_variant_orders.reverse()
    return next_variant_orders, queue


def queue_exit(queue, request_stock):
    for queue_order in range(len(queue) - 1, -1, -1):
        if queue[queue_order][3] > queue[queue_order][4]:
            # Remove request
            request_stock[queue[queue_order][1]][0] -= queue[queue_order][2]
            del (queue[queue_order])
        else:
            pass
    return queue, request_stock


def queue_delay(queue, delay_time):
    for queue_order in range(len(queue)):
        queue[queue_order][3] += delay_time
    return queue
