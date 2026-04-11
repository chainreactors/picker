---
title: Understanding Defender AV Scans
url: https://textslashplain.com/2026/04/10/understanding-defender-av-scans/
source: text/plain
date: 2026-04-10
fetch_date: 2026-04-11T04:21:15.227921
---

# Understanding Defender AV Scans

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Understanding Defender AV Scans

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-04-102026-04-10](https://textslashplain.com/2026/04/10/understanding-defender-av-scans/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [malware](https://textslashplain.com/tag/malware/)

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-7.png?w=233)](https://textslashplain.com/wp-content/uploads/2026/04/image-7.png)

Microsoft Defender Antivirus Defender is intended to operate silently in the background, without requiring any active attention from the user. *Because Defender is included for free as a component of Windows, it doesn’t need to nag or otherwise bother the user for attention in an attempt to “prove its value”, unlike some antivirus products that require subscription fees*.

The default mode for Defender is called “Real-time Protection” (RTP) and in that mode, Defender will automatically scan files for malicious content as they are opened and closed. This means that, even if you did have a malicious file on your PC, the instant it tries to load, the threat is blocked.

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-1.jpeg?w=509)](https://textslashplain.com/wp-content/uploads/2026/04/image-1.jpeg)

If you use the Windows Security App’s toggle to turn RTP off, it will turn itself back on whenever you reboot, or after a variable interval (controlled by various factors including management policies and signature updates).

Given the default real-time scanning behavior, you may wonder why the File Explorer’s legacy context menu offers a “Scan with Microsoft Defender…” menu item. *Note that this is the Legacy Context menu, shown when Shift+RightClicking on a file. The Default context menu shown by a regular right-click does not offer the Scan command.*

[![](https://textslashplain.com/wp-content/uploads/2026/04/image.png?w=327)](https://textslashplain.com/wp-content/uploads/2026/04/image.png)

Confusion around this command is especially common because, in most cases, the item doesn’t *seem to do* anything: the Windows Security app just opens to the “Virus & threat protection” page:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-3.png?w=832)](https://textslashplain.com/wp-content/uploads/2026/04/image-3.png)

The scan you’ve asked for typically executes so quickly, that you have to look closely to realize that your requested scan actually completed– see the text “*1 file scanned*” at the bottom.

🤔 So, in a world of Real-time Protection, why does this command exist at all? Is there ever a need to use it?

The one scenario where the “Scan” menu item does more than nothing is the case of archive files (Zip, 7z, CAB, etc). Defender doesn’t scan these files on open/close for a few reasons (performance: decompressing data can take a long time, functionality: a password may be needed to decompress).

However, if a user actually tries to *use* a file from within an archive, that file is extracted and scanned at that time:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-4.png?w=599)](https://textslashplain.com/wp-content/uploads/2026/04/image-4.png)

If you wanted to scan the contents of an unencrypted archive without actually extracting it, the **Scan with Microsoft Defender…** menu item will do just that and recognize the threat inside the archive:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-5.png?w=520)](https://textslashplain.com/wp-content/uploads/2026/04/image-5.png)

Therefore, the only meaningful use of the “Scan” option in Defender is to scan an archive file that you plan to *give someone else to open on a different computer,* although it’s extremely likely that *their device* would also be running Defender and would also scan any files extracted from the archive.

Unfortunately, there’s lots of bad/outdated advice out there about the need for manual AV scanning, but I’m happy to see that both Microsoft Copilot and Google Gemini understand the very limited usefulness of this command. I was also happy to see Gemini offered the following:

**Pro Tip:** If you ever suspect a file is malicious but Defender insists that it’s clean, try uploading it to **[VirusTotal](https://www.virustotal.com/gui/home/search)** (an awesome service I’ve [blogged about before](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/#:~:text=To%20get%20a%20broader%20security%20ecosystem%20view)). VirusTotal will scan the file using over 70 different antivirus engines simultaneously to give you a second (and 3rd,4th,5th,6th,7th…) opinion.

## Other Scans

You may’ve noticed other options on the Scan options page, including “Quick scan”, “Full scan”, “Custom scan”, and “offline scan”.

* **Quick Scan** scans a small set of locations where malware commonly tries to hide, including startup locations.
* **Full scan** is self-explanatory: it scans all of your files on your disks.
* **Custom scan** is self-explanatory: it scans the location you choose. The menu item discussed above kicks off a custom-scan for a single file or folder.

All of these scans are basically redundant in a world of RTP: files are scanned on access, so manual scans are not required for protection. The final option, **Microsoft Defender Antivirus (offline scan)** is different than the others. This scan is a special one that reboots your system and begins a scan before Windows boots. This scan type can find certain types of malware that might otherwise try to hide from Defender. Note that you may be prompted for your BitLocker recovery key:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-8.png?w=699)](https://textslashplain.com/wp-content/uploads/2026/04/image-8.png)

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-9.png?w=346)](https://textslashplain.com/wp-content/uploads/2026/04/image-9.png)

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-10.png?w=729)](https://textslashplain.com/wp-content/uploads/2026/04/image-10.png)

tl;dr: *Don’t worry, we’ve got your back.*

-Eric

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/04/10/understanding-defender-av-scans/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/04/10/understanding-defender-av-scans/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-04-102026-04-10](https://textslashplain.com/2026/04/10/understanding-defender-av-scans/)Posted in[security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [malware](https://textslashplain.com/tag/malware/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:](https://textslashplain.com/2026/03/24/windows-choose-where-to-get-apps/)

### Leave a comment [Cancel reply](/2026/04/10/understanding-defender-av-scans/#respond)

Δ

## Search Text/Plain

Search for:

## Pages

* [About](https://textslashplain.com/about/)
* [Browse All Posts](https://textslashplain.com/browse-all-posts/)
* [Categories](https://textslashplain.com/categories/)
* [Cruises](https://textslashplain.com/cruises/)
* [IEInternals Archive](https://textslashplain.com/ieinternals-archive/)
* [Real-World Races](https://textslashplain.com/races/)

## RSS

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscr...