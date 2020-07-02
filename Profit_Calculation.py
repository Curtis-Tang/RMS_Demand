"""
This section calculate the profit
"""


def dml_profit_identify(order_list, profit_time_grade):
    """
    Assign profit grade according to lead time
    :param order_list:
    :param profit_time_grade:
    :return:
    """
    total_grade = len(profit_time_grade)
    for order in range(len(order_list)):
        if order_list[order][4] != -1:
            # Calculate lead-time
            lead_time = order_list[order][4] - order_list[order][0]
            order_list[order][-1] = lead_time
            for grade in range(total_grade):
                if lead_time <= profit_time_grade[grade] * order_list[order][3]:
                    order_list[order][-2] = total_grade - grade
                    break
                else:
                    order_list[order][-2] = 0
    return order_list


def rms_profit_identify(order_production_time, order_time, current_order_finish_time, profit_time_grade):
    for grade in range(len(profit_time_grade)):
        if current_order_finish_time - order_time <= profit_time_grade[grade] * order_production_time:
            return len(profit_time_grade) - grade
    return 0


def profit_calculation(order_list, simulation_time, profit_gain_grade, rms_process_time_array):
    profit_grade = len(profit_gain_grade)
    refuse_order = 0
    effective_order = 0
    total_profit = 0
    for order in range(len(order_list)):
        # Skip first 3 months
        if order_list[order][0] < 7884000:
            continue
        # Ignore last 3 months
        elif order_list[order][0] > simulation_time - 7884000:
            break
        elif order_list[order][5] <= 0:
            refuse_order += 1
            effective_order += 1
        else:
            effective_order += 1
            # Variant unit profit produce rate * batch size * emphasise rate
            current_order_profit = rms_process_time_array[order_list[order][1]]
            current_order_profit *= order_list[order][2]
            current_order_profit *= profit_gain_grade[int(profit_grade - order_list[order][5])]
            total_profit += current_order_profit
    total_profit /= 1_000_000
    refuse_rate = refuse_order / effective_order * 100
    return total_profit, refuse_rate


def profit_summarising(profit_record):
    """
    rms_refuse_rate - P0;
    dml_refuse_rate - P1;
    rms_final_profit - P2;
    dml_final_profit - P3 """
    sample_size = len(profit_record)
    rms_profit_average = 0
    dml_profit_average = 0
    rms_refuse_average = 0
    dml_refuse_average = 0
    advance_probability = 0
    for record in range(sample_size):
        rms_profit_average += profit_record[record][0]
        dml_profit_average += profit_record[record][1]
        rms_refuse_average += profit_record[record][2]
        dml_refuse_average += profit_record[record][3]
        if profit_record[record][0] > profit_record[record][1]:
            advance_probability += 1
    rms_refuse_average /= sample_size
    dml_profit_average /= sample_size
    rms_refuse_average /= sample_size
    dml_refuse_average /= sample_size
    advance_probability /= sample_size
    return rms_profit_average, dml_profit_average, rms_refuse_average, dml_refuse_average, advance_probability * 100
