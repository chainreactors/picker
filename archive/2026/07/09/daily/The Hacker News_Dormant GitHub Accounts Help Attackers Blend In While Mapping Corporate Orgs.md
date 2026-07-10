---
title: Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs
url: https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:12.795499
---

# Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Dormant GitHub Accounts Help Attackers Blend In While Mapping Corporate Orgs](https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html)

**Ravie Lakshmanan**Jul 09, 2026Developer Security / Supply Chain Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDslymdYqhkFwIm3ZeaXVZweYVT_R1d6LCQhIm799y9-5hQ3C45cumIStxGYheFbwosbd_JtrB6FgOthR2KJgfe8PYs0k47eGV7263ATac5UR0t7OOaqOUGOf5DHAR4b0IaKTozk0UEiHJz5-nze3b1ureycPGqdPVlqrImWreOWwMpGxC8kgBvONCLGbH/s1700-e365/github-ghost.jpg)

Datadog Security Labs is warning of "several overlapping campaigns" that are systematically enumerating corporate GitHub organizations, repositories, and user accounts through the GitHub API.

"Operators rely on automated scraping tooling with custom or legitimate-sounding user agents, leveraging GitHub 'ghost' accounts that are often years old, or compromised OAuth tokens and personal access tokens (PATs) from legitimate users," Julie Agnes Sparks, senior security engineer at Datadog, [said](https://securitylabs.datadoghq.com/articles/coordinated-github-api-enumeration/).

While the activity in most cases involves targeting public data, select instances have gone beyond public information enumeration to successfully clone private repositories.

The campaign employs a mix of automated scanner tools, over 50 dormant accounts, and dozens of legitimate accounts that have had their personal access tokens (PATs) exposed unintentionally or compromised through some other method to facilitate the enumeration.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

What's notable about the "ghost" accounts is that they were created two to five years ago and intentionally left inactive for extended periods of time before weaponizing them to issue API traffic across multiple organizations. This technique is strategic as it aims to avoid raising any red flags and pass off the activity as legitimate, as opposed to creating new accounts and immediately using them for scraping.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-p7tS8EgDedWZ3DHn6JMzEdkr0NzmVNTTWmFRqTvu_1bZdqgH4r_UKic2ka8FSE65yrGbRgqSqGECX7l2_5t9vqYvl2MF8O2_pQfPDXfyZ9GN3uUnWsSilR7Q5ECPxyVmnVdN9hBIiNyGy672WDfEvtNrTnuQpz8UB0AzbeFqmWVtKHTidP6EWYvjOaGa/s1700-e365/scrape.jpg)

Because a large chunk of GitHub's API surface is reachable without authentication, the enumeration queries return the necessary data, while blending into normal API usage. Some of them include -

* Listing an organization's public repositories
* Walking a user's followers and following lists
* Enumerating gists, starred repos, and org memberships, and
* Running GraphQL queries against public objects

This information can be used by a threat actor to conduct reconnaissance and programmatically map out an organization's GitHub-related activity, such as its public repositories, its members, who those members follow, and which projects they modify.

Data access has been confirmed in a few scenarios, with the attackers taking steps to clone a private repository belonging to a single organization.

"Individually, most of these requests are unremarkable. They hit public endpoints, authenticate cleanly or not at all, and return successful responses," Datadog said. "The concern lies in the aggregate: a group of accounts moving in sync across companies' GitHub organizations with versioned custom tooling iterating over weeks, and in the worst case, actors that stopped enumerating and started cloning."

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [Developer Security](https://thehackernews.com/search/label/Developer%20Security), [GitHub](https://thehackernews.com/search/label/GitHub), [Reconnaissance](https://thehackernews.com/search/label/Reconnaissance), [Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

⚡ Top Stories This Week

[![ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](data:image/svg+xml;base64... "ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories")

ThreatsDay: AI Compute Hijacking, Apple Email Flaw, BlueHammer Ransomware + 14 Stories](https://thehackernews.com/2026/07/threatsday-ai-compute-hijacking-apple.html)

[![Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](data:image/svg+xml;base64... "Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability")

Chrome Ad Blocker with 10M+ Installs Found with Dormant Script Injection Capability](ht...