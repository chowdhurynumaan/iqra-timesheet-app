# Duplicate Employee Cleanup Guide

This guide explains how to safely remove duplicate employee records from Firestore using the cleanup script.

## Quick Start

### Step 1: Get Your Firebase Service Account Key

1. Open [Firebase Console](https://console.firebase.google.com)
2. Select the **apps-e1163** project (it should be at the top)
3. Click the **⚙️ Settings icon** (top left, near project name)
4. Go to the **"Service Accounts"** tab
5. Click the blue **"Generate New Private Key"** button
6. A JSON file will download automatically:
   - File name: `apps-e1163-xxxxxxxxxxxxx.json`
   - This is your **service account key**

### Step 2: Place the Key File

1. **Rename** the downloaded file to: `serviceAccountKey.json`
2. **Move it** to your project root folder:
   ```
   g:\My Drive\00 Engagements\IQRA\Apps\TimeSheet\serviceAccountKey.json
   ```

### Step 3: Install Dependencies

Open PowerShell in your project folder and run:

```powershell
npm install firebase-admin
```

### Step 4: Run the Cleanup Script

```powershell
node cleanup-duplicates.js
```

## What the Script Does

✅ **Safe & Non-Destructive:**
- Scans all employee records in Firestore
- Groups them by Employee ID + Month
- **Keeps** the oldest version (first uploaded)
- **Deletes** newer duplicates
- Shows a detailed log of what will be deleted before confirming

📊 **Example Output:**
```
🔍 Scanning for duplicate employee records...

Found 39 total employee records

⚠️  Found 2 copies of: ABDUR RASHID (ID: 7, Month: 2026_03)
   🗑️  Will delete: employees/emp_7_2026_03_old

📋 Summary:
   Total records: 39
   Duplicates found: 1
   Will delete: 1 documents

🗑️  Deleting duplicate documents...

   ✅ Deleted: employees/emp_7_2026_03_old
```

## Security Notes

⚠️ **IMPORTANT:**
- The `serviceAccountKey.json` contains sensitive credentials
- **NEVER commit it to GitHub** (it's in `.gitignore`)
- **NEVER share it** with anyone
- Delete it from your local machine after running the script (or keep it safe)
- If accidentally exposed, regenerate a new key from Firebase Console

## Troubleshooting

**Error: "Service account key not found"**
- Make sure you renamed the file to `serviceAccountKey.json`
- Make sure it's in the project root folder (same level as `dashboard.html`)
- Check the file extension is `.json` (not `.txt`)

**Error: "Firebase Admin not initialized"**
- The service account key might be invalid or corrupted
- Try downloading a fresh key from Firebase Console

**Error: Permission denied**
- Your user account might not have permission to delete from Firestore
- Ask your Firebase admin to grant you `Editor` role or delete permissions

## After Cleanup

1. ✅ Verify in [Firebase Console Firestore](https://console.firebase.google.com) that duplicates are gone
2. 💾 Optional: Delete `serviceAccountKey.json` from your machine for security
3. 🔄 Refresh your dashboard - it should no longer show duplicate employees

## Questions?

If something goes wrong:
1. Save the full error message
2. Check that your `serviceAccountKey.json` is valid
3. Verify you have the correct Firebase project selected
