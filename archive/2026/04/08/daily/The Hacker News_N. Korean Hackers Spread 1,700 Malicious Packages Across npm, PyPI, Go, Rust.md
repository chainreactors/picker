---
title: N. Korean Hackers Spread 1,700 Malicious Packages Across npm, PyPI, Go, Rust
url: https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html
source: The Hacker News
date: 2026-04-08
fetch_date: 2026-04-09T04:32:34.532798
---

# N. Korean Hackers Spread 1,700 Malicious Packages Across npm, PyPI, Go, Rust

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [N. Korean Hackers Spread 1,700 Malicious Packages Across npm, PyPI, Go, Rust](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html)

**Ravie Lakshmanan**Apr 08, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiJCapdeJ9Q-yAbFZ7EG69FNg_jPvK7YptY2C7TN6txlcPM_bvVrcbqN1bi-vy2IFi8Ai485K-DZblHR8XwZxdch90kWSv48wjvZF7oj0wy0IMd-B7VPuSiUbSFSJKAlErnSUZWjyVOf-Fyy-LqlxLbGLA7rxIkxlgc6_WRyCNH3XWDLb5GtnmjvxFjUrt/s1700-e365/pack.jpg)

The North Korea-linked persistent campaign known as **[Contagious Interview](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)** has spread its tentacles by publishing malicious packages targeting the Go, Rust, and PHP ecosystems.

"The threat actor's packages were designed to impersonate legitimate developer tooling [...], while quietly functioning as malware loaders, extending Contagious Interview’s established playbook into a coordinated cross-ecosystem supply chain operation," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/contagious-interview-campaign-spreads-across-5-ecosystems) in a Tuesday report.

The complete list of identified packages is as follows -

* npm: dev-log-core, logger-base, logkitx, pino-debugger, debug-fmt, debug-glitz
* PyPI: logutilkit, apachelicense, fluxhttp, license-utils-kit
* Go: github[.]com/golangorg/formstash, github[.]com/aokisasakidev/mit-license-pkg
* Rust: logtrace
* Packagist: golangorg/logkit

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

These loaders are designed to fetch platform-specific second-stage payloads, which turn out to be a piece of malware with infostealer and remote access trojan (RAT) capabilities. It's primarily focused on gathering data from web browsers, password managers, and cryptocurrency wallets.

However, a Windows version of the malware delivered via "license-utils-kit" incorporates what's described by Socket as a "full post-compromise implant" that's equipped to run shell commands, log keystrokes, steal browser data, upload files, terminate web browsers, deploy AnyDesk for remote access, create an encrypted archive, and download additional modules.

"That makes this cluster notable not just for its cross-ecosystem reach, but for the depth of post-compromise functionality embedded in at least part of the campaign," Boychenko added.

What makes the latest set of libraries noteworthy is that the malicious code is not triggered during installation.Rather, it's embedded into seemingly legitimate functions that align with the package's advertised purpose. For instance, in the case of "logtrace," the code is concealed within "Logger::trace(i32)," a method that's unlikely to raise a developer's suspicion.

The expansion of Contagious Interview across five open-source ecosystems is a further sign that the campaign is a well-resourced and persistent supply chain threat engineered to systematically infiltrate these platforms as initial access pathways to breach developer environments for espionage and financial gain.

In all, Socket said it has identified [more than 1,700 malicious packages](https://socket.dev/supply-chain-attacks/north-korea-s-contagious-interview-campaign) linked to the activity since the start of January 2025.

The discovery is part of a broader software supply chain compromise campaign undertaken by North Korean hacking groups. This includes the [poisoning](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html) of the popular Axios npm package to distribute an implant called WAVESHAPER.V2 after taking control of the package maintainer's npm account via a tailored social engineering campaign.

The attack has been attributed to a financially motivated threat actor known as UNC1069, which overlaps with BlueNoroff, Sapphire Sleet, and Stardust Chollima. Security Alliance (SEAL), in a report published today, said it blocked 164 UNC1069-linked domains impersonating services like Microsoft Teams and Zoom between February 6 and April 7, 2026.

"UNC1069 operates multi-week, low-pressure social engineering campaigns across Telegram, LinkedIn, and Slack – either impersonating known contacts or credible brands or by leveraging access to previously compromised company and individual accounts – before delivering a fraudulent Zoom or Microsoft Teams meeting link," SEAL [said](https://radar.securityalliance.org/advisory-on-dprk-unc1069-fake-microsoft-teams-and-zoom-calls/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

These fake meeting links are used to serve ClickFix-like lures, resulting in the execution of malware that contacts an attacker-controlled server for data theft and targeted post-exploitation activity across Windows, macOS, and Linux.

"Operators deliberately do not act immediately following initial access. The implant is left dormant or passive for a period following compromise," SEAL added. "The target typically reschedules the failed call and continues normal operations, unaware that the device is compromised. This patience extends the operational window and maximizes the value extracted before any incident response is triggered."

In a statement shared with The Hacker News, Microsoft said financially-driven North Korean threat actors are actively evolving their toolset and infrastructure, using domains masquerading as U.S.-based financial institutions and video conferencing applications for social engineering.

"What we are seeing consistently is ongoing evolution in how DPRK-linked, financially motivated actors operate, shifts in tooling, infrastructure, and targeting, but with clear continuity in behavior and intent," Sherrod DeGrippo, general manager for threat intelligence at Microsoft, said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIid...