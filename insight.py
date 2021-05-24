import json

with open('generated_data.json', 'r') as gen_data:
    data = json.load(gen_data)

    for sheet in data:
        print(sheet['10'])
        print(sheet['29'])
        print(sheet['34'])
        print(sheet['38'])
