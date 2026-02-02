# src/reporter.py
import os
import json
from loader import load_data
from checks import check_missing, check_duplicates, check_outliers, check_schema

# Load CSV
df = load_data()

# Define expected columns
expected_columns = ["id", "age", "salary"]  # adjust if needed

# Run checks
report = {
    "missing_values": check_missing(df),
    "duplicate_rows": check_duplicates(df),
    "outliers": check_outliers(df),
    "schema_issues": check_schema(df, expected_columns)
}

# Save report in project root
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../quality_report.json")
with open(output_path, "w") as f:
    json.dump(report, f, indent=4)

# Console summary
print("\n=== DATA QUALITY REPORT ===")
for k, v in report.items():
    print(f"{k}: {v}")

print(f"\nReport saved to {output_path}")
