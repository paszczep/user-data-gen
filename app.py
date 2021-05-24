from sheet import AnswerSheet
from const import GEN_PROFILES, BUDGET_CLSS
from random import randint, randrange, gauss
import json
from const import TIME_FORMAT, FORM_QUESTIONS
from datetime import datetime, timedelta
import pandas as pd


def random_date(from_date, until_date):
    """
    This function will return a random datetime between two datetime objects.
    """
    delta = until_date - from_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)

    return from_date + timedelta(seconds=random_second)


def random_human_date(from_date, until_date):
    """
    This function will return a random datetime between two datetime objects.
    Normally distributed around hour given in the from_date + 3 HRS.
    """
    delta_days = (until_date - from_date).days
    random_days = randrange(delta_days)
    random_second = int(gauss(3*60*60, 3.5*60*60))
    delta = timedelta(days=random_days) + timedelta(seconds=random_second)
    return from_date + delta


def get_ordered_end_time_samples(
        n=1100,
        start='2021-02-06 12:00:00',
        end='2021-03-20 12:00:00'):
    starting_with = datetime.strptime(start, TIME_FORMAT)
    ending_with = datetime.strptime(end, TIME_FORMAT)
    samples = n

    times_list = []
    for example in range(samples):
        gen_date = random_human_date(
            starting_with,
            ending_with).strftime(TIME_FORMAT)
        times_list.append(gen_date)
    sorted_times_list = sorted(times_list, key=lambda x: x)
    return sorted_times_list


end_time_o_clocks = get_ordered_end_time_samples(n=5000)

i = 1
list_o_gen_samples = [FORM_QUESTIONS]
car_cost_class = pd.read_csv('all_cars_data.csv')

output_car_groups = {}

for end_time in end_time_o_clocks:
    random_profile = GEN_PROFILES[randint(0, len(GEN_PROFILES) - 1)]
    bob = AnswerSheet(random_profile, i, end_time, car_cost_class)
    if i < 7000:
        list_o_gen_samples.append(bob.answers)
    i += 1

    selected_body = bob.answers[29]
    selected_car = bob.answers[38]
    car_budget = bob.answers[10]

    # if random_profile not in output_car_groups:
    #     output_car_groups[random_profile] = {}
    #
    # if selected_body not in output_car_groups[random_profile]:
    #     output_car_groups[random_profile][selected_body] = {}
    #
    # if car_budget not in output_car_groups[random_profile][selected_body]:
    #     output_car_groups[random_profile][selected_body][car_budget] = []
    #
    # if selected_car not in output_car_groups[random_profile][selected_body][car_budget]:
    #     output_car_groups[random_profile][selected_body][car_budget].append(selected_car)

# result = {}
#
# for profile in output_car_groups:
#     result[profile] = {}
#     for body_type in output_car_groups[profile]:
#         result[profile][body_type] = {}
#         for value in BUDGET_CLSS.values():
#             if value not in output_car_groups[profile][body_type]:
#                 continue
#             result[profile][body_type][value] = output_car_groups[profile][body_type][value]
#
# output_car_groups = result

json_forms = "generated_data.json"
# json_groups = "generated_groups.json"

with open(json_forms, 'w') as outfile:
    json.dump(list_o_gen_samples, outfile)
#
# with open(json_groups, 'w') as outfile1:
#     json.dump(output_car_groups, outfile1)


