import re
def extract_log_details(log_entry):


    pattern = r'\[(.*?)\] (.*?) \(IP: (.*?)\)-"(.*?)"'
    match = re.search(pattern, log_entry)
    if match:
        return {
            'Timestamp': match.group(1),
            'Username': match.group(2),
            'IP Address': match.group(3),
            'Activity': match.group(4)
        }
    return

log_entry = '[2024-10-10 12:34:56] s kumar (IP: 192.168.1.1)-"Login successful"'
log_details = extract_log_details(log_entry)

if log_details:
    print("Timestamp:", log_details['Timestamp'])
    print("Username:", log_details['Username'])
    print("IP Address:", log_details['IP Address'])
    print("Activity:", log_details['Activity'])
else:
    print("No match found.")
