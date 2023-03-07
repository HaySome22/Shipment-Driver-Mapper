import math
import sys

import numpy as np
from scipy.optimize import linear_sum_assignment

vowels = set('aeiou')


def calculate_ss(shipment, driver):
    shipment, driver = shipment.lower(), driver.lower()
    shipment_length, driver_length = len(shipment), len(driver)
    if shipment_length % 2 == 0:
        base_ss = sum([1.5 for c in driver if c in vowels])
    else:
        base_ss = sum([1 for c in driver if c not in vowels])
    if math.gcd(shipment_length, driver_length) > 1:
        return base_ss * 1.5
    else:
        return base_ss


def map_shipments_to_drivers(shipments, drivers):
    # Create a cost matrix and perform a maximum cost assignment
    num_shipments, num_drivers = len(shipments), len(drivers)
    cost_matrix = np.zeros((num_shipments, num_drivers))
    for i in range(num_shipments):
        for j in range(num_drivers):
            cost_matrix[i][j] = calculate_ss(shipments[i], drivers[j])
    _, col_ind = linear_sum_assignment(cost_matrix, maximize=True)

    # Create the optimal map from the assignment results
    shipment_driver_map = {}
    total_ss = 0
    for i in range(num_shipments):
        shipment_driver_map[shipments[i]] = drivers[col_ind[i]]
        total_ss += cost_matrix[i][col_ind[i]]
    return shipment_driver_map, total_ss


def format_and_print(shipment_driver_map, total_ss):
    for shipment, driver in shipment_driver_map.items():
        print(f"{shipment} -> {driver}")
    print(f"Total SS: {total_ss}")


if __name__ == '__main__':
    # todo validate inputs
    shipments, drivers = open(sys.argv[1]).read().splitlines(), open(sys.argv[2]).read().splitlines()
    format_and_print(*map_shipments_to_drivers(shipments, drivers))
