---
title: New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs
url: https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:24.777711
---

# New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs

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

![cybersecurity](data:image/svg+xml;base64...)

# [New Interrupt Injection Attack Can Bypass Spectre v2 Defenses on Intel and AMD CPUs](https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html)

**Swati Khandelwal**Aug 06, 2026Vulnerability / Hardware Security

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiA_BgCPUTlxOgmh4ljCoOazIkcoSA_BHUGZmfAuhxD8TiUzui2nhB5b5KV_lv50ocFWI14FG5RIe8rqrm6D8ZC8ACR7mY1bXE4JADKcTRIY1bfIeXtnYs07yXk2T9Jsv0-vcxPkKbl6FuNXxXylv5BQQQLTDSpJ2XSyqxvIsxYy5d2X1Kwt_2CSJegj9Tv/s1700-e365/place.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOSra_DOAu8v1CYXAo4z3cStSiHsuM6iF5vjHKmq0Q4kXMtGQ3n5EBjJoLNRzEFgW6xs6-GuSP0tUAX-EPYRHaDQQNHuz-8xSFbp__BShjMumlZdcwuZkl3GkVebYtWoYuqfgbyt-yKGo1OAal-ElVBKnRaiwjQKO7hgynkFx06IVH7Ipm43p4wc6NR9Y/s1700-e365/TONTOU.gif)

An unprivileged Linux program can time a hardware interrupt to land in the gap between a processor sanitizing its branch predictor and the kernel using it, re-poisoning the predictor after the defense has run.

MIT CSAIL researchers **Daniël Trujillo** and **Mengjia Yan** named the technique **INTERRUPT INJECTION**. On an AMD Zen 2 machine running Linux 6.14 with every default Spectre v2 mitigation on, their exploit leaked arbitrary kernel memory at 5.47 bytes per second with 91.97% accuracy, enough to locate and read /etc/shadow, which stores the system's password hashes, in five of ten attempts.

It needs no privileges, only local code execution, so the risk sits on shared systems running an affected processor.

The pair [disclosed](https://www.csail.mit.edu/news/new-attack-slips-past-latest-defenses-built-your-computers-processor) to AMD and Intel on February 5. AMD told them it plans a kernel patch; MIT says one has since shipped and arrives in a normal operating system update.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

A fix is in the Linux kernel. The commit, ["x86/bugs: Make Safe-RET robust against interrupt injection"](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f5fdd6665ac4d8528ed1c9242cb1cf7a7f5bdb0e), is dated June 2 and was written by Borislav Petkov and co-developed with David Kaplan, both AMD engineers. It describes the attack in the same terms the researchers do: injecting interrupts while Safe-RET runs "can neutralize the safe return sequence, potentially leading to data leakage through speculative execution."

The patch fixes up register state as though the Safe-RET sequence had completed, and avoids executing a RET instruction after the interrupt returns. That is one of the two routes the paper proposed.

AMD published a bulletin on August 6, [AMD-SB-7061](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7061.html), titled "Safe RET Interrupt Vulnerability," naming Zen 1 through Zen 4 processors as affected. Its summary says an attacker running code on an affected system "could inject an interrupt at a precise moment to disrupt Safe RET," which "could potentially weaken that protection and may result in information disclosure." AMD adds that the issue "appears to be associated with the Linux implementation of the Safe RET mitigation."

The bulletin credits Trujillo and says the behavior was demonstrated on Zen 1 and Zen 2, with Zen 3 and Zen 4 suggested but not demonstrated. The paper reports AMD testing on Zen 2 and Zen 4 only. The section headed "Affected Products and Mitigation" lists processors and nothing else: no patch reference, no kernel version, and no CVE.

According to the [paper](https://people.csail.mit.edu/mengjia/data/2026.USENIX.TONTOU.pdf) the researchers shared with The Hacker News, Intel does not consider a mitigation necessary.

Neither AMD's bulletin nor MIT's announcement points to the kernel commit. Without a CVE or a named kernel release, an administrator has to know the commit subject to check whether a given machine carries the fix.

The kernel reports SRSO status at /sys/devices/system/cpu/vulnerabilities/spec\_rstack\_overflow, and the [documentation defining that file's values](https://kernel.org/doc/html/latest/admin-guide/hw-vuln/srso.html) made no mention of interrupts when The Hacker News checked it on August 6.

The Hacker News has contacted AMD, Intel, and Arm for comment and will update this story with any response.

Each of these defenses sanitizes or isolates branch predictor state so an attacker's earlier training cannot steer a kernel branch. Intel does it on kernel entry, with [eIBRS](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html) and, depending on the processor, either a [branch history buffer clearing loop](https://thehackernews.com/2022/03/new-exploit-bypasses-existing-spectre.html) or the BHI\_DIS\_S control. AMD does it immediately before each kernel return, with saferet.

All of them assume nothing hostile runs in between. Trujillo and Yan call the class TONTOU, for Time-of-Neutralization to Time-of-Use, after the TOCTOU races familiar from software. Interrupts break that assumption, because they fire almost anywhere and Linux lets any user schedule them with nanosecond granularity.

If interrupt handling can execute between neutralization and use, the interrupt-return path is part of the Spectre v2 defense even when the mitigation was designed around kernel entry or return.

On Zen 2 that window is two instructions, six bytes. The researchers widened their odds by evicting those bytes from L1 and L2 cache using a sibling hyperthread, slowing them down, and by picking the write syscall, which left them controlling two registers.

Interrupts landed inside the window 5% to 12% of the time, and around 2% with those registers under attacker control. Once inside, the handler itself became the training gadget, armed with [Inception](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7005.html) ([CVE-2023-20569](https://thehackernews.com/2023/08/collidepower-downfall-and-inception-new.html)) to fill the return stack buffer with an attacker-chosen target. Inception is the 2023 AMD flaw saferet exists to stop.

Mispredictions turned up in kernel code on three of the four machines tested, at success rates of 0.75% on Zen 2, 0.22% on Intel Arrow Lake, and 0.037% on Cascade Lake Refresh. Zen 4 produced none in that test, and no...