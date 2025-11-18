import psutil
import datetime

# Log file
LOG_FILE = "/var/log/sa"

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 300

def log_alert(message):
    """Log alert to file and print on console"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"{timestamp} - ALERT: {message}"

    print(alert_message)

    with open(LOG_FILE, "a") as f:
        f.write(alert_message + "\n")


def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU Usage: {cpu_usage}%")

def check_memory():
    mem = psutil.virtual_memory()
    mem_usage = mem.percent
    if mem_usage > MEM_THRESHOLD:
        log_alert(f"High Memory Usage: {mem_usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"Low Disk Space: {disk_usage}% used")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"Too many running processes: {process_count}")


if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

    print("Health check completed.")

