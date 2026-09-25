"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT    
Date  : 25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
hostname = input("Enter a hostname: ")
used_gb = float(input("Enter the amount of GB used: "))
total_gb = float(input("Enter the total amount of GB: "))

# ================================================================== PROCESS
free_gb = total_gb - used_gb
percent_used_gb = (used_gb / total_gb) * 100

percent_free_gb = (free_gb / total_gb) * 100 #calculates percentage of free GB available out of total GB 

# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)

print(f"{"Used GB":<20}:{used_gb:>10.2f}")
print(f"{"Total GB":<20}:{total_gb:>10.2f}")
print(f"{"Free GB":<20}:{free_gb:>+10.2f}")
print(f"{"Percent of GB used":<20}:{percent_used_gb:>10.2f} %")
print(f"{"Percent of GB free":<20}:{percent_free_gb:>10.2f} %")

print("=" * 34)



