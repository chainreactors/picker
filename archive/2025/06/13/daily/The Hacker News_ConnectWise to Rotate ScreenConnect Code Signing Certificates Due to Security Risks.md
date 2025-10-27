---
title: ConnectWise to Rotate ScreenConnect Code Signing Certificates Due to Security Risks
url: https://thehackernews.com/2025/06/connectwise-to-rotate-screenconnect.html
source: The Hacker News
date: 2025-06-13
fetch_date: 2025-10-06T23:00:46.861767
---

# ConnectWise to Rotate ScreenConnect Code Signing Certificates Due to Security Risks

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

# [ConnectWise to Rotate ScreenConnect Code Signing Certificates Due to Security Risks](https://thehackernews.com/2025/06/connectwise-to-rotate-screenconnect.html)

**Jun 12, 2025**Ravie LakshmananVulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhk3QlNkn7Bo38IBom9kTvZbDB12pWc7ctUsv_TA4eum35uBmoNqWf1-5FppHbzHDVPHB810PTiXId_rQluAJuunrpnof4Du5up7rcDH8rErag4I2Gq5ZgPR9Xxe-bd_yQmKL6-0gZou43I5c3yIQGJ3H3fv1CmivoXdBMojx4HL9XaVxDUHiiYs_u5cq2C/s790-rw-e365/code-signing.jpg)

ConnectWise has disclosed that it's planning to rotate the digital code signing certificates used to sign ScreenConnect, ConnectWise Automate, and ConnectWise remote monitoring and management (RMM) executables due to security concerns.

The company [said](https://www.connectwise.com/company/trust/advisories) it's doing so "due to concerns raised by a third-party researcher about how ScreenConnect handled certain configuration data in earlier versions."

While the company did not publicly elaborate on the nature of the problem, it has shed more light in a non-public FAQ accessible only to its customers (and later [shared on Reddit](https://www.reddit.com/r/sysadmin/comments/1l6qsao/connectwise_rotating_signing_certs_due_to/)) -

*The concern stems from ScreenConnect using the ability to store configuration data in an available area of the installer that is not signed but is part of the installer. We are using this ability to pass down configuration information for the connection (between the agent and server) such as the URL where the agent should call back without invalidating the signature. The unsigned area is used by our software and others for customization, however, when coupled with the capabilities of a remote control solution, it could create an insecure design pattern by today's security standards.*

Besides issuing new certificates, the company said it's releasing an update that's designed to improve how the aforementioned configuration data is managed in ScreenConnect.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The revocation of digital certificates is expected to take place by June 13 at 8 p.m. ET (June 14, 12 a.m. UTC). ConnectWise has emphasized that the issue does not involve a compromise of its systems or certificates.

It's worth noting that automatically ConnectWise is already in the process of updating certificates and agents across all its cloud instances of Automate and RMM.

However, those using on-premise versions of ScreenConnect or Automate are required to update to the latest build and validate that all agents are updated before the cutoff date to avoid any possible service disruptions.

"We had already planned enhancements to certificate management and product hardening, but these efforts are now being implemented on an accelerated timeline," ConnectWise said. "We understand this may create challenges and are committed to supporting you through the transition."

The development comes merely days after the company [disclosed](https://thehackernews.com/2025/05/connectwise-hit-by-cyberattack-nation.html) that a suspected nation-state threat actor breached its systems and affected a small number of its customers by exploiting CVE-2025-3935 to conduct ViewState code injection attacks.

It also comes as attackers are increasingly relying on legitimate RMM software like ScreenConnect and others to [obtain stealthy, persistent remote access](https://lumu.io/blog/connectwise-screenconnect-malware/), effectively allowing them to blend in with normal activity and fly under the radar.

This attack methodology, called living-off-the-land (LotL), makes it possible to hijack the software's inherent capabilities for remote access, file transfer, and command execution.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[code signing](https://thehackernews.com/search/label/code%20signing)[ConnectWise](https://thehackernews.com/search/label/ConnectWise)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[digital Certificate](https://thehackernews.com/search/label/digital%20Certificate)[endpoint security](https://thehackernews.com/search/label/endpoint%20security)[Incident response](https://thehackernews.com/search/label/Incident%20response)[ScreenConnect](https://thehackernews.com/search/label/ScreenConnect)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defens...