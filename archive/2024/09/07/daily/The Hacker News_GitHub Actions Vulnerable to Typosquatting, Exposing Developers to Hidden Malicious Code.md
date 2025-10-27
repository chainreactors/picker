---
title: GitHub Actions Vulnerable to Typosquatting, Exposing Developers to Hidden Malicious Code
url: https://thehackernews.com/2024/09/github-actions-vulnerable-to.html
source: The Hacker News
date: 2024-09-07
fetch_date: 2025-10-06T18:31:45.075537
---

# GitHub Actions Vulnerable to Typosquatting, Exposing Developers to Hidden Malicious Code

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

# [GitHub Actions Vulnerable to Typosquatting, Exposing Developers to Hidden Malicious Code](https://thehackernews.com/2024/09/github-actions-vulnerable-to.html)

**Sep 06, 2024**Ravie LakshmananSoftware Security / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6ouqKcDvZSytTquetMMAV8KwtIzuMmRC7FzZZbe3eFjobkEPNOJkrLZyIOL_p8Cvljb1dSlf9QtwnDU5sruAJNAStOu1dFI9D07wjJJGiDGJXc0-8KK5l_sGE6OKQJK_iGA5jx5k7oAOShKXmfTLRRPLqwq4-iqu_18WGN6mNR1yrpk1jOGL9RbR7XSep/s790-rw-e365/Code.jpg)

Threat actors have long leveraged typosquatting as a means to trick unsuspecting users into visiting malicious websites or downloading booby-trapped software and packages.

These attacks typically involve registering domains or packages with names slightly altered from their legitimate counterparts (e.g., goog1e.com vs. google.com).

Adversaries targeting open-source repositories across platforms have relied on developers making typing errors to initiate [software supply chain attacks](https://thehackernews.com/2024/09/hackers-hijack-22000-removed-pypi.html) through PyPI, npm, Maven Central, NuGet, RubyGems, and Crate.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The latest findings from cloud security firm Orca show that even [GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions), a continuous integration and continuous delivery ([CI/CD](https://thehackernews.com/2024/01/tensorflow-cicd-flaw-exposed-supply.html)) platform, is not immune from the threat.

"If developers make a typo in their GitHub action that matches a typosquatter's action, applications could be made to run malicious code without the developer even realizing," security researcher Ofir Yakobi [said](https://orca.security/resources/blog/typosquatting-in-github-actions/) in a report shared with The Hacker News.

The attack is possible because anyone can publish a GitHub Action by creating a GitHub account with a temporary email account. Given that actions run within the context of a user's repository, a malicious action could be exploited to tamper with the source code, steal secrets, and use it to deliver malware.

All that the technique involves is for the attacker to create organizations and repositories with names that closely resemble popular or widely-used GitHub Actions.

If a user makes inadvertent spelling errors when setting up a GitHub action for their project and that misspelled version has already been created by the adversary, then the user's workflow will run the malicious action as opposed to the intended one.

"Imagine an action that exfiltrates sensitive information or modifies code to introduce subtle bugs or backdoors, potentially affecting all future builds and deployments," Yakobi said.

"In fact, a compromised action can even leverage your GitHub credentials to push malicious changes to other repositories within your organization, amplifying the damage across multiple projects."

Orca said that a search on GitHub revealed as many as 198 files that invoke "action/checkout" or "actons/checkout" instead of "[actions/checkout](https://github.com/actions/checkout)" (note the missing "s" and "i"), putting all those projects at risk.

This form of typosquatting is appealing to threat actors because it's a low-cost, high-impact attack that could result in powerful software supply chain compromises, affecting several downstream customers all at once.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users are advised to double-check actions and their names to ensure they are referencing the correct GitHub organization, stick to actions from trusted sources, and periodically scan their CI/CD workflows for typosquatting issues.

"This experiment highlights how easy it is for attackers to exploit typosquatting in GitHub Actions and the importance of vigilance and best practices in preventing such attacks," Yakobi said.

"The actual problem is even more concerning because here we are only highlighting what happens in public repositories. The impact on private repositories, where the same typos could be leading to serious security breaches, remains unknown."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[GitHub Actions](https://thehackernews.com/search/label/GitHub%20Actions)[Malware](https://thehackernews.com/search/label/Malware)[Open-Source](https://thehackernews.com/search/label/Open-Source)[software development](https://thehackernews.com/search/label/software%20development)[Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)[typosquatting](https://thehackernews.com/search/label/typosquatting)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-ke...