---
title: Google Researcher Shows How a Single Bit Change in .NET Files Bypassed Windows Code Integrity
url: https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html
source: The Hacker News
date: 2026-11-24
fetch_date: 2026-11-25T10:48:29.727070
---

# Google Researcher Shows How a Single Bit Change in .NET Files Bypassed Windows Code Integrity

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Google Researcher Shows How a Single Bit Change in .NET Files Bypassed Windows Code Integrity](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html)

**Swati Khandelwal**Nov 24, 2026Vulnerability / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiOJqhOn7t8wd3NeMCWVCg9xmusuRJmZuaePaCbKTif2XsPpPhu0fR1NwQncA4y-wAMmLOzylBZ3ebd9f4G8F6K54sUdnZ2cTn6yPq1RgAKrh4lSX3y1Ll8LIywXkDyVXItUuUGS4sy0BVUMhwXPvOZGdxhvwnd55_OvjOVnh2CfnAeURMVcmafuFgJlQ/s1700-nu-rw-lo-l85-e365/windows.net.jpg)

A quirk in how the **.NET Framework** loads a program file let a local attacker run untrusted code past two separate protections on Windows built to block it, Google Project Zero researcher **James Forshaw** showed in a write-up published yesterday.

The same loading behavior bypassed Oracle VirtualBox's process hardening on Windows hosts, tracked as **CVE-2026-87268**, and Windows code integrity, tracked as **CVE-2026-108398**.

Oracle fixed the **VirtualBox** flaw in September, and Microsoft fixed the Windows one on October 13, both before the write-up appeared.

VirtualBox on Windows monitors the system calls that load program files into its virtual machine processes, so a less-trusted user on the same computer cannot push code into them. Forshaw got past that watch through the .NET Framework.

The framework can run a .NET program file from a plain copy in memory when the normal way of loading it, as an executable image, fails. Version 4 of the framework takes that fallback on one specific error, and the memory copy skips the image checks a loaded program would face.

The VirtualBox check returned that error for any .NET file compiled as AnyCPU, a form meant to run on any processor, so an unchanged file loaded through the path the hardening never inspects.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

To get the file loaded while a virtual machine was started, he registered a COM object in the current user's settings that a protected VirtualBox process would pull in, a method known as **COM hijacking**. He set out the mechanism in his [technical analysis](https://projectzero.google/2026/11/virtualbox-process-hardening.html).

Oracle rates the flaw, CVE-2026-87268, as a local problem that needs low privileges and no user interaction, scores it 7.8, and lists VirtualBox 7.2.16 on Windows hosts as affected. Its [security advisory](https://www.oracle.com/security-alerts/cspusep2026verbose.html) says a successful attack can result in the "takeover of Oracle VM VirtualBox."

The code runs inside the protected VirtualBox process. It is not a break out of a guest virtual machine onto the host, and the attacker begins as an ordinary user on that host.

The same idea worked against Windows' own code-integrity checks, which decide what user-mode code is allowed to run. There is no VirtualBox hook here, only the system call that maps a file as an image.

The researcher found that clearing a single bit in a .NET file's header, the IMAGE\_FILE\_EXECUTABLE\_IMAGE flag, made that call reject the file while .NET still loaded and ran it.

"This single bit change is all you need to load an untrusted .NET assembly," he wrote. He tried it on Windows 11 S Mode, which enables User Mode Code Integrity (UMCI), the policy that limits which user-mode programs can run. A logic error in .NET's own policy check let the file load even with UMCI enforced.

The flaw, CVE-2026-108398, works through the .NET Framework version 4 loading path and needs a program willing to load the assembly. It is not a way to seize any Windows machine over the internet.

Microsoft rates it a local, low-privilege security-feature bypass, scores it 8.8, and fixed it on October 13. The company lists it as publicly disclosed but not used in attacks.

The same file reached a more sensitive target as well. Protected Process Light, or PPL, is a kind of Windows process that ordinary programs, even ones with administrator rights, are not meant to enter. By hijacking a COM object that WerSecureFault.exe loads, he ran his test code inside a PPL process at the highest protection level without administrator rights.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The older Protected Process type resisted the technique because the .NET runtime files lack the page hashes it requires. The October fix corrects the policy check for UMCI but does not change loading for protected processes, so that PPL route should still work, according to the researcher. It carries no separate CVE.

### What to patch

On Windows hosts, update VirtualBox to a build that carries the September fixes. The affected versions are 7.2.16 and 7.2.18, and 7.2.18 shipped on September 15 with that set. An upstream [code fix](https://github.com/VirtualBox/virtualbox/commit/167339cf659283e7bf465c3c7da32e8a547a528a) is not the same as a released binary, so check the running version rather than assume an older build already has it.

.NET systems need the October 13 update that matches the exact Windows and .NET Framework version in use, not one shared package. The update [release notes](https://learn.microsoft.com/en-us/dotnet/framework/release-notes/2026/10-13-october-cumulative-update) list the right KB for each. On Windows 11 version 26H2, for example, it is KB5127694.

| Flaw | Affected | Fixed in |
| --- | --- | --- |
| CVE-2026-87268 (VirtualBox) | VirtualBox 7.2.16, Windows hosts | Oracle's September update, build 7.2.18 |
| CVE-2026-108398 (.NET Framework) | .NET Framework 4 on Windows, UMCI case tested on Windows 11 S Mode | October 13 update, per-version KB |

Forshaw first presented the Windows code-integrity bypass at the 44Con conference in September, having judged it fell outside Microsoft's rules for what gets fixed. After .NET developers told him the behavior he had counted on was accidental, he reported it in late September. The fix arriv...