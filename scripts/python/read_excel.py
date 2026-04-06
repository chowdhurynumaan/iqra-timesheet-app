import xlrd
import os

file_path = 'Employee Form.xls'

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit(1)

try:
    wb = xlrd.open_workbook(file_path)
    print(f"✅ Successfully opened: {file_path}")
    print(f"📊 Sheets in workbook: {wb.sheet_names()}\n")
    
    # Read each sheet
    for sheet_idx, sheet_name in enumerate(wb.sheet_names()):
        ws = wb.sheet_by_index(sheet_idx)
        print(f"\n{'='*80}")
        print(f"Sheet {sheet_idx + 1}: {sheet_name}")
        print(f"{'='*80}")
        print(f"Dimensions: {ws.nrows} rows × {ws.ncols} columns\n")
        
        # Display first 20 rows
        print("Data:")
        print("-" * 80)
        for row_idx in range(min(20, ws.nrows)):
            row_data = []
            for col_idx in range(ws.ncols):
                cell_value = ws.cell_value(row_idx, col_idx)
                # Format for display
                if isinstance(cell_value, float):
                    if cell_value == int(cell_value):
                        row_data.append(str(int(cell_value)))
                    else:
                        row_data.append(str(cell_value))
                else:
                    row_data.append(str(cell_value))
            
            # Print row
            print(f"Row {row_idx + 1:2d}: {' | '.join(f'{v[:15]:15}' for v in row_data[:10])}")
        
        if ws.nrows > 20:
            print(f"... ({ws.nrows - 20} more rows)")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
