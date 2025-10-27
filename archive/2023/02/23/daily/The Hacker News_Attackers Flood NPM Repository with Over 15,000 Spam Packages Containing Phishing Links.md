---
title: Attackers Flood NPM Repository with Over 15,000 Spam Packages Containing Phishing Links
url: https://thehackernews.com/2023/02/attackers-flood-npm-repository-with.html
source: The Hacker News
date: 2023-02-23
fetch_date: 2025-10-04T07:54:23.369544
---

# Attackers Flood NPM Repository with Over 15,000 Spam Packages Containing Phishing Links

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

# [Attackers Flood NPM Repository with Over 15,000 Spam Packages Containing Phishing Links](https://thehackernews.com/2023/02/attackers-flood-npm-repository-with.html)

**Feb 22, 2023**Ravie LakshmananOpen Source / Supply Chain Attack

[![NPM Repository](data:image/png;base64... "NPM Repository")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN8s0kA6lEnh4cdbPEACkiYeGRAwlRwARe7ffrpmmrMZ8CWzLm6h0GWX2AFfC_cJeAxG6E_x4QknT8Nx-FG7n6f6M1a0wMj5pG9asnc96__wYgzL6byOXWrWbg_ORUK5SOgjDOYvYIFl3S2y5XkHWplkikgmjDHe8JDDAbLuqanBXVqNOLlkf0fSxk/s790-rw-e365/npnn.png)

In what's a continuing assault on the open source ecosystem, [over 15,000 spam packages](https://gist.github.com/masteryoda101/a3f3500648f7e6da7bf89b3fb210e839) have flooded the npm repository in an attempt to distribute phishing links.

"The packages were created using automated processes, with project descriptions and auto-generated names that closely resembled one another," Checkmarx researcher Yehuda Gelb [said](https://checkmarx.com/blog/how-npm-packages-were-used-to-spread-phishing-links/) in a Tuesday report.

"The attackers referred to retail websites using referral IDs, thus profiting from the referral rewards they earned."

The modus operandi involves poisoning the registry with rogue packages that include links to phishing campaigns in their README.md files, evocative of a [similar campaign](https://thehackernews.com/2022/12/hackers-bombard-open-source.html) the software supply chain security firm exposed in December 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The fake modules masqueraded as cheats and free resources, with some packages named as "free-tiktok-followers," "free-xbox-codes," and "instagram-followers-free."

The ultimate goal of the operation is to entice users into downloading the packages and clicking on the links to the phishing sites with bogus promises of increased followers on social media platforms.

"The deceptive web pages are well-designed and, in some cases, even include fake interactive chats that appear to show users receiving the game cheats or followers they were promised," Gelb explained.

[![NPM Repository](data:image/png;base64... "NPM Repository")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha_axIMsdQhe5tuqLup_7eYq2CJHYUiXpp5W9jWNqIpBCvHggmm4CXnfFQtOXkDbLp6P4vLWNhpUk4LvGoHqoAg2RfMpPch1ufE3xlkVewla9IYN7OBFi7RYCcVop0ef1DepzIss6R3D8lGFXfV1LrNyo56to6hyV2BJzKT-GtOAmDUeT5NyiUoyIz/s790-rw-e365/npm.png)

The websites urge victims to fill out surveys, which then pave the way for additional surveys or, alternatively, redirect them to legitimate e-commerce portals like AliExpress.

The packages are said to have been uploaded to npm from multiple user accounts within hours between February 20 and 21, 2023, using a Python script that automates the whole process.

What's more, the Python script is also engineered to append links to the published npm packages on WordPress websites operated by the threat actor that claim to offer Family Island cheats.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is achieved by using the [selenium Python package](https://pypi.org/project/selenium/) to interact with the websites and make the necessary modifications.

In all, the use of automation allowed the adversary to publish a large number of packages in a short span of time, not to mention create several user accounts to conceal the scale of the attack.

"This shows the sophistication and determination of these attackers, who were willing to invest significant resources in order to carry out this campaign," Gelb said.

The findings once again demonstrate the challenges in securing the software supply chain, as threat actors continue to adapt with "new and unexpected techniques."

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-...