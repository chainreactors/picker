---
title: Critical NVIDIA Container Toolkit Flaw Allows Privilege Escalation on AI Cloud Services
url: https://thehackernews.com/2025/07/critical-nvidia-container-toolkit-flaw.html
source: The Hacker News
date: 2025-07-19
fetch_date: 2025-10-06T23:54:52.087214
---

# Critical NVIDIA Container Toolkit Flaw Allows Privilege Escalation on AI Cloud Services

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

# [Critical NVIDIA Container Toolkit Flaw Allows Privilege Escalation on AI Cloud Services](https://thehackernews.com/2025/07/critical-nvidia-container-toolkit-flaw.html)

**Jul 18, 2025**Ravie LakshmananCloud Security / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjK8uZXk5mrlVgL6bnl6z8OLacjraSmvu8texICW3V97vW7jSLhT3g-aMsytpUbGJjUrHbFfGZXOsCODtMiJWP0XpGAAtUxgIjRA_zlC3MIV0szla6yuvyEYXrCe5qpzG25GIrgU2kOPrGH9mcP75JiAJvMNprDz2Fm3jDixp2PJYtAX6z_Suf3BOmovne/s790-rw-e365/wiz.jpg)

Cybersecurity researchers have disclosed a critical container escape vulnerability in the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) that could pose a severe threat to managed AI cloud services.

The vulnerability, tracked as CVE-2025-23266, carries a CVSS score of 9.0 out of 10.0. It has been codenamed **NVIDIAScape** by Google-owned cloud security company Wiz.

"NVIDIA Container Toolkit for all platforms contains a vulnerability in some hooks used to initialize the container, where an attacker could execute arbitrary code with elevated permissions," NVIDIA [said](https://nvidia.custhelp.com/app/answers/detail/a_id/5659) in an advisory for the bug.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"A successful exploit of this vulnerability might lead to escalation of privileges, data tampering, information disclosure, and denial-of-service."

The shortcoming impacts all versions of NVIDIA Container Toolkit up to and including 1.17.7 and NVIDIA GPU Operator up to and including 25.3.0. It has been addressed by the GPU maker in versions 1.17.8 and 25.3.1, respectively.

The NVIDIA Container Toolkit refers to a collection of libraries and utilities that enable users to build and run GPU-accelerated Docker containers. The NVIDIA GPU Operator is designed to deploy these containers automatically on GPU nodes in a Kubernetes cluster.

Wiz, which shared details of the flaw in a Thursday analysis, said the shortcoming affects 37% of cloud environments, allowing an attacker to potentially access, steal, or manipulate the sensitive data and proprietary models of all other customers running on the same shared hardware by means of a three-line exploit.

The vulnerability stems from a misconfiguration in how the toolkit handles the Open Container Initiative (OCI) hook "createContainer." A successful exploit for CVE-2025-23266 can result in a complete takeover of the server. Wiz also characterized the flaw as "incredibly" easy to weaponize.

"By setting LD\_PRELOAD in their Dockerfile, an attacker could instruct the nvidia-ctk hook to load a malicious library," Wiz researchers Nir Ohfeld and Shir Tamari [added](https://www.wiz.io/blog/nvidia-ai-vulnerability-cve-2025-23266-nvidiascape).

"Making matters worse, the createContainer hook executes with its working directory set to the container's root filesystem. This means the malicious library can be loaded directly from the container image with a simple path, completing the exploit chain."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

All of this can be achieved with a "stunningly simple three-line Dockerfile" that loads the attacker's shared object file into a privileged process, resulting in a container escape.

The disclosure comes a couple of months after Wiz [detailed](https://thehackernews.com/2025/02/researchers-find-new-exploit-bypassing.html) a bypass for another vulnerability in NVIDIA Container Toolkit (CVE-2024-0132, CVSS score: 9.0 and CVE-2025-23359, CVSS score: 8.3) that could have been abused to achieve complete host takeover.

"While the hype around AI security risks tends to focus on futuristic, AI-based attacks, 'old-school' infrastructure vulnerabilities in the ever-growing AI tech stack remain the immediate threat that security teams should prioritize," Wiz said.

"Additionally, this research highlights, not for the first time, that containers are not a strong security barrier and should not be relied upon as the sole means of isolation. When designing applications, especially for multi-tenant environments, one should always 'assume a vulnerability' and implement at least one strong isolation barrier, such as virtualization."

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

[AI Security](https://thehackernews.com/search/label/AI%20Security)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Container Security](https://thehackernews.com/search/label/Container%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Data Tampering](https://thehackernews.com/search/label/Data%20Tampering)[Docker](https://thehackernews.com/search/label/Docker)[Kubernetes](https://thehackernews.com/search/label/Kubernetes)[nvidia](https://thehackernews.com/search/label/nvidia)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data...