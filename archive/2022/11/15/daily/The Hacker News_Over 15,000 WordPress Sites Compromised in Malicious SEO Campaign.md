---
title: Over 15,000 WordPress Sites Compromised in Malicious SEO Campaign
url: https://thehackernews.com/2022/11/over-15000-wordpress-sites-compromised.html
source: The Hacker News
date: 2022-11-15
fetch_date: 2025-10-03T22:48:55.023170
---

# Over 15,000 WordPress Sites Compromised in Malicious SEO Campaign

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

# [Over 15,000 WordPress Sites Compromised in Malicious SEO Campaign](https://thehackernews.com/2022/11/over-15000-wordpress-sites-compromised.html)

**Nov 14, 2022**Ravie Lakshmanan

[![Malicious SEO Campaign](data:image/png;base64... "Malicious SEO Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBZGqnqpQKTBZldgAOdAg7coVTSO8ZrW9dTlfcZZezvPvQsm-rrvHtWIjc_uBDQaJxKYOYL36vg5oCZjBctgKsQ9x84BHjnN3CSoJOisster-H2irqfp3mT8R7MljmoeJbvCjwPoGZ_Q591twq7CYwamQ1rSG6S6SBNJd3Vr-a3cIsMTLhURx58kB-/s790-rw-e365/wordpress-code.jpg)

A new malicious campaign has compromised [over 15,000 WordPress websites](https://publicwww.com/websites/%22ois.is%22/) in an attempt to redirect visitors to bogus Q&A portals.

"These malicious redirects appear to be designed to increase the authority of the attacker's sites for search engines," Sucuri researcher Ben Martin [said](https://blog.sucuri.net/2022/11/massive-ois-is-black-hat-redirect-malware-campaign.html) in a report published last week, calling it a "clever black hat SEO trick."

The search engine poisoning technique is designed to promote a "handful of fake low quality Q&A sites" that share similar website-building templates and are operated by the same threat actor.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A notable aspect of the campaign is the ability of the hackers to modify over 100 files per website on average, an approach that contrasts dramatically from other attacks of this kind wherein only a limited number of files are tampered with to reduce footprint and escape detection.

Some of the most commonly infected pages consist of wp-signup.php, wp-cron.php, wp-links-opml.php, wp-settings.php, wp-comments-post.php, wp-mail.php, xmlrpc.php, wp-activate.php, wp-trackback.php, and wp-blog-header.php.

[![Malicious SEO Campaign](data:image/png;base64... "Malicious SEO Campaign")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjs3NGK78GLfv2vd5H3dxig7FL6ZdU67ABBozSlwwWJVWJXjzchdT8-HkPSxvq43l5exu5zf-dzaVBiI3Xd6xOSLhnCDJLCUt3pbwodVg5JK7m_leM_pUQL4Ijncbz1D9K23PGiVxiAAb5qYdo-Do6JTBJQIKCKah84FI7odwPISkE7wHzYfVug1i7R/s790-rw-e365/wordpress.jpg)

This extensive compromise allows the malware to execute the redirects to websites of the attacker's choice. It's worth pointing out that the redirects don't occur if the [wordpress\_logged\_in cookie](https://wordpress.org/support/article/cookies/) is present or if the current page is wp-login.php (i.e., the login page) so as to avoid raising suspicion.

The ultimate goal of the campaign is to "drive more traffic to their fake sites" and "boost the sites' authority using fake search result clicks to make Google rank them better so that they get more real organic search traffic."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The injected code achieves this by initiating a redirect to a PNG image hosted on a domain named "[ois[.]is](https://urlscan.io/search/#ois.is)" that, instead of loading an image, takes the website visitor to a Google search result URL of a spam Q&A domain.

It's not immediately clear how the WordPress sites are breached, and Sucuri said it did not notice any obvious plugin flaws being exploited to carry out the campaign.

That said, it's suspected to be a case of brute-forcing the WordPress administrator accounts, making it essential that users enable two-factor authentication and ensure that all software is up-to-date.

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

[Google](https://thehackernews.com/search/label/Google)[SEO poisoning](https://thehackernews.com/search/label/SEO%20poisoning)[Sucuri](https://thehackernews.com/search/label/Sucuri)[WordPress](https://thehackernews.com/search/label/WordPress)[WordPress SEO](https://thehackernews.com/search/label/WordPress%20SEO)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked P...