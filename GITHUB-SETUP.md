# TimeSheet App - GitHub Repository Setup

## Overview
This folder contains the **CODE ONLY** for the TimeSheet application. Data files and documents are kept separate on your local drive and are NOT pushed to GitHub.

## What's in the Repository

### ✅ Files Tracked (In Repo)
```
reports/
├── dashboard.html          ← Main application code
├── index.html             ← Alternative entry point (if needed)

src/                       ← JavaScript modules (if created)
├── firestore.js           ← Firestore functions
├── utils.js               ← Utility functions
└── ...

.gitignore                 ← Defines what NOT to push
GITHUB-SETUP.md           ← This file
README.md                 ← Public documentation
LICENSE                   ← License file
*.md                      ← Documentation files
```

### ❌ Files NOT Tracked (Local Only)
```
data/                      ← Excel files (*.xls, *.xlsx)
documents/                 ← PDFs and reports
archives/                  ← Backup files

*.xls, *.xlsx, *.csv       ← Data files
*.pdf, *.txt               ← Documents

config.firebaserc.js       ← Contains API keys
firestore.rules            ← Security rules
.env, .env.local           ← Environment variables

.venv/, node_modules/      ← Dependencies
```

---

## 🚀 Quick Start: Push Code to GitHub

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. **Repository name**: `iqra-timesheet-app` (or similar)
3. **Description**: "Attendance timesheet dashboard with Firebase integration"
4. **Public/Private**: Your choice
5. **Initialize with README**: NO (we'll push ours)
6. Click **Create Repository**

### Step 2: Initialize Git Locally
```bash
cd "g:\My Drive\00 Engagements\IQRA\Apps\TimeSheet"
git init
git add .
git commit -m "Initial commit: TimeSheet app with Firebase integration"
```

### Step 3: Connect to GitHub
```bash
# Replace YOUR_USERNAME and your-repo-name
git remote add origin https://github.com/YOUR_USERNAME/iqra-timesheet-app.git
git branch -M main
git push -u origin main
```

### Step 4: Verify
Go to your repository URL: `https://github.com/YOUR_USERNAME/iqra-timesheet-app`

---

## 📋 File Organization (What Gets Pushed)

### Public (GitHub)
```
✅ Reports folder with dashboard.html
✅ Source code (if modularized)
✅ README files
✅ .gitignore
✅ License
```

### Private (Local Only)
```
❌ data/ folder (monthly Excel files)
❌ documents/ folder (PDFs, reports)
❌ archives/ folder (backups)
❌ config files with API keys
❌ Security rules files
```

---

## 🔄 Monthly Workflow

1. **Receive** `All Reports.xls` from your team
2. **Open** dashboard from your local folder
3. **Upload** file to dashboard
4. **Edit** if needed (changes are tracked)
5. **Save to Cloud** (saves to Firestore)
6. **Update GitHub** with any code changes (if applicable)

```
All Reports.xls (LOCAL)
    ↓
Dashboard (LOCAL + CODE)
    ↓
Firestore (CLOUD)
GitHub (CODE ONLY)
```

---

## 📊 Repository Structure

```
iqra-timesheet-app/
│
├── reports/
│   └── dashboard.html          ← Main application
│
├── src/                        ← Reusable modules (optional)
│   ├── components/
│   ├── utils/
│   └── services/
│
├── docs/                       ← Documentation
│   ├── SETUP.md
│   ├── USER_GUIDE.md
│   └── ARCHITECTURE.md
│
├── .gitignore                  ← Ignore data files
├── README.md                   ← Project overview
├── LICENSE                     ← License (MIT, etc)
├── GITHUB-SETUP.md            ← This file
└── package.json               ← If using npm
```

---

## 🔐 Security: Keep API Keys Safe

### ❌ NEVER Push
- `config.firebaserc.js` (has API key)
- `.env` files
- `firestore.rules`
- Data files with sensitive info

### ✅ Safe to Push
- `dashboard.html` (API key is public, safe)
- Documentation
- Source code

---

## 🔄 Updating the Repository

### After Making Code Changes

```bash
# Check what changed
git status

# Stage changes
git add reports/dashboard.html

# Commit with message
git commit -m "Add edit functionality with change tracking"

# Push to GitHub
git push origin main
```

### Make Regular Commits

```bash
git add .
git commit -m "Update: Month detection, data merging, edit mode"
git push origin main
```

---

## 📝 Commit Message Examples

Good commit messages:
```
Add month detection from Excel files
Implement change tracking and audit logs
Add editable employee metrics
Fix data merging for duplicate months
Improve UI responsiveness
```

---

## 🆘 If You Make Mistakes

### Undo Last Commit (before push)
```bash
git reset --soft HEAD~1
```

### Undo Push (advanced)
```bash
git revert HEAD
git push origin main
```

### Clear Git History (fresh start)
```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/repo.git
git push -u origin main
```

---

## 👥 Sharing with Team

### Public Repository
- Anyone can see the code
- Team can fork and contribute
- Submit pull requests

### Private Repository  
- Only invited people can see
- More secure
- Still easy to collaborate

### Settings → Collaborators
1. Go to GitHub repo settings
2. Click "Collaborators"
3. Add team members' GitHub usernames

---

## 📚 Resources

- [GitHub Desktop](https://desktop.github.com/) - Visual Git client
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [GitHub Docs](https://docs.github.com/)

---

## 💡 Best Practices

1. **Commit often** - Small, meaningful commits
2. **Clear messages** - Describe what you changed and why
3. **Push regularly** - Don't let changes pile up
4. **Use branches** - For testing new features (advanced)
5. **Review before push** - Check what you're about to push

---

## Example: Complete Monthly Update

```bash
# Start of month: Get latest code
git pull origin main

# During month: Make code improvements
git add reports/dashboard.html
git commit -m "Improve month detection accuracy"

# End of month: Push final code
git push origin main

# Data (Excel files) stays on local drive
# Firestore backup is in cloud
# GitHub has clean code history
```

---

**Status**: Ready for GitHub
**Repo Visibility**: Your choice (public/private)
**Data Security**: Safe (not in repo)
**Backup**: Firestore + GitHub
