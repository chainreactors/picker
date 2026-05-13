---
title: Patch Tuesday, May 2026 Edition
url: https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/
source: Krebs on Security
date: 2026-05-12
fetch_date: 2026-05-13T05:47:39.651832
---

# Patch Tuesday, May 2026 Edition

Advertisement

[![](/b-knowbe4/52.jpg)](https://www.knowbe4.com/secure-humans-and-agents?utm_source=krebs&utm_medium=display&utm_campaign=brand-ai-campaign-26&utm_content=static-human-ready)

Advertisement

[![](/b-doppel/10.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=imitation)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, May 2026 Edition

May 12, 2026

[0 Comments](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/#respond)

Artificial intelligence platforms may be just as susceptible to social engineering as human beings, but they are proving remarkably good at finding security vulnerabilities in human-made computer code. That reality is on full display this month with some of the more widely-used software makers — including **Apple**, **Google**, **Microsoft**, **Mozilla** and **Oracle** — fixing near record volumes of security bugs, and/or quickening the tempo of their patch releases.

As it does on the second Tuesday of every month, Microsoft today released software updates to address at least 118 security vulnerabilities in its various **Windows** operating systems and other products. Remarkably, this is the first Patch Tuesday in nearly two years that Microsoft is not shipping any fixes to deal with emergency zero-day flaws that are already being exploited. Nor have any of the flaws fixed today been previously disclosed (potentially giving attackers a heads up in how to exploit the weakness).

Sixteen of the vulnerabilities earned Microsoft’s most-dire “critical” label, meaning malware or miscreants could abuse these bugs to seize remote control over a vulnerable Windows device with little or no help from the user. **Rapid7** has done much of the heavy lifting today in identifying some of the more concerning critical weaknesses this month, including:

* [CVE-2026-41089](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41089): A critical stack-based buffer overflow in Windows Netlogon that offers an attacker SYSTEM privileges on the domain controller. No privileges or user interaction are required, and attack complexity is low. Patches are available for all versions of Windows Server from 2012 onwards.
* [CVE-2026-41096](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41096): A critical RCE in the Windows DNS client implementation worthy of attention despite Microsoft assessing exploitation as less likely.
* [CVE-2026-41103](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41103): A critical elevation of privilege vulnerability that allows an unauthorized attacker to impersonate an existing user by presenting forged credentials, thus bypassing Entra ID. Microsoft expects that exploitation is more likely.

May’s Patch Tuesday is a welcome respite from April, which saw Microsoft [fix a near-record 167 security flaws](https://krebsonsecurity.com/2026/04/patch-tuesday-april-2026-edition/). Microsoft was among a few dozen tech giants given access to a “**Project Glasswing**,” a much-hyped AI capability developed by **Anthropic** that appears quite effective at unearthing security vulnerabilities in code.

Apple, another early participant in Project Glasswing, typically fixes an average of 20 vulnerabilities each time it ships a security update for iOS devices, said **Chris Goettl**, vice president of product management at **Ivanti**. On May 11, Apple shipped iOS 15, which addressed at least 52 vulnerabilities and backported the changes all the way to iPhone 6s and iOS 15.

Last month, Mozilla released **Firefox 150**, which resolved [a whopping 271 vulnerabilities](https://arstechnica.com/ai/2026/04/mozilla-anthropics-mythos-found-271-zero-day-vulnerabilities-in-firefox-150/) that were reportedly discovered during the Glasswing evaluation.

“Since Firefox 150.0.0 released, they have been on a more aggressive weekly cadence for security updates including the release of Firefox 150.0.3 on May Patch Tuesday resolving between three to five CVEs in each release,” Goettl said.

The software giant Oracle likewise recently increased its patch pace in response to their work with Glasswing. In its most recent quarterly patch update, Oracle addressed at least 450 flaws, including [more than 300 fixes for remotely exploitable, unauthenticated flaws](https://www.securityweek.com/oracle-patches-450-vulnerabilities-with-april-2026-cpu/). But at the end of April, Oracle announced it was switching to a monthly update cycle for critical security issues.

On May 8, Google started rolling out updates to its Chrome browser that [fixed an astonishing 127 security flaws](https://www.forbes.com/sites/daveywinder/2026/05/08/critical-new-google-security-update-127-chrome-security-vulnerabilities-confirmed/) (up from just 30 the previous month). Chrome automagically downloads available security updates, but installing them requires fully restarting the browser.

If you encounter any weirdness applying the updates from Microsoft or any other vendor mentioned here, feel free to sound off in the comments below. Meantime, if you haven’t backed up your data and/or drive lately, doing that *before* updating is generally sound advice. For a more granular look at the Microsoft updates released today, checkout [this inventory](https://isc.sans.edu/forums/diary/Microsoft%20May%202026%20Patch%20Tuesday/32980/) by the **SANS Internet Storm Center**.

*This entry was posted on Tuesday 12th of May 2026 05:46 PM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Anthropic](https://krebsonsecurity.com/tag/anthropic/) [apple](https://krebsonsecurity.com/tag/apple/) [Chris Goettl](https://krebsonsecurity.com/tag/chris-goettl/) [Firefox 150](https://krebsonsecurity.com/tag/firefox-150/) [google](https://krebsonsecurity.com/tag/google/) [Ivanti](https://krebsonsecurity.com/tag/ivanti/) [microsoft](https://krebsonsecurity.com/tag/microsoft/) [Mozilla](https://krebsonsecurity.com/tag/mozilla/) [Oracle](https://krebsonsecurity.com/tag/oracle/) [Project Glasswing](https://krebsonsecurity.com/tag/project-glasswing/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [sans internet storm center](https://krebsonsecurity.com/tag/sans-internet-storm-center/)

Post navigation

[← Canvas Breach Disrupts Schools & Colleges Nationwide](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/)

### Leave a Reply [Cancel reply](/2026/05/patch-tuesday-may-2026-edition/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

Website

Δ

Advertisement

[![](/b-doppel/11.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=imitation)

Advertisement

Mailing List

[Subscribe here](/subscribe/)

Search KrebsOnSecurity

Search for:

Recent Posts

* [Patch Tuesday, May 2026 Edition](https://krebsonsecurity.com/2026/05/patch-tuesday-may-2026-edition/)
* [Canvas Breach Disrupts Schools & Colleges Nationwide](https://krebsonsecurity.com/2026/05/canvas-breach-disrupts-schools-colleges-nationwide/)
* [Anti-DDoS Firm Heaped Attacks on Brazilian ISPs](https://krebsonsecurity.com/2026/04/anti-ddos-firm-heaped-attacks-on-brazilian-isps/)
* [‘Scattered Spider’ Member ‘Tylerb’ Pleads Guilty](https://krebsonsecurity.com/2026/04/scattered-spider-member-tylerb-pleads-guilty/)
* [Patch Tuesday, April 2026 Edition](https://krebsonsecurity.com/2026/04/patc...