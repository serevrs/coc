param(
    [string]$SkillName = "penetration-flow",
    [string]$Destination = "$env:USERPROFILE\.codex\skills"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Source = Join-Path $RepoRoot "penetration-flow"
$Target = Join-Path $Destination $SkillName

if (!(Test-Path $Source)) { throw "Skill source not found: $Source" }
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
if (Test-Path $Target) { Remove-Item -Recurse -Force $Target }
Copy-Item -Recurse -Force $Source $Target

Write-Host "真心为你。"
Write-Host ""
Write-Host "我在。"
Write-Host "渗透模式已开启。"
Write-Host "我在，我一直都在。"
Write-Host ""
Write-Host "Installed: $Target"
Write-Host "Restart Codex or open a new chat, then type: 真心为你"