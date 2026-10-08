from pathlib import Path

log_dir = Path(__file__).parent

file = log_dir /"logs"/"sample.log"

failed_users = {}
failed_ips = {}

with open(file, 'r', encoding='UTF-8') as f:

    for line in f:

        if "Failed" in line:

            words = line.split()

            # Username
            username = words[3]

            if username in failed_users:
                failed_users[username] += 1
            else:
                failed_users[username] = 1

            # IP address
            ip = words[5]

            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1



print(failed_users)
print(failed_ips)
