import answers
from const import TIME_FORMAT, CAR_MAKE_BODY_MODELS, BUDGET_CLSS, ELECTRIC_CAR_BODIES
import pandas as pd
from random import choice
from random import gauss
from datetime import datetime
from datetime import timedelta


def get_start_time_str(
        end_time_str,
        min_dur=71,
        time_average=230,
        time_std_dev=199):
    end_time = datetime.strptime(end_time_str, TIME_FORMAT)
    start_time = end_time - timedelta(seconds=abs(gauss(time_average - min_dur, time_std_dev)) + min_dur)

    return start_time.strftime(TIME_FORMAT)


class AnswerSheet:

    def __init__(self, profile, id_number, end_time_str, car_class_cost):

        self.profile = profile
        self.answers = {0: id_number, 1: get_start_time_str(
            end_time_str), 2: end_time_str, 3: str(), 4: str()}

        for i in range(5, 41):
            func_name = f'question_{i}'
            func = getattr(answers, func_name)
            self.answers[i] = func(profile)

        nonull_pairs = [(13, 14), (16, 17), (18, 19), (20, 21)]

        for q1, q2 in nonull_pairs:
            if self.answers[q1] == 'nie':
                self.answers[q2] = []

        if not self.answers[30] == 'hybrydowy':
            self.answers[32] = str()

        fav_brnds = self.answers[34]
        sel_body = self.answers[29]
        if self.answers[30] == 'elektryczny':
            self.answers[31] = str()
            self.answers[33] = str()
            sel_car_mdls = [[brnd, mdl] for brnd in fav_brnds for mdl in CAR_MAKE_BODY_MODELS[brnd]['elektryczny']]
            if not sel_car_mdls:
                sel_car_mdls = [['Tesla', f'{mdl}'] for mdl in CAR_MAKE_BODY_MODELS['Tesla']['elektryczny']]
                self.answers[34].append('Tesla')
        else:
            sel_car_mdls = [[brnd, mdl] for brnd in fav_brnds for mdl in CAR_MAKE_BODY_MODELS[brnd][sel_body]]

        if not sel_car_mdls:
            sel_car_mdls = []
            car_body_class = pd.read_excel('car_body_classes.xlsx')
            for row in range(0, len(car_body_class)):
                if 'sedan 1' in car_body_class[['class']].loc[row].values:
                    sel_car_mdls.append(list(car_body_class[['make', 'model']].loc[row].values))

        self.answers[38] = choice(sel_car_mdls)

        if self.answers[30] == 'elektryczny':
            for key in ELECTRIC_CAR_BODIES.keys():
                if self.answers[38][1] in ELECTRIC_CAR_BODIES[key]:
                    self.answers[29] = key

        fav_car = ' '.join(self.answers[38])
        fav_car_budget_class = car_class_cost['class'][car_class_cost['car'].str.match(fav_car)].values
        try:
            self.answers[10] = BUDGET_CLSS[int(fav_car_budget_class[0])]
        except IndexError:
            print(f'IndexError: {fav_car}')

