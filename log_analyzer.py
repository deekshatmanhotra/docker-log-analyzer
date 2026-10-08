from pathlib import Path
import os

log_dir = Path(__file__).parent

file = log_dir / "logs" / "sample.log"

log_level = os.environ.get("LOG_LEVEL")

levels = {
    "INFO":1,
    "WARNING":2,
    "ERROR":3
    }

selected_level = levels.get(log_level.upper(), 1)


failed_users={}
failed_ip={}
with open(file, 'r', encoding='UTF-8') as f:
    for line in f:
        line_level = line.split()[0]

        if levels.get(line_level, 0) >= selected_level:
            print(line.strip())
        
