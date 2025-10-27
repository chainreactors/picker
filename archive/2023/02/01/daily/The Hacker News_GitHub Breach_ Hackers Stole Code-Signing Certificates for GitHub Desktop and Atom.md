---
title: GitHub Breach: Hackers Stole Code-Signing Certificates for GitHub Desktop and Atom
url: https://thehackernews.com/2023/01/github-breach-hackers-stole-code.html
source: The Hacker News
date: 2023-02-01
fetch_date: 2025-10-04T05:26:09.242096
---

# GitHub Breach: Hackers Stole Code-Signing Certificates for GitHub Desktop and Atom

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

# [GitHub Breach: Hackers Stole Code-Signing Certificates for GitHub Desktop and Atom](https://thehackernews.com/2023/01/github-breach-hackers-stole-code.html)

**Jan 31, 2023**Ravie LakshmananSecurity Incident / Encryption

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-cw_mRjni2aCB0SFStY1lK4OZair3ReHeI2QzLXPADxFi-MUk_rBLOYI9pHenIBVVvsjEnOs72mQxHVBPIhgzJWSWmLAXSS2Jdw1SOaZVAX50Iubm7uNcvJoBfOn887paOmgsb0FhtoOS1OWAWjeeKWVU3-IK5a8E_SOPCuk_BBO2W-0McjfUlOkW/s790-rw-e365/github.png)

GitHub on Monday disclosed that unknown threat actors managed to exfiltrate encrypted code signing certificates pertaining to some versions of GitHub Desktop for Mac and Atom apps.

As a result, the company is [taking the step](https://github.blog/2023-01-30-action-needed-for-github-desktop-and-atom-users/) of revoking the exposed certificates out of abundance of caution. The following versions of GitHub Desktop for Mac have been invalidated: 3.0.2, 3.0.3, 3.0.4, 3.0.5, 3.0.6, 3.0.7, 3.0.8, 3.1.0, 3.1.1, and 3.1.2.

Versions 1.63.0 and 1.63.1 of Atom are also expected to stop working as of February 2, 2023, requiring that users downgrade to a [previous version](https://github.com/atom/atom/releases/tag/v1.60.0) (1.60.0) of the source code editor. Atom was officially [discontinued](https://github.blog/2022-06-08-sunsetting-atom/) in December 2022. GitHub Desktop for Windows is not affected.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Microsoft-owned subsidiary said it detected unauthorized access to a set of repositories, including those from deprecated GitHub-owned organizations, used in the planning and development of GitHub Desktop and Atom on December 7, 2022.

The repositories are said to have been cloned a day before by a compromised personal access token ([PAT](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)) associated with a machine account. None of the repositories contained customer data, and the compromised credentials have since been revoked. GitHub did not disclose how the token was breached.

"Several encrypted code signing certificates were stored in these repositories for use via Actions in our GitHub Desktop and Atom release workflows," GitHub's Alexis Wales said. "We have no evidence that the threat actor was able to decrypt or use these certificates."

It's worth pointing out that a successful decryption of the certificates could permit an adversary to sign trojanized applications with these certificates and pass them off as originating from GitHub.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The three compromised certificates – two Digicert code signing certificates used for Windows and one Apple Developer ID certificate – are set for revocation on February 2, 2023.

The code hosting platform also said it released a new version of the Desktop app on January 4, 2023, that's signed with new certificates that were not exposed to the threat actor. It further emphasized that no unauthorized changes were made to the code in these repositories.

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

[Code Signing Certificate](https://thehackernews.com/search/label/Code%20Signing%20Certificate)[encryption](https://thehackernews.com/search/label/encryption)[GitHub](https://thehackernews.com/search/label/GitHub)[software security](https://thehackernews.com/search/label/software%20security)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public...