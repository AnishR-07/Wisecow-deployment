import os
import tarfile
import datetime
import paramiko


SOURCE_DIR = "/root/project/"          
BACKUP_NAME = "backup.tar.gz"            
LOCAL_BACKUP_PATH = f"/tmp/{BACKUP_NAME}"

REMOTE_SERVER = "192.168.226.135"           
REMOTE_USER = "root"                     
REMOTE_PASSWORD = "Lolipop@123"        
REMOTE_DIR = "/backups/"                 

LOG_FILE = "/var/log/backup_report.log"  


def log(message):
    """Write log with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"{timestamp} - {message}"
    print(msg)

    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def create_backup():
    """Creates a tar.gz backup file"""
    try:
        with tarfile.open(LOCAL_BACKUP_PATH, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        log("Backup archive created successfully.")
        return True
    except Exception as e:
        log(f"Backup creation failed: {e}")
        return False

def main():
    log("Backup process started.")

    if not create_backup():
        log("Backup FAILED during archive creation.")
        return

    log("Backup completed SUCCESSFULLY.")


if __name__ == "__main__":
    main()
