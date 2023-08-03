
from datetime import datetime
from random import randrange, seed

from dotenv import dotenv_values
from sqlalchemy import create_engine

cfg = dotenv_values(".env")

con_engine = create_engine(f"mysql+pymysql://{cfg['USR']}:{cfg['PWD']}@{cfg['HOST']}/{cfg['DB']}")
conn = con_engine.connect()


def db_exec(engine, sql):
    # print(f"sql: {sql}")
    if sql.strip().startswith('select'):
        return [dict(r) for r in engine.execute(sql).fetchall()]
    else:
        return engine.execute(sql)


def courtbot_main():
    context = dict()
    return context


def appearances(sql):
    results = list()

    for row in db_exec(conn, sql):
        appear = dict()
        appear['uuid'] = row['uuid']
        parties = row['parties']
        # TODO trying to stardardize. Do this smarter.
        parties = parties.replace('\n', ' ')
        parties = parties.replace('  ', ' ')
        parties = parties.replace(' v. ', ' vs ')
        parties = parties.replace(' vs. ', ' vs ')
        appear['parties'] = parties.split(' vs ')
        appear['scheduled_time'] = row['scheduled_time']
        appear['department'] = row['department']
        appear['location'] = f"{row['county_name']} County, {row['court_name']} Court"
        results.append(appear)

    return results


def find_random():
    seed()
    pk = db_exec(conn, "select max(pk) as pk from court_appearances")[0]['pk']
    rpk = randrange(pk)
    sql = f"""
    select c1.uuid, c1.parties, c1.scheduled_time, c2.department, c3.name as court_name, c4.name as county_name
    from court_appearances c1, court_calendar_depts c2, court_calendars c3, court_counties c4
    where c1.dept_pk = c2.pk and c2.calendar_pk = c3.pk and c3.county_pk = 1 and
        c1.pk > {rpk} order by c1.pk limit 10
    """
    print(f"sql: {sql}")
    return appearances(sql)


def find_appearances(args):

    first = args.get('first')
    last = args.get('last')
    sql = f"""
    select c1.uuid, c1.parties, c1.scheduled_time, c2.department, c3.name as court_name, c4.name as county_name
    from court_appearances c1, court_calendar_depts c2, court_calendars c3, court_counties c4
    where c1.dept_pk = c2.pk and c2.calendar_pk = c3.pk and c3.county_pk = 1 and
        (c1.parties like lower('{first}%%{last}%%vs%%') or c1.parties like lower('%%vs%%{first}%%{last}%%') or
        c1.parties like lower('{last},%%{first}%%vs%%') or c1.parties like lower('%%vs%%{last},%%{first}%%'))
    """

    # print(f"sql: {sql}")
    return appearances(sql)


def register_appearances(args):
    # params should look something like:
    #
    # 2572dcf6-911d-4ee3-9f21-1575f2e7d41a_foo@bar.com_408-111-2222
    #
    # Yes, this is lame. I will figure out proper get variables in flask forms.

    uuids_list = args.get('uuids')
    email = args.get('email')
    phone = args.get('phone')
    uuids = uuids_list.split(',')

    timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds() * 1000

    pk = db_exec(conn, "select max(pk) as pk from notify_reservations")[0]['pk']
    if pk is None:
        pk = 0

    results = list()

    for uuid in uuids:
        pk += 1
        sql = f"""
        insert into notify_reservations values
        ({pk}, '{uuid}', '{email}', '{phone}', {timestamp}, NULL)
        """
        db_exec(conn, sql)
        created = {'uuid': uuid, 'email': email, 'phone': phone}
        results.append(created)

    return {'status': 'ok', 'notifications': results}
