---
title: New Flaws in Microsoft macOS Apps Could Allow Hackers to Gain Unrestricted Access
url: https://thehackernews.com/2024/09/new-flaws-in-microsoft-macos-apps-could.html
source: The Hacker News
date: 2024-09-04
fetch_date: 2025-10-06T18:37:48.561840
---

# New Flaws in Microsoft macOS Apps Could Allow Hackers to Gain Unrestricted Access

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

# [New Flaws in Microsoft macOS Apps Could Allow Hackers to Gain Unrestricted Access](https://thehackernews.com/2024/09/new-flaws-in-microsoft-macos-apps-could.html)

**Sep 03, 2024**Ravie LakshmananEndpoint Security / Cyber Threat

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_JSKvRzgHgBeze4wIM8nSPfmqTYoR3gFyjaPolv_XJMmSX3trwCA-fvAfRLAwarm9XCk_bhR0bkyEnOb9dvWyNQbt0utUWtFcWCELj2uW502AhHyaCC-DG2iS8tM5KIe_-JtutYS-lOSNyLt7lwvsLZTAiFeVumE-UEsWrtpQSqL-YyA9gIeJv7pkRdkj/s790-rw-e365/msmacos.jpg)

Eight vulnerabilities have been uncovered in Microsoft applications for macOS that an adversary could exploit to gain elevated privileges or access sensitive data by circumventing the operating system's permissions-based model, which revolves around the Transparency, Consent, and Control ([TCC](https://thehackernews.com/2023/05/microsoft-details-critical-apple-macos.html)) framework.

"If successful, the adversary could gain any privileges already granted to the affected Microsoft applications," Cisco Talos [said](https://blog.talosintelligence.com/how-multiple-vulnerabilities-in-microsoft-apps-for-macos-pave-the-way-to-stealing-permissions/). "For example, the attacker could send emails from the user account without the user noticing, record audio clips, take pictures, or record videos without any user interaction."

The shortcomings span various applications such as Outlook, Teams, Word, Excel PowerPoint, and OneNote.

The cybersecurity company said malicious libraries could be injected into these applications and gain their entitlements and user-granted permissions, which could then be weaponized for extracting sensitive information depending on the access granted to each of those apps.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

TCC is a framework developed by Apple to manage access to sensitive user data on macOS, giving users added transparency into how their data is accessed and used by different applications installed on the machine.

This is maintained in the form of an encrypted database that records the permissions granted by the user to each application so as to ensure that the preferences are consistently enforced across the system.

"TCC works in conjunction with the application sandboxing feature in macOS and iOS," Huntress [notes](https://www.huntress.com/blog/full-transparency-controlling-apples-tcc) in its explainer for TCC. "Sandboxing restricts an app's access to the system and other applications, adding an extra layer of security. TCC ensures that apps can only access data for which they have received explicit user consent."

Sandboxing is also a countermeasure that guards against code injection, which enables attackers with access to a machine to insert malicious code into legitimate processes and access protected data.

"Library injection, also known as Dylib Hijacking in the context of macOS, is a technique whereby code is inserted into the running process of an application," Talos researcher Francesco Benvenuto said. "macOS counters this threat with features such as [hardened runtime](https://developer.apple.com/documentation/security/hardened_runtime), which reduce the likelihood of an attacker executing arbitrary code through the process of another app."

"However, should an attacker manage to inject a library into the process space of a running application, that library could use all the permissions already granted to the process, effectively operating on behalf of the application itself."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgHgzybcjG2MrpJutI7Az3lYQNe1VW1YhCmMK81KFVGOZ6n6Wuybwkl6XryMrDHx0-zC7RJyDdSFiWlfT-rTVzZ0Q7I4QaWMrRlyZiO0W4V9-of6jdzmtm55fLanl0ee0YDWfQlkxC4WyZladAW1escvaJkOK57sTcGWcR-0sXSAbaj6lmiq_JfRH8dlf9/s790-rw-e365/macos.jpg)

It however bears noting that attacks of this kind require the threat actor to already have a certain level of access to the compromised host so that it could be abused to open a more privileged app and inject a malicious library, essentially granting them the permissions associated with the exploited app.

In other words, should a trusted application be infiltrated by an attacker, it could be leveraged to abuse its permissions and gain unwarranted access to sensitive information without users' consent or knowledge.

This sort of breach could occur when an application loads libraries from locations the attacker could potentially manipulate and it has disabled library validation through a risky entitlement (i.e., set to true), which otherwise limits the loading of libraries to those signed by the application's developer or Apple.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"macOS trusts applications to self-police their permissions," Benvenuto noted. "A failure in this responsibility leads to a breach of the entire permission model, with applications inadvertently acting as proxies for unauthorized actions, circumventing TCC and compromising the system's security model."

Microsoft, for its part, considers the identified issues as "low risk" and that the apps are required to load unsigned libraries to support plugins. However, the company has stepped in to remediate the problem in its OneNote and Teams apps.

"The vulnerable apps leave the door open for adversaries to exploit all of the apps' entitlements and, without any user prompts, reuse all the permissions already granted to the app, effectively serving as a permission broker for the attacker," Benvenuto said.

"It's also important to mention that it's unclear how to securely handle such plug-ins within macOS' current framework. Notarization of third-party plug-ins is an option, albeit a complex one, and it would require Microsoft or Apple to sign third-party modules after verifying their security."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvW...