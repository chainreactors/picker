---
title: Smart App Control
url: https://textslashplain.com/2026/04/28/smart-app-control/
source: text/plain
date: 2026-04-28
fetch_date: 2026-04-29T05:11:28.415918
---

# Smart App Control

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Smart App Control

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-04-28](https://textslashplain.com/2026/04/28/smart-app-control/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Authenticode](https://textslashplain.com/tag/authenticode/), [Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [SmartAppControl](https://textslashplain.com/tag/smartappcontrol/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [Windows](https://textslashplain.com/tag/windows/)

Users of modern versions of Windows 11 have a powerful security feature for keeping their devices secure, known as [Smart App Control](https://learn.microsoft.com/en-us/windows/apps/develop/smart-app-control/overview).

I’ve talked about this feature a few times over the last year, but in April 2026, a powerful improvement landed. Previously, Smart App Control could not be turned back on if you ever turned it off. That limitation has been removed in Windows 11 version 25H2, making the feature far more practical to use and try out.

## What is Smart App Control?

While Windows’ [SmartScreen AppRep](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) feature only checks the reputation of the entry point program (typically a `.exe` file) from an untrusted origin (like the Internet), [Windows 11’s Smart App Control](https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003) goes further than SmartScreen and evaluates trust/signatures of **all**code (DLLs, scripts, etc) that is loaded by the Windows OS Loader and script engines. This provides a broader range of protection (somewhat akin to [Gatekeeper on MacOS](https://support.apple.com/en-ca/guide/security/sec5599b66df/web)) and addresses AppRep bypasses like [DLL hijacking](https://textslashplain.com/2015/12/18/dll-hijacking-just-wont-die/). If a code file is unsigned, Windows will consult the Microsoft Defender **Intelligent Security Graph** in the cloud to see whether the file is known to be trustworthy and permit it to load only if so.

Beyond trust evaluation, when Smart App Control is enabled, many dangerous file types are blocked from `ShellExecute()` entirely if a file is from an untrusted origin.

End-users can enable Smart App Control in the Windows Security App.

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-18.png?w=779)](https://textslashplain.com/wp-content/uploads/2026/04/image-18.png)

#### Automatic Enablement

By default, Smart App Control starts in Evaluation mode, meaning that it watches as you use your device to determine whether SAC’s protections are a good match for your use cases. While SAC works great for the majority of consumers, it tends to cause too much *friction* on devices used by Developers and within Enterprises, because these devices commonly interact with unsigned code or code that is not broadly used by the public.

### Other file types

One of the most exciting features of Smart App Control is that it blocks the Windows Shell from opening files of certain [types](https://textslashplain.com/2023/04/05/file-types/) if they [originate from untrusted locations](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/).

**As of April 2026, [the list](https://support.microsoft.com/en-us/topic/smart-app-control-has-blocked-an-app-with-a-dangerous-file-extension-60343058-66f2-4548-b978-e484e13abe89) of SAC-blocked-if-MotW extensions** is `.appref-ms, .appx, .appxbundle, .bat, .chm, .cmd, .com, .cpl, .dll, .drv, .gadget, .hta, .iso, .js, .jse, .lnk, .msc, .msp, .ocx, .pif, .ppkg, .printerexport, .ps1, .rdp, .reg, .scf, .scr, .settingcontent-ms, .sys, .url, .vb, .vbe, .vbs, .vhd, .vhdx, .vxd, .wcx, .website, .wsf, .wsh`.

If you attempt to open one of these potentially dangerous files from an untrusted source, you’ll encounter the following block dialog:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-16.png?w=558)](https://textslashplain.com/wp-content/uploads/2026/04/image-16.png)

Notably, this dialog box does not offer an override. If you’re confident that the file is from a trusted source, you could remove the MotW or temporarily disable SAC before opening it.

### Impact on Other Features

* Enabling SAC causes the [Choose where to get apps setting](https://textslashplain.com/2026/03/24/windows-choose-where-to-get-apps/) to be ignored.

* Enabling SAC causes [SmartScreen Application Reputation](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) to be disabled.

* When SAC is enabled, Microsoft Defender Antivirus enters a special “Hybrid” mode (similar to its passive mode). In Hybrid mode, Defender’s real-time protection feature is less-active, reducing the monitoring (BM and file open/close scans) for processes unless the system determines that the process is one that is particularly *interesting* (e.g. a script engine host).

* Unfortunately, SAC’s dangerous file type list is baked into the feature and is not extensible. It does **not** respect the `HighRiskFileTypes` list from the registry or the `EditFlags` of the file type.

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-17.png?w=548)](https://textslashplain.com/wp-content/uploads/2026/04/image-17.png)

### Developer Guidance

For software publishers, the best way to avoid problems with SAC blocking your app is to [sign your code](https://textslashplain.com/2024/11/15/best-practices-for-smartscreen-apprep/), already a longstanding best practice. Importantly, unlike SmartScreen AppRep (which only verifies the reputation files with an Internet origin), **SAC verifies signatures on *all* code modules**, including DLLs and packages like MSIs. That means that tricks like using a signed stub installer to drop unsigned code will not be good enough.

One early problem with Smart App Control is that the Code Integrity codepath didn’t support ECC signatures. That’s being addressed, but for broadest compatibility and least friction, you should still **avoid ECC for code-signing**.

### Other Links

* [Microsoft’s SAC FAQ](https://support.microsoft.com/en-us/windows/smart-app-control-frequently-asked-questions-285ea03d-fa88-4d56-882e-6698afdb7003)

Nitty Gritty – Nearly four years ago, [@n4r1B](https://x.com/n4r1B) posted an amazingly low-level exploration of the underlying implementation of SAC and the Windows code integrity technology that implements it.

* <https://n4r1b.com/posts/2022/08/smart-app-control-internals-part-1/>
* <https://n4r1b.com/posts/2022/09/smart-app-control-internals-part-2/>

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/04/28/smart-app-control/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/04/28/smart-app-control/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-04-28](https://textslashplain.com/2026/04/28/smart-app-control/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Authenticode](https://textslashplain.com/tag/authenticode/), [Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [SmartAppControl](https://textslashplain.com/tag/smartappcontrol/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [Windows](https://textslashplain.com/tag/windows/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Pos...