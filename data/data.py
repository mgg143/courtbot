
known_appearances = [
    '5576e34d-28a7-4e52-b19d-074501e70d7c',
    '653b7f70-d618-486b-8a81-c35bcad62f9b'
]


def courtbot_main():
    context = dict()
    return context


def find_appearances(params):
    first, last = params.split('_')
    if first.startswith('R') and last.startswith('K'):
        result = dict()
        parties = ['Ray Kiddy', 'State of California']
        appearances = list()
        appear1 = dict()
        appear1['uuid'] = known_appearances[0]
        appear1['parties'] = parties
        appear1['scheduled_time'] = '2023-07-19 10:15 am'
        appear1['location'] = 'Santa Clara County, Civil Court'
        appear1['department'] = '02'
        appearances.append(appear1)
        appear2 = dict()
        appear2['uuid'] = known_appearances[1]
        appear2['parties'] = parties
        appear2['scheduled_time'] = '2023-08-09 1:30 pm'
        appear2['location'] = 'Santa Clara County, Civil Court'
        appear2['department'] = '02'
        appearances.append(appear2)
        result['appearances'] = appearances
        return result
    return {}


def register_appearances(params):
    uuids_list, phone = params.split('_')
    uuids = uuids_list.split(',')
    if phone is None or len(phone) != 12:
        raise Exception(f"Phone number ({phone}) is not proper format")
    if uuids is None or len(uuids) == 0:
        raise Exception(f"Appearance UUIDS ({uuids}) are not correct.")

    created = 0
    for uuid in uuids:
        if uuid in known_appearances:
            created += 1
        else:
            raise Exception(f"uuid ({uuid}) not known.")

    return {'status': 'ok', 'notifications': created}
