---
title: 3 New Vulnerabilities Affect OT Products from German Companies Festo and CODESYS
url: https://thehackernews.com/2022/11/3-new-vulnerabilities-affect-ot.html
source: The Hacker News
date: 2022-12-01
fetch_date: 2025-10-04T00:13:58.957803
---

# 3 New Vulnerabilities Affect OT Products from German Companies Festo and CODESYS

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

# [3 New Vulnerabilities Affect OT Products from German Companies Festo and CODESYS](https://thehackernews.com/2022/11/3-new-vulnerabilities-affect-ot.html)

**Nov 30, 2022**Ravie Lakshmanan

[![Festo and CODESYS Companies](data:image/png;base64... "Festo and CODESYS Companies")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_yzJ-jfiqsUBkgbyDZrxejyeyXrWeR_yMzmWEhCfdr3PeQTFZbMQPO-Ak1Q_RCaJxyl6ep06_Xwrdat7x2-IAmPX93acPRzeg-xkRpnrxNWBwz9xGPLOlR4l9O7yToJdVL3iNbAMaC082mbYSEJquptpYp-3aBffy7QuorblM1FlVRV0NzB2gq9Qz/s790-rw-e365/ot.png)

Researchers have disclosed details of three new security vulnerabilities affecting operational technology (OT) products from CODESYS and Festo that could lead to source code tampering and denial-of-service (DoS).

The vulnerabilities, reported by Forescout Vedere Labs, are the latest in a long list of flaws collectively tracked under the name [OT:ICEFALL](https://thehackernews.com/2022/06/researchers-disclose-56-vulnerabilities.html).

"These issues exemplify either an insecure-by-design approach — which was usual at the time the products were launched – where manufacturers include dangerous functions that can be accessed with no authentication or a subpar implementation of security controls, such as cryptography," the researchers [said](https://www.forescout.com/blog/oticefall-continues-vedere-labs-discloses-three-new-vulnerabilities-affecting-ot-products-how-to-mitigate/).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most critical of the flaws is [CVE-2022-3270](https://nvd.nist.gov/vuln/detail/CVE-2022-3270) (CVSS score: 9.8), a critical vulnerability that affects Festo automation controllers using the Festo Generic Multicast (FGMC) protocol to reboot the devices without requiring any authentication and cause a denial of service (DoS) condition.

Another DoS shortcoming in Festo controllers ([CVE-2022-3079](https://nvd.nist.gov/vuln/detail/CVE-2022-3079), CVSS score: 7.5) relates to a case of unauthenticated, remote access to an undocumented web page ("cec-reboot.php") that could be exploited by an attacker with network access to Festo CPX-CEC-C1 and CPX-CMXX PLCs.

[![OT vulnerabilities](data:image/png;base64... "OT vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHYFP6yuttIsUY_EoDiS0yk10kds6QOV2ESnJNdfoNSK-9KmrQ52I8rruGeq7cO9LeqT0oof8jnCz6fz9y0eoaBoDNA-8HBwq1Bu-FVwEtDn6hnN6qGYGK0x69AyvBdn_9n8w3_pjEpoVOyFuPa44nfOPEIK3lEqqk6EsBSo_VXUIr7D7RZhGvVsAM/s790-rw-e365/flaws.png)

The third issue, on the other hand, concerns the use of weak cryptography in the CODESYS V3 runtime environment to secure download code and boot applications ([CVE-2022-4048](https://nvd.nist.gov/vuln/detail/CVE-2022-4048), CVSS score: 7.7), which could be abused by a bad actor to decrypt and manipulate the source code, thereby undermining confidentiality and integrity protections.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Forescout said it also identified two known CODESYS bugs impacting Festo CPX-CEC-C1 controllers ([CVE-2022-31806](https://nvd.nist.gov/vuln/detail/CVE-2022-31806) and [CVE-2022-22515](https://nvd.nist.gov/vuln/detail/CVE-2022-22515)) that stem from an unsafe configuration in the Control runtime environment, and could lead to a denial-of-service sans authentication.

"This is yet another example of a supply chain issue where a vulnerability has not been disclosed for all the products it affects," the researchers said.

To mitigate potential threats, organizations are recommended to discover and inventory vulnerable devices, enforce appropriate network segmentation controls, and monitor network traffic for anomalous activity.

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

[Internet of Things](https://thehackernews.com/search/label/Internet%20of%20Things)[Operational Technology](https://thehackernews.com/search/label/Operational%20Technology)[SCADA vulnerabilities](https://thehackernews.com/search/label/SCADA%20vulnerabilities)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehack...