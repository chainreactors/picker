---
title: CrowdStrike Explains Friday Incident Crashing Millions of Windows Devices
url: https://thehackernews.com/2024/07/crowdstrike-explains-friday-windows.html
source: The Hacker News
date: 2024-07-25
fetch_date: 2025-10-06T17:51:10.247891
---

# CrowdStrike Explains Friday Incident Crashing Millions of Windows Devices

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

# [CrowdStrike Explains Friday Incident Crashing Millions of Windows Devices](https://thehackernews.com/2024/07/crowdstrike-explains-friday-windows.html)

**Jul 24, 2024**Ravie LakshmananSoftware Update / IT Outage

[![Windows Crash](data:image/png;base64... "Windows Crash")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_zc429snn06MALdhwBfCgF1eDpztUmBLQL5G2XzeEfi49mgJYbGdvymusuix4w3KIH1jVxXW9UgE_hf-YG6RqP8cUEHc-Gbt0yhg6RW7vPdTgEzsQzWwoka0teYAQtOrpF7B-BGxjLzZHTA35n9FfQzjUjdRcyWReY_QXqyZe7Nm3W3KQH7TP2zBjTG81/s790-rw-e365/windows.png)

Cybersecurity firm CrowdStrike on Wednesday blamed an issue in its validation system for causing millions of Windows devices to crash as part of a [widespread outage](https://thehackernews.com/2024/07/faulty-crowdstrike-update-crashes.html) late last week.

"On Friday, July 19, 2024 at 04:09 UTC, as part of regular operations, CrowdStrike released a content configuration update for the Windows sensor to gather telemetry on possible novel threat techniques," the company [said](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/) in its Preliminary Post Incident Review (PIR).

"These updates are a regular part of the dynamic protection mechanisms of the Falcon platform. The problematic Rapid Response Content configuration update resulted in a Windows system crash."

The incident impacted Windows hosts running sensor version 7.11 and above that was online between July 19, 2024, 04:09 UTC and 05:27 UTC and received the update. Apple macOS and Linux systems were not affected.

CrowdStrike said it delivers security content configuration updates in two ways, one via Sensor Content that's shipped with Falcon Sensor and another through Rapid Response Content that allows it to flag novel threats using various behavioral pattern-matching techniques.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The crash is said to have been the result of a Rapid Response Content update containing a previously undetected error. It's worth noting that such updates are delivered in the form of Template Instances corresponding to specific behaviors – each of which is mapped to a unique Template Type – for enabling new telemetry and detection.

The Template Instances, in turn, are created using a Content Configuration System, after which they are deployed to the sensor over the cloud through a mechanism dubbed Channel Files, which are ultimately written to disk on the Windows machine. The system also encompasses a Content Validator component that carries out validation checks on the content before it is published.

"Rapid Response Content provides visibility and detections on the sensor without requiring sensor code changes," it explained.

"This capability is used by threat detection engineers to gather telemetry, identify indicators of adversary behavior and perform detections and preventions. Rapid Response Content is behavioral heuristics, separate and distinct from CrowdStrike's on-sensor AI prevention and detection capabilities."

These updates are then parsed by the Falcon sensor's Content Interpreter, which then allows the Sensor Detection Engine to detect or prevent malicious activity, depending on the customer's policy configuration.

While each new Template Type is stress tested for different parameters like resource utilization and performance impact, the root cause of the problem, per CrowdStrike, could be traced back to the rollout of the Interprocess Communication (IPC) Template Type on February 28, 2024, that was introduced to flag attacks that abuse [named pipes](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipes).

The timeline of events is as follows -

* **February 28, 2024** - CrowdStrike releases sensor 7.11 to customers with new IPC Template Type
* **March 5, 2024** - The IPC Template Type passes the stress test and is validated for use
* **March 5, 2024** - The IPC Template Instance is released to production via Channel File 291
* **April 8 - 24, 2024** - Three more IPC Template Instances are deployed in production
* **July 19, 2024** - Two additional IPC Template Instances are deployed, one of which passes validation despite having problematic content data

"Based on the testing performed before the initial deployment of the Template Type (on March 05, 2024), trust in the checks performed in the Content Validator, and previous successful IPC Template Instance deployments, these instances were deployed into production," CrowdStrike said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"When received by the sensor and loaded into the Content Interpreter, problematic content in Channel File 291 resulted in an out-of-bounds memory read triggering an exception. This unexpected exception could not be gracefully handled, resulting in a Windows operating system crash (BSoD)."

In response to the [sweeping disruptions](https://thehackernews.com/2024/07/cybercriminals-exploit-crowdstrike.html) caused by the crash and preventing them from happening again, the Texas-based company said it has improved its testing processes and enhanced its error handling mechanism in the Content Interpreter. It's also planning to implement a staggered deployment strategy for Rapid Response Content.

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
[**Share on ...