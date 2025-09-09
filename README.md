# 📡 Python Server Pinger with Latency Logger

**Description:**
This Python script monitors server availability by pinging a list of hosts and logging their response times (latency). It reads hosts from a `hosts.txt` file, pings each one, evaluates their status based on latency thresholds, and stores the results in a local SQLite database (`response_hosts_database`) along with a timestamp. Additionally, it writes detailed logs to a `.log` file (`response_hosts_log`) using Python’s `logging` module, providing structured feedback for each ping attempt. The script is compatible with Linux, macOS, and Windows systems.

During the development of this project, I learned how to work with several key Python libraries, including `subprocess`, `platform`, `sqlite3`, `logging`, and `datetime`. This helped me understand system-level operations, database handling, time formatting, and structured logging in Python.

## 🔧 Features
- Reads a list of hosts from a file
- Pings each host and measures latency
- Evaluates host availability with three statuses:
  - ✅ Available (latency < 100 ms)
  - ⚠️ Available, but slow response (latency ≥ 100 ms)
  - ❌ Unavailable (no response)
- Logs results into a SQLite database with timestamp
- Writes detailed logs to a `.log` file with INFO, WARNING, and ERROR levels
- Displays status and latency in the console
- Compatible with Linux, macOS, and Windows systems

## 📂 Database Structure
The `response_hosts_database` database contains a table named `data` with the following columns:
- `Number` – auto-incremented ID
- `Host` – hostname or IP address
- `Status` – availability (✅ / ⚠️ / ❌)
- `Latency` – response time in milliseconds
- `Timestamp` – date and time of the ping

## 📝 Log File
The script generates a log file named `response_hosts_log` which includes:
- Timestamped entries for each host
- Log levels:
  - `INFO` for successful pings
  - `WARNING` for slow responses
  - `ERROR` for unreachable hosts
