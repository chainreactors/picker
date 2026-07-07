---
title: 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems
url: https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:05.108918
---

# 16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems

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

# [16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html)

**Swati Khandelwal**Jul 06, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjG42lgj1grtq5EQICr-9RYvPU59uHFRBluzVoZ3TZLXEXBcF5bOPerpb_Ck-e6oNz6P4MO1VAiqbBXuPbImhng1CoRnRYHWSZTGOloHmYB5khhpCK5wW348uMgqmWIjTQPnOwCGV7OiPXJoJDWV0n1IPGP80hADXD3AnmRKbTb8jxyGQenhlgIpvNo29I/s1700-e365/linux-kvm.jpg)

A use-after-free bug in Linux's KVM hypervisor can be triggered from a guest virtual machine to corrupt the shadow-page state of the host kernel that runs it.

Dubbed '[Januscape](https://github.com/V4bel/Januscape)' and tracked as [CVE-2026-53359](https://nvd.nist.gov/vuln/detail/CVE-2026-53359), the flaw sits in the shadow MMU code that KVM shares across both Intel and AMD. The public proof-of-concept panics the host; the researcher claims that a separate, unreleased exploit turns the same bug into full host code execution.

Security researcher [Hyunwoo Kim (@v4bel)](https://x.com/v4bel) found and reported the bug. He described Januscape as the first guest-to-host exploit triggerable on both Intel and AMD, to the best of public knowledge. The flaw went unnoticed for roughly 16 years.

According to Kim, the exploit was used as a zero-day submission in [Google's kvmCTF](https://security.googleblog.com/2024/06/virtual-escape-real-reward-introducing.html), the controlled KVM vulnerability reward program that offers up to $250,000 for full guest-to-host escapes.

## How It Works

To run a virtual machine, KVM keeps its own private set of page tables that mirror the guest's memory layout. When it needs one of these tracking pages, it looks for an existing one to reuse.

The problem: it matched them by memory address alone and ignored what type of tracking page it was grabbing. Two different types can share the same address but do completely different jobs, so KVM would sometimes reuse the wrong kind.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

That mix-up scrambles KVM's internal records of which page belongs where, and once those records are wrong, something has to give.

Most of the time, the kernel notices the mess and shuts itself down on the spot to avoid doing damage. That crash is what the public demonstration triggers: a guest can knock over the whole host, taking every other VM on that machine down with it.

The rarer, worse case happens when the freed tracking page gets handed out for another use before the kernel cleans up. The cleanup then scribbles a value into memory it no longer owns. An attacker only controls where that write lands, not what gets written, but even that limited foothold can be worked up into running code on the host.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWII438TnKqzUiPCHjtwVr1UylqF9K0J20MeiuiXAo5npYotak_K7JdQtfVH1PyQQJsLrCVjA59LIUwVf-LHg_xtl3PKf3rNZwlpuHh9CkPUCo6yW_INktscrsJKT5u5vF8fIzG01Kcqx1-Be1lynI5JxMtyb3f7UsWrlSQviPVRtH3Fa-FiEUZBDX6p0/s1700-e365/Januscape.gif)

The flaw behaves the same on Intel and AMD chips; only the final, hardest step of turning it into full control takes different work on each.

## Who Is Affected

The vulnerable code has been present since [commit 2032a93d66fa](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=2032a93d66fa) in August 2010 (kernel 2.6.36 era) and was fixed by [commit 81ccda30b4e8](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=81ccda30b4e8), merged into mainline on June 19, 2026.

The attack requires two things from the guest side: root inside the VM, a common condition on rented cloud instances, and nested virtualization exposed by the host. Even on hosts that run hardware EPT or NPT by default, nested virtualization forces KVM back through the legacy shadow MMU, which is where the bug sits.

The exploit needs no cooperation from QEMU or any userspace VMM. It is purely an in-kernel KVM bug.

The practical concern is any x86 environment that hosts untrusted guests with nested virtualization enabled. An attacker who rents a single such instance can panic the host, taking down every other tenant VM on the same physical machine.

Kim said the withheld full exploit runs code as root on the host, which would expose other guests on the same machine to that root access. On distributions like RHEL, where /dev/kvm is world-writable (0666), Kim noted the same bug could also serve as a local privilege escalation to root, though the guest-to-host path is the higher-impact use.

## A Busy Few Months for One Researcher

Januscape is Kim's third Linux kernel exploit disclosure in roughly two months. In May 2026, he disclosed [Dirty Frag](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html) ([CVE-2026-43284 / CVE-2026-43500](https://github.com/V4bel/dirtyfrag)), a page-cache write vulnerability chain that delivers deterministic root on most major distributions, extending the same bug class as Dirty Pipe and Copy Fail.

In June, he published [ITScape](https://github.com/V4bel/ITScape) (CVE-2026-46316), the first publicly demonstrated guest-to-host escape on KVM/arm64, exploiting a race condition in the virtual interrupt controller. Januscape now adds the x86 side; the same trigger fires on both Intel and AMD, with the PoC carrying a separate code path for each vendor.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

Google launched kvmCTF in 2024 specifically because KVM underpins both Android and Google Cloud. A separate KVM x86 shadow paging...