import json

three_day = 0.003
two_day = 0.011
one_day = 0.033
normal_day = 0.145
fast_day = 0.808

day_list = [three_day, two_day, one_day, normal_day, fast_day]

day_obj = [
    {"desc": "three_day_fast", "p": 0.003},
    {"desc": "two_day_fast", "p": 0.011},
    {"desc": "one_day_fast", "p": 0.033},
    {"desc": "normal_day", "p": 0.145},
    {"desc": "fast_day", "p": 0.808}
]

next_num = 1
for obj in day_obj:
    obj['p_nums'] = [x for x in range(next_num, next_num + int(obj['p'] * 1000))]
    next_num = max(obj['p_nums']) + 1


json_day_obj = json.dumps(day_obj)

print(json_day_obj)