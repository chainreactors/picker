---
title: AIOS WordPress Plugin Faces Backlash for Storing User Passwords in Plain Text
url: https://thehackernews.com/2023/07/aios-wordpress-plugin-faces-backlash.html
source: The Hacker News
date: 2023-07-15
fetch_date: 2025-10-04T11:55:42.795503
---

# AIOS WordPress Plugin Faces Backlash for Storing User Passwords in Plain Text

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

# [AIOS WordPress Plugin Faces Backlash for Storing User Passwords in Plaintext](https://thehackernews.com/2023/07/aios-wordpress-plugin-faces-backlash.html)

**Jul 14, 2023**Ravie LakshmananPassword Security / WordPress

[![AIOS WordPress Plugin](data:image/png;base64... "AIOS WordPress Plugin")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ3d2uVb-IzbIxsjpnYW3I90a25AKW-qDM1GD9kMPKq5m_PEkGkvtxMpMhP7_SeVHwytMVAV7RD3xy4Io0FFGJrarJDNY8tsdOwBcZHQwa81qaSNvTJupUtzjryC7hdiCIxKrkUpUHwt_uxOgBBHPLN7_A-SQ9KUs3iqWF6pX6mMetTWy2ZLnH9swafyUg/s790-rw-e365/wordpress.jpg)

All-In-One Security (AIOS), a WordPress plugin installed on over one million sites, has issued a security update after a bug introduced in version 5.1.9 of the software caused users' passwords being added to the database in plaintext format.

"A malicious site administrator (i.e. a user already logged into the site as an admin) could then have read them," UpdraftPlus, the maintainers of AIOS, [said](https://aiosplugin.com/all-in-one-security-aios-wordpress-security-plugin-release-5-2-0/).

"This would be a problem if those site administrators were to try out those passwords on other services where your users might have used the same password. If those other services' logins are not protected by two-factor authentication, this could be a risk to the affected website."

The issue surfaced nearly three weeks ago when a user of the plugin [reported](https://wordpress.org/support/topic/cleartext-passwords-written-to-aiowps_audit_log/) the behavior, stating they were "absolutely shocked that a security plugin is making such a basic security 101 error."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

AIOS also noted that the updates remove the existing logged data from the database, but emphasized successful exploitation requires a threat actor to have already compromised a WordPress site by other means and have administrative privileges, or gained unauthorized access to unencrypted site backups.

"As such, the opportunity for someone to gain privileges that they did not already have, are small," the company said. "The patched version stops passwords from being logged, and clears all previous saved passwords."

As a precaution, it's recommended that users enable two-factor authentication on WordPress and change the passwords, particularly if the same credential combinations have been used on other sites.

The disclosure comes as Wordfence revealed a critical flaw impacting WPEverest's [User Registration](https://wordpress.org/plugins/user-registration/) plugin (CVE-2023-3342, CVSS score: 9.9) that has over 60,000 active installations. The vulnerability has been addressed in version 3.0.2.1.

"This vulnerability makes it possible for an authenticated attacker with minimal permissions, such as a subscriber, to upload arbitrary files, including PHP files, and achieve remote code execution on a vulnerable site's server," Wordfence researcher István Márton [said](https://www.wordfence.com/blog/2023/07/interesting-arbitrary-file-upload-vulnerability-patched-in-user-registration-wordpress-plugin/).

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

[password](https://thehackernews.com/search/label/password)[WordPress](https://thehackernews.com/search/label/WordPress)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://the...