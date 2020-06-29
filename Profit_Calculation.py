"""
This section calculate the profit
"""


def profit_clarify(order_list, profit_time_grade):
    """
    Assign profit grade according to lead time
    :param order_list:
    :param profit_time_grade:
    :return:
    """
    total_grade = len(profit_time_grade)
    for order in range(len(order_list)):
        if order_list[order][-1] != -1 or order_list[order][-2] != 0:
            pass
    return order_list


def profit_calculation(order_list, profit_gain_grade):
    pass

