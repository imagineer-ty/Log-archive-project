import sys
import os
import tarfile
from datetime import datetime


# Ensure correct usage
if len(sys.argv) != 2:
    print("Usage: python log_archive.py <log-directory>")
    sys.exit(1)


# Directory provided by user
log_dir = sys.argv[1]


# Check directory exists
if not os.path.isdir(log_dir):
    print("Error: Directory does not exist")
    sys.exit(1)


# Create archive directory if missing
archive_dir = "archives"
os.makedirs(archive_dir, exist_ok=True)


# Create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


# Archive filename
archive_name = f"logs_archive_{timestamp}.tar.gz"
archive_path = os.path.join(archive_dir, archive_name)


# Compress logs
with tarfile.open(archive_path, "w:gz") as tar:
    tar.add(log_dir, arcname=os.path.basename(log_dir))


# Log archive creation
with open("archive.log", "a") as f:
    f.write(f"{timestamp} - Archived {log_dir} -> {archive_path}\n")


print(f"Archive created: {archive_path}")


# -----------------------------
# Auto-delete old archives
# -----------------------------

retention_days = 7
now = datetime.now()

for file in os.listdir(archive_dir):

    file_path = os.path.join(archive_dir, file)

    if os.path.isfile(file_path):

        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        age = now - file_time

        if age.days > retention_days:

            os.remove(file_path)

            with open("archive.log", "a") as f:
                f.write(f"{datetime.now()} - Deleted old archive {file}\n")