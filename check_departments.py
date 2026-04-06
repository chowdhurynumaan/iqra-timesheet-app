import xlrd

# Load the Employee Form
wb = xlrd.open_workbook('data/employee_form.xls')
ws = wb.sheet_by_index(0)

print(f"Sheet: {ws.name}")
print(f"Dimensions: {ws.nrows} rows x {ws.ncols} cols\n")

# Get all rows
rows = [[ws.cell_value(i, j) for j in range(ws.ncols)] for i in range(ws.nrows)]

# Print first 10 rows to see structure
print("First 10 rows:")
for i, row in enumerate(rows[:10], 1):
    print(f"Row {i}: {row}\n")

# Assuming column with departments (likely around column 3-5 based on typical employee forms)
print("\n" + "="*80)
print("Looking for departments...")
print("="*80 + "\n")

# Get all unique values from each column to identify which might be departments
for col_idx in range(min(10, len(rows[0]) if rows else 0)):
    values = [row[col_idx] for row in rows[1:] if row and col_idx < len(row) and row[col_idx]]
    unique_vals = set(str(v).strip() for v in values if v)
    if unique_vals and len(unique_vals) <= 20:  # Likely department/category column
        print(f"Column {col_idx}: {sorted(unique_vals)}")

# Try to find departments in common positions
print("\n" + "="*80)
print("Checking likely department columns (3-5):")
print("="*80 + "\n")

for col_idx in range(2, min(6, len(rows[0]) if rows else 0)):
    depts = set()
    for row in rows[1:]:
        if row and col_idx < len(row) and row[col_idx]:
            dept = str(row[col_idx]).strip()
            if dept and dept.lower() not in ['nan', 'none', '']:
                depts.add(dept)
    if depts:
        print(f"Column {col_idx} unique values ({len(depts)} total):")
        print(sorted(depts))
        print()
