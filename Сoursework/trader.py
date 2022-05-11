import random
import json
import csv
import argparse
from typing import List, Dict, Union
from datetime import datetime


class Trader:
    def __init__(self, usd_amount):
        self.usd_amount = float(usd_amount)
        self.config_json_file = 'config.json'
        self.logs_json_file = 'logs.json'
        self.data_csv_file = 'data.csv'
        self.json_config_file_list = self._read_json_config_file()
        self.json_logs_file_list = self._read_json_logs_file()
        self.csv_file_list = self._read_csv_file()
        self.uah_account = self.json_config_file_list['uah_account']
        self.usd_account = self.json_config_file_list['usd_account']
        self.initial_course = self.json_config_file_list['initial_course']
        self.delta = self.json_config_file_list["delta"]

    def _read_json_config_file(self) -> Union[List, Dict]:
        with open(self.config_json_file, 'r') as file:
            data = json.load(file)
        return data

    def _read_json_logs_file(self) -> Union[List, Dict]:
        with open(self.logs_json_file, 'r') as file:
            data = json.load(file)
        return data

    def _read_csv_file(self) -> Union[List, Dict]:
        data = []
        with open(self.data_csv_file, 'r', newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                data.append(row)
        return data

    def _write_csv_file(self):
        fieldnames = ["UAH_account", "USD_account", "Course"]
        with open(self.data_csv_file, 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.csv_file_list)

    def _add_logs(self, actions):
        log = {f'{datetime.now()}': actions}
        with open(self.logs_json_file, "w") as file:
            self.json_logs_file_list.append(log)
            json.dump(self.json_logs_file_list, file, indent=2)

    def return_course_now(self) -> str:
        for row in self.csv_file_list:
            info = f"Course: {row['Course']}"
            return info

    def do_new_course(self):
        new_course = round(random.uniform(self.initial_course - self.delta, self.initial_course + self.delta), 2)
        for row in self.csv_file_list:
            row["Course"] = new_course
        self._write_csv_file()
        info = f'New course: {new_course}'
        self._add_logs(info)

    def return_available(self) -> str:
        for row in self.csv_file_list:
            info = f"USD: {row['USD_account']} - UAH: {row['UAH_account']}"
            return info

    def buy_or_sell_dollars(self, buy_or_sell):
        for row in self.csv_file_list:
            uah_amount = self.usd_amount * float(row['Course'])
            if buy_or_sell == 'buy':
                if float(row["UAH_account"]) >= self.usd_amount * float(row['Course']):
                    row["USD_account"] = round(float(row["USD_account"]) + self.usd_amount, 2)
                    row["UAH_account"] = round(float(row["UAH_account"]) - uah_amount, 2)
                    info = f'Buy {round(self.usd_amount, 2)} USD'
                else:
                    balance_required = round(self.usd_amount * float(row['Course']), 2)
                    info = f"UNAVAILABLE, REQUIRED BALANCE UAH {balance_required}, AVAILABLE {row['UAH_account']}"
                    print(info)
            elif buy_or_sell == 'sell':
                if float(row["USD_account"]) >= self.usd_amount:
                    row["USD_account"] = round(float(row["USD_account"]) - self.usd_amount, 2)
                    row["UAH_account"] = round(float(row["UAH_account"]) + uah_amount, 2)
                    info = f'Sell {round(self.usd_amount, 2)} USD'
                else:
                    info = f"UNAVAILABLE, REQUIRED BALANCE USD {self.usd_amount}, AVAILABLE {row['USD_account']}"
                    print(info)
        self._write_csv_file()
        self._add_logs(info)

    def buy_or_sell_all_dollars(self, buy_or_sell):
        for row in self.csv_file_list:
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
        self._write_csv_file()
        self._add_logs(info)

    def restart_trader(self):
        for row in self.csv_file_list:
            row["USD_account"] = self.usd_account
            row["UAH_account"] = self.uah_account
            row["Course"] = self.initial_course
        self._write_csv_file()
        with open('logs.json', 'w') as file:
            data = []
            json.dump(data, file)


parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("amount", nargs='?', default=0)
args = parser.parse_args()
try:
    trader = Trader(args.amount) if args.amount != "ALL" else Trader(0)
    if args.action == "RATE":
        trader._add_logs(trader.return_course_now())
        print(trader.return_course_now())
    elif args.action == 'AVAILABLE':
        trader._add_logs(trader.return_available())
        print(trader.return_available())
    elif args.action == 'BUY':
        if args.amount == 'ALL':
            trader.buy_or_sell_all_dollars("buy")
        else:
            if float(args.amount) > 0:
                trader.buy_or_sell_dollars('buy')
            else:
                print("I don't work with negative numbers")
    elif args.action == 'SELL':
        if args.amount == 'ALL':
            trader.buy_or_sell_all_dollars("sell")
        else:
            if float(args.amount) > 0:
                trader.buy_or_sell_dollars('sell')
            else:
                print("I don't work with negative numbers")
    elif args.action == 'NEXT':
        trader.do_new_course()
    elif args.action == 'RESTART':
        trader.restart_trader()
except ValueError:
    print('Something went wrong :(')
