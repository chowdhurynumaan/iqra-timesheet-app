# TimeSheet Project Structure

## Overview
This document describes the reorganized project folder structure for the TimeSheet application.

## Directory Layout

```
TimeSheet/
├── src/                          # Application source code
│   ├── index.html               # Main HTML entry point
│   └── dashboard.html           # Analytics dashboard (primary)
│
├── scripts/                      # Automation and utility scripts
│   ├── python/                  # Python utilities
│   │   ├── read_excel.py
│   │   ├── check_departments.py
│   │   ├── check_departments_v2.py
│   │   ├── read_depts.py
│   │   ├── read_employee_form.py
│   │   ├── count_employees.py
│   │   ├── read_both_forms.py
│   │   └── read_data_form.py
│   │
│   └── powershell/              # PowerShell automation
│       ├── auto-sync.ps1        # Git auto-commit and push
│       ├── setup-autosync.ps1   # Setup script
│       └── deploy-rules.sh      # Firebase rules deployment
│
├── config/                       # Configuration files
│   ├── firestore.rules          # Firestore security rules
│   ├── config.firebaserc.js     # Firebase configuration
│   └── apps-e1163-firebase-adminsdk-fbsvc-88ebd4f358.json  # Firebase credentials
│
├── data/                         # Application data
│   ├── forms/                   # Employee forms and templates
│   │   └── Employee Form.xls    # Master employee list (34 employees)
│   │
│   └── samples/                 # Sample and test data
│       ├── pdf_analysis.json
│       ├── pdf_table_data.json
│       └── daily_breakdown_sample.json
│
├── docs/                         # Documentation
│   ├── README.md                # Project overview
│   ├── START_HERE.md            # Quick start guide
│   ├── FIREBASE_SETUP.md        # Firebase configuration
│   ├── GITHUB-SETUP.md          # GitHub setup instructions
│   ├── IMPLEMENTATION_GUIDE.md  # Development guide
│   ├── AUTO-SYNC-SETUP.md       # Auto-sync configuration
│   ├── USER_GUIDE.md            # User guide
│   └── SETUP.md                 # General setup
│
├── reports/                      # Generated reports (deprecated, see src/)
│   └── dashboard.html           # Legacy dashboard
│
├── archives/                     # Archived/deprecated files
│   ├── Employee Form - Copy.xls
│   ├── Attendance Analytics Pro.pdf
│   └── dashboard_v0.html
│   └── dashboard_v1.html
│
├── documents/                    # Additional documents
│
├── .vscode/                      # VS Code configuration
│   └── tasks.json               # Task definitions
│
└── .venv/                        # Python virtual environment
```

## File Organization Guide

### Source Code (src/)
- **index.html** - Main application entry point
- **dashboard.html** - Primary analytics and reporting interface

### Scripts (scripts/)
- **Python utilities** - Data processing, analysis, and validation scripts
- **PowerShell automation** - Git synchronization and Firebase deployment

### Configuration (config/)
- **Firestore Rules** - Database security and access control
- **Firebase Config** - Project configuration and credentials
- **Environment Setup** - Application secrets (Firebase service account)

### Data (data/)
- **forms/** - Employee roster and form templates
  - Master file: `Employee Form.xls` (34 active employees)
- **samples/** - Sample datasets for testing and analysis

### Documentation (docs/)
- Setup and configuration guides
- User documentation
- Development guides
- Firebase and GitHub setup instructions

## Important Notes

1. **Employee Form Master File**: `data/forms/Employee Form.xls` contains the authoritative employee list with 34 active employees
2. **Deprecated Files**: Old versions in `archives/` are kept for reference but should not be used
3. **Credentials**: Firebase service account JSON is in `config/` and should never be committed to git
4. **Auto-Sync**: PowerShell task in `.vscode/tasks.json` now correctly references `scripts/powershell/auto-sync.ps1`

## Recent Reorganization (Latest Update)

- Moved all Python scripts to `scripts/python/`
- Moved all PowerShell scripts to `scripts/powershell/`
- Consolidated configuration files in `config/`
- Moved documentation to `docs/`
- Consolidated data in `data/` with subfolders for forms and samples
- Moved source files to `src/`
- Updated task references to point to new script locations

This cleaner structure improves maintainability and makes the project easier to navigate.
