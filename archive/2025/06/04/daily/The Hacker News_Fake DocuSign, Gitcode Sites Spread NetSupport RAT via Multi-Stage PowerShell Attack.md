---
title: Fake DocuSign, Gitcode Sites Spread NetSupport RAT via Multi-Stage PowerShell Attack
url: https://thehackernews.com/2025/06/fake-docusign-gitcode-sites-spread.html
source: The Hacker News
date: 2025-06-04
fetch_date: 2025-10-06T22:56:39.964911
---

# Fake DocuSign, Gitcode Sites Spread NetSupport RAT via Multi-Stage PowerShell Attack

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

# [Fake Docusign, Gitcode Sites Spread NetSupport RAT via Multi-Stage PowerShell Attack](https://thehackernews.com/2025/06/fake-docusign-gitcode-sites-spread.html)

**Jun 03, 2025**Ravie LakshmananUnited States

[![Multi-Stage PowerShell Attack](data:image/png;base64... "Multi-Stage PowerShell Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLNENpdsB0Pqp0I5iQ4s5zrozDrgByxfk-yDFOxmin2fclguJsn69wAWQONtUhmISdg7jRUl3qbe1GUexK4oCgYLswA9D29DPhnGNRf5JTeusPsnG0qoguazIjK2YpfLROoDyYpbR8DEKvaRBqIN8O9joqY3zC_yTJz4q2ZGW7mZW4fW-kheuCGsQrKizo/s790-rw-e365/power.jpg)

Threat hunters are alerting to a new campaign that employs deceptive websites to trick unsuspecting users into executing malicious PowerShell scripts on their machines and infect them with the [NetSupport RAT](https://thehackernews.com/2025/02/threat-actors-exploit-clickfix-to.html) malware.

The DomainTools Investigations (DTI) team said it identified "malicious multi-stage downloader Powershell scripts" hosted on lure websites that masquerade as Gitcode and Docusign.

"These sites attempt to deceive users into copying and running an initial PowerShell script on their Windows Run command," the company [said](https://dti.domaintools.com/how-threat-actors-exploit-human-trust/) in a technical report shared with The Hacker News.

"Upon doing so, the powershell script downloads another downloader script and executes on the system, which in turn retrieves additional payloads and executes them eventually installing NetSupport RAT on the infected machines."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It's believed that these counterfeit sites may be propagated via social engineering attempts over email and/or social media platforms.

The PowerShell scripts present hosted on the fake Gitcode sites are designed to download a series of intermediate PowerShell scripts from an external server ("tradingviewtool[.]com") that are used in succession to launch NetSupport RAT on victim machines.

DomainTools said it also identified several websites spoofing Docusign (e.g., docusign.sa[.]com) to deliver the same remote access trojan but with a twist: Using [ClickFix](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html)-style CAPTCHA verifications to dupe victims into running the malicious PowerShell script.

Like the recently [documented](https://thehackernews.com/2025/05/eddiestealer-malware-uses-clickfix.html) attack chains delivering the EDDIESTEALER infostealer, users who land on the pages are asked to prove they are not a robot by completing the check.

[![Multi-Stage PowerShell Attack](data:image/png;base64... "Multi-Stage PowerShell Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSlR2z11Z-fpMmu6kDYBRskDdYWHJ68HhjcbfH11ccb-BT3MfKXFs040acvhc7XVRcMBYtAz0JxaD7DQvtt7m2szCH6i9JOlbxYp5J_5dwJw082inucufbj__cAEUfbYHrIh_29SXzee6YABmIvSqQ1eZ6OaSmAIRr0vFitAbPD0o0JfmWd67dW1rKU7Kk/s790-rw-e365/robot.jpg)

Triggering the CAPTCHA verification causes an obfuscated PowerShell command to be clandestinely copied to the user's clipboard -- a technique called clipboard poisoning -- after which they are instructed to launch the Windows Run dialog ("Win + R"), paste ("CTRL + V"), and press Enter, causing the script to be executed in the process.

The PowerShell script works by downloading a persistence script ("wbdims.exe") from GitHub to ensure that the payload is launched automatically when the user logs in to the system.

"While this payload was no longer available during the time of investigation, the expectation is that it checks in with the delivery site via 'docusign.sa[.]com/verification/c.php,'" DomainTools said. "Upon doing so, it triggers a refresh in the browser for the page to display the content of 'docusign.sa[.]com/verification/s.php?an=1.'"

This results in the delivery of a second-stage PowerShell script, which then downloads and executes a third-stage ZIP payload from the same server by setting the URL parameter "an" to "2." The script proceeds to unpack the archive and run an executable named "jp2launcher.exe" present within it, ultimately leading to the deployment of NetSupport RAT.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The multiple stages of scripts downloading and running scripts that download and run yet more scripts is likely an attempt to evade detection and be more resilient to security investigations and takedowns," the company said.

It's currently not clear who is behind the campaign, but DomainTools pointed out that it identified similar delivery URL, domain naming, and registration patterns in connection with a [SocGholish](https://www.domaintools.com/resources/blog/a-website-attacked/) (aka FakeUpdates) campaign detected in October 2024.

"Notably, the techniques involved are commonplace and NetSupport Manager is a legitimate administration tool known to be leveraged as a RAT by multiple threat groups such as [FIN7](https://thehackernews.com/2025/04/fin7-deploys-anubis-backdoor-to-hijack.html), [Scarlet Goldfinch](https://redcanary.com/blog/threat-intelligence/scarlet-goldfinch/), [Storm-0408](https://thehackernews.com/2025/03/microsoft-warns-of-malvertising.html), and others."

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
[![Facebook Messenger](...