import xlrd

file_path = 'Employee Form.xls'
wb = xlrd.open_workbook(file_path)
ws = wb.sheet_by_index(0)

print(f"📊 Total rows: {ws.nrows}")
print(f"📊 Total columns: {ws.ncols}\n")

# Find where employee data starts (row 7 has headers with *ID)
print("=" * 100)
print("EMPLOYEE DATA (Row 9 onwards):")
print("=" * 100)

employee_count = 0
for row_idx in range(8, ws.nrows):  # Start from row 9 (index 8)
    id_val = ws.cell_value(row_idx, 0)
    name_val = ws.cell_value(row_idx, 1)
    dept_val = ws.cell_value(row_idx, 2)
    auth_val = ws.cell_value(row_idx, 3)
    
    # Check if this is an employee row (has ID)
    if id_val and str(id_val).strip() and str(id_val).strip().isdigit():
        employee_count += 1
        print(f"Row {row_idx + 1:2d} | ID: {id_val:3.0f} | Name: {name_val:20} | Dept: {dept_val:3.0f} | Auth: {auth_val}")
    elif name_val and str(name_val).strip() and not str(name_val).startswith('*'):
        # Some rows might have name but not ID
        employee_count += 1
        print(f"Row {row_idx + 1:2d} | ID: {id_val:>8} | Name: {name_val:20} | Dept: {dept_val:3.0f} | Auth: {auth_val}")

print(f"\n✅ Total employees found: {employee_count}")
