---
title: Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass Container Isolation
url: https://thehackernews.com/2026/03/nine-crackarmor-flaws-in-linux-apparmor.html
source: The Hacker News
date: 2026-03-13
fetch_date: 2026-03-14T04:14:27.565831
---

# Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass Container Isolation

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass Container Isolation](https://thehackernews.com/2026/03/nine-crackarmor-flaws-in-linux-apparmor.html)

**Ravie Lakshmanan**Mar 13, 2026Linux / Vulnerability

[![Nine CrackArmor Flaws](data:image/png;base64... "Nine CrackArmor Flaws")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjq_iDZMyZB2yYcYrlFVa1dJoHT3mV0d9HfTPEpKmflkN-4zBDaSNIurPPADFGUW9GfTfMaCDlwUb6ywLpKiQa5CtSGSC6sPJIqfe-gRWhUa_z1B6Obazf_U5NuRX-ruWpomgMJQqcjD7XPeoyhgbVplGYCX3zQKFKmSIf0iSBwoUXhuE1ZZeZns9-fMlNr/s1700-e365/linux-root.jpg)

Cybersecurity researchers have disclosed multiple security vulnerabilities within the Linux kernel's [AppArmor](https://apparmor.net/) module that could be exploited by unprivileged users to circumvent kernel protections, escalate to root, and undermine container isolation guarantees.

The nine confused deputy vulnerabilities have been collectively codenamed **CrackArmor** by the Qualys Threat Research Unit (TRU). The cybersecurity company said the issue has existed since 2017. No CVE identifiers have been assigned to the shortcomings.

AppArmor is a Linux security module that provides mandatory access control (MAC) and secures the operating system against external or internal threats by preventing known and unknown application flaws from being exploited. It has been included in the mainline Linux kernel since version 2.6.36.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"This 'CrackArmor' advisory exposes a [confused deputy flaw](https://cwe.mitre.org/data/definitions/441.html) allowing unprivileged users to manipulate security profiles via pseudo-files, bypass user-namespace restrictions, and execute arbitrary code within the kernel," Saeed Abbasi, senior manager of Qualys TRU, [said](https://blog.qualys.com/vulnerabilities-threat-research/2026/03/12/crackarmor-critical-apparmor-flaws-enable-local-privilege-escalation-to-root).

"These flaws facilitate local privilege escalation to root through complex interactions with tools like Sudo and Postfix, alongside denial-of-service attacks via stack exhaustion and Kernel Address Space Layout Randomization (KASLR) bypasses via out-of-bounds reads."

[Confused deputy vulnerabilities](https://blog.qualys.com/vulnerabilities-threat-research/2025/07/24/fortifying-your-cloud-against-cross-service-confused-deputy-attacks) occur when a privileged program is coerced by an unauthorized user into misusing its privileges to perform unintended, malicious actions. The problem essentially exploits the trust associated with a more-privileged tool to execute a command that leads to privilege escalation.

Qualys said an entity that doesn't have permissions to perform an action can manipulate AppArmor profiles to disable critical service protections or enforce deny-all policies, triggering denial-of-service (DoS) attacks in the process.

"Combined with kernel-level flaws inherent in profile parsing, attackers bypass user-namespace restrictions and achieve Local Privilege Escalation (LPE) to full root," it added.

"Policy manipulation compromises the entire host, while namespace bypasses facilitate advanced kernel exploits such as arbitrary memory disclosure. DoS and LPE capabilities result in service outages, credential tampering via passwordless root (e.g., /etc/passwd modification), or KASLR disclosure, which enables further remote exploitation chains."

To make matters worse, CrackArmor enables unprivileged users to create fully‑capable user namespaces, effectively getting around Ubuntu's [user namespace restrictions](https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces) implemented via AppArmor, as well as subvert critical security guarantees like container isolation, least‑privilege enforcement, and service hardening.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

The cybersecurity company said it's withholding the release of proof-of-concept (PoC) exploits for the identified flaws to give users some time to prioritize patches and minimize exposure.

The problem affects all Linux kernels since version 4.11 on any distribution that integrates AppArmor. With more than 12.6 million enterprise Linux instances operating with AppArmor enabled by default in several major distributions, such as Ubuntu, Debian, and SUSE, immediate kernel patching is advised to mitigate these vulnerabilities.

"Immediate kernel patching remains the non-negotiable priority for neutralizing these critical vulnerabilities, as interim mitigation does not offer the same level of security assurance as restoring the vendor-fixed code path," Abbasi noted.

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

[Access Control](https://thehackernews.com/search/label/Access%20Control), [AppArmor](https://thehackernews.com/search/label/AppArmor), [Container Security](https://thehackernews.com/search/label/Container%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Kernel Security](https://thehackernews.com/search/label/Kernel%20Security), [linux](https://thehackernews.com/...