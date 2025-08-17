import numpy as np
import operator


def calculate_cost(periodd, option):
    """
    Apply tariff logic based on selected option.
    option=0: Domestic, option=1: Commercial, option=2: Industrial
    Returns cost breakdown and totals.
    """
    values = periodd.values
    matrix = np.concatenate([values])
    m, n = periodd.shape

    sum_val = 0
    cost = 0
    details = {}
    highesttime = None
    highestdemand = None
    tcost = 0
    tsum = 0

    # Domestic Tariff
    if option == 0:
        # Simplified demo version – extend as needed
        sum_val = matrix[:, 1].sum()
        cost = sum_val * 0.218
        details["blocks"] = [["All kWh", str(round(sum_val)), "0.218", str(round(cost, 2))]]

    # Commercial Tariff
    elif option == 1:
        sum_val = matrix[:, 1].sum()
        cost = sum_val * 0.435
        details["blocks"] = [["All kWh", str(round(sum_val)), "0.435", str(round(cost, 2))]]

    # Industrial Tariff
    elif option == 2:
        values = periodd.values
        Output = max(values, key=operator.itemgetter(1))
        highesttime = Output[0]
        highestdemand = Output[1]

        sum_val = matrix[:, 1].sum()
        cost = sum_val * 0.336
        tcost = cost + round(highestdemand) * 23.70
        tsum = round(highestdemand) + sum_val

        details["blocks"] = [
            ["All kWh", str(round(sum_val)), "0.336", str(round(cost, 2))],
            ["Maximum Demand Charge", str(round(highestdemand)), "23.70", str(round(highestdemand * 23.70, 2))],
        ]
        details["highest"] = (highesttime, highestdemand)

    return cost, tcost, tsum, details
