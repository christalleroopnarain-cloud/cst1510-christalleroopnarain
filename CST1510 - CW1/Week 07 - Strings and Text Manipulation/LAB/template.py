"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT   
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Takes a messy raw line, cleans and parses it into a dictionary."""
    line = raw_line.strip()
    hostname, rest = line.split(",", 1) #separating hostname from the values to handle the values better

    fields = {}
    fields["hostname"] = hostname.strip().lower()

    for line in rest.split(","):
        key, value = line.split("=")
        fields[key.strip().lower()] = float(value.strip())
    return fields

def status_of(used, total):
    """Calculates percentage from used and total then returns status"""
    percent = (used/total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


raw_records = []   
with open("my_records.txt") as f:
    for l in f:
        raw_records.append(l)


flagged = 0 #flagged == "OVER LIMIT" records only
for raw_record in raw_records:
    rec_dict = parse_line(raw_record) 
    status = status_of(rec_dict["used"], rec_dict["total"]) #finding status using the dictionary keys
    if status == "OVER LIMIT":
        flagged += 1 #Incrementing the flagged counter if status is OVER LIMIT 

    print(f"{rec_dict} {status}") 

print(f"Summary: {flagged} out of {len(raw_records)} records were flagged.")


#Tested with used=unknown: ValueError: could not convert string to float: 'unknown'