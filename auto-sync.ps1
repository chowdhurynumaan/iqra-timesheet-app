# Auto-commit and push script for TimeSheet App
# Usage: Run this periodically to auto-commit all changes

$RepoPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RepoPath

# Commit all changes
Write-Host "📝 Committing changes..." -ForegroundColor Green
git add -A
$Status = git status --porcelain

if ($Status) {
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Message = "Auto-sync: $Timestamp"
    git commit -m $Message
    
    # Push to remote
    Write-Host "📤 Pushing to GitHub..." -ForegroundColor Cyan
    git push origin main
    Write-Host "✅ Auto-sync complete!" -ForegroundColor Green
} else {
    Write-Host "✓ No changes to commit" -ForegroundColor Yellow
}
