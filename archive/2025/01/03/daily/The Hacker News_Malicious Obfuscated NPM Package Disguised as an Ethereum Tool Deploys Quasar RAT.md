---
title: Malicious Obfuscated NPM Package Disguised as an Ethereum Tool Deploys Quasar RAT
url: https://thehackernews.com/2025/01/malicious-obfuscated-npm-package.html
source: The Hacker News
date: 2025-01-03
fetch_date: 2025-10-06T20:13:12.622162
---

# Malicious Obfuscated NPM Package Disguised as an Ethereum Tool Deploys Quasar RAT

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

# [Malicious Obfuscated NPM Package Disguised as an Ethereum Tool Deploys Quasar RAT](https://thehackernews.com/2025/01/malicious-obfuscated-npm-package.html)

**Jan 02, 2025**Ravie LakshmananOpen Source / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOAOE-hDsnbTCkykPjdOwRzhzo0X8rAAO5TMYzUzenCBAEIfmDCmogaEuYXuC5mJkemlQ0Msl68z2-JO5Zybetnp_AV8DP8Cah0bBfTKg8HEaJUjsIlbjPGD3vNjYWVPk6a6DfRhySraz9X1HNsHFTg3PTvMp6tRLgYYd3rEcfJ2fcp7C9q2g3m9YTRQqg/s790-rw-e365/npm.png)

Cybersecurity researchers have discovered a malicious package on the npm package registry that masquerades as a library for detecting vulnerabilities in Ethereum smart contracts but, in reality, drops an open-source remote access trojan called Quasar RAT onto developer systems.

The heavily obfuscated package, named [ethereumvulncontracthandler](https://www.npmjs.com/package/ethereumvulncontracthandler), was published to npm on December 18, 2024, by a user named "solidit-dev-416." As of writing, it continues to be available for download. It has been [downloaded 66 times](https://npm-stat.com/charts.html?package=ethereumvulncontracthandler) to date.

"Upon installation, it retrieves a malicious script from a remote server, executing it silently to deploy the RAT on Windows systems," Socket security researcher Kirill Boychenko [said](https://socket.dev/blog/quasar-rat-disguised-as-an-npm-package) in an analysis published last month.

The malicious code embedded into ethereumvulncontracthandler is obscured with multiple layers of obfuscation, leveraging techniques like Base64- and XOR-encoding, as well as minification to resist analysis and detection efforts.

The malware also performs checks to avoid running in sandboxed environments, prior to acting as a loader by fetching and executing a second-stage payload from a remote server ("jujuju[.]lat"). The script is designed to run PowerShell commands to initiate the execution of Quasar RAT.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The remote access trojan, for its part, establishes persistence through Windows Registry modifications and contacts a command-and-control (C2) server ("captchacdn[.]com:7000") to receive further instructions that allow it to gather and exfiltrate information.

Quasar RAT, first [publicly released](https://www.cisa.gov/news-events/analysis-reports/ar18-352a) on GitHub in July 2014, has been used for both [cybercrime](https://thehackernews.com/2023/10/quasar-rat-leverages-dll-side-loading.html) and [cyber espionage campaigns](https://thehackernews.com/2024/09/blind-eagle-targets-colombian-insurance.html) by various threat actors over the years.

"The threat actor also uses this C2 server to catalog infected machines, and manage multiple compromised hosts simultaneously if this campaign is part of a botnet infection," Boychenko said.

"At this stage, the victim's machine is fully compromised, and is under complete surveillance and control by the threat actor, ready for regular check-ins and to receive updated instructions."

### The Ballooning Problem of Fake Stars on GitHub

The disclosure comes as a new study undertaken by Socket, alongside academics from Carnegie Mellon University and North Carolina State University, has revealed a rapid surge in inauthentic "stars" that are used to artificially inflate the popularity of malware-laced GitHub repositories.

While the [phenomenon](https://thehackernews.com/2024/04/beware-githubs-fake-popularity-scam.html) has been [around for some time](https://thehackernews.com/2024/07/stargazer-goblin-creates-3000-fake.html), the research discovered that the majority of fake stars are used to promote short-lived malware repositories masquerading as pirating software, game cheats, and cryptocurrency bots.

Advertised via GitHub star merchants like Baddhi Shop, BuyGitHub, FollowDeh, R for Rank, and Twidium, the "open" black market is suspected to be behind as many 4.5 million "fake" stars from 1.32 million accounts and spanning 22,915 repositories, illustrating the scale of the problem.

[Baddhi Shop](https://dagster.io/blog/fake-stars), The Hacker News [found](https://baddhi.shop/product/buy-github-followers/), lets prospective customers buy 1,000 GitHub stars for $110. "Buy GitHub Followers, Stars, Forks, and Watchers to boost your repository's credibility and visibility," a description on the site reads. "Real engagement attracts more developers and contributors to your project!"

"Only a few repositories with fake star campaigns are published in package registries such as npm and PyPI," the researchers [said](https://arxiv.org/abs/2412.13459). "Even fewer are widely adopted. At least 60% of the accounts that participated in fake star campaigns have trivial activity patterns."

As the open-source software supply chain continues to be an attractive vector for cyber attacks, the findings reiterate that star count alone is an unreliable signal of quality or reputation of GitHub repositories and should not be used without further review.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In a statement shared with WIRED in October 2023, the Microsoft-owned code hosting platform [said](https://www.wired.com/story/github-stars-black-market-coders-cheat/) it's been aware of the problem for years and that it actively works to remove fake starrers from the service.

"The main vulnerability of star count as a metric lies in the fact that the actions of all GitHub users share equal weight in its definition," the researchers said.

"As a result, star count can be easily inflated with a high volume of bot accounts or (arguably low reputation) crowdsourced humans, as we have shown in our study. To avoid such exploitation, GitHub may consider presenting a weighted metric to signal repository popularity (e.g., based on dimensions of network centrality), which is considerably harder to fake."

Found this article interesting? Follow...