import datetime
import argparse

parser = argparse.ArgumentParser(description='A punch-card machine.')

parser.add_argument("command")

args = parser.parse_args()


def show_log():
    with open("../data/logfile") as log_file:
        print log_file.read()

def show_stat():
    with open("../data/logfile") as log_file:
        print "logs: " + str(len(log_file.readlines()))

def get_date():
    return datetime.datetime.now().isoformat()

def add():
    with open("../data/logfile","a") as log_file:
        log_file.write(get_date()+"\n")
        print "log added"

if args.command == "view":
    show_log()
elif args.command == "add":
    add()
elif args.command == "stat":
    show_stat()
