"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT      
Date  : 08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns "OVER LIMIT"(100% or more), "WARNING" (90% or more), or "OK" (anything else)"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Works out and returns the difference and the percentage as two values."""
    difference = limit - value
    percentage = (value / limit) * 100
    return difference, percentage


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



over_limit_count = 0
flag = 1

while flag != 0:
    hostname = input("Enter a hostname: ") # label == hostname
    if hostname == 'quit':
        flag = 0
    else:
        used_gb = float(input("Enter the amount of GB used: "))  #value == used_gb
        total_gb = float(input("Enter the total amount of GB: ")) #limit == total_gb

        free_gb, percent_used_gb = check(used_gb, total_gb)      # difference==free_gb, percent == percent_used_gb

        status = status_of(percent_used_gb)
        if status == "OVER LIMIT":
            over_limit_count += 1  

        print_report(hostname, used_gb, total_gb, free_gb, percent_used_gb, status)   


print(f"Number of records that were over limit: {over_limit_count}")






