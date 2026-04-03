# Firebase Setup for TimeSheet App

## Overview
This TimeSheet application uses Firebase Firestore as a backend for storing attendance reports and employee data. The application is configured to use a **dedicated namespace** to avoid conflicts with other applications using the same Firebase project.

## Firebase Configuration

### Project Details
- **Project ID**: apps-e1163
- **Auth Domain**: apps-e1163.firebaseapp.com
- **Database**: Cloud Firestore
- **Storage**: apps-e1163.firebasestorage.app

### API Key
```
AIzaSyAjGzS58U5ybbI5CYJUk2NRZBuLJpMJihQ
```

## Data Isolation Strategy

### Collection Namespace: `timesheet_app/`

All TimeSheet data is stored under the `timesheet_app` namespace to prevent conflicts with other applications:

```
firestore_root/
├── timesheet_app/              ← TimeSheet App (ISOLATED)
│   └── data/
│       ├── reports/            ← Saved attendance reports
│       │   ├── report_1704067200000/
│       │   │   ├── reportId: "report_1704067200000"
│       │   │   ├── timestamp: 2024-01-01
│       │   │   ├── totalEmployees: 45
│       │   │   ├── employees: [...]
│       │   │   └── dateRange: {...}
│       │   └── report_1704153600000/
│       │
│       ├── employees/          ← Individual employee records
│       │   ├── emp_1001
│       │   ├── emp_1002
│       │   └── ...
│       │
│       └── analytics/          ← Aggregated analytics data
│
├── hifz_classes/               ← Other App (UNTOUCHED)
├── hifz_students/              ← Other App (UNTOUCHED)
├── artifacts/                  ← Other App (UNTOUCHED)
└── attendance_records/         ← Legacy (No Auth)
```

## Security Rules

The Firestore security rules (`firestore.rules`) implement:

1. **Admin-Only Full Access**
   - UID: `MpcB7f35m0bITsSK1D7ACWFmch32`
   - Can read, write, delete everything

2. **TimeSheet App Isolation**
   - Authenticated users can read/write to `timesheet_app/*`
   - Only admin can delete
   - Completely separate from other apps' data

3. **Other Apps Protection**
   - `hifz_classes/`, `hifz_students/`, `artifacts/` remain untouched
   - Each maintains its own access rules
   - No interference from TimeSheet app

## API Reference

### Save Attendance Report
```javascript
await saveAttendanceReport(employees, timestamp)
```
- Saves complete attendance report with all employee data
- Auto-generates unique reportId
- Location: `timesheet_app/data/reports/{reportId}`

### Save Employee Record
```javascript
await saveEmployeeRecord(employee)
```
- Saves individual employee data
- Location: `timesheet_app/data/employees/emp_{id}`

### Load Previous Reports
```javascript
const reports = await loadPreviousReports(limit)
```
- Retrieves previous reports from Firestore
- Optional limit parameter (default: 10)

### Generic Save
```javascript
await saveToFirestore(collectionPath, docId, data)
```
- Generic save function for custom collections
- Example: `saveToFirestore('timesheet_app/data/analytics', 'daily_stats', data)`

## How to Deploy Rules

### Using Firebase Console
1. Go to https://console.firebase.google.com
2. Select project: `apps-e1163`
3. Navigate to Firestore → Rules
4. Copy contents of `firestore.rules`
5. Click "Publish"

### Using Firebase CLI
```bash
firebase login
firebase init firestore
# Replace firestore.rules with the file from this folder
firebase deploy --only firestore:rules
```

## Testing & Verification

### Check Isolation
1. Open Firebase Console
2. Go to Firestore Database
3. Look for `timesheet_app` collection
4. Should see:
   - `timesheet_app/data/reports/` ← Contains saved reports
   - `timesheet_app/data/employees/` ← Individual records
5. Other collections remain unchanged ✅

### Browser Console Logs
When saving a report:
```
✅ Firebase initialized safely for TimeSheet App
📦 Using collection namespace: timesheet_app/data
✅ Saved to Firestore: timesheet_app/data/reports/report_1704067200000
```

## Important Notes

⚠️ **Do NOT Change These:**
- API Key (public, safe to expose)
- Collection namespace (`timesheet_app`)
- Security rules without admin approval

✅ **Safe to Change:**
- Employee data
- Report retention policies
- Analytics calculations
- Add new fields to employee records

## Backup & Recovery

Firestore provides automatic backups. To export data:
```bash
gcloud firestore export gs://your-bucket/backup-folder
```

## Future Enhancements

- [ ] Add real-time sync of employee data
- [ ] Create scheduled analytics aggregation
- [ ] Add export to Google Sheets integration
- [ ] Implement data validation rules
- [ ] Add timestamp-based report versions
- [ ] Create department-level analytics

## Support

For issues or questions, refer to:
- [Firebase Firestore Documentation](https://firebase.google.com/docs/firestore)
- [Security Rules Guide](https://firebase.google.com/docs/firestore/security/start)
- [Dashboard Code](reports/dashboard.html)
