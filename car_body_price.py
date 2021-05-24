import pandas as pd
from const import MAKE_BODY_MODELS

car_cost_class = pd.read_excel('car_classes.xlsx')

body_class = pd.DataFrame(columns=['make', 'model', 'class'])

for make in MAKE_BODY_MODELS:
    for body in MAKE_BODY_MODELS[make]:
        for model in MAKE_BODY_MODELS[make][body]:
            index = car_cost_class['car'].str.match(' '.join([make, model]))
            cost_class = car_cost_class['class'][index].values[0]
            car_category = ' '.join([body, str(cost_class)])
            body_class = body_class.append({'make': make, 'model': model, 'class': car_category}, ignore_index=True)

body_class.to_excel('car_body_classes.xlsx')



# ELEKTRYCZNE
