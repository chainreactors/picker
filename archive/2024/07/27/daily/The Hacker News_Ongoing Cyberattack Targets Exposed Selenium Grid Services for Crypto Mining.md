---
title: Ongoing Cyberattack Targets Exposed Selenium Grid Services for Crypto Mining
url: https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html
source: The Hacker News
date: 2024-07-27
fetch_date: 2025-10-06T17:46:33.010061
---

# Ongoing Cyberattack Targets Exposed Selenium Grid Services for Crypto Mining

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

# [Ongoing Cyberattack Targets Exposed Selenium Grid Services for Crypto Mining](https://thehackernews.com/2024/07/ongoing-cyberattack-targets-exposed.html)

**Jul 26, 2024**Ravie Lakshmanan

[![Selenium Grid Services](data:image/png;base64... "Selenium Grid Services")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2i7C43DMM8mOa0N-NjcBn5Qm-gRmGw6z119CapcJv50YKTZCOQQTn5TmZ54Vc7pTeMNnxsQEX42FeZ3NYPp6DmMEJszVR5OA-8juH8GnasK-guCL6ePQej3GvrtH9q5I1Oizi-m5JffLwK1SzZXpCRxIzgdz2t5dSrZGAmR4pZGqPlDnJ3lYFNqnL0tVi/s790-rw-e365/wiz.png)

Cybersecurity researchers are sounding the alarm over an ongoing campaign that's leveraging internet-exposed [Selenium Grid services](https://www.selenium.dev/documentation/grid/) for illicit cryptocurrency mining.

Cloud security firm Wiz is tracking the activity under the name **SeleniumGreed**. The campaign, which is targeting older versions of Selenium (3.141.59 and prior), is believed to be underway [since at least April 2023](https://www.reddit.com/r/selfhosted/comments/12drr31/remote_server_compromised/).

"Unbeknownst to most users, Selenium WebDriver API enables full interaction with the machine itself, including reading and downloading files, and running remote commands," Wiz researchers Avigayil Mechtinger, Gili Tikochinski, and Dor Laska [said](https://www.wiz.io/blog/seleniumgreed-cryptomining-exploit-attack-flow-remediation-steps).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"By default, authentication is not enabled for this service. This means that many publicly accessible instances are misconfigured and can be accessed by anyone and abused for malicious purposes."

Selenium Grid, part of the Selenium automated testing framework, enables parallel execution of tests across multiple workloads, different browsers, and various browser versions.

[![Selenium Grid Services](data:image/png;base64... "Selenium Grid Services")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqih8ayDXUE-FnQc37y2Jmhns9Ej8thYPs5yv2pyZBUkS2ryNEzVKAJzqV0K7VxsCwVqrSswB4XHw6_zvUwret9dWwHvm0vOUqDJZoPW87xoAzwIY0IwO8vGwLlrgEHqy2PmBTyAmAjnymHHIoPmjfrmCUpS5gSKul5MrhQgHN4VDdGhUCsmSRlEAABd4h/s790-rw-e365/code.png)

"Selenium Grid must be protected from external access using appropriate firewall permissions," the project maintainers [warn](https://www.selenium.dev/documentation/grid/getting_started/#warning) in a support documentation, stating that failing to do so could allow third-parties to run arbitrary binaries and access internal web applications and files.

Exactly who is behind the attack campaign is currently not known. However, it involves the threat actor targeting publicly exposed instances of Selenium Grid and making use of the WebDriver API to run Python code responsible for downloading and running an XMRig miner.

It starts with the adversary sending a request to the vulnerable Selenium Grid hub with an aim to execute a Python program containing a Base64-encoded payload that spawns a reverse shell to an attacker-controlled server ("164.90.149[.]104") in order to fetch the final payload, a modified version of the open-source XMRig miner.

"Instead of hardcoding the pool IP in the miner configuration, they dynamically generate it at runtime," the researchers explained. "They also set XMRig's TLS-fingerprint feature within the added code (and within the configuration), ensuring the miner will only communicate with servers controlled by the threat actor."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The IP address in question is said to belong to a legitimate service that has been compromised by the threat actor, as it has also been found to host a publicly exposed Selenium Grid instance.

Wiz said it's possible to execute remote commands on newer versions of Selenium and that it identified more than 30,000 instances exposed to remote command execution, making it imperative that users take steps to close the misconfiguration.

"Selenium Grid is not designed to be exposed to the internet and its default configuration has no authentication enabled, so any user that has network access to the hub can interact with the nodes via API," the researchers said.

"This poses a significant security risk if the service is deployed on a machine with a public IP that has inadequate firewall policy."

### Update

Selenium, in an advisory released on July 31, 2024, urged users to upgrade their instances to the latest version to mitigate against the threat.

"Selenium Grid by default doesn't have any authentication as the assumption has always been that we want you to put this behind a secure network to prevent people from abusing your resources," it [said](https://www.selenium.dev/blog/2024/protecting-unsecured-selenium-grid/). "Another way to combat this is to use a cloud provider to run your Selenium Grid."

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

[Automated Testing](https://thehackernews.com/search/label/Automated%20Testing)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[crypto mining](https://thehackernews.com/search/label/crypto%20mining)[Cyber Threat](https://thehackernews.com/...