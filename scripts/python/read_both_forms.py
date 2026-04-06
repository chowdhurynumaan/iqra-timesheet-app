import xlrd

files_to_check = [
    'Employee Form.xls',
    'Employee Form - Copy.xls'
]

for file_path in files_to_check:
    try:
        print(f"\n{'='*100}")
        print(f"📄 Reading: {file_path}")
        print(f"{'='*100}\n")
        
        wb = xlrd.open_workbook(file_path)
        ws = wb.sheet_by_index(0)
        
        print(f"📊 Total rows: {ws.nrows}")
        print(f"📊 Total columns: {ws.ncols}\n")
        
        print("EMPLOYEES (starting from row 9):")
        print("-" * 100)
        
        employee_count = 0
        for row_idx in range(8, ws.nrows):  # Start from row 9 (index 8)
            id_val = ws.cell_value(row_idx, 0)
            name_val = ws.cell_value(row_idx, 1)
            dept_val = ws.cell_value(row_idx, 2)
            
            # Check if this is an employee row (has ID)
            if id_val and str(id_val).strip() and str(id_val).strip().replace('.0', '').isdigit():
                employee_count += 1
                id_clean = int(id_val) if isinstance(id_val, float) else id_val
                print(f"{employee_count:2d}. Row {row_idx + 1:2d} | ID: {id_clean:3} | Name: {name_val:25} | Dept: {dept_val}")
        
        print(f"\n✅ Total employees: {employee_count}")
        
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
