---
title: New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts
url: https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:24.473777
---

# New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts

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

# [New Zapscape KVM Flaw Could Let Privileged L1 Guest Code Escape to Linux Hosts](https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html)

**Swati Khandelwal**Aug 06, 2026Virtualization Security / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5BBX-j7uA7NqPF9tVWhx3y09F3whJ3zweRoWGyI2kJDxhW6ymOG1oumq5Oz0sZWtCAKSCALcd9TTl7Kf5Mo3aqE3aWKH8jfKWt2uUD-CUa6tmid-3MvMTM08EAEhg5iLQ2mlEgFkVeuVKv1QkRqr2T0Ya9JcNtMYheggInGndCG0n-N7BPjyH9vbKCg8/s1700-e365/Zapscape.gif)

**Zapscape**, a new Linux kernel vulnerability, could allow an attacker with kernel privileges inside an L1 guest virtual machine (VM) to escape KVM isolation and execute code on the host. The risk applies when nested virtualization is exposed to untrusted guests.

The flaw is tracked as **CVE-2026-64561** and affects KVM/x86's shadow memory management unit (MMU), which manages shadow page tables used for nested guest memory translation.

Security researcher **Hyunwoo Kim,** who disclosed the bug, said the demonstrated exploit path can run commands on the host with kernel, or root, privileges.

The upstream fix has been merged, and administrators running KVM hosts that expose nested virtualization to untrusted guests should update to a fixed stable kernel or a vendor package that backports the patch.

The required L1 kernel privilege usually means guest root. Intel systems also require both EPT page-walk length 4 and 5 to be exposed to the L1 guest. AMD has no equivalent condition.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Zapscape is a stale-root check ordering flaw in KVM's shadow-MMU bookkeeping that can lead to a use-after-free. During guest-triggered page fault handling, KVM can reclaim MMU pages and invalidate the shadow MMU root page still being used by the fault-handling path. Because the path does not check the root again, KVM can continue under the invalidated root.

In a [technical write-up](https://github.com/V4bel/Zapscape/blob/main/assets/write-up.md), Kim described the issue as a use-after-free in the recursive zap path used when KVM reclaims shadow pages. KVM checked whether the current root was stale before making more MMU pages available. Reclaim could then invalidate that same root, but KVM continued the fault path and created child shadow pages under it.

Those child pages inherited the invalid state from the parent and were still placed on KVM's active MMU page list. Later cleanup could attach the same list link to two lists at once, then free the page while stale list references remain, creating a dangling link and post-free write.

Kim's public **proof-of-concept** uses that primitive to build a full chain that creates a root-owned file named /Zapscape on the host running the vulnerable KVM.

The proof-of-concept targets AMD nested SVM/NPT on Linux 7.1.3. Kim recommends running it under QEMU TCG for safe testing. QEMU is not the vulnerable component. Kim said the bug lives in in-kernel KVM and is triggered independently of QEMU's emulation.

Kim's August 6 write-up includes a public proof-of-concept, but it does not claim the flaw has been exploited in the wild. Kim also described it as "not a weaponized exploit that runs immediately" in cloud environments, saying real-world use would require moving the L1 actions into a guest kernel module and adapting the exploit to the host kernel configuration and memory backend.

The [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2026-64561) lists Linux 5.9 and later as affected until fixed stable releases, including 6.6.148, 6.12.101, 6.18.42, 7.1.6, and 7.2-rc5.

[Red Hat](https://access.redhat.com/security/cve/cve-2026-64561) assigned a preliminary CVSS score of 7.0 in its advisory and classified the issue as CWE-825, or expired pointer dereference.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Package status depends on each Linux vendor's tracker, not only upstream version strings. Red Hat cautions that its packages often carry backported fixes without rebasing to a new upstream version.

As of August 6, 2026, Debian's tracker listed bullseye, bookworm, and trixie kernel packages, including their security repositories, as vulnerable. It also listed forky as vulnerable and sid as fixed at 7.1.6-1.

According to the disclosure timeline, Kim reported the issue to security@kernel.org on July 11, 2026. A patch was posted and merged on July 21, the issue was submitted to the linux-distros list on August 1 under a five-day embargo, and CVE-2026-64561 was assigned on August 4. Public disclosure followed on August 6.

The fix, merged as commit 2abd5287f083, moves the stale-root check after make\_mmu\_pages\_available(). If reclaim invalidates the current root, KVM now restarts the fault with RET\_PF\_RETRY instead of continuing to map or fetch under the invalid root.

The disclosure follows Kim's earlier KVM work, including [Januscape](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html) (CVE-2026-53359), a separate KVM/x86 shadow-MMU issue covered by The Hacker News in July, and ITScape (CVE-2026-46316), a KVM/arm64 escape published in June.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Kernel Security](https://thehackernews.com/search/label/Kernel%20Security), [linux](https://thehackernews.com/search/label...