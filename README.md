# 📡 Python Server Pinger with Latency Logger
 
**Description:**
This Python script checks the availability of servers by pinging them and logs their response time (latency) into a local SQLite database.
It reads a list of hosts from a `hosts.txt` file, pings each one, evaluates their status, and stores the results in `connection_hosts_log.db` along with a timestamp.

During the development of this project, I learned how to work with several key Python libraries, including `subprocess`, `platform`, `sqlite3`, and `datetime`.
This helped me understand system-level operations, database handling, and time formatting in Python.

## 🔧 Features
- Reads a list of hosts from a file
- Pings each host and measures latency
- Evaluates host availability (✅ / ❌)
- Logs results into a SQLite database with timestamp
- Displays status and latency in the console

## 📂 Database Structure
The `connection_hosts_log.db` database contains a table named `data` with the following columns:
- `Number` – auto-incremented ID
- `Host` – hostname or IP address
- `Status` – availability (✅ / ❌)
- `Latency` – response time in milliseconds
- `Timestamp` – date and time of the ping
