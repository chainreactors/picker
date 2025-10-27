---
title: Cybercriminals Deploy CORNFLAKE.V3 Backdoor via ClickFix Tactic and Fake CAPTCHA Pages
url: https://thehackernews.com/2025/08/cybercriminals-deploy-cornflakev3.html
source: The Hacker News
date: 2025-08-22
fetch_date: 2025-10-07T00:48:47.331301
---

# Cybercriminals Deploy CORNFLAKE.V3 Backdoor via ClickFix Tactic and Fake CAPTCHA Pages

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Cybercriminals Deploy CORNFLAKE.V3 Backdoor via ClickFix Tactic and Fake CAPTCHA Pages](https://thehackernews.com/2025/08/cybercriminals-deploy-cornflakev3.html)

**Aug 21, 2025**Ravie LakshmananMalware / Cryptocurrency

[![Fake CAPTCHA Pages](data:image/png;base64... "Fake CAPTCHA Pages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbT3j2vzgoIvsAp8iLEcd7KiWNBHY3w0QWVemp1qG36ncpih2LrlDaXmtHqzzt9EQElI6R-8WZCMQIEs93IynqW1TCRpRKr-E8JwFuTgG5AqvpV_HbfppvAiQqtCdpbyZVqIWw1WJ0svpqWDPQWonCmWL61-eJ5JOSO1V3sGwZqnZq2lphKEt-bQR3KWqR/s2800/captchaa.jpg)

Threat actors have been observed leveraging the deceptive social engineering tactic known as [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html) to deploy a versatile backdoor codenamed CORNFLAKE.V3.

Google-owned Mandiant [described](https://security.googlecloudcommunity.com/community-blog-42/a-cereal-offender-analyzing-the-cornflake-v3-backdoor-5682) the activity, which it tracks as UNC5518, as part of an access-as-a-service scheme that employs fake CAPTCHA pages as lures to trick users into providing initial access to their systems, which is then monetized by other threat groups.

"The initial infection vector, dubbed ClickFix, involves luring users on compromised websites to copy a malicious PowerShell script and execute it via the Windows Run dialog box," Google [said](https://cloud.google.com/blog/topics/threat-intelligence/analyzing-cornflake-v3-backdoor) in a report published today.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The access provided by UNC5518 is assessed to be leveraged by at least two different hacking groups, UNC5774 and UNC4108, to initiate a multi-stage infection process and drop additional payloads -

* UNC5774, another financially motivated group that delivers CORNFLAKE as a way to deploy various subsequent payloads
* UNC4108, a threat actor with unknown motivation that uses PowerShell to deploy tools like VOLTMARKER and NetSupport RAT

The attack chain likely begins with the victim landing a fake CAPTCHA verification page after interacting with search results that employ search engine optimization (SEO) poisoning or malicious ads.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqc-L5nRadxfY17lnxdb403VFwAylXGHVPnd2EitV1VdntEcMHjB4cxxT4qeEmpOo1-5kBsIAwvTFX6ACa96c5AsP2hHSU7uX_FkP7XFIF8EUSfknfPLkwA942RL9bXIGAImh_9yAZqO9fBaGqybsIPe_CgRiRCO_qD9AFC9e5Mwsr5YrDwm7A535NdLf0/s2600/captcha.jpg)

The user is then tricked into running a malicious PowerShell command by launching the Windows Run dialog, which then executes the next-stage dropper payload from a remote server. The newly downloaded script checks if it's running within a virtualized environment and ultimately launches CORNFLAKE.V3.

Observed in both JavaScript and PHP versions, CORNFLAKE.V3 is a backdoor that supports the execution of payloads via HTTP, including executables, dynamic-link libraries (DLLs), JavaScript files, batch scripts, and PowerShell commands. It can also collect basic system information and transmit it to an external server. The traffic is proxied through Cloudflare tunnels in an attempt to avoid detection.

"CORNFLAKE.V3 is an updated version of CORNFLAKE.V2, sharing a significant portion of its codebase," Mandiant researcher Marco Galli said. "Unlike V2, which functioned solely as a downloader, V3 features host persistence via a registry Run key, and supports additional payload types."

Both generations are markedly different from their progenitor, a C-based downloader that uses TCP sockets for command-and-control (C2) communications and only has the ability to run DLL payloads.

Persistence on the host is achieved by means of Windows Registry changes. At least three different payloads are delivered via CORNFLAKE.V3. This comprises an Active Directory reconnaissance utility, a script to harvest credentials via Kerberoasting, and another backdoor referred to as WINDYTWIST.SEA, a C version of WINDYTWIST that supports relaying TCP traffic, providing a reverse shell, executing commands, and removing itself.

Select versions of WINDYTWIST.SEA have also been observed attempting to move laterally in the network of the infected machine.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"To mitigate malware execution through ClickFix, organizations should disable the Windows Run dialog box where possible," Galli said. "Regular simulation exercises are crucial to counter this and other social engineering tactics. Furthermore, robust logging and monitoring systems are essential for detecting the execution of subsequent payloads, such as those associated with CORNFLAKE.V3."

### The Rise of ClicFix Kits

The use of ClickFix has soared in popularity among threat actors over the past year, as it dupes users into infected their machines under the pretext of helping the solve minor technical issues, completing CAPTCHA verification checks by impersonating Cloudflare Turnstile, or spoofing a Discord server supposedly needing to verify a user before they can join.

This, in turn, entails giving users instructions that involve clicking prompts and copying, pasting, and running commands directly in the Windows Run dialog box, Windows Terminal, Windows PowerShell, or macOS Terminal, depending on the operating system used.

"Because ClickFix relies on human intervention to launch the malicious commands, a campaign that uses this technique could get past conventional and automated security solutions," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/) in a detailed write-up. "It's often combined with delivery vectors such as phishing, malvertising, and drive-by compromises, most of which even impersonate legitimate brands and organizations to further reduce suspicion from their targets."

[![](data:image/png;base64...)](http...