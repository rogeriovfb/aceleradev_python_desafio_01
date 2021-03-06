from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


def is_daytime(start, minute):
    return 6 < datetime.fromtimestamp(start + minute * 60).hour < 22


def call_cost(call, base_cost):
    cost = base_cost
    duration = datetime.fromtimestamp(call['end']) - datetime.fromtimestamp(call['start'])
    for minute in range(0, int(duration.seconds / 60)):
        if is_daytime(call['start'], minute):
            cost += 0.09
    return cost


def classify_by_phone_number(records):
    bills_dict = {}
    base_cost = 0.36
    for call in records:
        bills_dict[call['source']] = round(bills_dict.get(call['source'], 0) + call_cost(call, base_cost), 2)
    bills = [{'source': source, 'total': total} for source, total in bills_dict.items()]
    bills = sorted(bills, key=lambda cost: cost['total'], reverse=True)
    return bills


classify_by_phone_number(records)
