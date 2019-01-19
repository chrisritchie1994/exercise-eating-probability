import json

excersize_obj = [
    {"desc": "heavy_lift", "p": 0.1428},
    {"desc": "sprint", "p": 0.2850},
    {"desc": "light_lift", "p": 0.2850},
    {"desc": "just_normal", "p": 0.1436},
    {"desc": "yoga", "p": 0.1436}
]

next_num = 1
for obj in excersize_obj:
    obj['p_nums'] = [x for x in range(next_num, next_num + int(obj['p'] * 10000))]
    next_num = max(obj['p_nums']) + 1


json_day_obj = json.dumps(excersize_obj)

print(json_day_obj)