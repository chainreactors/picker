---
title: Four-Byte Write and Timing Bug Let Researchers Run Code in Windows SmartScreen Enclave
url: https://thehackernews.com/2026/10/four-byte-write-and-timing-bug-let.html
source: The Hacker News
date: 2026-10-14
fetch_date: 2026-10-15T06:45:40.018063
---

# Four-Byte Write and Timing Bug Let Researchers Run Code in Windows SmartScreen Enclave

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Four-Byte Write and Timing Bug Let Researchers Run Code in Windows SmartScreen Enclave](https://thehackernews.com/2026/10/four-byte-write-and-timing-bug-let.html)

**Swati Khandelwal**Oct 14, 2026Vulnerability / Virtualization

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizNi7OCo6m5vsFkEP85LndyXnfiDgk2h5R0WwW_yHZ7mdK6Uh9xuLaI5ddFQJ45fW7jG8eC4VtIHJT1IQaUJCoAEMClMEiv9dA9kASwDQJj4l61ZSIlqW2bw605LQLL5kNUszoxI8Wkr54oguKY7guQGE9rwUmvzCVUjt19-0pWJpxir366NU5eqopHmk/s1700-nu-rw-lo-l85-e365/enclave.jpg)

Security researchers ran their own code inside a protected part of Windows that is meant to stay sealed off even when the rest of the computer is taken over.

The protected area is a **VBS enclave**, an isolated slice of memory the operating system uses to guard secrets, and the one they broke into handles passwords for a Windows anti-phishing feature.

The work was done in a lab as a proof of concept, has not been seen in real attacks, and Microsoft fixed the flaw in its September 8, 2026 update.

The flaw is tracked as [CVE-2026-83498](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83498). Microsoft rates it an elevation-of-privilege issue, Critical, with a CVSS score of 7.8, and says it has not been exploited and was not publicly known before the fix. Microsoft also says it found the same issue internally. The research, by the security firm [Doyensec](https://blog.doyensec.com/2026/10/13/Sfape.html), was published October 13, more than a month after the patch.

A VBS enclave is a signed library that a normal Windows program loads but cannot read or change once it is running. The Windows hypervisor keeps the enclave's memory in a more trusted world, called VTL1 or Isolated User Mode, that ordinary code in the normal world, VTL0, cannot reach, [according to Microsoft](https://learn.microsoft.com/en-us/windows/win32/trusted-execution/vbs-enclaves).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The design is meant to protect what is inside even if an attacker has already taken over the normal kernel or is running as SYSTEM. Running attacker-chosen code inside that world is what makes this research notable.

The enclave Doyensec attacked is SFAPE.dll, the component behind Enhanced Phishing Protection in Microsoft Defender SmartScreen. That feature watches text you type or paste and warns you if you enter your Windows sign-in password into an unsafe place, such as Notepad or a phishing page.

To do this without exposing the password, Windows intercepts it at login and stores it in hashed form within the enclave, so later inputs can be checked against it. On a Windows 11 system, the program that loads this enclave is lsass.exe, the process that handles sign-in credentials and runs as SYSTEM.

The attack does not work from a distance. It needs a program already running on the machine that loads and calls the enclave; for SFAPE, that's LSASS. Microsoft's own rating says the same: the attack vector is local, and the attacker needs low-level access and no help from the user. In short, this is a way for code that already has a foothold to reach into the more trusted world next to it, not a way in from outside.

Doyensec built the attack from a small mistake and widened it step by step. Calling the enclave's Initialize function a second time makes it write a fixed four-byte error value to an address the calling program controls, and this time it skips the address check the first call performs.

Doyensec is clear that this alone is weak, writing that calling it an arbitrary write "would be a huge overstatement." Aimed at the right spot, though, that one write corrupts the value the enclave uses to tell its own memory from the host's, so its safety check stops working. From there, a timing bug in another function triggers a controlled wipe. That wipe redirects how the enclave looks up a stored object, and the resulting read and write let the researchers replace the table that decides which code the enclave may run.

The result is attacker-chosen code running inside the enclave. The work broke the enclave's isolation; it did not show that a user's password was read or stolen, and Microsoft's advisory describes the impact as data leakage from or code execution inside the enclave.

Microsoft fixed the flaw in the September 8, 2026 cumulative update, [KB5124008](https://support.microsoft.com/en-gb/servicing/os/windows-11/2026/09/kb5124008-windows-11-24h2-25h2-security-update), for Windows 11 versions 24H2 and 25H2. Doyensec compared the old and new files and found the patched enclave now checks the address before that first write and tightens the function the timing bug relied on.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The update also ships a new policy that prevents the old, vulnerable enclave from loading at all, so a patched system cannot run it. There is no separate workaround to apply; installing the update is the action.

One gap outlives this fix. Windows has no general blocklist for vulnerable enclaves like the one it keeps for vulnerable drivers, and the September policy only blocks the old SFAPE file. An older Microsoft Edge enclave with a similar read-and-write flaw, [CVE-2023-36880](https://github.com/google/security-research/security/advisories/GHSA-wwr4-v5mr-3x9w) from 2023, is still allowed to load, Doyensec said.

Whether that was a deliberate choice or an oversight is unclear. That matters because loading a signed but flawed enclave is a known trick, sometimes called "bring your own vulnerable enclave," that [earlier research from Akamai](https://www.akamai.com/blog/security-research/virtualized-insecurity-attackers-weaponize-vbs-enclaves) and [Outflank](https://www.outflank.nl/blog/2025/02/03/secure-enclaves-for-offensive-operations-part-i/) used to hide code and data from security tools. Blocking one flawe...