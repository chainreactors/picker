---
title: 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros
url: https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:34.563258
---

# 15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [15-Year-Old GhostLock Flaw Enables Root and Container Escape on Most Linux Distros](https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html)

**Swati Khandelwal**Jul 08, 2026Vulnerability / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid8ZRwAprNDN6zAPixm22IlrKWp03FJdQF0TxCV5v_jxckPLkOHRSzHQERbDNw_FZdnyluuhyphenhyphenGZ7pSX51cjBl-S8PrqhgARlAe8VfWPabk7t4hAy37ZSrRu6oXfRYlXP7s1x1OBYW9WHmgWobGS0wiC0mrO42xHWHrSI3ICLM5OFzsOA3tVCcs4_N1yPU/s1700-e365/linux-root.gif)

Researchers at [Nebula Security](https://nebusec.ai/research/ionstack-part-2/) have disclosed GhostLock ([CVE-2026-43499](https://nvd.nist.gov/vuln/detail/CVE-2026-43499)), a 15-year-old Linux kernel flaw that lets any logged-in user take full root control of a machine that has not been patched.

The vulnerable code has shipped by default in essentially every mainstream distribution since 2011. The flaw needs no special permission, no unusual settings, and no network access; ordinary threading calls from any local program are enough.

Nebula turned it into a working root exploit that is 97% reliable in its testing and also escapes containers, and says Google awarded the team $92,337 through its [kernelCTF](https://google.github.io/security-research/kernelctf/rules.html) bug-bounty program.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

No one is known to be exploiting it in the wild, but Nebula has published [working exploit code](https://github.com/NebuSec/CyberMeowfia/tree/main/IonStack/CVE-2026-43499), so anyone can now run it. Patching is the priority.

## How the bug works

The kernel has a system for keeping an urgent task from getting stuck behind a trivial one. Part of it is a cleanup step that tidies up after a task once it stops waiting.

Normally, that works fine. But in one rare case, where a lock operation hits a dead end and has to back out, the cleanup runs at the wrong moment and wipes the wrong task's record.

That mistake leaves the kernel holding a "note" that points at a scrap of memory it has already thrown away and reused. Trusting that stale pointer is the whole bug, the kind of slip known as a use-after-free. From there, Nebula's team chained a few clever steps to turn that small mistake into full control, ending by tricking the kernel into running their own code as the all-powerful "root" user. On their test machine, it took about five seconds.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8wc03LNvZ2a7JyIbKiIlqmTOq9oU4QhrvhSF7Gd5ybjKRVk_StUELtKyqVdEACftPHxSdAKFU2uTkEdcQr2wtvd-clQ97Y2gEOUzuWcaA-6F5ulxA0FFtbYGt-Uo47JVTu-FPMD5bD8DH8p5T8raE9CZlN4jlS8PsjRevYiHF3GgxFlxl_h2C9oUAc50/s1700-e365/linux-exploit.jpg)

The flaw has been in Linux since 2011 and was fixed in April, with distributions now rolling out the patch ([3bfdc63936dd](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?id=3bfdc63936dd4773109b7b8c280c0f3b5ae7d349)). It affects nearly every Linux build and scores 7.8 out of 10 (high, not critical) because an attacker needs to already be logged in to the machine. Nebula found it with VEGA, its AI-driven bug-hunting tool.

## What to do

Install your distribution's current kernel, not just the first patched build. The original fix introduced a separate crash bug (CVE-2026-53166), and the cleanup for that was still settling upstream in early July, so early builds may lack the final version.

There is no complete workaround, since the operations that trigger it are routine for any local process.

Availability is uneven so far. Ubuntu, for example, had patched its newest release and some cloud kernels, but as of early July still listed 24.04, 22.04, and 20.04 LTS as vulnerable or in progress. Check your distribution's advisory and confirm the fixed package version rather than assuming one is waiting.

Two build options, RANDOMIZE\_KSTACK\_OFFSET and STATIC\_USERMODE\_HELPER, make this exploit harder, but they are mitigations, not fixes. Patch shared and multi-tenant machines first, cloud servers, containers, and CI runners, where an attacker is most likely to find the local foothold this bug needs.

## Not the only kernel-to-root bug this year

GhostLock joins a run of 2026 Linux privilege-escalation bugs, several of which share a detail: an automated tool found them.

VEGA found GhostLock; days earlier, researchers disclosed [Bad Epoll](https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html) (CVE-2026-46242), a close cousin that also turns an unprivileged user into root. It was proven through kernelCTF and, unusually for this class of bug, works on Android.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Bad Epoll sits in the same stretch of code where Anthropic's Mythos model was credited with a related flaw. What they share is old, heavily used kernel machinery that few had reread in years, until automated tools started combing it. Futex priority inheritance dates to 2011. The class is not theoretical: another 2026 bug, [Copy Fail](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html) (CVE-2026-31431), is already on CISA's list of vulnerabilities seen in real-world attacks.

GhostLock is also the second half of a chain Nebula calls **IonStack**. The first half, CVE-2026-10702, is a Firefox flaw that runs code inside the browser and escapes its sandbox; GhostLock carries it the rest of the way to root.

Nebula has already demonstrated the full chain, from a single tap on a malicious link to full control, against Firefox on Android. That is why a "local only" kernel bug still matte...