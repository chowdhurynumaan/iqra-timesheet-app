# TimeSheet Attendance Dashboard

A smart attendance tracking and reporting application that parses Excel timesheets, displays employee metrics, and saves data to Firebase Firestore with automatic change tracking.

## ✨ Features

### Core Functionality
- 📊 **Upload & Parse** - Supports CSV, XLS, XLSX files
- 🎯 **Smart Detection** - Automatically detects month from data
- 📈 **Rich Analytics** - Attendance rates, late arrivals, department summaries
- ☁️ **Cloud Sync** - Saves to Firebase Firestore
- 📝 **Edit Tracking** - Full audit log of all changes
- 🔍 **Smart Merge** - Detects new, modified, and unchanged data

### Dashboard Features
- 👥 **Employee Performance** - Color-coded performance tiers
- 📋 **Daily Breakdown** - Detailed punch time analysis
- 📊 **Charts** - Visual analytics with Chart.js
- 🖨️ **Print & Export** - CSV, Excel, and print-ready formats
- 🔐 **Secure** - Firebase authentication and isolation

## 🚀 Quick Start

### 1. Open Dashboard
```
Open in browser: reports/dashboard.html
```

### 2. Upload Monthly Report
- Click "Upload Report" 
- Select your `All Reports.xls` file
- Wait for data parsing

### 3. Review Data
- Check employee metrics
- Verify attendance rates
- Review late arrivals

### 4. Save to Cloud
- Click "☁️ Save to Cloud"
- Confirm data changes
- Data saved with audit trail

### 5. Edit if Needed
- Click "✏️ Edit" on any employee
- Modify times, hours, or absences
- Click "💾 Save Changes"
- All edits are tracked

## 📁 Repository Structure

```
reports/
├── dashboard.html              ← Main application

docs/
├── SETUP.md                   ← Setup guide
├── USER_GUIDE.md              ← How to use
└── ARCHITECTURE.md            ← Technical design

.gitignore                     ← What NOT to push
README.md                      ← This file
LICENSE                        ← License
```

## 🛠️ Technologies

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Firebase Firestore
- **Libraries**: 
  - Chart.js - Analytics charts
  - PapaParse - CSV parsing
  - XLSX - Excel parsing

## 📌 Monthly Workflow

```
1. Receive: All Reports.xls (from team)
   ↓
2. Upload: To dashboard
   ↓
3. Detect: Month automatically
   ↓
4. Merge: Compare with existing Firestore data
   ↓
5. Review: Check new/modified/unchanged records
   ↓
6. Save: To Firestore with change tracking
   ↓
7. Edit: Make adjustments if needed (tracked)
   ↓
8. Archive: Data stays in cloud, code in GitHub
```

## 🔄 Data Flow

```
Your Computer (Local)
├── All Reports.xls (data file)
├── dashboard.html (code)
└── Browser uploads file

Firebase Firestore (Cloud)
├── timesheet_app/data/reports/ (all reports)
├── timesheet_app/data/months/{YYYY_MM}/ (by month)
├── timesheet_app/audit/ (change history)
└── timesheet_app/employees/ (individual records)

GitHub (Code Repository)
└── dashboard.html (only code, no data)
```

## 🔐 Security

- **Data Isolation**: TimeSheet data in separate Firestore namespace
- **Access Control**: Firestore rules manage who can read/write
- **Audit Trail**: All changes logged with timestamps and user info
- **No Secrets in GitHub**: API keys and sensitive config stay local
- **Firebase Auth**: Only authenticated users can save data

## 📊 Change Tracking

Every data modification is tracked:

```
{
  timestamp: "2024-04-03T15:30:00Z",
  empId: "1001",
  empName: "Ahmed Khan",
  field: "lateMin",
  oldValue: "45",
  newValue: "50",
  changedBy: "user@example.com",
  changeType: "MODIFIED"
}
```

## 📈 Supported File Formats

| Format | Support | Example |
|--------|---------|---------|
| Excel (.xlsx) | ✅ Full | All Reports.xlsx |
| Excel (.xls) | ✅ Full | All Reports.xls |
| CSV (.csv) | ✅ Full | attendance.csv |
| PDF | ❌ No | - |

## 🎯 Data Merge Logic

When uploading new data:

| Case | Action | Example |
|------|--------|---------|
| New employee | ✅ Add | ID 1045 not in Jan data |
| Modified data | 🔄 Update | Hours changed 160→165 |
| Same data | ⚠️ Skip | No changes detected |
| Deleted employee | 🗑️ Note | Employee in Firestore but not in file |

## 📋 Excel File Format Supported

The dashboard auto-detects these sheet types:
- `Attend. Logs` - Detailed punch times
- `Attendance summary` - Summary metrics
- `Abnormal` - Exceptions and anomalies
- `Schedu. information sheet` - Schedule data
- `Attend. Report` - Generic attendance reports

## 🖥️ System Requirements

- Modern web browser (Chrome, Firefox, Edge, Safari)
- Internet connection (for Firestore sync)
- Excel file (Any month's data)

## 📚 Documentation

- **[User Guide](docs/USER_GUIDE.md)** - How to use the dashboard
- **[Setup Guide](docs/SETUP.md)** - Initial setup instructions
- **[Architecture](docs/ARCHITECTURE.md)** - Technical design details
- **[Firebase Config](../FIREBASE_SETUP.md)** - Database configuration
- **[GitHub Setup](../GITHUB-SETUP.md)** - Push code to GitHub

## 🐛 Troubleshooting

### File won't upload
- Ensure file is valid Excel or CSV
- Check file isn't corrupted
- Try renaming to `All Reports.xlsx`

### Data not saving to cloud
- Check internet connection
- Verify Firebase is initialized
- Check browser console (F12) for errors

### Month not detected
- Ensure file has date range (DD-MM-YYYY ~ DD-MM-YYYY)
- Or include month name in header
- Check first few rows for date info

### Firestore not showing data
- Go to Firebase Console
- Select project: `apps-e1163`
- Navigate to Firestore Database
- Look for: `timesheet_app/data/`

## 🤝 Contributing

Improvements welcome! 

```bash
# Fork the repository
# Create a branch
git checkout -b feature/your-feature

# Make changes
# Commit
git add .
git commit -m "Add feature description"

# Push
git push origin feature/your-feature

# Create Pull Request on GitHub
```

## 📞 Support

- Check documentation files first
- Review console logs (F12)
- Check Firebase Console for data
- Verify Firestore security rules

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🎉 Version History

- **v1.0** (April 2024) - Initial release
  - Upload & parse Excel files
  - Display attendance dashboard
  - Firebase Firestore integration
  - Monthly data organization
  - Change tracking & audit logs
  - Editable fields with full history

## 📝 Notes

- **Data Files**: Not included in repo (stay on your local drive)
- **API Keys**: Safely in Firebase config (not in GitHub)
- **Backup**: Firestore provides automatic backups
- **Archives**: Old files kept for reference

---

**Status**: Production Ready ✅  
**Last Updated**: April 2024  
**Maintained By**: IQRA Team  
**Project**: TimeSheet Attendance App
