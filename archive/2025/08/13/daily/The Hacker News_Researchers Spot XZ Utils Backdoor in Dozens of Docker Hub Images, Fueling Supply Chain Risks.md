---
title: Researchers Spot XZ Utils Backdoor in Dozens of Docker Hub Images, Fueling Supply Chain Risks
url: https://thehackernews.com/2025/08/researchers-spot-xz-utils-backdoor-in.html
source: The Hacker News
date: 2025-08-13
fetch_date: 2025-10-07T00:53:14.295773
---

# Researchers Spot XZ Utils Backdoor in Dozens of Docker Hub Images, Fueling Supply Chain Risks

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

# [Researchers Spot XZ Utils Backdoor in Dozens of Docker Hub Images, Fueling Supply Chain Risks](https://thehackernews.com/2025/08/researchers-spot-xz-utils-backdoor-in.html)

**Aug 12, 2025**Ravie LakshmananMalware / Container Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlx4HJDVqoAicklUmY5-7Ddt7tGPfhyvC7NwtRS2qwQuxm-lNNZ4F1ZEVIZZqoVeJXAMb5YPIhG8fFZ0_Nyi8NZy740DlsrFdoT-zjX_oR_CjP05ZOmVoEgBSPEhX3yn7b2OZVin65Br3PpBtYxdFdY44ZyXd9HW7i99VAN0wbBxylQlXmslOzjUQwY671/s790-rw-e365/docker-malware.jpg)

New research has uncovered Docker images on Docker Hub that contain the infamous XZ Utils backdoor, more than a year after the discovery of the incident.

More troubling is the fact that other images have been built on top of these infected base images, effectively propagating the infection further in a transitive manner, Binarly REsearch [said](https://www.binarly.io/blog/persistent-risk-xz-utils-backdoor-still-lurking-in-docker-images) in a report shared with The Hacker News.

The firmware security company said it discovered a total of 35 images that ship with the backdoor. The incident once again highlights the risks faced by the software supply chain.

Binarly's Alex Matrosov told the publication that the investigation was prompted after it detected malicious code in one of their customer's environments, ultimately finding that the images had been pulled from Docker Hub.

The XZ Utils supply chain event (CVE-2024-3094, CVSS score: 10.0) [came to light](https://thehackernews.com/2024/03/urgent-secret-backdoor-found-in-xz.html) in late March 2024, when Andres Freund sounded the alarm on a backdoor embedded within XZ Utils versions 5.6.0 and 5.6.1.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Further [analysis](https://thehackernews.com/2024/04/malicious-code-in-xz-utils-for-linux.html) of the malicious code and the broader compromise led to [several startling discoveries](https://thehackernews.com/2024/04/popular-rust-crate-liblzma-sys.html), the first and foremost being that the backdoor could lead to unauthorized remote access and enable the execution of arbitrary payloads through SSH.

Specifically, the backdoor – placed in the liblzma.so library and used by the OpenSSH server – was designed such that it triggered when a client interacts with the infected SSH server.

By hijacking the RSA\_public\_decrypt function using the glibc's IFUNC mechanism, the malicious code allowed an attacker possessing a specific private key to bypass authentication and execute root commands remotely," Binarly explained.

The second finding was that the changes were pushed by a developer named "Jia Tan" (JiaT75), who spent almost two years contributing to the open-source project to build trust until they were given maintainer responsibilities, signaling the meticulous nature of the attack.

"This is clearly a very complex state-sponsored operation with impressive sophistication and multi-year planning," Binarly noted at the time. "Such a complex and professionally designed comprehensive implantation framework is not developed for a one-shot operation."

The latest research from the company shows that the impact of the incident continues to send aftershocks through the open-source ecosystem even after all these months.

This includes the discovery of 12 Debian Docker images that contain [one of the XZ Utils backdoor](https://www.virustotal.com/gui/file/319feb5a9cddd81955d915b5632b4a5f8f9080281fb46e2f6d69d53f693c23ae), and another set of second-order images that include the compromised Debian images.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Binarly said it [reported](https://github.com/debuerreotype/docker-debian-artifacts/issues/246) the base images to the Debian maintainers, who said they have "made an intentional choice to leave these artifacts available as a historical curiosity, especially given the following extremely unlikely (in containers/container image use cases) factors required for exploitation."

However, the company pointed out that leaving publicly available Docker images that contain a potential network-reachable backdoor carries a significant security risk, despite the criteria required for successful exploitation – the need for network access to the infected device with the SSH service running.

"The xz-utils backdoor incident demonstrates that even short-lived malicious code can remain unnoticed in official container images for a long time, and that can propagate in the Docker ecosystem," it added.

"The delay underscores how these artifacts may silently persist and propagate through CI pipelines and container ecosystems, reinforcing the critical need for continuous binary-level monitoring beyond simple version tracking."

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

[Container Security](https://thehackernews.com/search/label/Container%20Security)[Debian](https://thehackernews.com/search/label/Debian)[Docker Hub](https://thehackernews.com/search/label/Docker%20Hub)[Malware](https://thehackernews.com/search/label/Malware)[Software Supply Chain Attack](https://thehackernews.com/sear...