import pandas as pd

table = pd.read_excel('car_body_classes.xlsx')

table = table[['make', 'model', 'class']]

table['car'] = [' '.join([table['make'][i], table['model'][i]]) for i in range(len(table))]
table[['body', 'budget']] = [table['class'][i].split(' ') for i in range(len(table))]

table.to_csv('all_cars_data.csv')
