---
title: Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication
url: https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:11.701714
---

# Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Attackers Chain Two PaperCut Flaws to Execute Code Without Authentication](https://thehackernews.com/2026/08/attackers-chain-two-papercut-flaws-to.html)

**Ravie Lakshmanan**Aug 28, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdtPabCvuR_F2UFdCw8LS5eoXtD-jOpbuCy8WZYRycSP2vu_6yQK45qTehHimhoS-eXFPMTwg5jNM3m_X7ma5ELVz60Rjt3rlQhrqE4iTz8ggysLCt388GyaBVQbT28sGDv9a6drKNZooBiQNy0L3v8Gc3vxB9JILUD-eTtj5LZAlBbA3EyLlp5SkgIKPG/s1700-e365/1000103914.jpg)

Malicious actors are exploiting a [newly patched security flaw](https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html) in PaperCut NG and MF to execute arbitrary code on susceptible instances, as the company released a fresh emergency fix with additional hardening.

"This vulnerability gives an unauthenticated attacker remote control over PaperCut's trusted configuration, which could be used to execute arbitrary Java code inside the application's process," Huntress researchers John Hammond and Andrew Brandt [said](https://www.huntress.com/blog/papercut-actively-exploited).

Specifically, an attacker can leverage an unauthenticated request to make changes to the server configuration and ultimately achieve code execution. Huntress has explained the flaw as follows -

*In unpatched versions of PaperCut NG and PaperCut MF, a specifically crafted request can refer to one page that is rendered for the response, and another page that owns the component or action being executed.*

*PaperCut's authorization check could trust the rendered page and miss the permissions required by the component behind it. We found that an unauthenticated request could be utilized in this way to make changes to the server configuration. This enables access to sensitive endpoints that can trigger unsafe actions, and ultimately lets an ill-intended actor execute any arbitrary attacked-controlled code.*

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

PaperCut has since [publicly disclosed two flaws](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/) -

* **CVE-2026-82078** (CVSS score: 9.4) - An unsafe dynamic class loading vulnerability exists in the database connection utilities of PaperCut MF and PaperCut NG. The application instantiates database driver classes based on configurable driver names without validating against an allowlist of approved drivers
* **CVE-2026-81578** (CVSS score: 8.8) - An improper access control vulnerability exists in the web management interface of PaperCut MF and PaperCut NG. Under specific conditions, unauthenticated remote requests targeting administrative functions can trigger backend actions prior to the completion of access validation checks.

The development comes after PaperCut [released](https://thehackernews.com/2026/08/papercut-zero-day-exploited-in-attacks.html) a second emergency patch that it said includes "additional hardening beyond the original emergency patch." The Australian company has yet to share details about the nature of the malicious activity weaponizing the flaws.

"At this time, we don't have enough evidence to determine the threat actors' ultimate end goal," John Hammond, senior principal security researcher at Huntress, told The Hacker News. "Based on what we observed, the activity appears consistent with early-stage reconnaissance or validation, including commands to identify the victim’s user account and operating system."

According to preemptive exposure management firm watchTowr, attackers are chaining together both vulnerabilities to bypass authentication and gain remote code execution on affected instances.

"CVE-2026-81578 allows you to bypass authentication, and from there, you can edit a configuration file to exploit CVE-2026-82078 and gain Remote Code Execution," Jake Knott, head of threat intelligence at watchTowr, told The Hacker News.

The cybersecurity company said it also [discovered](https://www.linkedin.com/posts/yesterday-watchtowr-rapidly-reacted-to-share-7499107361605722112-b2gE) multiple patch bypasses and an additional authentication bypass vulnerability, adding one of the patch bypasses has been remediated in the second emergency patch. That said, new patch bypasses affecting the latest, fully patched version have been identified.

Huntress said it has observed limited exploitation on two customer environments, with the attackers executing Base64-encoded commands on the targeted server as part of post-exploitation activity to determine user account and operating system using a chained command "whoami & ver."

Also deployed as part of the attack is a Java .class file that's operating system agnostic and can run commands under either Linux or Windows systems to fingerprint the machine and obtain a directory listing of files stored on the computer. The data is written to a file named "Udydn.out" in a "/data/content/" path relative to the program's installation directory.

Once this step is complete, the .class file deletes "Udydn.out," the server's "server.log" file, and a "/data/internal/derby.log" file.

In another incident recorded on August 27, 2026, the threat actors are said to have used a different version of the .class file that runs a tweaked version of the command to also capture the list of running processes: "whoami & ver & tasklist"

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Organizations that have PaperCut NG and MF in their environment are advised to remove public exposure immediately and apply the patch as soon as possible. It's also recommended to restrict PaperCut Application Server web access to trusted IP addresses or place it behind a VPN or another controlled administrative path.

"PaperCut is a prime target for attackers of every motivation, as not only is it an internet-facing pivot into a corporate environment, but it is a sensitive information treasure trove i...