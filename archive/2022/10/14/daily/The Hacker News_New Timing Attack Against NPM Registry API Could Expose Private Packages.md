---
title: New Timing Attack Against NPM Registry API Could Expose Private Packages
url: https://thehackernews.com/2022/10/new-timing-attack-against-npm-registry.html
source: The Hacker News
date: 2022-10-14
fetch_date: 2025-10-03T19:53:18.972105
---

# New Timing Attack Against NPM Registry API Could Expose Private Packages

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

# [New Timing Attack Against NPM Registry API Could Expose Private Packages](https://thehackernews.com/2022/10/new-timing-attack-against-npm-registry.html)

**Oct 13, 2022**Ravie Lakshmanan

[![Private NPM Packages](data:image/png;base64... "Private NPM Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRbRwj5640GFnhBdC7HwA7MdKVf985l49-Ru5KkihVPBaD3wangueCf76HZwu_8bNOJ02cgF3ORhvB4zFzPhdQHT14vS8RE6xCWAj69CPqGbgETs2A-ZpEhpl0rv66fnvsZyRATbc6GovVO1_j5ik89ZHEc6Ga3QdN8sjtnTQ-QNh_epBCi3-zDMFi/s790-rw-e365/npm.jpg)

A novel timing attack discovered against the npm's registry API can be exploited to potentially disclose private packages used by organizations, putting developers at risk of supply chain threats.

"By creating a list of possible package names, threat actors can detect organizations' [scoped private packages](https://docs.npmjs.com/about-scopes) and then masquerade public packages, tricking employees and users into downloading them," Aqua Security researcher Yakir Kadkoda [said](https://blog.aquasec.com/private-packages-disclosed-via-timing-attack-on-npm).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Scoped Confusion attack banks on analyzing the time it takes for the [npm API](https://docs.npmjs.com/cli/v8/using-npm/registry) (registry.npmjs[.]org) to return an HTTP 404 error message when querying for a private package, and measuring it against the response time for a non-existing module.

[![Private NPM Packages](data:image/png;base64... "Private NPM Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2VTamefvEl1uje1aW2aYkM7OhtvBb7zNDupFjwz8EANmbHOJKHDf42NvABjiU9ufbrZNLnwlCiCKKNv_L_XsC6tqLQWCEF8mfjtfh8Wrh1sfE47N5x93mTUj45jO31Tq5NHb9PyAbd6INjrt_ezqd6aN4eMOmIIesSzbH03VReBq20veRSWQzv99S/s790-rw-e365/ms.jpg)

"It takes on average less time to get a reply for a private package that does not exist compared to a private package that does," Kadkoda explained.

The idea, ultimately, is to identify packages internally used by companies, which could then be used by threat actors to create public versions of the same packages in an attempt to poison the software supply chain.

[![Private NPM Packages](data:image/png;base64... "Private NPM Packages")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOg233I2A6RQLbGfCVotRqnQCkBt4HC3N8ule2UkAskkGH_ywgQeKtX6OyFUFS4TB9XeRQpzzLsm_MYZLsRwZWxVVJJrNOgq1Se4uhjAEJ4jm2cCfUNxxR_7M1WHsBPpr-x8nGSz_I5RUGQfBZaDYtZVW-9VL68GBMxJnA5-p_U02q57SBAev9O-oy/s790-rw-e365/npm.jpg)

The latest findings are also different from [dependency confusion attacks](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html) in that it requires the adversary to first guess the private packages used by an organization and then publish phony packages with the same name under the public scope.

Dependency confusion (aka [namespace confusion](https://checkmarx.com/blog/new-technique-used-by-attackers-in-npm-to-avoid-detection/)), in contrast, relies on the fact that package managers check public code registries for a package before private registries, resulting in the retrieval of a malicious higher version package from the public repository.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Aqua Security said it disclosed the bug to GitHub on March 8, 2022, prompting the Microsoft-owned subsidiary to issue a response that the timing attack will not be fixed due to architectural limitations.

As preventive measures, it's recommended that organizations routinely scan npm and other package management platforms for lookalike or spoofed packages that masquerade as the internal counterparts.

"If you don't find public packages similar to your internal packages, consider creating public packages as placeholders to prevent such attacks," Kadkoda said.

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

[npm repository](https://thehackernews.com/search/label/npm%20repository)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)...