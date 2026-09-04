---
title: Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon
url: https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html
source: The Hacker News
date: 2026-09-03
fetch_date: 2026-09-04T06:44:15.369643
---

# Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Researcher Releases FalconFlank PoC Showing Privilege Escalation in CrowdStrike Falcon](https://thehackernews.com/2026/09/researcher-releases-falconflank-poc.html)

**Ravie Lakshmanan**Sep 03, 2026Vulnerability / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmg6caSDWQVOPIIl9NAXS4ofXmOdWz1eIGPMKMLCbHXc_uWiv11QNh2k-f43JAoVVQNMQj54d2yqJ_iO9vzwIO8nvQIyxr7N6GDCKsYDmSJEpyjiUBsY-zhMcmfEsWcEqDrKvrEkXxQC1LPldFXkqbJHO81V7oHnsRtuyjMZKzubBjwrK_yQ2xT2om89Ja/s1700-nu-rw-lo-l85-e365/windows-exploit.jpg)

The security researcher known as Chaotic Eclipse (aka INFINITE NIGHTMARE, MSNightmare, and Nightmare-Eclipse) has dropped a new zero-day dubbed **FalconFlank**, a proof-of-concept (PoC) for a privilege escalation flaw impacting Crowdstrike Falcon.

"FalconFlank is a 0-day privilege escalation that abuses the office malicious macros remediation in CrowdStrike Falcon Sensor," the researcher [said](https://github.com/MSNightmare/FalconFlank) in a GitHub README file, adding the cybersecurity company may already have detections for the flaw by now.

"So if you want to test, you either have to add it to the exclusions or obfuscate the PoC and change the DLL load technique."

The PoC, the researcher added, works in a fully updated Windows 11 25H2 machine or Windows Server 2025 with CrowdStrike Falcon. In a statement shared with The Hacker News, a CrowdStrike spokesperson said they are currently investigating the report.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"We are actively investigating these claims and advise customers to disable the Microsoft Office File Suspicious Macro Removal Windows policy setting," the spokesperson said. "Customers remain protected through the Cloud Anti-malware for Microsoft Office Files settings. We refer customers to the FalconFlank Tech Alert in the CrowdStrike support portal."

The development comes days after Chaotic Eclipse released a PoC for another privilege escalation flaw impacting Kaspersky's endpoint security product for Windows (version 14.0.0.504). The exploit has been codenamed [HardBreacher](https://github.com/MSNightmare/HardBreacher).

"The PoC is not in the best shape at all, it is basically duct tapped, I just managed to make it work and that's all," the researcher said. "It will fail to run with error so you just have to keep rerunning it. If it succeeds, it will create a file in C:\Windows\System32\MY\_SNAKE\_IS\_SOLID.dll with full permissions for the current user."

"The interesting part about this is that Kaspersky completely loses it when you take control over the UI process, you can cause it to stop functioning, grant/block access to files it's not supposed to, if the PoC succeeds, the entire operating system becomes a hot mess."

When reached for comment, Kaspersky told The Hacker News that it has resolved the HardBreacher issue. "The corresponding fix is delivered via an automatic update, or users can trigger database update manually," the company said.

Last month, the researcher also published a PoC for a Microsoft Defender zero-day called [ShieldBreak](https://thehackernews.com/2026/08/shieldbreak-zero-day-poc-claims.html) (aka CVE-2026-69414) that could [grant an attacker](https://blog.qualys.com/product-tech/2026/08/24/shieldbreak-the-windows-defender-zero-day-with-no-patch-detect-it-mitigate-it-with-qualys) the ability to run arbitrary code with NT AUTHORITY\SYSTEM privileges. It's assessed to be a patch bypass for CVE-2026-50656 (aka RoguePlanet). Microsoft has yet to release a fix.

"Like its predecessors, ShieldBreak explores a different corner of the Windows operating system," LevelBlue [said](https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking). "Where RedSun abused the Cloud Files API and TieringEngineService to redirect a Defender write into System32, and LegacyHive weaponized offline registry hive manipulation and the NT Object Manager namespace, ShieldBreak combines Cloud Files, Object Manager namespace manipulation, direct Windows Defender API invocation, and a timing race in the remediation path."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

"The result is a self-contained local privilege escalation chain in which Windows Defender's own clean engine is redirected to write an attacker-supplied DLL to C:\Windows\System32\phoneinfo.dll, followed by SYSTEM execution through the built-in Windows Error Reporting task."

Shortly after, the researcher claimed that Microsoft continues to ghost them and refuses to engage in "any sort of communication," [stating](https://blog.projectnightcrawler.dev/posts/2026-08-14-just-cut-the-lies-already/) the company is "trying hard to paint me as some insane criminal."

"I can't even report the bugs I find to their respective vendors because of the restrictions by Microsoft, all of this is of their own doing and you know, they don't even bother to check my case to figure out what's wrong," they [said](https://blog.projectnightcrawler.dev/posts/2026-08-13-what-other-options-do-i-have/) in a post dated August 14, 2026.

"Think I will start publishing bugs for third-parties in that window where Patch Tuesday isn't released yet. I just want to live like a normal human being for once in my life, is that too much to ask for...?"

*(The story was updated after publication to include responses from CrowdStrike and Kaspersky.)*

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#...