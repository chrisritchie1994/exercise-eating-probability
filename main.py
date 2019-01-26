import day_prob
from sqlalchemy.orm import sessionmaker
from db_model import *
from sms import send_sms


def daily_execution():
    prior_day = session.execute("""SELECT * FROM random_life.days WHERE id = (SELECT MAX(id) FROM random_life.days);
    """).fetchone()  # change to random_life.days in production
    if prior_day is None:
        day = day_prob.run_day_regular()
    else:
        day = day_prob.run_day(prior_day)
    day_entry = Days(created_date=day.created_date, eating_style=day.eating_style,
                     dietary_style=day.dietary_style, end_date=day.end_date, fast_duration=day.fast_duration,
                     exercise_style=day.exercise_style)
    day_seed_entry = DaySeed(seed=day_prob.rand_seed)
    session.add(day_entry)  # inserts into database
    session.add(day_seed_entry)
    session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/random_life', echo=True)  # must change for prod
    Session = sessionmaker(bind=engine)
    session = Session()
    Session.configure(bind=engine)
    daily_execution()
    send_sms(session)
    session.close()
