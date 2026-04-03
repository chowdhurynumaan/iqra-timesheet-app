# TimeSheet Dashboard - Setup Guide

## 🚀 Initial Setup (One Time)

### Step 1: Prerequisites

Before you begin, you need:
- ✅ Web browser (Chrome, Firefox, Edge, Safari)
- ✅ Internet connection
- ✅ Firebase account (already set up)
- ✅ GitHub account (for code backup)
- ✅ Excel file with attendance data

### Step 2: Access the Dashboard

You already have everything set up! Just open:

```
reports/dashboard.html
```

Or use the full path:
```
G:\My Drive\00 Engagements\IQRA\Apps\TimeSheet\reports\dashboard.html
```

### Step 3: Firebase Authentication

First time you save to cloud:
1. Dashboard will prompt you to authenticate
2. Sign in with Google or email
3. Grant Firebase permissions
4. You're done!

This only happens once. Future saves will be automatic.

---

## 📋 File Distribution

### What You Have Locally
```
G:\My Drive\00 Engagements\IQRA\Apps\TimeSheet\
├── reports/
│   └── dashboard.html          ← USE THIS
├── data/
│   └── *.xls files             ← Store monthly files here
├── documents/
│   └── *.pdf files             ← Reports and docs
├── archives/
│   └── *.xlsx, *.html         ← Old backups
└── (config files)
```

### What's Backed Up in Cloud
- ☁️ Firestore: All employee data and change history
- 🐙 GitHub: Dashboard code (dashboard.html only)

### What's Automatically Organized
```
Firestore Structure:
timesheet_app/
├── data/
│   ├── reports/           (All complete reports)
│   ├── months/            (Organized by month)
│   │   ├── 2024_01/
│   │   ├── 2024_02/
│   │   ├── 2024_03/
│   │   └── 2024_04/
│   └── employees/         (Individual records)
└── audit/                 (Change history)
```

---

## 🔐 Security & Backups

### Your Data is Safe
- ✅ Firestore automatically backs up everything
- ✅ Change history kept forever
- ✅ Month-based organization
- ✅ Employee records indexed

### Your Code is Versioned
- ✅ GitHub has all code changes
- ✅ Easy rollback if needed
- ✅ Public sharing available
- ✅ Collaborate with team

### Your Files are Private
- ✅ Data files stay on your computer
- ✅ Config files not in GitHub
- ✅ Sensitive info protected
- ✅ .gitignore prevents accidents

---

## 📅 Monthly Process

### Month Begins
1. ✅ Receive `All Reports.xls` from team
2. ✅ Dashboard is ready to use

### During Month (Optional)
- 🔄 Can upload updated files anytime
- 📝 Make edits with full tracking
- ☁️ Save to cloud as needed

### End of Month
1. 📤 Upload final `All Reports.xls`
2. ✏️ Make any corrections
3. ☁️ Click "Save to Cloud"
4. ✅ Data merged and tracked
5. 🎯 Everything's done!

### Start of Next Month
1. Repeat with new Excel file
2. Dashboard remembers previous months
3. Detects new month automatically
4. Merges new data smartly

---

## 🔧 Configuration (Already Done)

### Firebase Setup ✅
- Project: `apps-e1163`
- Database: Firestore
- Namespace: `timesheet_app`
- Rules: Deployed (data isolated)

### Git Setup ✅
- Local repository ready
- .gitignore configured
- Ready to push to GitHub

### Dashboard Setup ✅
- Code optimized
- Change tracking enabled
- Month detection built-in
- Data merging automatic

---

## 🐙 Push to GitHub (First Time)

### Option A: Using PowerShell (Easiest)

```powershell
cd "g:\My Drive\00 Engagements\IQRA\Apps\TimeSheet"

# Initialize Git
git init
git add .
git commit -m "Initial commit: TimeSheet app with Firebase integration"

# Connect to GitHub (replace USERNAME and repo-name)
git remote add origin https://github.com/USERNAME/iqra-timesheet-app.git
git branch -M main
git push -u origin main
```

### Option B: Using GitHub Desktop (GUI)

1. Download: https://desktop.github.com/
2. Create repo: File → New Repository
3. Name: `iqra-timesheet-app`
4. Local path: Your TimeSheet folder
5. Click "Create Repository"
6. Publish to GitHub (button on top)

### Option C: On GitHub.com

1. Go to https://github.com/new
2. Create repository with name
3. Follow instructions
4. Push using command line

---

## 📝 After First Push

### Regular Updates

```powershell
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Description of what changed"

# Push
git push
```

### Example Commits

```
"Update month detection for 2024 data"
"Improve change tracking display"
"Fix data merging logic"
"Add employee edit functionality"
```

---

## ✅ Verification Checklist

After setup, verify everything:

- [ ] Dashboard opens in browser
- [ ] Upload button works
- [ ] Can select Excel file
- [ ] Data displays correctly
- [ ] Can click "Save to Cloud"
- [ ] Firestore shows data
- [ ] GitHub has code backed up
- [ ] .gitignore preventing data files

---

## 📊 Testing the Full Workflow

### Test 1: Upload & Save

```
1. Open dashboard.html
2. Click "Upload Report"
3. Select monthly Excel file
4. Data displays
5. Click "☁️ Save to Cloud"
6. Confirm changes
✅ SUCCESS: Data saved to Firestore
```

### Test 2: Edit & Track

```
1. Click ✏️ Edit on any employee
2. Change a value
3. Click 💾 Save Changes
4. See confirmation message
✅ SUCCESS: Change tracked and saved
```

### Test 3: Upload Again (Merge)

```
1. Upload same file again
2. Dashboard shows "No changes"
3. Try uploading modified file
4. Dashboard shows what changed
✅ SUCCESS: Smart merging works
```

### Test 4: GitHub Push

```
1. Open PowerShell
2. cd to TimeSheet folder
3. git push
4. Check GitHub.com
✅ SUCCESS: Code backed up on GitHub
```

---

## 🆘 If Something Doesn't Work

### "Dashboard won't load"
- Check file path is correct
- Right-click file → "Open with" → Browser
- Try different browser

### "Firebase not responding"
- Check internet connection
- Try again in 30 seconds
- Check Firebase console

### "Git command not found"
- Install Git: https://git-scm.com/
- Restart PowerShell
- Try again

### "Can't push to GitHub"
- Create repo first on GitHub.com
- Use correct repository URL
- Check username/token

---

## 📞 Getting Help

### For Dashboard Issues
- Check [USER_GUIDE.md](USER_GUIDE.md)
- Review [Firebase Setup](../FIREBASE_SETUP.md)
- Check browser console (F12)

### For Git Issues
- Check [GitHub Setup](../GITHUB-SETUP.md)
- Review Git basics
- GitHub has excellent docs

### For Data Issues
- Check Firestore Console
- Review change log
- Backup in archives folder

---

## 🎯 You're All Set!

Everything is configured and ready to use:

✅ Dashboard works locally  
✅ Firebase stores data  
✅ GitHub backs up code  
✅ Change tracking enabled  
✅ Month detection works  
✅ Data merging smart  
✅ Edit functionality ready  

**Start using it:**
1. Open `reports/dashboard.html`
2. Upload your next `All Reports.xls`
3. Click "☁️ Save to Cloud"
4. All done!

---

**Happy timesheeting!** 🎉
