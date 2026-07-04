---
title: New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android
url: https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html
source: The Hacker News
date: 2026-07-03
fetch_date: 2026-07-04T05:49:52.222192
---

# New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android

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

# [New "Bad Epoll" Linux Kernel Flaw Lets Unprivileged Users Gain Root, Hits Android](https://thehackernews.com/2026/07/new-bad-epoll-linux-kernel-flaw-lets.html)

**Swati Khandelwal**Jul 03, 2026Linux / Android

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggOXDckpE46PYIzBnXsx_kyHzFvlcB3l8qEr6feRNBhRQMKc2p5r2pQArl-NrsoB2z6vE917nXVHpuuMZOgZcRDMlwbVYC0ocK3uIsb-h59qed_kuvDKwvukQCAs-VDcE5Ail8mTRSPpnNfrPzKv5oAMQ9fJCDNE_2PpPrN9a9mOwGUIs0TnWq6_r58HM/s1700-e365/root-linux.gif)

A newly disclosed Linux kernel flaw called **Bad Epoll** (CVE-2026-46242) lets an ordinary user with no special access take full control of a machine as root. It affects Linux desktops, servers, and Android, and a fix is out.

**Bad Epoll** sits in the same small stretch of kernel code where Anthropic's most powerful AI model, **[Mythos](https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html)**, recently found a different bug.

The AI caught one flaw and missed this one. A researcher, Jaeyoung Chung, found it and built a working attack.

## How the Bug Works

Epoll is a standard Linux feature that lets a program watch many files or network connections at once. Servers, network services, and web browsers all lean on it. You cannot simply switch it off.

Bad Epoll is a "use-after-free" bug. Two parts of the kernel try to clean up the same internal object at the same time. One frees the memory while the other is still writing into it. That brief collision lets an attacker corrupt kernel memory, then climb from a normal account up to root.

The catch is timing. The window where the two paths collide is only about six machine instructions wide, so a random attempt almost never lands in it. Chung's exploit widens that window and retries without crashing, reaching root about 99% of the time on tested systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Two things make it more dangerous: by his account, it can be triggered from inside Chrome's renderer sandbox, which blocks almost every other kernel bug, and it can reach Android, which most Linux privilege bugs cannot.

Chung submitted the flaw as a zero-day to Google's kernelCTF program, and full technical details are in his [public writeup](https://github.com/J-jaeyoung/bad-epoll). There is no sign it has been used in real attacks: as of this writing, it is not on CISA's Known Exploited Vulnerabilities list, and the only working code is that kernelCTF proof of concept. An Android version of the exploit is still in progress.

Both bugs trace back to a single 2023 change to the epoll code. Chung says Mythos found the first of the two, now tracked as CVE-2026-43074, with a fix landing earlier in 2026.

Anthropic has separately said Mythos [found Linux kernel privilege-escalation bugs](https://red.anthropic.com/2026/mythos-preview/), though it has not publicly linked that work to Bad Epoll. Finding the first one was a real result, because race-condition bugs are notoriously hard to spot.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtnZFy61eL7vjWXOintv-DnYQlkLtuGFI3RFS5U90wBUg5udUGhhL0Vr94Uko9hDMdKltJqZCWmOZL2xyu6C2AYB0VRwboGPwBaRrboVUWnyd6LkRAryVTyv99VypVt5wiQ7jQRApNLzcPCKZ2F3cDVfiuoLEtJ15h5nuJRmqz09oxH8eWaYlZyiQ0dHM/s1700-e365/roots.jpg)

So why did the same AI miss the sibling flaw? Chung offers two likely reasons and is careful to say no one can be sure.

* First, the timing window is tiny, so the exact sequence of events is hard to picture even while staring at the code.
* Second, there is little evidence at runtime.

Once the first bug is patched, Bad Epoll's memory error usually does not trip KASAN, the kernel's main bug detector, so nothing flags that something is wrong.

Epoll cannot be turned off, so there is no workaround. Apply upstream commit [a6dc643c6931](https://git.kernel.org/stable/c/a6dc643c69311677c574a0f17a3f4d66a5f3744b), or install your distribution's backport when it lands. Kernels built on 6.4 or newer are affected unless they already have the fix.

Older 6.1-based kernels, including some Android phones such as the Pixel 8, are not, because the bug arrived in 6.4.

## A Bad Year for the Linux Kernel

Bad Epoll joins a well-known family of kernel bugs used to root Android, following earlier entries called [Bad Binder](https://thehackernews.com/2019/10/android-kernel-vulnerability.html), [Bad IO\_uring](https://thehackernews.com/2025/04/linux-iouring-poc-rootkit-bypasses.html), and Bad Spin.

It also lands in a busy stretch for Linux privilege flaws, though most of the recent ones work differently. [Copy Fail](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html) (CVE-2026-31431) landed in April and is now on CISA's [Known Exploited Vulnerabilities](https://thehackernews.com/2026/05/cisa-adds-actively-exploited-linux-root.html) list. [The Dirty Frag chain](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html), [Fragnesia](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html), [DirtyClone](https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html), [pedit COW](https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html) came after it.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Both are deterministic page-cache-write bugs, like [Dirty Pipe](https://thehackernews.com/2022/03/researchers-warn-of-linux-kernel-dirty.html) (2022), with no race to win, which makes them far more reliable to run. Bad Epoll is the older, harder kind: a race you have to win, like [Dirty Cow](https://thehackernews.com/2016/10/linux-kern...