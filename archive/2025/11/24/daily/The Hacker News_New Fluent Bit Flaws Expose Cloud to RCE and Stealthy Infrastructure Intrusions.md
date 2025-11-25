---
title: New Fluent Bit Flaws Expose Cloud to RCE and Stealthy Infrastructure Intrusions
url: https://thehackernews.com/2025/11/new-fluent-bit-flaws-expose-cloud-to.html
source: The Hacker News
date: 2025-11-24
fetch_date: 2025-11-25T03:13:33.613844
---

# New Fluent Bit Flaws Expose Cloud to RCE and Stealthy Infrastructure Intrusions

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [New Fluent Bit Flaws Expose Cloud to RCE and Stealthy Infrastructure Intrusions](https://thehackernews.com/2025/11/new-fluent-bit-flaws-expose-cloud-to.html)

**Nov 24, 2025**Ravie LakshmananVulnerability / Container Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglthAM8BOOHnPV1FD-cS4ytxy6NAV-36uBknDThxhfkbb4DdfzRkVt03DWxFsmD3Q9xTBCvTJa2Fh_E47zrbVeSIWaopvPq4LhNcz6kSjVhJ_ahBpgn4SdUUT67vPM5JJzMcr8Ua8tiY0Ms25mD1NK144NWo4wW4udxwocySfkBfmE92C1OUwHNvjfni_l/s790-rw-e365/bit-main.jpg)

Cybersecurity researchers have discovered five vulnerabilities in [Fluent Bit](https://github.com/fluent/fluent-bit), an open-source and lightweight telemetry agent, that could be chained to compromise and take over cloud infrastructures.

The security defects "allow attackers to bypass authentication, perform path traversal, achieve remote code execution, cause denial-of-service conditions, and manipulate tags," Oligo Security said in a [report](https://www.oligo.security/blog/critical-vulnerabilities-in-fluent-bit-expose-cloud-environments-to-remote-takeover) shared with The Hacker News.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Successful exploitation of the flaws could enable attackers to disrupt cloud services, manipulate data, and burrow deeper into cloud and Kubernetes infrastructure. The list of identified vulnerabilities is as follows -

* **CVE-2025-12972** - A path traversal vulnerability stemming from the use of unsanitized [tag values](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) to generate output filenames, making it possible to write or overwrite arbitrary files on disk, enabling log tampering and remote code execution.
* **CVE-2025-12970** - A stack buffer overflow vulnerability in the Docker Metrics input plugin (in\_docker) that could allow attackers to trigger code execution or crash the agent by creating containers with excessively long names.
* **CVE-2025-12978** - A vulnerability in the tag-matching logic lets attackers spoof trusted tags – which are assigned to every event ingested by Fluent Bit – by guessing only the first character of a Tag\_Key, allowing an attacker to reroute logs, bypass filters, and inject malicious or misleading records under trusted tags.
* **CVE-2025-12977** - An improper input validation of tags derived from user-controlled fields, allowing an attacker to inject newlines, traversal sequences, and control characters that can corrupt downstream logs.
* **CVE-2025-12969** - A missing security.users authentication in the [in\_forward plugin](https://docs.fluentbit.io/manual/data-pipeline/outputs/forward) that's used to receive logs from other Fluent Bit instances using the [Forward protocol](https://docs.fluentd.org/input/forward), allowing attackers to send logs, inject false telemetry, and flood a security product's logs with false events.

"The amount of control enabled by this class of vulnerabilities could allow an attacker to breach deeper into a cloud environment to execute malicious code through Fluent Bit, while dictating which events are recorded, erasing or rewriting incriminating entries to hide their tracks after an attack, injecting fake telemetry, and injecting plausible fake events to mislead responders," researchers said.

The CERT Coordination Center (CERT/CC), in an independent advisory, [said](https://kb.cert.org/vuls/id/761751) many of these vulnerabilities require an attacker to have network access to a Fluent Bit instance, adding they could be used for authentication bypass, remote code execution, service disruption, and tag manipulation.

Following responsible disclosure, the issues have been addressed in [versions 4.1.1](https://github.com/fluent/fluent-bit/releases/tag/v4.1.1) and 4.0.12 released last month. Amazon Web Services (AWS), which also engaged in coordinated disclosure, has urged customers running Fluentbit to update to the latest version for optimal protection.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Given Fluent Bit's popularity within enterprise environments, the shortcomings have the potential to impair access to cloud services, allow data tampering, and seize control of the logging service itself.

Other recommended actions include avoiding use of dynamic tags for routing, locking down output paths and destinations to prevent tag-based path expansion or traversal, mounting /fluent-bit/etc/ and configuration files as read-only to block runtime tampering, and running the service as non-root users.

The development comes more than a year after Tenable detailed a flaw in Fluent Bit's built-in HTTP server ([CVE-2024-4323](https://thehackernews.com/2024/05/linguistic-lumberjack-vulnerability.html) aka Linguistic Lumberjack) that could be exploited to achieve denial-of-service (DoS), information disclosure, or remote code execution.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Container Security](https://thehackernews.com/search/label/Container%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Kubernetes](http...