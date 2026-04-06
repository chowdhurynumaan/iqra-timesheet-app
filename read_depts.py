import zipfile
import xml.etree.ElementTree as ET

def extract_departments_from_xlsx(filepath):
    try:
        with zipfile.ZipFile(filepath, 'r') as zf:
            # Try to read shared strings (may not exist)
            shared_strings = []
            try:
                strings_xml = zf.read('xl/sharedStrings.xml').decode('utf-8')
                strings_root = ET.fromstring(strings_xml)
                for si in strings_root.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                    t_elem = si.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                    if t_elem is not None:
                        shared_strings.append(t_elem.text or '')
                    else:
                        shared_strings.append('')
                print("Using shared strings for cell values")
            except:
                print("No shared strings file found, will use inline values")
            
            # List all sheet files
            sheets = [f for f in zf.namelist() if f.startswith('xl/worksheets/sheet')]
            print(f"Found {len(sheets)} worksheets: {sheets}\n")
            
            # List all files for debugging
            all_files = zf.namelist()
            xl_files = [f for f in all_files if f.startswith('xl/')]
            print(f"Files in xl/ folder: {xl_files[:15]}\n")
            
            if sheets:
                sheet_xml = zf.read(sheets[0]).decode('utf-8')
                root = ET.fromstring(sheet_xml)
                
                # Find all rows
                rows = root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row')
                print(f"Found {len(rows)} rows in first sheet\n")
                
                # Extract header row and find department column
                if rows:
                    header_row = rows[0]
                    header_cells = header_row.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
                    headers = []
                    dept_col_idx = None
                    
                    for col_idx, cell in enumerate(header_cells):
                        # Try to get value - first check for reference to shared strings
                        val_elem = cell.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                        if val_elem is not None and val_elem.text:
                            try:
                                if shared_strings:
                                    str_idx = int(val_elem.text)
                                    header_val = shared_strings[str_idx] if str_idx < len(shared_strings) else val_elem.text
                                else:
                                    header_val = val_elem.text
                            except:
                                header_val = val_elem.text
                        else:
                            header_val = ''
                        
                        headers.append(header_val)
                        if 'dept' in str(header_val).lower() or 'section' in str(header_val).lower():
                            dept_col_idx = col_idx
                    
                    print(f"Headers: {headers}\n")
                    
                    if dept_col_idx is not None:
                        print(f"Department column found at index {dept_col_idx}: {headers[dept_col_idx]}\n")
                        departments = set()
                        
                        # Extract departments from all rows (skip header)
                        for row in rows[1:]:
                            cells = row.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c')
                            if len(cells) > dept_col_idx:
                                cell = cells[dept_col_idx]
                                val_elem = cell.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                                if val_elem is not None and val_elem.text:
                                    try:
                                        if shared_strings:
                                            str_idx = int(val_elem.text)
                                            dept = shared_strings[str_idx] if str_idx < len(shared_strings) else val_elem.text
                                        else:
                                            dept = val_elem.text
                                    except:
                                        dept = val_elem.text
                                    
                                    if dept and str(dept).strip():
                                        departments.add(str(dept).strip())
                        
                        print(f"Unique Departments ({len(departments)}):")
                        for dept in sorted(departments):
                            print(f"  • {dept}")
                    else:
                        print("Department column not found")
                        print(f"Available headers: {headers}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

extract_departments_from_xlsx('data/employee_form.xls')
