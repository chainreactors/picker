---
title: Defensive Technology: Controlled Folder Access
url: https://textslashplain.com/2024/11/15/defensive-technology-controlled-folder-access/
source: text/plain
date: 2024-11-16
fetch_date: 2025-10-06T19:17:48.756111
---

# Defensive Technology: Controlled Folder Access

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Defensive Technology: Controlled Folder Access

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-11-152025-05-05](https://textslashplain.com/2024/11/15/defensive-technology-controlled-folder-access/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/)Tags:[Defender](https://textslashplain.com/tag/defender/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/), [Windows](https://textslashplain.com/tag/windows/)

Most client software’s threat models (e.g. Edge, [Chrome](https://chromium.googlesource.com/chromium/src/%2B/HEAD/docs/security/faq.md#Why-arent-compromised_infected-machines-in-Chromes-threat-model)) explicitly exclude threats where the local computer was compromised by malware. That’s because, without a trusted computing base, it’s basically impossible to be secure against attackers. This concept was immortalized decades ago in the [Ten Immutable Laws of Security](https://web.archive.org/web/20160311224620/https%3A//technet.microsoft.com/en-us/library/hh278941.aspx):

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-5.png?w=986)](https://textslashplain.com/wp-content/uploads/2024/11/image-5.png)

In the intervening years, new technologies (like [Secure Enclaves](https://textslashplain.com/2024/01/03/the-blind-doorkeeper-problem-or-why-enclaves-are-tricky/)) have been launched in an attempt to provide *some* defenses even when a PC has been compromised, but they remain very limited in their capabilities. In my view, **preventing initial access** represents the most important security investment we can make.

## Protecting Files

Nevertheless, there’s value in defense-in-depth and making life harder for attackers even *after* they get access to a PC.

In that vein, Windows 10 has a feature called [Controlled Folder Access](https://learn.microsoft.com/en-us/defender-endpoint/controlled-folders) (CFA) which aims to help protect against [ransomware](https://learn.microsoft.com/en-us/security/ransomware/human-operated-ransomware). In the common ransomware attack, malicious native code running on the user’s machine begins encrypting their files with a randomly-generated key that is sent to the attacker. After files have been encrypted, a ransom note is shown demanding that the user pay money to get the decryption key.

CFA impedes this attack by preventing applications with “unknown” reputation from touching files in sensitive/protected folders, including the user’s Documents, Pictures, and Favorites folders, as well as any folders selected by the user. You can enable CFA using the **Ransomware protection** section of the Windows Security app:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-1.png?w=465)](https://textslashplain.com/wp-content/uploads/2024/11/image-1.png)

Rather than moving sensitive files to a protected vault, it’s more like you’ve hired a bouncer to keep questionable apps out. If you want to protect more folders, click the *Protected Folders* link and choose the folders you’d like protected. If you need to allow an unknown app to access protected files, you can do so using the *Allow an app* link.

When Defender blocks access, you’ll see a small toast notification:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-7.png?w=461)](https://textslashplain.com/wp-content/uploads/2024/11/image-7.png)

You can see blocked actions in both the **Protection history** section of the Windows Security app:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-6.png?w=907)](https://textslashplain.com/wp-content/uploads/2024/11/image-6.png)

…as well as the Windows Defender node of the Windows Event Viewer:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-3.png?w=778)](https://textslashplain.com/wp-content/uploads/2024/11/image-3.png)

If you’re managing devices with Intune or Group Policy, you can also enable CFA in “[Audit Mode](https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders#:~:text=in%20protected%20folders.-,Audit%20Mode,-%2D%20Changes%20are%20allowed)“, which will log untrusted accesses without blocking them.

## How?

This feature depends upon the Windows Defender filesystem filter driver (`WDFilter`). From kernel mode, the filter watches for access to protected folders. If access is requested by an untrusted process, any `Write` permission bit is stripped from the request.

## Non-Obvious Bits

While CFA is conceptually pretty simple, under the covers there’s a fair bit of complexity.

For one thing, various well-known and legitimate applications (like Microsoft Office) offer extensibility models that could be used to load malicious modules. Similarly, well-known applications (e.g. Notepad) could have [malicious code injected into them](https://attack.mitre.org/techniques/T1055/012/). So, Defender has to watch what’s loaded into each process and may consider an otherwise “friendly” process ***tainted*** for the purposes of CFA.

Additionally CFA could be circumvented if a process directly accesses a disk volume using low-level APIs. If CFA blocks an unknown app from accessing a disk in this way, there’s no folder path to show, so the toast (perhaps confusingly) claims that CFA blocked the app from “making changes to memory.”

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-4.png?w=445)](https://textslashplain.com/wp-content/uploads/2024/11/image-4.png)

Finally, CFA must carefully handle all of the myriad equivalent ways in which a file’s path can be represented, for example:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-8.png?w=885)](https://textslashplain.com/wp-content/uploads/2024/11/image-8.png)

Referring to local files using a UNC path and 8.3 filename syntax

## Debugging

In some cases, understanding *why* a process has triggered CFA could be difficult. For example, several engineers at Microsoft recently found that running most command-line tools (like `ping.exe`) in the SYSTEM32 folder was triggering the `making changes to memory` toast. *This seems very strange — a network tool like* `ping` *isn’t expected to be touching the local disk at all!*

Using [SysInternals’ Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) to log the process behavior can reveal the root cause. Click Filter > Enable Advanced Output. Use the toolbar toggle button to filter to FileSystem events, and create a filter for `Operation is IRP_MJ_CREATE`:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-31.png?w=645)](https://textslashplain.com/wp-content/uploads/2024/11/image-31.png)

Look through the `IRP_MJ_CREATE` events to find those for the `C:` volume:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-29.png?w=501)](https://textslashplain.com/wp-content/uploads/2024/11/image-29.png)

In this case, we see that an AMD GPU driver `amdkmdag.sys` is opening the `C:` volume for Write Access as in the context of `ping.exe` as it shuts down, leading to the toast:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-30.png?w=614)](https://textslashplain.com/wp-content/uploads/2024/11/image-30.png)

To discover whether a process is being treated as *tainted* by the engine, see the `MPLog-#####` file inside `C:\ProgramData\Microsoft\Windows Defender\Support`. For example, a value of `TaintType:0x1` indicates that an untrusted module was loaded into the process.

## Online Backup

Beyond Controlled Folder Access, Windows’ other built-in anti-ransomware approach is to enable online backup to a cloud file provider like OneDrive. The recovery experience offered by OneDrive depends on which level of account you have:

[![](https://textslashplain.com/wp-content/uploads/2...