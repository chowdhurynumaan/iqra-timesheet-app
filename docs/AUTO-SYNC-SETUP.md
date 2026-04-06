# Auto-Sync Setup Guide

## 🚀 Three Ways to Enable Auto-Commit & Push

### Option 1: Manual Run (One-time)
Run the auto-sync script manually whenever you want:
```powershell
.\auto-sync.ps1
```

### Option 2: VS Code Task
Use VS Code's built-in task runner:
1. Press `Ctrl+Shift+P`
2. Search for "Run Task"
3. Select **"Auto-Sync: Commit & Push"**
4. Changes will be committed and pushed

### Option 3: Scheduled Auto-Sync (Recommended)
Keep changes automatically synced with GitHub every 30 minutes:

#### Step 1: Run the Setup Script
```powershell
# Opens PowerShell as Admin - paste after you run this command:
powershell -Command "Start-Process powershell -Verb RunAs"

# Then paste this in the admin PowerShell:
cd "g:\My Drive\00 Engagements\IQRA\Apps\TimeSheet"
.\setup-autosync.ps1
```

#### Step 2: Choose Your Interval
The default is every 30 minutes. To change:
```powershell
.\setup-autosync.ps1 -Interval 5min    # Every 5 minutes
.\setup-autosync.ps1 -Interval 15min   # Every 15 minutes
.\setup-autosync.ps1 -Interval hourly  # Every hour
```

#### Step 3: Verify It's Working
Windows will run the task automatically in the background. Check:
1. Open **Task Scheduler** (Windows + R → `taskschd.msc`)
2. Find **"TimeSheet-AutoSync"** in the task list
3. Right-click → **Run** to test immediately

#### To Remove Scheduled Task:
```powershell
.\setup-autosync.ps1 -Uninstall
```

---

## What Gets Committed?

✅ **Included**: Code files (HTML, CSS, JS)
❌ **Excluded**: Data files (Excel, JSON), node_modules, local files (see .gitignore)

So your Excel reports and data stay private locally, only code syncs to GitHub.

---

## Git Hooks (Automatic Push)

The repository also has a post-commit hook that automatically pushes after each manual commit:
- Location: `.git/hooks/post-commit`
- Effect: Any time you `git commit`, it automatically runs `git push`

---

## Example Workflow

```
1. You upload a new Excel file to dashboard.html
2. You edit the dashboard code
3. Every 30 minutes → auto-sync runs
4. Changes are automatically:
   - Committed: "Auto-sync: 2026-04-05 14:30:00"
   - Pushed: To GitHub main branch
5. Your GitHub repo stays up-to-date automatically
```

---

## Troubleshooting

**Scheduled task doesn't run?**
- Ensure PowerShell execution policy allows scripts: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
- Run the setup script with admin privileges

**Push fails silently?**
- Check GitHub credentials are stored (Windows Credential Manager)
- Run `git push` manually to see any auth errors

**Want to see what's being committed?**
- Open a terminal and run: `git log --oneline -10` to see recent commits
