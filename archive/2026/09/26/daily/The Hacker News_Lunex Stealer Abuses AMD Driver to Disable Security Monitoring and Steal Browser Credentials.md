---
title: Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials
url: https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html
source: The Hacker News
date: 2026-09-26
fetch_date: 2026-09-27T07:25:09.237696
---

# Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser Credentials](https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html)

**Ravie Lakshmanan**Sep 26, 2026Malware / Endpoint Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlKEfNLMvV7mEVtxmw1nS48l0bWRxvhvRH5MHdn20FjDTm6B0_5okfLjQ49AamYo9DPVC1aV1O2bl11Vd8776ziWsV96tcxQviDK0RjOnGK_Dyx_Zs2e2VBjgChf91_H2cHH0u_UoyAGlGlJkKnozWFqf-sxmXNW0QlnfY3Ilgdkg3p4qG7p3Z0SmdnJMq/s1700-nu-rw-lo-l85-e365/stealer-malware.jpg)

The [Psychedelic Stealer](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html) malware distributed via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks is part of a wider malware-as-a-service (MaaS) platform called **Lunex**.

The new findings come from Ontinue, which described the activity as a four-stage attack chain aimed at targeting Ukrainian-speaking users.

"The attack chain begins with a fake CAPTCHA page and culminates in the deployment of a fully-featured C2 agent," Ontinue threat researcher Rhys Downing [said](https://www.ontinue.com/resource/lunex-unmasked-a-new-information-stealer-deployed-through-byovd/) in a technical report. "The stealer extracts credentials and data from seven Chromium-based browsers, exfiltrates cryptocurrency wallets, and establishes persistent remote filesystem access through a PowerShell-based Native Messaging Host installed within the victim's browser."

The infection makes use of bogus MSI installers delivered via ClickFix to trigger a series of actions, including delivering a loader dubbed LunexLoader that's designed to bypass User Account Control (UAC) on Windows using the CMSTPLUA COM object, leverage the bring your own vulnerable driver ([BYOVD](https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html)) attack for defense evasion, and finally download the stealer payload.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The use of the BYOVD technique is significant, not least because it's rarely employed as a precursor to a final-stage payload like an information stealer. Lunex takes advantage of a vulnerable kernel-mode driver for AMD Radeon Software ("PDFWKRNL.sys"), which is [susceptible](https://thehackernews.com/2023/11/researchers-find-34-windows-drivers.html) to [CVE-2023-20598](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6009.html), to [escalate privileges](https://github.com/unkvolism/pdfwkrnl) and blind security-related processes while keeping them running.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7yEJ97LR-W2z0F_VjMhJWnTgGBkC6gWvnCEWJcA248K7pyJzSLKcWBXUs7FOKEWMFbS2ibGIvvzaIvCLk4O0RZZoMbKMS4gzEb9RzeyP2fwJPn7ks-nockpI_ycotqUBVIJ5SjM19_TrFrskk2FuojQ_K85mGXlbKcjne6qck37R8AzHX0bz3GVfZPAAx/s1700-nu-rw-lo-l85-e365/lunex.jpg)

Psychedelic Stealer was [first documented](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html) earlier this week by Arctic Wolf Labs, detailing the threat actor's modus operandi of compromising legitimate websites belonging to a hair-treatment clinic, a scale-model manufacturer, a specialist bookseller, a psychological facility, a tool retailer, and an automotive retailer to inject an iframe element designed to serve the ClickFix lure.

"Our analysis of the attack chain found that, before the stealer is delivered, the malware is designed to use a legitimate but vulnerable driver to switch off security tools on the victim's machine. With those protections disabled, the information stealer is then deployed to take browser passwords, session cookies, and cryptocurrency wallet data," Downing told The Hacker News.

The earliest reference to Lunex in cybersecurity literature dates back to June 2026, when BlueTeamCoolTeam's Luke Wilkinson [identified](https://blueteam.cool/posts/lunex-c2-osint/) six active Lunex Stealer's command-and-control (C2) panels across the U.S., Finland, Germany, the Netherlands, and Ukraine.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTQwIafXmaCwtK6byfnmH_RiR0PCPadYECjTkNHdLdXbSaiKNITFEamVKRK25pX3f1m4dkNYQ31cL6WEnPaCQ5txCb55CvtKmitlRkLf02VHD4J7PI-Sct5WLhO37cmDhpxa0Um8BSH-2baw-3IP01PvXoSowhnU1CAg3t1WudpwjQOApYPk83QQhnf4Mc/s1700-nu-rw-lo-l85-e365/lun.png) |
| LunexStealer (aka Psychedelic Stealer) C2 Panel | Source: BlueTeamCoolTeam |

It's worth noting that both Psychedelic Stealer and LunexStealer refer to the same component of the MaaS platform. "'Psychedelic' is the name of the malware file that runs on victims' devices, while Lunex is the underlying platform being sold to multiple criminal groups, which is the reason for the name 'Lunex' and 'LunexStealer,'" Downing explained.

Upon execution, LunexStealer communicates with the Lunex panel at 193.178.159[.]128 over HTTP to facilitate comprehensive information theft -

* Steal credentials from Google Chrome, Microsoft Edge, Brave, Yandex Browser, Opera, Opera GX, and Vivaldi.
* Enumerate five desktop cryptocurrency wallets, Bitcoin Core, Litecoin, Exodus, Atomic Wallet, and Electrum, and four browser extension wallets, MetaMask, MetaMask Legacy, OKX Wallet, and SafePal Wallet, and exfiltrate relevant data from them.
* Establish persistence using a Registry Run key, a hidden scheduled task named "psychedelicloveUtils," and register a [Chrome native-messaging bridge or host](https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging) (NMH) that allows the stealer to perform additional actions.

"The host is backed by a 13,200-byte PowerShell script embedded in the .rdata section that implements the Chrome Native Messaging protocol over standard input and output," Downing said. "The NMH operates within Chrome’s process context. It survives stealer binary deletion, system reboots...