---
title: Attack Techniques: Full-Trust Script Downloads
url: https://textslashplain.com/2024/05/20/attack-techniques-full-trust-script-downloads/
source: text/plain
date: 2024-05-21
fetch_date: 2025-10-06T16:51:00.804636
---

# Attack Techniques: Full-Trust Script Downloads

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Full-Trust Script Downloads

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-05-202025-04-23](https://textslashplain.com/2024/05/20/attack-techniques-full-trust-script-downloads/)Posted in[security](https://textslashplain.com/category/security/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [malware](https://textslashplain.com/tag/malware/), [security](https://textslashplain.com/tag/security/)

While it’s common to think of cyberattacks as being conducted by teams of elite cybercriminals leveraging the freshest 0-day attacks against victims’ PCs, the reality is far more mundane.

Most attacks start as social engineering attacks: **abusing a user’s misplaced trust**.

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-11.png?w=613)](https://textslashplain.com/wp-content/uploads/2024/05/image-11.png)

*Most attackers don’t* hack *in, they* log *in.* The most common cyberattack is **[phishing](https://textslashplain.com/tag/Phishing/)**: Stealing the user’s password by asking them for it.

The next most common **Initial Access Vector** is socially-engineered **malware**: sending the user a malicious file and asking them to open it. When the malicious file runs, it disables security defenses, downloads more malware, and begins stealing data and performing other malicious activities.

Attackers have many choices for deploying their malware — on Windows, they can write evil executable files (`.EXE`, `.SCR`, `.COM`, etc) or installers (`.MSI`, `.MSIX`, etc).

However, for simplicity and compatibility reasons, one of the most common initial access choices for attackers is a file targeting the legacy scripting engines (`.JS`, `.VBS`, `.HTA`, `.WSH`).

### Legacy Script Engines

These scripting file types, created alongside Internet Explorer in the 1990s, have been supported for almost 30 years now, and they still work on the latest versions of Windows. Unlike JavaScript running in your browser, **these file types run outside of your browser, with no sandbox** constraining their ability to reconfigure your system and steal your files.

* JavaScript running in Chrome or Edge cannot read a file from your desktop without your explicitly selecting that file, whereas JavaScript running inside `wscript.exe` can read every file from your desktop, download and run any program without any prompts, and so forth.
* VBScript no longer runs in browsers, but the Windows Scripting engines (`cscript.exe` and `wscript.exe`) are perfectly happy to run VBS files and provide full access to your system.
* You can think of a [`HTA` file](https://en.wikipedia.org/wiki/HTML_Application) as a prehistoric [Electron app](https://en.wikipedia.org/wiki/Electron_%28software_framework%29) — it’s basically Internet Explorer with **no sandbox and all of the security features turned off.**

This level of power is, in a word, totally 🍌**bananas**🍌.

Why does it still exist?

Legacy compatibility.

### User Experience

In Edge, the .HTA file type is marked as `DANGEROUS` and thus HTA downloads are blocked by default:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-13.png?w=724)](https://textslashplain.com/wp-content/uploads/2024/05/image-13.png)

…but even blocked files can be sent to the user inside an archive (e.g. a ZIP File) and the user need only open the ZIP to be able to get at the HTA within.

In contrast, Chrome treats the HTA type as `[ALLOW_ON_USER_GESTURE](https://textslashplain.com/2021/05/19/download-blocking-by-file-type/)` and does not block .`HTA` downloads:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-14.png?w=611)](https://textslashplain.com/wp-content/uploads/2024/05/image-14.png)

Reading [the source](https://source.chromium.org/chromium/chromium/src/%2B/main%3Acomponents/safe_browsing/content/resources/download_file_types.asciipb), you can see that Chrome does not treat any of these file types as dangerous:

```
file_types {
  # HTML Application. Executes as a fully trusted application.
  extension: "hta"
  platform_settings {
    platform: PLATFORM_TYPE_WINDOWS
    danger_level: ALLOW_ON_USER_GESTURE
  }
}
file_types {
  # JavaScript file. May open using Windows Script Host with user level privileges.
  extension: "js"
  platform_settings {
    platform: PLATFORM_TYPE_WINDOWS
    danger_level: ALLOW_ON_USER_GESTURE
  }
}
file_types {
  extension: "vbs"
  platform_settings {
    platform: PLATFORM_TYPE_WINDOWS
    danger_level: ALLOW_ON_USER_GESTURE
  }
}
```

After you click open, the only thing standing between your PC and the potentially malicious code is a 2003-era security prompt:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-21.png?w=897)](https://textslashplain.com/wp-content/uploads/2024/05/image-21.png)

After the file starts running, your security software *may* be able to catch malicious behavior at runtime using a feature called the [Antimalware Scan Interface](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal), but I wouldn’t bet my PC on it.

### A Smarter and Safer Future?

The new Windows 11 Smart App Control feature dramatically reduces the threat of an attacker sending the victim a simple script or batch file that takes over their PC. A wide swath of file types, including scripts (`.js,.vbs,.hta`,`.ps1`), batch commands (`.bat,.cmd`) and numerous other dangerous types [are blocked from running](https://support.microsoft.com/en-us/topic/smart-app-control-has-blocked-an-app-with-a-dangerous-file-extension-60343058-66f2-4548-b978-e484e13abe89) if they [came from the web](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/).

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-15.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/05/image-15.png)

### Mitigations

You can easily block attacks against the legacy scripting engines today. There are numerous ways to do so, but perhaps the simplest approach which blocks browser and email attack vectors is to point the file types at a safe application (e.g. Notepad).

To do so, simply open the Windows Settings’ app and navigate to **Choose defaults by file type**. Search for a type:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-19.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/05/image-19.png)

Click the arrow icon, scroll the app list to pick a safe handler, then click **Set default**:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-22.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/05/image-22.png)

After fixing VBS, fix the other types:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-17.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/05/image-17.png)

In the unlikely event that you ever need to run one of these files inside its original handler, you can easily do so from the command line. Just run e.g. `mshta.exe theApp.hta` or `cscript.exe myScript.js` to run the file.

### Blocking HTA Files

HTA Files are such a longstanding security problem that there’s a [simple Group Policy](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-internetexplorer#disablehtmlapplication) (backed by a registry key) that blocks running them. From an elevated command prompt, run:

`REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Internet Explorer\Hta" /v "DisableHTMLApplication" /t REG_DWORD /d 1 /f`

…or create the key yourself using `regedit.exe`:

[![](https://textslashplain.com/wp-content/uploads/2024/05/image-32.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/05/image-32.png)

After doing so, double-clicking on a HTA file will silently do nothing.

Stay safe out there!

-Eric

### Share this:

* [Click to share on X (Opens in ne...