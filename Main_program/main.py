# Python pinging server with latency
# Author: DusanB98

import subprocess
import platform

file_path = "/home/dusan/Desktop/Github/Python_projects/Network_automation/Main_program/hosts.txt"

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

# Printing result of pinging
for host in hosts:
    latency = pinging_hosts_latency(host)
    if pinging_hosts_latency(host):
        print(f"✅ Host '{host}' is available, latency {latency:.2f} ms")
    else:
        print(f"❌ Host '{host}' is unavailable")