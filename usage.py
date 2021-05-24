import csv
import json
import pandas as pd
import random
from random import gauss
import time
from const import BUDGET_CLSS
from operation import Operation

beginning = time.perf_counter()

input_file = "generated_data.json"

with open(input_file, 'r') as base_data:
    foundation = json.load(base_data)

    # val_list = list(BUDGET_CLSS.values())

    CAR_BODY_CLASS = pd.read_csv('all_cars_data.csv')

    # total_operations = DataFrame(columns=['user', 'operation_type', 'duration', 'car_make',
    #                                       'car_model', 'car_body', 'price_point'])

    with open('total_operations.csv', 'w', newline='') as target_csv:
        csv_columns = ['id', 'operation_type', 'duration', 'car_make', 'car_model', 'car_body', 'price_point']
        writer = csv.DictWriter(target_csv, fieldnames=csv_columns)
        writer.writeheader()

        j = 0
        for element in foundation[1:]:

            all_seen_cars = []
            all_price_check_cars = []
            all_investigated_cars = []

            wanted_body = element['29']
            budget = list(BUDGET_CLSS.keys())[list(BUDGET_CLSS.values()).index(element['10'])]
            body_price = ' '.join([wanted_body, str(budget)])

            number = random.randint(2, 5)

            for n in range(1, number + 1):

                # user sees cars of the same body type he wants
                seen_cars = []
                for i in range(len(CAR_BODY_CLASS)):
                    if wanted_body in CAR_BODY_CLASS['class'][i]:
                        car_make = CAR_BODY_CLASS['make'][i]
                        car_model = CAR_BODY_CLASS['model'][i]
                        car_class = CAR_BODY_CLASS['class'][i]
                        seen_cars.append([car_make, car_model, car_class])
                sample_size = random.randint(int(0.2 * len(seen_cars)), int(0.8 * len(seen_cars)))
                seen_cars = random.sample(seen_cars, sample_size)
                all_seen_cars += seen_cars

                # user checks price of seen cars of price point +/- 1
                price_check_cars = []
                for i in range(len(seen_cars)):
                    car_cls = int(seen_cars[i][2][-1])
                    if car_cls == budget or car_cls == budget - 1 or car_cls == budget + 1:
                        price_check_cars.append(seen_cars[i])
                all_price_check_cars += price_check_cars

                # user further investigates cars of interest
                investigated_cars = []
                for i in range(len(price_check_cars)):
                    car_mk = price_check_cars[i][0].split()[0]
                    if car_mk in element['34']:
                        investigated_cars.append(price_check_cars[i])
                all_investigated_cars += investigated_cars

            chosen_vehicle = [element['38'][0], element['38'][1], ' '.join([wanted_body, str(budget)])]

            all_seen_cars.insert(0, chosen_vehicle)
            all_price_check_cars.insert(0, chosen_vehicle)
            all_investigated_cars.insert(0, chosen_vehicle)

            seen_times = []
            for i in range(len(all_seen_cars)):
                t = abs(gauss(0.6, 0.6)) + 0.8
                seen_times.append(t)
            seen_times = sorted(seen_times)[::-1]
            i = 0
            for tile in all_seen_cars:
                bob = Operation(element['0'], 'listed', seen_times[i], tile[0], tile[1],
                                tile[2].split(' ')[0], tile[2].split(' ')[1])
                i += 1
                writer.writerow(bob.print_operation())
                # total_operations = pd.concat([pd.DataFrame(bob.print_operation(), index=[j]), total_operations])
                # j += 1

            price_times = []
            for i in range(len(all_price_check_cars)):
                t = abs(gauss(5, 0.6)) + 0.75
                price_times.append(t)
            price_times = sorted(price_times)[::-1]
            i = 0
            for tile in all_price_check_cars:
                bob = Operation(element['0'], 'payment-details', price_times[i], tile[0], tile[1],
                                tile[2].split(' ')[0], tile[2].split(' ')[1])
                i += 1
                writer.writerow(bob.print_operation())
                # total_operations = pd.concat([pd.DataFrame(bob.print_operation(), index=[j]), total_operations])
                # j += 1
            details_times = []
            for i in range(len(all_seen_cars)):
                t = abs(gauss(10, 3)) + 5
                details_times.append(t)
            details_times = sorted(details_times)[::-1]
            i = 0
            for tile in all_seen_cars:
                bob = Operation(element['0'], 'car-details', details_times[i], tile[0], tile[1], tile[2].split(' ')[0],
                                tile[2].split(' ')[1])
                i += 1
                writer.writerow(bob.print_operation())
                # total_operations = pd.concat([pd.DataFrame(bob.print_operation(), index=[j]), total_operations])
                # j += 1

# total_operations.to_csv('total_operations.csv')

conclusion = time.perf_counter()

print('elapsed [min]: ', (conclusion - beginning)/60)
