---
title: Side-by-Side with HelloJackHunter: Unveiling the Mysteries of WinSxS
url: https://blog.zsec.uk/hellojackhunter-exploring-winsxs/
source: ZephrSec - Adventures In Information Security
date: 2024-05-13
fetch_date: 2025-10-06T17:15:15.167131
---

# Side-by-Side with HelloJackHunter: Unveiling the Mysteries of WinSxS

[![ZephrSec - Adventures In Information Security](https://blog.zsec.uk/content/images/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [LTR101 Posts](https://blog.zsec.uk/tag/ltr101/)
* [Photo Blog](https://photos.zsec.uk/)
* [Pre-register for my course](https://blog.zsec.uk/mae/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[Research](/tag/research/)

 Featured

# Side-by-Side with HelloJackHunter: Unveiling the Mysteries of WinSxS

This post explores Windows Side-by-Side (WinSxS) and DLL hijacking, deep-diving some tooling I've written and some of the fun along the way.

* [![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png)](/author/andy/)

#### [Andy Gill](/author/andy/)

12 May 2024
• 11 min read

![Side-by-Side with HelloJackHunter: Unveiling the Mysteries of WinSxS](/content/images/size/w2000/2024/05/signal-2024-05-05-125514_002.jpeg)

Chasing Sunset, photos.zsec.uk

This post on Windows Side-by-Side loading is a deeper dive into research I picked up at the tail end of 2023, in my free time between Christmas and New Year's.

As we know, Dynamic-link library(DLL) Side loading / DLL Hijacking is nothing new, nor is Windows Side-by-Side (WinSxS); however, side loading is handy from an adversarial tradecraft perspective, be it for establishing initial access, persistence, privilege escalation, or execution within an environment.

I picked up the research after reading a great post from [John Carroll](https://twitter.com/TheContractorio?ref=blog.zsec.uk) about [ExpLoading,](https://thecontractor.io/exploading/?ref=blog.zsec.uk) which is a technique for hijacking search orders from the current directory. At the time, I was also looking into WinSxS, as someone had mentioned in a blog post, but the blog lacked any proof of concept code, leading me down my rabbit hole.

Thus, a lot of this tooling and blog post were born; during my research, I identified work by another researcher who had dove into DLL hijacking and function export and  proxying in the past:

* Xenov - [Talk](https://www.youtube.com/watch?v=1p29rcq9DAE&ref=blog.zsec.uk) / [T[ooling](https://github.com/Xenov-X/DLL-Exports-Reverse-Proxy-Gen?ref=blog.zsec.uk)](https://github.com/Xenov-X/DLL-Exports-Reverse-Proxy-Gen?ref=blog.zsec.uk)

While doing this research, I leveraged Aaron's code and rewrote it in Python3, [which I've forked here](https://github.com/ZephrFish/DLL-Exports-Reverse-Proxy-Gen?ref=blog.zsec.uk). Still, the original intention of this tooling is similar to what HelloJackHunter does, so the rewrite was warranted. Building upon others' work is how we learn and improve.

## Side Loading / Hijacking 101

Dynamic-Link Library (DLL) search order hijacking, often shortened to DLL hijacking, exploits an application's execution flow via external DLLs. By hijacking the search order used to load legitimate content, it is possible to force an application to load a malicious DLL.

When a vulnerable application([I've found a few in the wild that are non-WinSxS binaries, including a CVE I got in 2020 for Nvidia](https://blog.zsec.uk/nvidia-cve-2020/)) is set to run with elevated privileges, any malicious DLL loaded into it inherits those elevated privileges, thus enabling privilege escalation. The application's behaviour often remains undisturbed since malicious DLLs are designed to seamlessly load the legitimate ones they replace or in cases where DLL paths aren't explicitly defined.

This discreet DLL launching capability presents myriad opportunities. In scenarios where the use of Rundll32 is impractical, diverting the execution flow of a trusted binary, adhering to the principle of living off the land (LOLBINS), offers a means to deploy malicious DLLs from diverse locations and inject them into legitimate processes.

## What is WinSxS?

WinSxS, standing for "Windows Side by Side", is a directory located in `C:\Windows\WinSxS`, where Windows keeps files essential for installing the operating system alongside backups or different versions of those files. There are a bunch of sub-folders and copies of just about every binary on a Windows environment, which makes it ripe for exploitation. As a result, lots of [LOLBINS](https://lolbas-project.github.io/?ref=blog.zsec.uk) may bypass execution policies.

WinSxS plays a crucial role in handling updates. When you install updates, new versions of system files are added to the folder. This ensures that applications' latest versions are available, contributing to overall system security and performance.

![](https://blog.zsec.uk/content/images/2024/05/image-4.png)

What this also means is we can leverage legitimate binaries and multiple versions of said binaries for malicious purposes, taking DLL hijacking out of the equation for a moment; what it means is there are several copies of PowerShell and cmd.exe, too; here's an example from a W10 VM:

* `c:\Windows\WinSxS\amd64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.22621.2506_none_6ae72c5495fc1170\cmd.exe`
* `c:\Windows\WinSxS\amd64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.22621.2506_none_6ae72c5495fc1170\f\cmd.exe`
* `c:\Windows\WinSxS\amd64_microsoft-windows-commandprompt_31bf3856ad364e35_10.0.22621.2506_none_6ae72c5495fc1170\r\cmd.exe`
* `c:\Windows\WinSxS\amd64_microsoft-windows-powershell-exe_31bf3856ad364e35_10.0.22621.2506_none_48f0644b7dd22b85\powershell.exe`
* `c:\Windows\WinSxS\amd64_microsoft-windows-powershell-exe_31bf3856ad364e35_10.0.22621.2506_none_48f0644b7dd22b85\f\powershell.exe`
* `c:\Windows\WinSxS\amd64_microsoft-windows-powershell-exe_31bf3856ad364e35_10.0.22621.2506_none_48f0644b7dd22b85\r\powershell.exe`

Now, in your environment, these paths may vary; therefore, investigating the version of WinSxS of binaries is always worth doing and may present additional options for execution within an environment.  What I have seen in specific environments is the ability to leverage alternate paths to bypass weak application allowlisting implementations that `C:\Windows\System32` might be blocked `WinSxS` may come to your aid.

## Putting the Two Together

Now that we're more clued up on WinSxS and DLL Hijacking, what about combining the two to form an automated identification and hunt workflow? The typical workflow looks like the following:

1. Hunt out binaries in WinSxS
2. Map out DLLs being called from $currentdir
3. Run HelloJackHunter and point it in a for loop at the DLLs

![](https://blog.zsec.uk/content/images/2024/05/image-5.png)

Hunting available binaries is relatively easy and just requires some PowerShell to start; the advice would be to do the research on your own dev system and replicate more in the target environment because none of the one-liners supplied are meant to be opsec safe and are more for highlighting quick paths to get the stuff you need/want.

## Mapping out Available Binaries

There are many ways to hunt out binaries. Simply searching in Explorer for \*.exe will give you a GUI list, or using something like [everything.exe](https://www.voidtools.com/?ref=blog.zsec.uk) will allow you to copy and export the paths, or merely use PowerShell like so and point it at the WinSxS directory:

```
GCI -Path C:\Windows\WinSxS -Recurse -Filter *.exe | Select -First 20 | Select Name, FullName, @{l='FileVersion';e={[System.Version]($_.VersionInfo.FileVersion)}} | Group Name | ForEach-Object { $_.Group | Sort-Object -Property FileVersion -Descending | Select-Object -First 1 }
```

![](https://blog.zsec.uk/content/images/2024/05/image-1.png)

I ran this on a Windows 10 VM and generated a nice list of available binaries, which you can download and play with here([https://github.com/ZephrFish/HelloJackHunter/blob/main/WinSxSBins.txt](https://github.com/ZephrFish/HelloJackHunter/blob/main/WinSxSBins.txt?ref=blog.zsec.uk)). Or, if you want to run t...