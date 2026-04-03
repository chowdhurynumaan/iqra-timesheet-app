# TimeSheet Dashboard - User Guide

## 📖 Step-by-Step Usage

### Step 1: Open the Dashboard

Open your web browser and navigate to:
```
File → Open... → Select: reports/dashboard.html
```

Or use the absolute path:
```
file:///G:/My Drive/00 Engagements/IQRA/Apps/TimeSheet/reports/dashboard.html
```

The dashboard will load with:
- Upload button at the top
- Empty table ready for data
- Firebase connection initialized

### Step 2: Upload Your Monthly Report

1. **Click** "Upload Report" button (top left)
2. **Select** your `All Reports.xls` file
3. **Wait** for parsing (takes 2-5 seconds)
4. Dashboard will display all employees

### Step 3: Review the Data

The dashboard shows:

#### 📊 Top Statistics
- **Total Employees** - Count of all employees
- **Total Absences** - Days missed across org
- **Total Late Minutes** - Minutes late across org
- **Avg. Attendance** - Overall attendance %

#### 📈 Charts
- **Top 15 Late Arrivals** - Bar chart of employees
- **Attendance by Department** - Department breakdown
- **Late Minutes by Department** - Dept lateness

#### 👥 Employee Cards
Each employee shows:
- **Name & ID** - Employee identification
- **Performance Tier** - Excellent/Good/At Risk/Critical
- **Attendance %** - Percentage of days present
- **Punctuality %** - On-time percentage
- **Hours** - Total hours worked
- **Late Minutes** - Total late minutes
- **Absences** - Days missed
- **Days Worked** - Total working days

#### 📋 Daily Breakdown
For each employee, click to expand:
- Date, Day name
- Clock in/out times
- Hours that day
- Late minutes if applicable
- Status (✅ on-time, ⚠️ incomplete, ❌ absent)

### Step 4: Filter & Search

#### Search by Name or ID
```
🔍 Search box: Type employee name or ID
```

#### Filter by Department
```
1. Click Department dropdown
2. Select specific department
3. Dashboard updates
```

#### Filter by Date Range
```
1. Select Start Date
2. Select End Date
3. Click "Apply" button
4. Shows data only for that period
```

### Step 5: Make Changes (Edit Mode)

#### Edit Employee Data

1. **Click ✏️ Edit** button on any employee card
2. **Edit the following fields** (highlighted in yellow):
   - Hours
   - Late Minutes
   - Absences
3. **Click 💾 Save Changes**
4. Change is logged and saved

#### Change Tracking

Every change shows:
- Employee name
- Field modified
- Old value → New value
- Timestamp
- Who made the change (if auth enabled)

### Step 6: Save to Cloud

#### Manual Save

1. **Click ☁️ Save to Cloud** button
2. **Review summary**:
   - New records
   - Modified records
   - Unchanged records
   - Detailed field changes
3. **Click OK** to confirm
4. **Data saves to Firestore** with full audit trail

#### What Gets Saved
```
For April 2024, all employees:
├── Report ID: report_2024_04_xxxxx
├── Metadata: Month, year, date range
├── Change log: All modifications
├── Employee data: Complete records
└── Audit trail: Who, what, when
```

### Step 7: Export Data

#### Export as CSV
```
Click: Export CSV
→ Downloads: attendance_report.csv
```

#### Export as Excel
```
Click: Export Excel
→ Downloads: attendance_report.xlsx
```

#### Print Selected Employees
```
1. Click checkbox next to employee name
2. Click: Print Selected
3. Print dialog appears
4. Choose printer and print
```

---

## 🎯 Common Workflows

### Workflow 1: First Time Setup

```
1. Open dashboard.html
2. Click "Upload Report"
3. Select All Reports.xls
4. Review data displayed
5. Click "☁️ Save to Cloud"
6. Confirm save
✅ Data saved to Firestore
```

### Workflow 2: Monthly Update

```
1. Open dashboard.html
2. Upload new All Reports.xls
3. Dashboard shows:
   - New employees (if any)
   - Modified hours (if any)
   - Missing records (if any)
4. Review changes shown in popup
5. Click "☁️ Save to Cloud"
✅ Month data updated with change tracking
```

### Workflow 3: Fix Employee Error

```
1. Find employee in dashboard
2. Click ✏️ Edit
3. Change the incorrect field
4. Click 💾 Save Changes
✅ Change saved with audit trail
```

### Workflow 4: Department Report

```
1. Click Department dropdown
2. Select specific department
3. View only that department
4. Click "Export CSV" or "Print Selected"
✅ Department report ready
```

