---
title: Critical Security Flaw Reported in Passwordstate Enterprise Password Manager
url: https://thehackernews.com/2022/12/critical-security-flaw-reported-in.html
source: The Hacker News
date: 2022-12-23
fetch_date: 2025-10-04T02:23:37.614771
---

# Critical Security Flaw Reported in Passwordstate Enterprise Password Manager

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

# [Critical Security Flaw Reported in Passwordstate Enterprise Password Manager](https://thehackernews.com/2022/12/critical-security-flaw-reported-in.html)

**Dec 22, 2022**Ravie LakshmananPassword Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgaCPSyzY1sDKD4a7YhOzTAgtYpKNWPslbv5UVX9ifToFSw6NPnkzcrmeIxV6p7oBgq8t5VrQ3NCGrRLgf5f3i1cAtzhkzd2_FsikfJSuyjjXl_H4yYSokSGVgBG-0anRNF7noeYvaTXopcxriyrle5Hc2iDIh87tPQ0HKgwz80loYsR3rmzTDtJp3ow/s790-rw-e365/password.png)

Multiple high-severity vulnerabilities have been disclosed in **Passwordstate** password management solution that could be exploited by an unauthenticated remote adversary to obtain a user's plaintext passwords.

"Successful exploitation allows an unauthenticated attacker to exfiltrate passwords from an instance, overwrite all stored passwords within the database, or elevate their privileges within the application," Swiss cybersecurity firm modzero AG [said](https://www.modzero.com/modlog/archives/2022/12/19/better_make_sure_your_password_manager_is_secure/index.html) in a report published this week.

"Some of the individual vulnerabilities can be chained to gain a shell on the Passwordstate host system and dump all stored passwords in cleartext, starting with nothing more than a valid username."

Passwordstate, developed by an Australian company named Click Studios, has over [29,000 customers](https://www.clickstudios.com.au/our-customers.aspx) and is used by more than 370,000 IT professionals.

One of the flaws also impacts [Passwordstate version 9.5.8.4](https://chrome.google.com/webstore/detail/passwordstate/appojfilknpkghkebigcdkmopdfcjhim) for the Chrome web browser. The latest version of the browser add-on is 9.6.1.2, which was released on September 7, 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of vulnerabilities identified by modzero AG is below -

* [CVE-2022-3875](https://nvd.nist.gov/vuln/detail/CVE-2022-3875) (CVSS score: 9.1) - An authentication bypass for Passwordstate's API
* [CVE-2022-3876](https://nvd.nist.gov/vuln/detail/CVE-2022-3876) (CVSS score: 6.5) - A bypass of access controls through user-controlled keys
* [CVE-2022-3877](https://nvd.nist.gov/vuln/detail/CVE-2022-3877) (CVSS score: 5.7) - A stored cross-site scripting ([XSS](https://www.imperva.com/learn/application-security/cross-site-scripting-xss-attacks/)) vulnerability in the URL field of every password entry
* No CVE (CVSS score: 6.0) - An insufficient mechanism for securing passwords by using server-side symmetric encryption
* No CVE (CVSS score: 5.3) - Use of hard-coded credentials to list audited events such as password requests and user account changes through the API
* No CVE (CVSS score: 4.3) - Use of insufficiently protected credentials for Password Lists

Exploiting the vulnerabilities could permit an attacker with knowledge of a valid username to extract saved passwords in cleartext, overwrite the passwords in the database, and even elevate privileges to achieve remote code execution.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkwrTWpLamcU7AdQTyEZ5r7Wz7GLpy1NMwN3lrF-VNmh9agx-DH2bnBe_7m5T94yxiUEqRg1lv41iqrhhKE82DWBWKO-f0z_6mrSiHAkme8XsSAw2GglM45Z4cwW9NN6UZqG9YJU3qAswK48V52GmjDQw-068hHWP5sKm1sEpPEZ2NpRU7BZcopEEq/s790-rw-e365/shell.gif)

What's more, an improper authorization flow (CVSS score: 3.7) identified in the Chrome browser extension could be weaponized to send all passwords to an actor-controlled domain.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

In an attack chain demonstrated by modzero AG, a threat actor could forge an API token for an administrator account and exploit the XSS flaw to add a malicious password entry to obtain a reverse shell and grab the passwords hosted in the instance.

Users are recommended to update to [Passwordstate 9.6 - Build 9653](https://www.clickstudios.com.au/passwordstate-changelog.aspx) released on November 7, 2022, or later versions to mitigate the potential threats.

Passwordstate, in April 2021, fell victim to a [supply chain attack](https://thehackernews.com/2021/04/passwordstate-warns-of-ongoing-phishing.html) that allowed the attackers to leverage the service's update mechanism to drop a backdoor on customer's machines.

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

[Password Management](https://thehackernews.com/search/label/Password%20Management)[password manager](https://thehackernews.com/search/label/password%20manager)[password security](https://thehackernews.com/search/label/password%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Imperson...