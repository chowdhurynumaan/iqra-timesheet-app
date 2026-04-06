import xlrd
import os

file_path = 'Employee Form.xls'

if not os.path.exists(file_path):
    print(f"❌ File not found: {file_path}")
    exit(1)

try:
    wb = xlrd.open_workbook(file_path)
    print(f"✅ Successfully opened: {file_path}")
    print(f"📊 Sheets in workbook: {wb.sheet_names()}\n")
    
    # Read first sheet
    ws = wb.sheet_by_index(0)
    print(f"Sheet: {ws.name}")
    print(f"Dimensions: {ws.nrows} rows × {ws.ncols} columns\n")
    
    # Display all rows
    print("=" * 200)
    print("Content:")
    print("=" * 200)
    for row_idx in range(ws.nrows):
        row_data = []
        for col_idx in range(ws.ncols):
            cell_value = ws.cell_value(row_idx, col_idx)
            if isinstance(cell_value, float):
                if cell_value == int(cell_value):
                    row_data.append(str(int(cell_value)))
                else:
                    row_data.append(str(cell_value))
            else:
                row_data.append(str(cell_value))
        
        print(f"Row {row_idx + 1:2d}: {' | '.join(f'{v[:20]:20}' for v in row_data)}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
