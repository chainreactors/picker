---
title: Researchers Uncover Over a Dozen Security Flaws in Akuvox E11 Smart Intercom
url: https://thehackernews.com/2023/03/researchers-uncover-over-dozen-security.html
source: The Hacker News
date: 2023-03-14
fetch_date: 2025-10-04T09:32:14.137071
---

# Researchers Uncover Over a Dozen Security Flaws in Akuvox E11 Smart Intercom

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

# [Researchers Uncover Over a Dozen Security Flaws in Akuvox E11 Smart Intercom](https://thehackernews.com/2023/03/researchers-uncover-over-dozen-security.html)

**Mar 13, 2023**Ravie LakshmananEnterprise Security / Privacy

[![Akuvox E11 Smart Intercom](data:image/png;base64... "Akuvox E11 Smart Intercom")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIebhaN2ERGc2MIbXo9fcgLZ2UtH-7B0-LQmagEMIgqb8rEyaUD3a50-big8yVVZv2kz9azN7yjBCp990MW6UkOs0M2upg_b3p5DnmS3tLiiier7aa6CWLatlVP8J1UgiSEIBDqp7GhtPOP68pFOgcZueHYLe-yR1L_7f2hATXNx-YzVgZGfVt6EvN/s790-rw-e365/app.png)

More than a dozen security flaws have been disclosed in E11, a smart intercom product made by Chinese company **Akuvox**.

"The vulnerabilities could allow attackers to execute code remotely in order to activate and control the device's camera and microphone, steal video and images, or gain a network foothold," Claroty security researcher Vera Mens [said](https://claroty.com/team82/research/the-silent-spy-among-us-modern-attacks-against-smart-intercoms) in a technical write-up.

Akuvox E11 is described by the company on its website as a "[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol) [Session Initiation Protocol] video doorphone specially designed for villas, houses, and apartments."

The [product listing](https://www.akuvox.com/ProductsDisp.aspx?pid=32), however, has been taken down from the website, displaying an error message: "Page does not exist." A [snapshot](https://webcache.googleusercontent.com/search?q=cache%3Ahttps%3A%2F%2Fwww.akuvox.com%2FProductsDisp.aspx%3Fpid%3D32&ie=UTF-8) captured by Google shows that the page was live as recently as March 12, 2023, 05:59:51 GMT.

The attacks can manifest either through remote code execution within the local area network (LAN) or remote activation of the E11's camera and microphone, allowing the adversary to collect and exfiltrate multimedia recordings.

A third attack vector takes advantage of an external, insecure file transfer protocol (FTP) server to download stored images and data.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The most severe of the issues are as follows -

* [**CVE-2023-0344**](https://claroty.com/team82/disclosure-dashboard/cve-2023-0344) (CVSS score: 9.1) - Akuvox E11 appears to be using a custom version of dropbear SSH server. This server allows an insecure option that by default is not in the official dropbear SSH server.

* [**CVE-2023-0345**](https://claroty.com/team82/disclosure-dashboard/cve-2023-0345) (CVSS score: 9.8) - The Akuvox E11 secure shell (SSH) server is enabled by default and can be accessed by the root user. This password cannot be changed by the user.

* [**CVE-2023-0352**](https://claroty.com/team82/disclosure-dashboard/cve-2023-0352) (CVSS score: 9.1) - The Akuvox E11 password recovery webpage can be accessed without authentication, and an attacker could download the device key file. An attacker could then use this page to reset the password back to the default.

* [**CVE-2023-0354**](https://claroty.com/team82/disclosure-dashboard/cve-2023-0354) (CVSS score: 9.1) - The Akuvox E11 web server can be accessed without any user authentication, and this could allow an attacker to access sensitive information, as well as create and download packet captures with known default URLs.

A majority of the 13 security issues remain unpatched to date, with the industrial and IoT security company noting that Akuvox has since addressed the FTP server permissions issue by disabling the "the ability to list its content so malicious actors could not enumerate files anymore."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings have also prompted the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to [release](https://www.cisa.gov/news-events/alerts/2023/03/09/cisa-releases-five-industrial-control-systems-advisories) an Industrial Control Systems (ICS) advisory of its own last week.

[![Akuvox E11 Smart Intercom](data:image/png;base64... "Akuvox E11 Smart Intercom")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDMO-4kAaeqs1wH6w2AxI7WU-52yvpWUDpryfhWPFKS886nmg64hyljAtQ44EwUDdBDZUr6J6yijwobBc0Fos4YCGIlfcGjBKZZMsS3QOKhHqus2bHQf7z4RmlQhTdzxNrsgMktq6c9b2u-zko63FyzY_vVXiBexJx_jQlwhmcOTAMhJHauNZqHUwZ/s790-rw-e365/poc.png)

"Successful exploitation of these vulnerabilities could cause loss of sensitive information, unauthorized access, and grant full administrative control to an attacker," the agency [cautioned](https://www.cisa.gov/news-events/ics-advisories/icsa-23-068-01).

In the absence of patches, organizations using the doorphone are advised to disconnect it from the internet until the vulnerabilities are fixed to mitigate potential remote attacks.

It's also advised to change the default password used to secure the web interface and "segment and isolate the Akuvox device from the rest of the enterprise network" to prevent lateral movement attacks.

The development comes as Wago released patches for several of its programmable logic controllers (PLCs) to [address](https://cert.vde.com/de/advisories/VDE-2022-060/) four vulnerabilities (CVE-2022-45137, CVE-2022-45138, CVE-2022-45139, and CVE-2022-45140) two of which could be exploited to achieve full system compromise.

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
[**Share on Email](#link_sh...