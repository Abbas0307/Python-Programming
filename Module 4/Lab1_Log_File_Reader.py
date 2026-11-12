# MODULE 4 - LAB 1: Log File Reader
# Reads a log file and displays entries by log level.

from pathlib import Path

LOG_FILE = Path("sample_app.log")

def create_sample_log():
    """Create a small example log file if one does not exist."""
    if not LOG_FILE.exists():
        sample_lines = [
            "2026-11-12 09:00:00 INFO Application started",
            "2026-11-12 09:02:15 WARNING Disk space is getting low",
            "2026-11-12 09:03:40 ERROR Database connection failed",
            "2026-11-12 09:05:10 INFO User login successful",
            "2026-11-12 09:07:25 ERROR Unable to load user profile",
        ]
        LOG_FILE.write_text("\n".join(sample_lines) + "\n", encoding="utf-8")

def read_logs():
    create_sample_log()

    try:
        lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        print("Could not read log file:", error)
        return

    print("\n===== APPLICATION LOG READER =====")
    print("Log file:", LOG_FILE)
    print("Total log entries:", len(lines))

    level = input("Filter by level (INFO/WARNING/ERROR or ALL): ").strip().upper()
    if level not in ("INFO", "WARNING", "ERROR", "ALL"):
        print("Invalid filter. Showing all entries.")
        level = "ALL"

    print("\n----- LOG ENTRIES -----")
    matched = 0

    for line in lines:
        if level == "ALL" or f" {level} " in line:
            print(line)
            matched += 1

    print("\nMatching entries:", matched)

if __name__ == "__main__":
    read_logs()
