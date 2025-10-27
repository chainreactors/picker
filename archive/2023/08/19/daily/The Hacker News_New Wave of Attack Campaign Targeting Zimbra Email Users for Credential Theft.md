---
title: New Wave of Attack Campaign Targeting Zimbra Email Users for Credential Theft
url: https://thehackernews.com/2023/08/new-wave-of-attack-campaign-targeting.html
source: The Hacker News
date: 2023-08-19
fetch_date: 2025-10-04T12:02:50.465316
---

# New Wave of Attack Campaign Targeting Zimbra Email Users for Credential Theft

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

# [New Wave of Attack Campaign Targeting Zimbra Email Users for Credential Theft](https://thehackernews.com/2023/08/new-wave-of-attack-campaign-targeting.html)

**Aug 18, 2023**Ravie LakshmananEmail Seucrity / Cyber Attack

[![Zimbra Email](data:image/png;base64... "Zimbra Email")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEja-l7cdRHiixu4jpKXBSEansVPWAlUHA4F73XQjErlFeiFeLk2OnCaMs4D7B_z_7h-yX70yEfLf7EYeRMEDlPuBWwH-ljKQrZir_6JM_6rt57G_ixjwFdu5HWNEFVH3fhC3tbt1iw4s3qFjh-iUWvFdUrtdRf26W31FTR_Yav9CRX5Wye1Whl7Jjz0N24V/s790-rw-e365/zimbra.jpg)

A new "mass-spreading" social engineering campaign is targeting users of the Zimbra Collaboration email server with an aim to collect their login credentials for use in follow-on operations.

The activity, active since April 2023 and still ongoing, targets a wide range of small and medium businesses and governmental entities, most of which are located in Poland, Ecuador, Mexico, Italy, and Russia. It has not been attributed to any known threat actor or group.

"Initially, the target receives an email with a phishing page in the attached HTML file," ESET researcher Viktor Šperka [said](https://www.welivesecurity.com/en/eset-research/mass-spreading-campaign-targeting-zimbra-users/) in a report. "The email warns the target about an email server update, account deactivation, or similar issue and directs the user to click on the attached file."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The messages also spoof the from address to appear as if they are coming from a Zimbra administrator in a likely attempt to convince the recipients into opening the attachment.

The HTML file contains a Zimbra login page tailored to the targeted organization, with the Username field prefilled with the victim's email address to make it seem more authentic. Once the credentials are entered, they are collected from the HTML form and sent via a HTTPS POST request to an actor-controlled server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuNThrJg9sw7LfUNxQvtBunCA6xhY-ndpbdMuXHdRGSCRRP6tBJs3B7Nwv-B3YTACUwolnBQnieIzxk9slxMtRZlPnDjUsPMqUswNt5F_JJ3Og2gDWpCzxI5C5rgUUXMPQ9kwyLfz5TUVgh7BwnXmO3d2JzsLhkBFqwVMtGkh7bvO-dw4pueg8zcBVc8-1/s790-rw-e365/map.jpg)

What makes the attacks stand out is their ability to propagate further. Subsequent phishing waves have leveraged accounts of previously targeted, legitimate companies, suggesting that the infiltrated administrator accounts associated with those victims were used to send emails to other entities of interest.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"One explanation is that the adversary relies on password reuse by the administrator targeted through phishing – i.e., using the same credentials for both email and administration," Šperka noted.

While the campaign is not technically sophisticated, it banks on the fact that "HTML attachments contain legitimate code, and the only telltale element is a link pointing to the malicious host" that's embedded in the source code.

"This way, it is much easier to circumvent reputation-based anti-spam policies, compared to phishing techniques where a malicious link is directly placed in the email body," Šperka said.

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

[social engineering](https://thehackernews.com/search/label/social%20engineering)[Zimbra](https://thehackernews.com/search/label/Zimbra)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;...