---

## 🔍 Understanding the Data

### Performance Tiers

| Tier | Criteria | Color |
|------|----------|-------|
| **Excellent** | No absences, ≤0 late min | 🟢 Green |
| **Good** | ≤1 absence, ≤100 late min | 🟢 Green |
| **At Risk** | >1 absence, >100 late min | 🟠 Amber |
| **Critical** | >3 absences OR >200 late min | 🔴 Red |

### Metrics Explained

- **Attendance %**: (Days Worked / Total Days) × 100
- **Punctuality %**: 100 - ((Late Days / Days Worked) × 100)
- **Late Minutes**: Minutes after start time (e.g., 9:15 AM = 15 min late)
- **Absences**: Days with no punch record
- **Worked Days**: Days employee checked in

### Daily Status Indicators

| Icon | Meaning |
|------|---------|
| ✅ | Checked in, on time, complete day |
| ⚠️ | Incomplete punch (missing in/out) |
| ❌ | Entire day missed (absent) |

---

## ⚙️ Settings & Controls

### Control Panel

Located below stats, includes:

1. **Data Source**
   - Sheet selector
   - Choose which sheet to parse
   - Default: Auto-detect

2. **Department**
   - Dropdown filter
   - Shows: All, Operations, etc.
   - Updates display instantly

3. **Date Range**
   - Start date picker
   - End date picker
   - Apply button
   - Filters displayed data

4. **Export Options**
   - CSV export (spreadsheet)
   - Excel export (formatted)
   - ☁️ Cloud save (Firestore)
   - Print (formatted output)

---

## 💡 Tips & Tricks

### Tip 1: Bulk Edit
1. Edit multiple employees one at a time
2. Each saves separately
3. All tracked in audit log
4. Save to cloud at end (includes all changes)

### Tip 2: Export Before Save
1. Make edits
2. Export to Excel
3. Review exported file
4. Save to cloud

### Tip 3: Check Daily Details
1. Hover over employee card
2. Scroll to Daily Breakdown
3. See punch times per day
4. Click a day to see details

### Tip 4: Print by Department
1. Filter by department
2. Select relevant employees
3. Click Print Selected
4. Choose: Print to PDF or Printer

### Tip 5: Data Comparison
1. Save report to cloud at month start
2. Upload updated file mid-month
3. See exactly what changed
4. Decide to accept or reject changes

---

## 🔜 What Happens After Save

### On Firestore

Your data is organized by month:
```
timesheet_app/
├── data/
│   └── months/
│       └── 2024_04/           (April 2024)
│           ├── report_...     (Complete report)
│           ├── emp_1001       (Ahmed Khan)
│           ├── emp_1002       (Fatima Ahmed)
│           └── ...
└── audit/
    └── audit_2024_04_...      (Change history)
```

### On GitHub (Code)

Your code is backed up:
```
Your repository (iqra-timesheet-app)
├── reports/
│   └── dashboard.html
├── README.md
└── (Other code files)
```

### In Your Browser

Next time you:
1. Open dashboard.html
2. Upload report
3. Previous month data loads from Firestore
4. New changes merge automatically

---

## 🆘 Troubleshooting

### "File won't upload"
**Solution**: 
- Ensure file is `.xls` or `.xlsx`
- Try opening file in Excel first to verify it's valid
- Rename to `All Reports.xls` exactly

### "Data looks wrong"
**Solution**:
- Check date range in file header
- Verify sheet name is correct
- Look at console (F12) for error messages

### "Can't edit field"
**Solution**:
- Click ✏️ Edit button first
- Field should turn yellow
- Type new value
- Click 💾 Save Changes

### "Changes not saving to cloud"
**Solution**:
- Check internet connection
- Try saving again
- Look for error popup
- Check browser console (F12)

### "Employee data seems incomplete"
**Solution**:
- Check Daily Breakdown section
- Scroll down in employee card
- Look at punch times
- Compare with original file

---

## 📞 Need Help?

1. **Check Daily Breakdown** - See actual punch times
2. **Review Change Log** - See what was modified
3. **Look at Firestore** - Verify data saved
4. **Check Browser Console** - F12 → Console tab
5. **Re-upload file** - Start fresh if needed

---

## ✅ Checklist: Before You Save

Before clicking "Save to Cloud":

- [ ] Uploaded the correct file
- [ ] Month detected correctly
- [ ] All employees showing
- [ ] Hours look reasonable
- [ ] No obvious errors
- [ ] Made any needed edits
- [ ] Reviewed change summary

---

**Good luck using the TimeSheet Dashboard!** 🎉
