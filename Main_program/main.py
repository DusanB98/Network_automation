# Python pinging server with latency
# Author: DusanB98

import subprocess
import platform
import sqlite3
import datetime

file_path = "/home/dusan/Desktop/Github/Python_projects/Network_automation/Main_program/hosts.txt"
data_log_file = "connection_hosts_log.db"

# Reading file of hosts with error notification
print()
try:
    with open(file=file_path, mode="r") as file:
        hosts = file.read()
        print("List of hosts:")
        print(hosts)
        hosts = hosts.splitlines()             # split a string into a list of lines at each newline character (\n)
except FileNotFoundError:
    print("──────────────────────")
    print(f"This file wasn't found")
    print("──────────────────────")
except PermissionError:
    print("──────────────────────────────────────────")
    print("You don't have permision to read this file")
    print("──────────────────────────────────────────")
print()

# function for pinging availability of hosts
def pinging_hosts_latency(host):
    os = platform.system().lower()

    if os == "linux":
        cmd = ["ping", "-c", "1", host]         # -c for linux/macOS
    else:
        cmd = ["ping", "-n", "1", host]         # -n for windows

    try:
        data_out = subprocess.run(
            cmd,                               # commands for pinging system
            capture_output=True,               # capture data from pinging
            text=True,                         # convert output data from bytes to string to process it with split() function
            check=True                         # ensures that a failed ping throws an exception
        ).stdout

        for data in data_out.split():           # using split() to find time of pinging (whole word)
            if "time=" in data:
                return float(data.replace("time=", ""))

        return True                            # host is available
    except subprocess.CalledProcessError:
        return False                           # host is unavailable

#sqlite3 creating database
def data_db_init():

    # creating connection with database (if doesn't exist, it will create new)
    database = sqlite3.connect(data_log_file)
    
    # creating SQL cursor, cmds are executed through this cursor
    cursor = database.cursor()

    # commadns for executing, first variable is name of column and capital words are commands, (data is variable)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            Number INTEGER PRIMARY KEY AUTOINCREMENT,
            Host TEXT,
            Status INTEGER,
            Latency REAL,
            Timestamp TEXT)
    """)

    # saving all changes and closing .db file
    database.commit()
    database.close()

def save_data(host, status, latency):

    # creating connection with database (if doesn't exist, it will create new)
    database = sqlite3.connect(data_log_file)
    
    # creating SQL cursor, cmds are executed through this cursor
    cursor = database.cursor()

    # Datetime customization for the right time format
    date_now = datetime.datetime.now()
    date_now = date_now.strftime("%H:%M:%S %m-%d-%Y")
    
    # Rounding latency time to 2 decimal places and adding ms
    latency = f"{latency:.2f} ms"

    # writing collected data to variable (data) which contains (Host, Status, Latency, Timestamp), "?" is position where are data written down
    cursor.execute("INSERT INTO data (Host, Status, Latency, Timestamp) VALUES (?, ?, ?, ?)",
                   (host, status, latency, date_now))

    # saving all changes and closing .db file
    database.commit()
    database.close()

# Calling functions and printing results
if __name__ == '__main__':
    data_db_init()

    for host in hosts:
        latency = pinging_hosts_latency(host)

        # sqlite3 database status check
        if latency:
            status = "✅"
        else: 
            status = "❌"

        save_data(host, status, latency)

        # console status check
        if pinging_hosts_latency(host):
            print(f"✅ Host '{host}' is available, latency {latency:.2f} ms")
        else:
            print(f"❌ Host '{host}' is unavailable")