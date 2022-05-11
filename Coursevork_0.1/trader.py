import random
import json
import csv
import argparse
from typing import List, Dict, Union
from datetime import datetime

def _read_json_config_file(filename: str) -> Union[List, Dict]:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def _read_json_logs_file(filename: str) -> Union[List, Dict]:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def _read_csv_file(filename: str) -> Union[List, Dict]:
    data = []
    with open(filename, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
    return data


def _write_csv_file(filename, data):
    fieldnames = ["UAH_account", "USD_account", "Course"]
    with open(filename, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def _add_logs(filename, actions):
    log = {f'{datetime.now()}': actions}
    with open(filename, "w") as file:
        json_logs.append(log)
        json.dump(json_logs, file, indent=2)


def return_course_now(csv_data) -> str:
    for row in csv_data:
        info = f"Course: {row['Course']}"
        return info


def do_new_course(course, delta, csv_data):
    new_course = round(random.uniform(course - delta, course + delta), 2)
    for row in csv_data:
        row["Course"] = new_course
    _write_csv_file('data.csv', csv_data)
    info = f'New course: {new_course}'
    _add_logs('logs.json', info)


def return_available(csv_file) -> str:
    for row in csv_file:
        info = f"USD: {row['USD_account']} - UAH: {row['UAH_account']}"
        return info


def buy_or_sell_dollars(usd_amount, csv_file, buy_or_sell):
    for row in csv_file:
        if buy_or_sell == 'buy':
            uah_amount = usd_amount * float(row['Course'])
            if float(row["UAH_account"]) >= usd_amount * float(row['Course']):
                row["USD_account"] = round(float(row["USD_account"]) + usd_amount, 2)
                row["UAH_account"] = round(float(row["UAH_account"]) - uah_amount, 2)
                info = f'Buy {usd_amount} USD'
            else:
                balance_required = round(usd_amount * float(row['Course']), 2)
                info = f"UNAVAILABLE, REQUIRED BALANCE UAH {balance_required}, AVAILABLE {row['UAH_account']}"
                print(info)
        elif buy_or_sell == 'sell':
            uah_amount = usd_amount * float(row['Course'])
            if float(row["USD_account"]) >= usd_amount:
                row["USD_account"] = round(float(row["USD_account"]) - usd_amount, 2)
                row["UAH_account"] = round(float(row["UAH_account"]) + uah_amount, 2)
                info = f'Sell {usd_amount} USD'
            else:
                info = f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {row['USD_account']}"
                print(info)
    _write_csv_file("data.csv", csv_file)
    _add_logs('logs.json', info)


def buy_or_sell_all_dollars(csv_file, buy_or_sell):
    for row in csv_file:
        if buy_or_sell == 'buy':
            all_usd_amount = round(float(row["UAH_account"]) / float(row['Course']), 2)
            if float(row["UAH_account"]) != 0:
                row["USD_account"] = round(float(row["USD_account"]) + all_usd_amount, 2)
                row["UAH_account"] = 0.00
                info = 'Byu all dollars'
            else:
                info = "NO MORE UAS"
                print(info)
        elif buy_or_sell == 'sell':
            all_uah_amount = round(float(row["USD_account"]) * float(row['Course']), 2)
            if float(row["USD_account"]) != 0:
                row["USD_account"] = 0.00
                row["UAH_account"] = round(float(row["UAH_account"]) + all_uah_amount, 2)
                info = 'Sell all dollars'
            else:
                info = "NO MORE USD"
                print(info)
    _write_csv_file("data.csv", csv_file)
    _add_logs('logs.json', info)


def restart_trader(csv_file):
    for row in csv_file:
        row["USD_account"] = usd_account
        row["UAH_account"] = uah_account
        row["Course"] = initial_course
    _write_csv_file("data.csv", csv_file)
    with open('logs.json', 'w') as file:
        data = []
        json.dump(data, file)


json_config = _read_json_config_file("config.json")
json_logs = _read_json_logs_file('logs.json')
csv_data = _read_csv_file('data.csv')
available_str = return_available(csv_data)
course_now = return_course_now(csv_data)
initial_course = json_config['initial_course']
uah_account = json_config['uah_account']
usd_account = json_config['usd_account']
delta = json_config["delta"]

parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("amount", nargs='?', default=0)
args = parser.parse_args()

if args.action == "RATE":
    _add_logs('logs.json', course_now)
    print(course_now)
elif args.action == 'AVAILABLE':
    _add_logs('logs.json', available_str)
    print(available_str)
elif args.action == 'BUY':
    if args.amount == 'ALL':
        buy_or_sell_all_dollars(csv_data, "buy")
    else:
        if float(args.amount) > 0:
            buy_or_sell_dollars(float(args.amount), csv_data, 'buy')
elif args.action == 'SELL':
    if args.amount == 'ALL':
        buy_or_sell_all_dollars(csv_data, "sell")
    else:
        if float(args.amount) > 0:
            buy_or_sell_dollars(float(args.amount), csv_data, 'sell')
elif args.action == 'NEXT':
    do_new_course(initial_course, delta, csv_data)
elif args.action == 'RESTART':
    restart_trader(csv_data)
