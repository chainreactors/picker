---
title: CISA's KEV Catalog Updated with 3 New Flaws Threatening IT Management Systems
url: https://thehackernews.com/2023/03/cisas-kev-catalog-updated-with-3-new.html
source: The Hacker News
date: 2023-03-09
fetch_date: 2025-10-04T09:03:38.319860
---

# CISA's KEV Catalog Updated with 3 New Flaws Threatening IT Management Systems

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

# [CISA's KEV Catalog Updated with 3 New Flaws Threatening IT Management Systems](https://thehackernews.com/2023/03/cisas-kev-catalog-updated-with-3-new.html)

**Mar 08, 2023**Ravie LakshmananVulnerability / Cybersecurity

[![IT Management Systems](data:image/png;base64... "IT Management Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7TpLK_R8uH3evBua6oPgzKIQ6rW7QXX47gT3VV5ROBDJ3685UjbPmBCfLCRsP6HWSsfbMGpkwukNJTtJOrEF0rvanahw6BtVbXKegX6jspuyoXf4kV1QI2BoPtKzJVvxw7lnswI9tD7TqHchchU-Fm7TbzIadJhG1lTwNthctSvxcauVqI5wKJj-X/s790-rw-e365/cyber.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has [added](https://www.cisa.gov/news-events/alerts/2023/03/07/cisa-adds-three-known-exploited-vulnerabilities-catalog) three security flaws to its Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, citing evidence of active exploitation.

The list of vulnerabilities is below -

* [CVE-2022-35914](https://nvd.nist.gov/vuln/detail/CVE-2022-35914) (CVSS score: 9.8) - Teclib GLPI Remote Code Execution Vulnerability
* [CVE-2022-33891](https://nvd.nist.gov/vuln/detail/cve-2022-33891) (CVSS score: 8.8) - Apache Spark Command Injection Vulnerability
* [CVE-2022-28810](https://nvd.nist.gov/vuln/detail/CVE-2022-28810) (CVSS score: 6.8) - Zoho ManageEngine ADSelfService Plus Remote Code Execution Vulnerability

The most critical of the three is [CVE-2022-35914](https://glpi-project.org/security-update-10-0-3-and-9-5-9/), which concerns a remote code execution vulnerability in the third-party library htmlawed present in [Teclib GLPI](https://github.com/glpi-project/glpi), an open source asset and IT management software package.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The exact specifics surrounding the nature of attacks are unknown, but the Shadowserver Foundation in October 2022 [noted](https://twitter.com/Shadowserver/status/1580475994590220288) that it has seen exploitation attempts against its honeypots.

Since then, a cURL-based one-line proof of concept (PoC) has been made available on GitHub and a "mass" scanner has been advertised for sale, VulnCheck security researcher Jacob Baines [said](https://vulncheck.com/blog/glpi-exploitation) in December 2022.

Furthermore, data gathered by GreyNoise has [revealed](https://viz.greynoise.io/query/?gnql=raw_data.web.paths%3A%22htmlawed%2Fhtmlawed%2FhtmLawedTest.php%22%20classification%3Amalicious) 40 malicious IP addresses from the U.S., the Netherlands, Hong Kong, Australia, and Bulgaria, attempting to abuse the shortcoming.

The second flaw is an unauthenticated command injection vulnerability in Apache Spark that has been exploited by the [Zerobot botnet](https://thehackernews.com/2022/12/zerobot-botnet-emerges-as-growing.html) to co-opt susceptible devices with the goal of carrying out distributed denial-of-service (DDoS) attacks.

Lastly, also added to the KEV catalog is a [remote code execution flaw](https://www.manageengine.com/products/self-service-password/advisory/CVE-2022-28810.html) in Zoho ManageEngine ADSelfService Plus that was patched in April 2022.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Multiple Zoho ManageEngine ADSelfService Plus contains an unspecified vulnerability allowing for remote code execution when performing a password change or reset," CISA said.

Cybersecurity company Rapid7, which [discovered](https://www.rapid7.com/blog/post/2022/04/14/cve-2022-28810-manageengine-adselfservice-plus-authenticated-command-execution-fixed/) the bug, said it detected active exploitation attempts by threat actors to "execute arbitrary OS commands in order to gain persistence on the underlying system and attempt to pivot further into the environment."

The development comes as API security firm Wallarm [said](https://lab.wallarm.com/vmware-nsx-manager-vulnerabilities-being-actively-exploited-in-the-wild/) it has found ongoing exploit attempts of two VMware NSX Manager flaws ([CVE-2021-39144](https://nvd.nist.gov/vuln/detail/cve-2021-39144) and [CVE-2022-31678](https://nvd.nist.gov/vuln/detail/CVE-2022-31678)) since December 2022 that could be leveraged to execute malicious code and siphon sensitive data.

## **Update: CISA Adds CVE-2021-39144 to KEV Catalog**

CISA on March 10, 2023, [added](https://www.cisa.gov/news-events/alerts/2023/03/10/cisa-adds-two-known-exploited-vulnerabilities-catalog) CVE-2021-39144 to its catalog of security flaws exploited in the wild, alongside [CVE-2020-5741](https://thehackernews.com/2023/03/lastpass-hack-engineers-failure-to.html), a remote code execution bug impacting Plex Media Server that was exploited in the LastPass breach.

Virtualization services provider VMware has also revised its [October 2022 advisory](https://www.vmware.com/security/advisories/VMSA-2022-0027.html) to confirm reports of active exploitation of CVE-2021-39144.

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

[CISA](https://thehackernews.com/search/label/CISA)[IT Management](https://thehackernews.com/search/label/IT%20Management)[KEV Catalog](https://thehackernews.com/search/label/KEV...