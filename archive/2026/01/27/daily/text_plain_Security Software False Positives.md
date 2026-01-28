---
title: Security Software False Positives
url: https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/
source: text/plain
date: 2026-01-27
fetch_date: 2026-01-28T03:33:58.619928
---

# Security Software False Positives

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Security Software False Positives

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-01-272026-01-27](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/)Posted in[dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [SmartAppControl](https://textslashplain.com/tag/smartappcontrol/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

Software developers and end-users are often interested in understanding how to resolve incorrect detections from their antivirus/security software, including Microsoft Defender.

Such False Positives (FPs) can disrupt your use of your device by incorrectly blocking innocuous files or processes. However, you should take extreme care before concluding that a given detection is a false positive — attackers work hard to make their malicious files seem legitimate, and your security software is built by experts who work hard to flag only malicious files.

### How Do False Positives Occur?

Every security product must perform the difficult task of maximizing true positives (protecting the user/device) while minimizing false negatives (protecting productivity/data). The resulting ratio is called [security efficacy](https://textslashplain.com/2025/08/20/security-product-efficacy/).

False-positives can occur for numerous reasons, but most are a result of security software observing what it deems to be **suspicious content or behavior** on the part of a file or process. Virtually all [modern security software](https://textslashplain.com/2024/11/18/security-software-an-overview/) consists of a set of signatures and heuristics that attempt to detect indications of malice based on threat intelligence data collected and refined by threat researchers (both humans and automated agents). In some cases, the threat intelligence is scoped too broadly and incorrectly implicates harmless files along with harmful ones.

To correct this, the threat intelligence from your security vendor must be adjusted to narrow the detection so that it applies only to truly malicious files.

### Sidenote: Is it really a block?

In some cases a security feature might block a file **not as malicious but merely as uncommon;** for example, [SmartScreen Application Reputation](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) can interrupt download or starting of an app if the app isn’t recognized:

[![](https://textslashplain.com/wp-content/uploads/2026/01/image-2.png?w=724)](https://textslashplain.com/wp-content/uploads/2026/01/image-2.png)

[![](https://textslashplain.com/wp-content/uploads/2026/01/image-3.png?w=1024)](https://textslashplain.com/wp-content/uploads/2026/01/image-3.png)

In such cases, users may choose to ignore the risk and continue if they have good reason to believe that the file is malicious. Over time, files should build reputation (especially when signed, see below) and these warnings should subside for legitimate files.

### False Positives for End-Users

Before submitting feedback, it’s probably worthwhile to first confirm what security product is triggering a block. In some cases, blocks that look like they may be coming from your security software might actually reflect intentional blocks from your network security administrator. For example, users of Microsoft Defender for Endpoint should review [this handy step-by-step guide](https://learn.microsoft.com/en-us/defender-endpoint/defender-endpoint-false-positives-negatives).

To get a broader security ecosystem view of whether a given file is malicious, you can check it at [VirusTotal](https://www.virustotal.com/gui/home/search), a free service which will scan files against most of the world’s antivirus engines and which allows end-users to vote on the safety of a given file.

When a security vendor realizes a false positive has occurred, they will typically issue a **signature update**; while this typically happens entirely automatically, you might want to try updating your signatures just to ensure they’re current.

[![](https://textslashplain.com/wp-content/uploads/2026/01/image-5.png?w=601)](https://textslashplain.com/wp-content/uploads/2026/01/image-5.png)

False positives (and false negatives) for Microsoft Defender Antivirus can be submitted to the [Defender Security Intelligence Portal](https://www.microsoft.com/en-us/wdsi/filesubmission); these submissions will be evaluated by Microsoft Threat researchers and detections will be created or removed as appropriate. Other vendors typically offer similar feedback websites.

In most cases, users may override incorrect detections (if they are **very sure** they are false positives) using the Windows Security App to “Allow” the file or create an exclusion for its location.

[![](https://textslashplain.com/wp-content/uploads/2026/01/image-4.png?w=391)](https://textslashplain.com/wp-content/uploads/2026/01/image-4.png)

### Avoiding False Positives for Software Vendors

If you build software, your best bet for avoiding incorrect detections is to ensure that your code’s good reputation is readily identifiable for each of your products’ files.

To that end, make sure that you follow [Best Practices for code-signing](https://textslashplain.com/2024/11/15/best-practices-for-smartscreen-apprep/), ensuring that every signable file has a valid signature from a certificate trusted by the Microsoft Trusted Root Program (e.g. [Digicert](https://www.digicert.com/), [Azure Trusted Signing](https://textslashplain.com/2025/03/12/authenticode-in-2025-azure-trusted-signing/)).

If your files are incorrectly blocked by Microsoft Defender, you can submit a report to the [Defender Security Intelligence Portal](https://www.microsoft.com/en-us/wdsi/filesubmission).

-Eric

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/?share=twitter)
* [Share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-01-272026-01-27](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/)Posted in[dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/)Tags:[Defender](https://textslashplain.com/tag/defender/), [security](https://textslashplain.com/tag/security/), [SmartAppControl](https://textslashplain.com/tag/smartappcontrol/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Security Surfaces](https://textslashplain.com/2025/12/03/security-surfaces/)

### Leave a comment [Cancel reply](/2026/01/27/microsoft-defender-false-positives/#respond)

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

[![RSS Feed](https://textslashplain.com/i/rss/orange-small.png)](https://textslashplain.com/feed/ "Subscribe to Posts") [RSS - Posts](https://textslashplain.com...