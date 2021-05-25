import answers
from const import TIME_FORMAT, MAKE_BODY_MODELS, BUDGET_CLSS, ELECTRIC_CAR_BODIES
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
        self.answers = {0: id_number,
                        1: get_start_time_str(end_time_str),
                        2: end_time_str,
                        3: str(),
                        4: str()}

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
            sel_car_mdls = [[brnd, mdl] for brnd in fav_brnds for mdl in MAKE_BODY_MODELS[brnd]['elektryczny']]
            if not sel_car_mdls:
                sel_car_mdls = [['Tesla', f'{mdl}'] for mdl in MAKE_BODY_MODELS['Tesla']['elektryczny']]
                self.answers[34].append('Tesla')
        else:
            sel_car_mdls = [[brnd, mdl] for brnd in fav_brnds for mdl in MAKE_BODY_MODELS[brnd][sel_body]]

        if not sel_car_mdls:
            sel_car_mdls = []
            car_body_class = car_class_cost
            budget_class = list(BUDGET_CLSS.keys())[list(BUDGET_CLSS.values()).index(self.answers[10])]
            selection_class = ' '.join([sel_body, str(budget_class)])
            for row in range(0, len(car_body_class)):
                if selection_class in car_body_class[['class']].loc[row].values:
                    sel_car_mdls.append(list(car_body_class[['make', 'model']].loc[row].values))

            if not sel_car_mdls:
                for row in range(0, len(car_body_class)):
                    if sel_body in car_body_class[['body']].loc[row].values:
                        sel_car_mdls.append(list(car_body_class[['make', 'model']].loc[row].values))
        try:
            self.answers[38] = choice(sel_car_mdls)
        except IndexError:
            print('IndexError', sel_body, list(BUDGET_CLSS.keys())[list(BUDGET_CLSS.values()).index(self.answers[10])])

        if self.answers[30] == 'elektryczny':
            for key in ELECTRIC_CAR_BODIES.keys():
                if self.answers[38][1] in ELECTRIC_CAR_BODIES[key]:
                    self.answers[29] = key

        fav_car = ' '.join(self.answers[38])
        fav_car_budget_class = int(car_class_cost['budget'][car_class_cost['car'].str.match(fav_car)].values[0])
        try:
            self.answers[10] = BUDGET_CLSS[fav_car_budget_class]
        except IndexError:
            print(f'IndexError: {fav_car}')

        # i_dunno_random = randint(0, 100)
        # if i_dunno_random == 0:
        #     self.answers[38] = str()
