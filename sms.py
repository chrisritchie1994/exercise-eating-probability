import boto3
import json


def send_sms(session):
    with open("labels.json") as f:
        labels = json.load(f)

    today = session.execute("""SELECT * FROM random_life.days WHERE CREATED_DATE = CURRENT_DATE();""").fetchone()

    message_obj = {}

    for k, v in today.items():
        if v is None:
            message_obj[k] = 'nothing today'
        elif k == 'eating_style' or k == 'dietary_style' or k == 'fast_duration' or k == 'exercise_style':
            message_obj[k] = labels[v]
        elif k == 'end_date':
            message_obj[k] = str(today['end_date'])[0:10]

    greeting = "Hey there complex adaptive system, I'm a stressor. \n" \
               "On the menu today:\n" \
               "Eating Style: {}\n" \
               "Dietary Style: {}\n" \
               "Fast Duration: {}\n" \
               "Exercise Style: {}\n" \
               "End Date: {}\n" \
               "- happy hunting".format(message_obj['eating_style'], message_obj['dietary_style'],
                                        message_obj['fast_duration'], message_obj['exercise_style'],
                                        message_obj['end_date'])

    subject = message_obj['end_date'] + " Day Exercise & Diet & Fast"

    with open("aws_cred.json") as f:
        aws_cred = json.load(f)

    client = boto3.client('sns',
                          region_name='ap-southeast-2',
                          aws_access_key_id=aws_cred['aws_access_key_id'],
                          aws_secret_access_key=aws_cred['aws_secret_access_key']
    )

    response = client.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:770550232289:random_exercise_eating_day',
        Subject=subject,
        Message=greeting
    )

