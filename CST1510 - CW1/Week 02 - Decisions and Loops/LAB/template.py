"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT  
Date  : 30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

over_limit_count = 0
flag = 1

while flag != 0:
    hostname = input("Enter a hostname (or 'quit' to finish): ") # label == hostname
    if hostname == 'quit':
        flag = 0
    else:      
        used_gb = float(input("Enter amount of GB used: "))     #value == used_gb
        total_gb = float(input("Enter total amount of GB: "))     #limit == total_gb
        
        free_gb = total_gb - used_gb           #difference == free_gb
        percent_used_gb = (used_gb / total_gb) * 100     #percent == percent_used_gb
        
        if percent_used_gb >= 100:
            status = "OVER LIMIT"
            over_limit_count += 1
        elif percent_used_gb >= 90:
            status = "WARNING"
        else:
            status = "OK"

    
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


print(f"Number of records that were over limit: {over_limit_count}")

