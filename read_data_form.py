import xlrd

file_path = r'data\Employee Form.xls'

try:
    print(f"📄 Reading: {file_path}\n")
    
    wb = xlrd.open_workbook(file_path)
    ws = wb.sheet_by_index(0)
    
    print(f"📊 Total rows: {ws.nrows}")
    print(f"📊 Total columns: {ws.ncols}\n")
    
    print("EMPLOYEES (starting from row 9):")
    print("-" * 120)
    
    employee_count = 0
    for row_idx in range(8, ws.nrows):
        id_val = ws.cell_value(row_idx, 0)
        name_val = ws.cell_value(row_idx, 1)
        dept_val = ws.cell_value(row_idx, 2)
        
        if id_val and str(id_val).strip() and str(id_val).strip().replace('.0', '').isdigit():
            employee_count += 1
            id_clean = int(id_val) if isinstance(id_val, float) else id_val
            print(f"{employee_count:2d}. Row {row_idx + 1:2d} | ID: {id_clean:3} | Name: {str(name_val):30} | Dept: {dept_val}")
    
    print(f"\n✅ Total employees: {employee_count}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
