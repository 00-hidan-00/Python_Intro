import random
import json
import csv
import argparse
from argparse import ArgumentParser
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


json_config = _read_json_config_file("config.json")
json_logs = _read_json_logs_file('logs.json')
csv_data = _read_csv_file('data.csv')


# ADD LOGS

def _add_logs(filename, actions):
    log = {f'{datetime.now()}': actions}
    with open(filename, "w") as file:
        json_logs.append(log)
        json.dump(json_logs, file, indent=2)


# NEW COURSE

def do_new_course(course, delta):
    new_course = round(random.uniform(course - delta, course + delta), 2)
    for row in csv_data:
        row["Course"] = new_course
    _write_csv_file('data.csv', csv_data)
    info = f'New course: {new_course}'
    _add_logs('logs.json', info)


#

def available(csv_file):
    for row in csv_file:
        info = f"USD: {row['USD_account']} - UAH: {row['UAH_account']}"
        _add_logs('logs.json', info)
        print(info)


# BUY OR SELL DOLLARS


def buy_or_sell_dollars(usd_amount, csv_file, buy_or_sell):
    for row in csv_file:
        if buy_or_sell == 'buy':
            uah_amount = usd_amount * float(row['Course'])
            if float(row["UAH_account"]) >= usd_amount * float(row['Course']):
                row["USD_account"] = round(float(row["USD_account"]) + usd_amount, 2)
                row["UAH_account"] = round(float(row["UAH_account"]) - uah_amount, 2)
                info = f'buy {usd_amount} USD'
            else:
                balance_required = round(usd_amount * float(row['Course']), 2)
                info = f"UNAVAILABLE, REQUIRED BALANCE UAH {balance_required}, AVAILABLE {row['UAH_account']}"
                print(info)
        elif buy_or_sell == 'sell':
            uah_amount = usd_amount * float(row['Course'])
            if float(row["USD_account"]) >= usd_amount:
                row["USD_account"] = round(float(row["USD_account"]) - usd_amount, 2)
                row["UAH_account"] = round(float(row["UAH_account"]) + uah_amount, 2)
                info = f'sell {usd_amount} USD'
            else:
                info = f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {row['USD_account']}"
                print(info)
        _write_csv_file("data.csv", csv_file)
        _add_logs('logs.json', info)


# BUY ALL DOLLARS

def buy_or_sell_all_dollars(csv_file, buy_or_sell):
    for row in csv_file:
        if buy_or_sell == 'buy':
            all_usd_amount = round(float(row["UAH_account"]) / float(row['Course']), 2)
            if float(row["UAH_account"]) != 0:
                row["USD_account"] = round(float(row["USD_account"]) + all_usd_amount, 2)
                row["UAH_account"] = 0.00
                info = 'byu all dollars'
            else:
                info = "NO MORE UAS"
                print(info)
        elif buy_or_sell == 'sell':
            all_uah_amount = round(float(row["USD_account"]) * float(row['Course']), 2)
            if float(row["USD_account"]) != 0:
                row["USD_account"] = 0.00
                row["UAH_account"] = round(float(row["UAH_account"]) + all_uah_amount, 2)
                info = 'sell all dollars'
            else:
                info = "NO MORE USD"
                print(info)
        _write_csv_file("data.csv", csv_file)
        _add_logs('logs.json', info)


# RESTART

def restart_data(csv_file):
    for row in csv_file:
        row["USD_account"] = json_config['usd_account']
        row["UAH_account"] = json_config['uah_account']
        row["Course"] = json_config['initial_course']
    _write_csv_file("data.csv", csv_file)
    with open('logs.json', 'w') as file:
        data = []
        json.dump(data, file)


course = json_config['initial_course']
delta = json_config["delta"]
usd_amount = 100

# do_new_course(course, delta)
# available(csv_data)
# buy_or_sell_dollars(usd_amount, csv_data, 'buy')
# buy_or_sell_all_dollars(csv_data, "buy")
# restart_data(csv_data)

print(123)
parser = argparse.ArgumentParser()

args = parser.parse_args()

print(args)