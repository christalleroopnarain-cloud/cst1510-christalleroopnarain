"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  : IT      
Date  : 15/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# label == hostname
#value == used_gb
#limit == total_gb

#difference == free_gb
#percentage == percent_used_gb


def check_record(value, limit):
    """Works out and returns the difference, the percentage and status as three values."""
    difference = limit - value
    percentage = (value / limit) * 100

    if percentage >= 100:
            status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK" 
    return difference, percentage, status


def print_report(hostname, used_gb, total_gb, free_gb, percent_used_gb, status):
    """Prints a report showing label, value, limit, difference, percent and status."""
    print()
    print("=" * 40)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 40)

    print(f"{"Used GB":<21}: {used_gb:>10.2f}")
    print(f"{"Total GB":<21}: {total_gb:>10.2f}")
    print(f"{"Free GB":<21}: {free_gb:>10.2f}")
    print(f"{"Percentage of GB used":<21}: {percent_used_gb:>10.2f} %")
    print(f"{"Status of GB usage":<21}: {status:>10}")

    print("=" * 40)


def load_records(path):
    """Reads label, value, limit lines from a file and returns the list."""
    records = []
    with open(path) as f:
         for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"hostname": label, "used_gb": float(value), "total_gb": float(limit)})
    return records



with open("data.txt", "w") as f:
    f.write("srv-01,87,120\n")
    f.write("srv-02,130,120\n")
    f.write("srv-03,45,200\n")
    f.write("srv-04,118,120\n")
    f.write("srv-05,60,100\n")
    f.write("srv-06,0,500\n")
    f.write("srv-07,450,500\n")
    f.write("srv-08,512,512\n")
    f.write("srv-09,89.5,100\n")
    f.write("srv-10,15,16\n")
    


over_limit_count = 0
try:
    records = load_records("data.txt")
    with open("results.txt", "w") as f:
        for row in records:
            free_gb, percent_used_gb, status = check_record(row["used_gb"], row["total_gb"])
            if status == "OVER LIMIT":
                over_limit_count += 1
            f.write(f"{row["hostname"]},{status}\n")

            print_report(row["hostname"], row["used_gb"], row["total_gb"], free_gb, percent_used_gb, status)


    print(f"Number of records that were over limit: {over_limit_count}")

except FileNotFoundError:
    print("File does not exist please create or use a new one.")
    records = []



