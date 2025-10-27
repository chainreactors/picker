---
title: GitHub Repojacking Bug Could've Allowed Attackers to Takeover Other Users' Repositories
url: https://thehackernews.com/2022/10/github-repojacking-bug-couldve-allowed.html
source: The Hacker News
date: 2022-11-01
fetch_date: 2025-10-03T21:29:41.363471
---

# GitHub Repojacking Bug Could've Allowed Attackers to Takeover Other Users' Repositories

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

# [GitHub Repojacking Bug Could've Allowed Attackers to Takeover Other Users' Repositories](https://thehackernews.com/2022/10/github-repojacking-bug-couldve-allowed.html)

**Oct 31, 2022**Ravie Lakshmanan

[![GitHub Repojacking Bug](data:image/png;base64... "GitHub Repojacking Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinn2Ya09b7c3AnMG82sfcWuBTRY7LW5gvFHKyrNQDA_UZyr-8iO3BvODR7i-AI1ygxZe9eU0FFb2ekIipvzAdFF2Be4lCH2Dru6kq_1tjPTf2p6hpTS816MD0acweWIWb6P4yDDp6NvEm9A-Zbh_9OujYb3SxI7gu7ZR_cY_fo883gSg3Pq5c3aPfy/s790-rw-e365/github.jpg)

Cloud-based repository hosting service GitHub has addressed a high-severity security flaw that could have been exploited to create malicious repositories and mount supply chain attacks.

The **RepoJacking** technique, [disclosed](https://checkmarx.com/blog/attacking-the-software-supply-chain-with-a-simple-rename/) by Checkmarx, entails a bypass of a protection mechanism called [popular repository namespace retirement](https://github.blog/2018-04-18-new-tools-for-open-source-maintainers/#popular-repository-namespace-retirement), which aims to prevent developers from pulling unsafe repositories with the same name.

The issue was addressed by the Microsoft-owned subsidiary on September 19, 2022 following responsible disclosure.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

RepoJacking [occurs](https://thehackernews.com/2022/05/pypi-package-ctx-and-php-library-phpass.html) when a creator of a repository opts to change the username, potentially enabling a threat actor to claim the old username and publish a rogue repository with the same name in an attempt to trick users into downloading them.

[![GitHub Repojacking Bug](data:image/png;base64... "GitHub Repojacking Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaMUY3mglP4kw49cOwdWmsxbstRbeZb-sG9W3xL_vrw-_JKz9iQh-5VhZ7V5mZNGAovI1IQhco8gAv-7lzRKV6I-4F2nEAoA0IUAjMaSw_3NlAe1dHXnGe2UFXW_yoc7E2NCzt2ADdQByLbBCdNgFyyr5bsBQq1tmNO4ttEhfnRkFR6XavGkBjZUvJ/s790-rw-e365/github.jpg)

While Microsoft's countermeasure "retire[s] the namespace of any open source project that had more than 100 clones in the week leading up to the owner's account being renamed or deleted," Checkmarx found that this can be circumvented through the "[repository transfer](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository)" feature.

The way this works is as follows -

* A threat actor creates a repository with the same name as the retired repository (say, "repo") owned by a user named "victim" but under a different username (say, "helper")
* "helper" transfers ownership of "repo" to a second account with username "attacker"
* "attacker" renames the account's username to "victim"
* The namespace "victim/repo" is now under the adversary's control

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In other words, the attack hinges on the quirk that GitHub only considers as retired the namespace, i.e., the combination of username and repository name, permitting a bad actor to reuse the repository name in conjunction with an arbitrary username.

[![GitHub Repojacking Bug](data:image/png;base64... "GitHub Repojacking Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMA1oe87rpU9KqFf6ECSaUApgd9b7mBWtNyoZbbLU2unzRye5NBj4R-nr_7LMIY0ksFlzxnTd51BbIOkLoU1hLNGUpegEspFHtkheOOmLnky9EAEOoMXiOUS217ZsQnMtmM9X558bJTujXSUInzMXHk5TIjG8eTBT1jLNuMJadvMpWOppln9A1mI1Z/s790-rw-e365/patch.jpg)

A successful [exploitation](https://github.com/checkmarx/chainjacking) could have effectively allowed attackers to push poisoned repositories, putting renamed usernames at risk of being a victim of supply chain attacks.

"If not explicitly tended, all renamed usernames on GitHub were vulnerable to this flaw, including over 10,000 packages on the Go, Swift, and Packagist package managers," Checkmarx researcher Aviad Gershon said.

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

[Checkmarx](https://thehackernews.com/search/label/Checkmarx)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[GitHub](https://thehackernews.com/search/label/GitHub)[Malware](https://thehackernews.com/search/label/Malware)[Software Code](https://thehackernews.com/search/label/Software%20Code)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://...