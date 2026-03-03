import sys
import os
import tarfile
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: log-archive <log-directory>")
    sys.exit(1)

log_dir = sys.argv[1]

if not os.path.isdir(log_dir):
    print("Error: Directory does not exist")
    sys.exit(1)

archive_dir = "archives"
os.makedirs(archive_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archive_name = f"logs_archive_{timestamp}.tar.gz"
archive_path = os.path.join(archive_dir, archive_name)

with tarfile.open(archive_path, "w:gz") as tar:
    tar.add(log_dir, arcname=os.path.basename(log_dir))

with open("archive.log", "a") as f:
    f.write(f"{timestamp} - Archived {log_dir} -> {archive_path}\n")

print(f"Archive created: {archive_path}")