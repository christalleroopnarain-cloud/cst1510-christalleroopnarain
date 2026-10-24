"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT     
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#label == hostname,  value == used_gb,  limit == total_gb
class Record:
    over_limit_count = 0

    def __init__(self, hostname, used_gb, total_gb):
        """Create a Record storing the hostname, used_gb and total_gb."""
        self.hostname = hostname
        self.used_gb = used_gb
        self.total_gb = total_gb

    def status(self):
        """Calculates percentage of used_gb to total_gb and returns OVER LIMIT, WARNING or OK based on the percentage."""
        percentage = (self.used_gb / self.total_gb) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read path and returns a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            hostname, used_gb, total_gb = line.strip().split(',')
            records.append(Record(hostname, float(used_gb), float(total_gb)))
    return records

with open("temp_recs.txt", "w") as f: #writing my own record file
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,95,100\n")
    f.write("R-004,45,100\n")
    f.write("R-005,100,100\n")
    
records = load_records("temp_recs.txt") #storing record list in a variable after calling load_records()

for record in records:
    status = record.status()
    if status == "OVER LIMIT":
        Record.over_limit_count += 1 #adding 1 to over_limit_count if status is over limit

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.hostname}")
    print("=" * 34)

    print(f"{"Used GB":<21}: {record.used_gb:>10.2f}")
    print(f"{"Total GB":<21}: {record.total_gb:>10.2f}")
    print(f"{"Status of GB usage":<21}: {status:>10}")
    
    print("=" * 34)

print(f"Number of records that were over limit: {Record.over_limit_count}")
