# Setup Auto-Sync Scheduled Task for TimeSheet App
# This script creates a Windows Scheduled Task that runs auto-sync every 5 minutes

param(
    [ValidateSet("5min", "15min", "30min", "hourly")]
    [string]$Interval = "30min",
    
    [switch]$Uninstall
)

$TaskName = "TimeSheet-AutoSync"
$RepoPath = "g:\My Drive\00 Engagements\IQRA\Apps\TimeSheet"
$ScriptPath = "$RepoPath\auto-sync.ps1"
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERNAME" -LogonType Interactive -RunLevel Highest

$Trigger = switch($Interval) {
    "5min" { New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 5) -RepetitionDuration (New-TimeSpan -Days 999) -At (Get-Date).AddMinutes(1) -Once }
    "15min" { New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 15) -RepetitionDuration (New-TimeSpan -Days 999) -At (Get-Date).AddMinutes(1) -Once }
    "30min" { New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration (New-TimeSpan -Days 999) -At (Get-Date).AddMinutes(1) -Once }
    "hourly" { New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Hours 1) -RepetitionDuration (New-TimeSpan -Days 999) -At (Get-Date).AddMinutes(1) -Once }
}

$Action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-ExecutionPolicy Bypass -NoProfile -File `"$ScriptPath`""

if ($Uninstall) {
    try {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "✅ Auto-sync scheduled task removed!" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Task not found or error removing it" -ForegroundColor Yellow
    }
} else {
    try {
        # Remove existing task if it exists
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
        
        # Create new task
        Register-ScheduledTask `
            -TaskName $TaskName `
            -Principal $Principal `
            -Action $Action `
            -Trigger $Trigger `
            -Description "Automatically commit and push TimeSheet app changes every $Interval" `
            -Force | Out-Null
            
        Write-Host "✅ Auto-sync scheduled task created successfully!" -ForegroundColor Green
        Write-Host "   Task: $TaskName" -ForegroundColor Gray
        Write-Host "   Interval: Every $Interval" -ForegroundColor Gray
        Write-Host "   Script: $ScriptPath" -ForegroundColor Gray
        Write-Host "" -ForegroundColor Gray
        Write-Host "Use this to change interval:" -ForegroundColor Cyan
        Write-Host "  .setup-autosync.ps1 -Interval 5min   # Every 5 minutes" -ForegroundColor Gray
        Write-Host "  .setup-autosync.ps1 -Interval 15min  # Every 15 minutes" -ForegroundColor Gray
        Write-Host "  .setup-autosync.ps1 -Interval 30min  # Every 30 minutes (default)" -ForegroundColor Gray
        Write-Host "  .setup-autosync.ps1 -Interval hourly # Every hour" -ForegroundColor Gray
        Write-Host "" -ForegroundColor Gray
        Write-Host "To remove scheduled task:" -ForegroundColor Cyan
        Write-Host "  .setup-autosync.ps1 -Uninstall" -ForegroundColor Gray
    } catch {
        Write-Host "❌ Error creating scheduled task: $_" -ForegroundColor Red
    }
}
