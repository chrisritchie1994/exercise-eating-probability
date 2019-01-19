import json
import random
import datetime

with open("exercise_probability.json") as f:
    exercise_prob = json.load(f)

with open("eating_style_probability.json") as f:
    eating_style_prob = json.load(f)

with open("fast_probability.json") as f:
    fast_prob = json.load(f)

with open("dietary_style_probability.json") as f:
    dietary_style_prob = json.load(f)


class Day:
    def __init__(self, eating_style=None, dietary_style=None, end_date=None, fast_duration=None, exercise_style=None):
        self.created_date = datetime.date.today()
        self.eating_style = eating_style
        self.dietary_style = dietary_style
        self.end_date = end_date
        self.fast_duration = fast_duration
        self.exercise_style = exercise_style

    def determine_exercise_style(self):
        rand = random.randint(1, 10000)
        for obj in exercise_prob:
            if obj['p_nums'][0] <= rand <= obj['p_nums'][1]:
                self.exercise_style = obj['desc']
        self.exercise_style = None  # used prior to 110kg, when < 110kg will include new exercise style

    def determine_eating_style(self):
        rand = random.randint(1, 1000)
        for obj in eating_style_prob:
            if obj['p_nums'][0] <= rand <= obj['p_nums'][1]:
                self.eating_style = obj['desc']

    def set_end_date(self):
        if self.eating_style == 'three_day_fast':
            self.end_date = self.created_date + datetime.timedelta(days=2)
        elif self.eating_style == 'two_day_fast':
            self.end_date = self.created_date + datetime.timedelta(days=1)
        else:
            self.end_date = self.created_date

    def determine_fast_day_variations(self):
        if self.eating_style == 'fast_day':
            rand = random.randint(1, 16)
            for obj in fast_prob:
                if obj['p_nums'][0] <= rand <= obj['p_nums'][1]:
                    self.fast_duration = obj['desc']
            rand = random.randint(1, 10)
            for obj in dietary_style_prob:
                if obj['p_nums'][0] <= rand <= obj['p_nums'][1]:
                    self.dietary_style = obj['desc']

    def call_day(self):
        self.determine_exercise_style()
        self.determine_eating_style()
        self.set_end_date()
        self.determine_fast_day_variations()


def run_day_regular():
    day = Day()
    day.call_day()
    return day


def run_day(prior_day):
    if datetime.date.today() <= prior_day['end_date'].date():
        day = Day(eating_style=prior_day['eating_style'], dietary_style=prior_day['dietary_style'],
                       end_date=prior_day['end_date'])
        day.determine_exercise_style()
    else:
        day = run_day_regular()
    #  print("Exercise style: {}, Eating Style: {}, End Date: {}, Fast Duration: {}, Dietary Style: {}".format(
    #    day.exercise_style, day.eating_style, day.end_date, day.fast_duration, day.dietary_style))
    return day

# Need to integrate ORM for MySQL database, build the initial model for testing
# Need to produce the monte carlo simulation to run the data and test probabilities
# Need to write the queries to analyse the data
# Upon certifying that the data is accurate, write the AWS message test
# Don't forget cool probability lines about percentage chance of happening
# Deploy model to AWS EC2 Server
# Add program to CRON, wait for following day for instructions from the randomness gods

