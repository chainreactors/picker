---
title: Evaluating Mitigations & Vulnerabilities in Chrome
url: http://security.googleblog.com/2024/10/evaluating-mitigations-vulnerabilities.html
source: Google Online Security Blog
date: 2024-10-04
fetch_date: 2025-10-06T18:46:37.178530
---

# Evaluating Mitigations & Vulnerabilities in Chrome

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Evaluating Mitigations & Vulnerabilities in Chrome](https://security.googleblog.com/2024/10/evaluating-mitigations-vulnerabilities.html "Evaluating Mitigations & Vulnerabilities in Chrome")

October 3, 2024

Posted by Alex Gough, Chrome Security Team

The Chrome Security Team is constantly striving to make it safer to browse the web. We invest in mechanisms to make classes of security bugs impossible, mitigations that make it more difficult to exploit a security bug, and sandboxing to reduce the capability exposed by an isolated security issue. When choosing where to invest it is helpful to consider how bad actors find and exploit vulnerabilities. In this post we discuss several axes along which to evaluate the potential harm to users from exploits, and how they apply to the Chrome browser.

Historically the Chrome Security Team has made major investments and driven the web to be safer. We pioneered browser [sandboxing](https://chromium.googlesource.com/chromium/src/%2B/HEAD/docs/design/sandbox.md), [site isolation](https://security.googleblog.com/2021/07/protecting-more-with-site-isolation.html) and the [migration to an encrypted web](https://blog.chromium.org/2023/08/towards-https-by-default.html). Today we’re investing in [Rust for memory safety](https://security.googleblog.com/2023/01/supporting-use-of-rust-in-chromium.html), hardening our existing C++ code-base, and improving detection with [GWP-asan](https://chromium.googlesource.com/chromium/src.git/%2B/HEAD/docs/gwp_asan.md) and [lightweight use-after-free](https://docs.google.com/document/d/1PE2tykvGqBJW3UpNcnOUwDHkkRAuNyfM5EHWDTNQ2VQ/edit?tab=t.0#heading=h.b966ynmd5x2b) (UAF) detection. Considerations of user-harm and attack utility shape our vulnerability [severity guidelines](https://chromium.googlesource.com/chromium/src/%2B/HEAD/docs/security/severity-guidelines.md) and payouts for bugs reported through our [Vulnerability Rewards Program](https://chromium.googlesource.com/chromium/src/%2B/refs/heads/main/docs/security/vrp-faq.md). In the longer-term the Chrome Security Team advocates for operating system improvements like less-capable lightweight processes, less-privileged GPU and NPU containers, improved application isolation, and support for hardware-based isolation, memory safety and flow control enforcement.

When contemplating a particular security change it is easy to fall into a trap of security nihilism. It is tempting to reject changes that do not make exploitation impossible but only make it more difficult. However, the scale we are operating at can still make incremental improvements worthwhile. Over time, and over the population that uses Chrome and browsers based on Chromium, these improvements add up and impose real costs on attackers.

### Threat Model for Code Execution

Our primary security goal is to make it safe to click on links, so people can feel confident browsing to pages they haven’t visited before. This document focuses on vulnerabilities and exploits that can lead to code execution, but the approach can be applied when mitigating other risks.

Attackers usually have some ultimate goal that can be achieved by executing their code outside of Chrome’s sandboxed or restricted processes. Attackers seek information or capabilities that we do not intend to be available to websites or extensions in the sandboxed renderer process. This might include executing code as the user or with system privileges, reading the memory of other processes, accessing credentials or opening local files. In this post we focus on attackers that start with JavaScript or the ability to send packets to Chrome and end up with something useful. We restrict discussion to memory-safety issues as they are a focus of current hardening efforts.

# User Harm ⇔ Attacker Utility

Chrome Security can scalably reduce risks to users by reducing attackers’ freedom of movement. Anything that makes some class of attackers’ ultimate goals more difficult, or (better) impossible, has value. People using Chrome have multiple, diverse adversaries. We should avoid thinking only about a single adversary, or a specific targeted user, the most advanced-persistent attackers or the most sophisticated people using the web. Chrome’s security protects a spectrum of people from a spectrum of attackers and risks. Focussing on a single bug, vector, attacker or user ignores the scale at which both Chrome and its attackers are operating. Reducing risks or increasing costs for even a fraction of threat scenarios helps someone, somewhere, be safer when using the web.

There are still better exploits for attackers and we should recognise and prioritize efforts that meaningfully prevent or fractionally reduce the availability or utility of the best bugs and escalation mechanisms.

### Good Bugs and Bad Bugs

All bugs are bad bugs but some bugs are more amenable to exploitation. High value bugs and escalation mechanisms for attackers have some or all of the following attributes:

**Reliable**

An exploit that sometimes crashes, or that when launched only sometimes allows for exploitation, is less useful than one that can be mechanically triggered in all cases. Crashes might lead to detection by the target or by defenders that collect the crashes. Attackers might not always have more than one chance to launch their attacks. Bugs that only surface when different threads must do things in a certain order require more use of resources or time to trigger. If attackers are willing to risk detection by causing a crash they can retry their attacks as Chrome uses a multi-process architecture for cross-domain iframes. Conversely, bugs that only occur when the main browser process shuts down are more difficult to trigger as attackers get a single attempt per session.

**Low-interaction**

Chrome exists so that people can visit websites and click on links so we take that as our baseline for minimal interaction. Exploits that only work if a user performs an action, even if that action might be expected, are more risky for an attacker. This is because the code expressing the bug must be resident on a system for longer, the exploit likely has a lower yield as the action won’t always happen, and the bug is less silent as the user might become suspicious if they seem to be performing actions they are not used to performing.

**Ubiquitous**

A bug that exists on several platforms and can be exploited the same way everywhere will be more useful than one which is only exploitable on one platform or needs to be ported to several platforms. Bugs that manifest on limited hardware types, or in fewer configurations, are only useful if the attacker has targets using them. Every bug an attacker has to integrate into their exploitation flow requires some ongoing maintenance and testing, so the fewer bugs needed the better. For Chrome some bugs only manifest on Linux, while others are present on all of our platforms. Chrome is one of the most ubiquitous software products today, but some of its libraries are even more widely used, so attackers may invest extra effort in finding and exploiting bugs in third party code that Chrome uses. Bugs that require a user to install an extension or rely on particular hardware configurations are less useful than ones reachable from any web page.

**Fast**

Attacks that require more than a few seconds to set up or execute are less likely to succeed and more likely to be caught. It is more difficult to test and develop a reliable exploit using a slow bug as the compile-test-debug cycle will be stretched.

**Scriptable**

Bugs that require an exploit to perform grooming or state manipulation to succeed are mor...