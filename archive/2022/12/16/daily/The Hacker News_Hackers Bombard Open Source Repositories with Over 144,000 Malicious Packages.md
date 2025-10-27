---
title: Hackers Bombard Open Source Repositories with Over 144,000 Malicious Packages
url: https://thehackernews.com/2022/12/hackers-bombard-open-source.html
source: The Hacker News
date: 2022-12-16
fetch_date: 2025-10-04T01:42:21.326747
---

# Hackers Bombard Open Source Repositories with Over 144,000 Malicious Packages

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

# [Hackers Bombard Open Source Repositories with Over 144,000 Malicious Packages](https://thehackernews.com/2022/12/hackers-bombard-open-source.html)

**Dec 15, 2022**Ravie Lakshmanan

[![Open Source Repositories](data:image/png;base64... "Open Source Repositories")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCvGBTr0eJQ9vY2EZAQk_q0EIZHgyE6bkZorns1gkL1pD4NCmFsd3Dd6UxwZ2IViF6jLfKC5-GNpPD3w6NH2QlgjwddYo3npNsoLiAFjd9-CdrSYfGRcwn0Q0NqYb7fSeNRubN_ipFr03Z1iCf_Y5-CzG_XnMMCK05RxSpsAMR5FhR2NJDV-1qA5R0/s790-rw-e365/hack.png)

NuGet, PyPi, and npm ecosystems are the target of a new campaign that has resulted in over 144,000 packages being published by unknown threat actors.

"The packages were part of a new attack vector, with attackers spamming the open source ecosystem with packages containing links to phishing campaigns," researchers from Checkmarx and Illustria [said](https://checkmarx.com/blog/how-140k-nuget-npm-and-pypi-packages-were-used-to-spread-phishing-links/) in a report published Wednesday.

Of the [144,294 phishing-related packages](https://gist.github.com/jossef/1c1152368ff6210340644f44afec7e8e) that were detected, 136,258 were published on NuGet, 7,824 on PyPi, and 212 on npm. The offending libraries have since been unlisted or taken down.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Further analysis has revealed that the whole process was automated and that the packages were pushed over a short span of time, with a majority of the usernames following the convention "<a-z><1900-2022>."

The fake packages themselves claimed to provide hacks, cheats, and free resources in an attempt to trick users into downloading them. The URLs to the rogue phishing pages were embedded in the package description.

[![Open Source Repositories](data:image/png;base64... "Open Source Repositories")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4xGygoFnSXkT_A_VRpVLMUuJolwOXw1zUOMLnXFtTY09PBN-_UPlAcwaZRYes9JDA78iqGJfh1yaV4HybISe0FoqvqRdGgJo9Drgua6Pu5Ew8vUbp7XkEBdqSr9D7Mo5IZpW0rR8MFu1nqH4X5vz5wV6caKWpiMlsRRqZbVKGTXOP6Xp_X_JTTJaF/s790-rw-e365/hack.png)

In all, the massive campaign encompassed more than [65,000 unique URLs](https://gist.github.com/jossef/77c4fd00fccf68b56d76a36c79799ca1) on 90 domains.

"The threat actors behind this campaign likely wanted to improve the search engine optimization (SEO) of their phishing sites by linking them to legitimate websites like NuGet," the researchers said. "This highlights the need to be cautious when downloading packages and only to use trusted sources."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

These deceptive and well-designed pages advertised Discord Nitro codes, game hacks, "free money" for Cash App accounts, gift cards, and increased followers on social media platforms like YouTube, TikTok, and Instagram.

The sites, as is typically the case, don't offer the promised rewards, instead prompting users to enter their email addresses and complete surveys, before redirecting them to legitimate e-commerce sites via an affiliate link to generate illicit referral revenues.

The poisoning of NuGet, PyPi, and npm with fabricated packages once again illustrates the evolving methods threat actors use to attack the software supply chain.

"Automating the process also allowed the attackers to create a large number of user accounts, making it difficult to trace the source of the attack," the researchers said. "This shows the sophistication and determination of these attackers, who were willing to invest significant resources in order to carry out this campaign."

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

[NPM Malware](https://thehackernews.com/search/label/NPM%20Malware)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[PyPI](https://thehackernews.com/search/label/PyPI)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN ...