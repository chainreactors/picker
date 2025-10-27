---
title: Unpatched Versa Concerto Flaws Let Attackers Escape Docker and Compromise Host
url: https://thehackernews.com/2025/05/unpatched-versa-concerto-flaws-let.html
source: The Hacker News
date: 2025-05-23
fetch_date: 2025-10-06T22:31:22.328903
---

# Unpatched Versa Concerto Flaws Let Attackers Escape Docker and Compromise Host

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

# [Critical Versa Concerto Flaws Let Attackers Escape Docker and Compromise Hosts](https://thehackernews.com/2025/05/unpatched-versa-concerto-flaws-let.html)

**May 22, 2025**Ravie LakshmananVulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh87QsFVBIFlfedDK4wVx2UBljH41DpB8LpvGy8_-FmdvCE7DfVyvzgP4RtBQdKcFtG-VyK1FeB7QZ_NHI5WG2Je16spCEjd0EuMh76kWAWB6KUfBHRNphRITcMvPpCFJ0J_hpp69tFhFrZiLAdX9LeSLSgaPI9eVLkKNvmaTWJ7nvlVIKuqsxXTZxQqzGL/s790-rw-e365/exploit.jpg)

Cybersecurity researchers have uncovered multiple critical security vulnerabilities impacting the Versa Concerto network security and SD-WAN orchestration platform that could be exploited to take control of susceptible instances.

It's worth noting that the identified shortcomings remain unpatched despite responsible disclosure on February 13, 2025, prompting a public release of the issues following the end of the 90-day deadline.

"These vulnerabilities, when chained together, could allow an attacker to fully compromise both the application and the underlying host system," ProjectDiscovery researchers Harsh Jaiswal, Rahul Maini, and Parth Malhotra [said](https://projectdiscovery.io/blog/versa-concerto-authentication-bypass-rce) in a report shared with The Hacker News.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The security defects are listed below -

* **[CVE-2025-34025](https://nvd.nist.gov/vuln/detail/CVE-2025-34025)** (CVSS score: 8.6) - A privilege escalation and Docker container escape vulnerability that's caused by unsafe default mounting of host binary paths and could be exploited to gain code execution on the underlying host machine
* **[CVE-2025-34026](https://nvd.nist.gov/vuln/detail/CVE-2025-34026)** (CVSS score: 9.2) - An authentication bypass vulnerability in the Traefik reverse proxy configuration that allows an attacker to access administrative endpoints, which could then be exploited to access heap dumps and trace logs by exploiting an internal Spring Boot Actuator endpoint via [CVE-2024-45410](https://github.com/traefik/traefik/security/advisories/GHSA-62c8-mh53-4cqv)
* **[CVE-2025-34027](https://nvd.nist.gov/vuln/detail/CVE-2025-34027)** (CVSS score: 10.0) - An authentication bypass vulnerability in the Traefik reverse proxy configuration that allows an attacker to access administrative endpoints, which could then be exploited to achieve remote code execution by exploiting an endpoint related to package uploads ("/portalapi/v1/package/spack/upload") via arbitrary file writes

Successful exploitation of CVE-2025-34027 could allow an attacker to leverage a race condition and write malicious files to disk, ultimately resulting in remote code execution using LD\_PRELOAD and a reverse shell.

"Our approach involved overwriting ../../../../../../etc/ld.so.preload with a path pointing to /tmp/hook.so," the researchers said. "Simultaneously, we uploaded /tmp/hook.so, which contained a compiled C binary for a reverse shell. Since our request triggered two file write operations, we leveraged this to ensure that both files were written within the same request."

"Once these files were successfully written, any command execution on the system while both persisted would result in the execution of /tmp/hook.so, thereby giving us a reverse shell."

In the absence of an official fix, users are advised to block semicolons in URL paths and drop requests where the Connection header contains the value X-Real-Ip. It's also recommended to monitor network traffic and logs for any suspicious activity.

### Update

Versa Networks, in a statement shared with The Hacker News, said the issues were addressed in Concerto version 12.2.1 GA released on April 16, 2025. The complete response from the company is below -

*Versa is committed to maintaining the highest standards of security and transparency across our platform.*

*On February 13, 2025, three vulnerabilities were identified and confirmed in our Concerto software platform. As part of our standard security response process, we developed and validated fixes, which were completed on March 7, 2025, and the hotfix made available to customers. A Generally Available (GA) software release containing these remediations was made available to all customers on April 16, 2025.*

*Many customers have already upgraded to the April 16th release, though we recognize some deployments may still be pending. Detailed information on affected releases and mitigation steps has been posted for customer access only.*

*There is no indication that these vulnerabilities were exploited in the wild, and no customer impact has been reported. All affected customers were notified through established security and support channels with guidance on how to apply the recommended updates.*

*Versa follows responsible disclosure practices and takes a proactive approach to identifying, mitigating, and communicating potential risks. Security is foundational to our platform, and we continue to invest in continuous monitoring, rapid response, and customer education as part of our commitment to trust and protection.*

*(The story was updated after publication to include a response from Versa Networks about the patch information.)*

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
[![Facebook...