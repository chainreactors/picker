---
title: Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access
url: https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
source: The Hacker News
date: 2026-11-21
fetch_date: 2026-11-22T09:02:52.654796
---

# Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [Attackers' AI Agents Found a Zero-Day in Medical-Imaging Software and Gained Root Access](https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html)

**Ravie Lakshmanan**Nov 21, 2026Artificial Intelligence / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEIG6Wgi3wGQXrsdGKEf4ORPFjHVGpRkoSUPraOJfKhGmB0vYFojLq2mCuOP3a71_XpNZusvn45ZDa1J3a7eQ0WE3XJY0FGunHVWB1yHBluJT5vSDCmzkhaFGiHjeKbnoah6noyZ3mNInS-mjJK1Gfcf7jT3A60ZYR_eknSgt_sEa6MNGM-DA5-aLXMbZ5/s1700-nu-rw-lo-l85-e365/medical-ai.jpg)

Suspected China-linked hackers used autonomous AI agents to find a previously unknown flaw in **MONAI Label**, an open-source medical imaging server, and gain root access to a university server, Amazon Threat Intelligence said this week.

The flaw allows an attacker with no account to write files outside the server's storage folder, and it affects MONAI Label 0.8.5 and earlier in the default setup, which runs with no login enabled.

The maintainers have merged a fix in the source code, but there is still no fixed version to install.

MONAI Label is a server that research teams use to label medical scans and train imaging models; it is a separate program from the broader MONAI framework.

The weakness is a path-traversal flaw in the parts of the server that store uploaded images and labels. A file identifier supplied by the caller is appended to the storage folder and written to disk without checking that the result remains within that folder.

The server writes with the privileges of the account it runs under, so an attacker cannot write anywhere on the machine, but a writable code or settings location can open a path to running code. Authentication is off by default, so any client that can reach the server over the network can set off the write. Versions 0.8.5 and earlier are affected.

Amazon reconstructed the intrusion after finding the operator's own **Cairn** control panel sitting on the internet without a password. Cairn is an open-source framework that runs AI agents as automated penetration testers, and the exposed panel revealed the agents' task settings, prompts, and run history.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

Over about 48 hours in September, the agents mapped the application's interface and reached the point of writing files to the server in roughly 11 minutes, the company said in its [incident report](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/).

The agents worked with little step-by-step direction. The operator set the goal of getting shell access and chose the targets, and the agents selected the methods themselves, according to the company.

Investigators tie the campaign to a China-linked actor with moderate confidence, pointing to Simplified Chinese prompts, China Standard Time settings, and targets likely of interest to China. They did not connect the work to a named group or establish that a government was behind it.

A root shell came later, and not within those 11 minutes. In a separate session, the agents used the same flaw to plant a file that Python runs automatically at startup. They then triggered a training feature that started a new Python process, which loaded that file and connected back to the attacker as root.

That root access was on one university server, and whether another MONAI Label system would give the same result depends on how it is run and what its service account can do.

In a later session, the operator handed the agents a tunnel into a second university network running the same software. Amazon believes the network was broken into in the same way but has not confirmed the second compromise.

The maintainers confirmed the flaw and merged [the source fix](https://github.com/Project-MONAI/MONAILabel/pull/1915) on October 19, which forces uploads to resolve inside the approved folders and rejects empty names or names that begin with a dot.

Their [security advisory](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94), published earlier this week, still lists no patched version and says the correction will arrive in a future release. The newest [release listing](https://pypi.org/project/monailabel/) remains 0.8.5, which dates to 2024. A merged fix in source code is not the same as a package you can install.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The flaw is now listed in the [CVE record](https://www.cve.org/CVERecord?id=CVE-2026-133968) as CVE-2026-133968, published this week and rated 9.8 out of 10, a critical score. The project's advisory still shows no CVE assigned, which is a lag in updating that page, not a sign of a second flaw.

### What to Do Now

With no fixed release available, the practical steps are to cut off exposure and limit what a compromised server could reach:

* Block untrusted network access to MONAI Label servers with firewall and routing rules, not just hard-to-guess URLs.
* Turn on authentication, which the server leaves off by default.
* Run the server under a limited account rather than root, and restrict the folders it can write to.
* Do not assume a source build is safe. Confirm it includes the October fix before treating it as patched.
* If a server was reachable, check for unexpected Python startup files and unusual training jobs, the path the reported attack used.

The company's account is based on its own reconstruction and has not been independently confirmed. It does not show that patient scans or records were taken, that clinical systems were touched, or that the attacker reached past the university targets described.

The campaign also included failed operations, and the root result on one server should not be taken as the outcome for every MONAI Label deployment.

Found this article interesting? Follow us on [Google News](https://news.google.com/publicatio...