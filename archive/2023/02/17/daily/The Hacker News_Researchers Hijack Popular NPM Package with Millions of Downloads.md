---
title: Researchers Hijack Popular NPM Package with Millions of Downloads
url: https://thehackernews.com/2023/02/researchers-hijack-popular-npm-package.html
source: The Hacker News
date: 2023-02-17
fetch_date: 2025-10-04T07:17:04.926881
---

# Researchers Hijack Popular NPM Package with Millions of Downloads

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

# [Researchers Hijack Popular NPM Package with Millions of Downloads](https://thehackernews.com/2023/02/researchers-hijack-popular-npm-package.html)

**Feb 16, 2023**Ravie LakshmananSupply Chain / Software Security

[![NPM Package](data:image/png;base64... "NPM Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrpUTdAxuYym2X7U9P7i51yplVFxB2x35Ng1TFBZV0fuwcqE2DoUoktBTnyzNZKV7gAGXNWy4mccjamKqeAQVzsyqwt13M1POW2bPDkkUo4y99QtMuqIzvzzXveWbplcT-Lbkoq0ZHij5qxqAAEQgqIhxSbXvSWBmhlfONa4VbVL068gZrFIYsAV4w/s790-rw-e365/npm.png)

A popular npm package with more than 3.5 million weekly downloads has been found vulnerable to an account takeover attack.

"The package can be taken over by recovering an expired domain name for one of its maintainers and resetting the password," software supply chain security company Illustria [said](https://blog.illustria.io/illustria-discovers-account-takeover-vulnerability-in-a-popular-package-affecting-1000-8aaaf61ebfc4) in a report.

While npm's security protections limit users to have only one active email address per account, the Israeli firm said it was able to reset the GitHub password using the recovered domain.

The attack, in a nutshell, grants a threat actor access to the package's associated GitHub account, effectively making it possible to publish trojanized versions to the npm registry that can be weaponized to conduct supply chain attacks at scale.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This is achieved by taking advantage of a GitHub Action that's configured in the repository to automatically publish the packages when new code changes are pushed.

"Even though the maintainer's npm user account is properly configured with [two-factor authentication], this automation token bypasses it," Bogdan Kortnov, co-founder and CTO of Illustria, said.

[![NPM Package](data:image/png;base64... "NPM Package")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2MmWqxPG_Y4a-N8YiwNPu6ydQOJ7ExaC7s61eWd45SCGoqCP3xjHg_trXersXIUZ_5zghPdHhyYv5Knlf2sqPMVIa3uJfcmSO-QW9KJ_jWYyPh_8v2sE0mw8CgJHRxZI5ZE3B4BfyZOXFWvXm7w3gObNAPaHpcsKEzbj1XLMjH5ncRswENv6l4TyL/s790-rw-e365/gi.png)

Illustria did not disclose the name of the module, but noted that it reached out to its maintainer, who has since taken steps to secure the account.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is not the first time [developer](https://thehackernews.com/2021/10/popular-npm-package-hijacked-to-publish.html) [accounts](https://thehackernews.com/2021/11/two-npm-packages-with-22-million-weekly.html) have been found vulnerable to takeovers in recent years. In May 2022, a threat actor [registered](https://thehackernews.com/2022/05/pypi-package-ctx-and-php-library-phpass.html) an expired domain used by the maintainer associated with the ctx Python package to seize control of the account and distribute a malicious version.

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

[npm package](https://thehackernews.com/search/label/npm%20package)[programming](https://thehackernews.com/search/label/programming)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco AS...