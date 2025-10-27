---
title: That Network Traffic Looks Legit, But it Could be Hiding a Serious Threat
url: https://thehackernews.com/2025/07/that-network-traffic-looks-legit-but-it.html
source: The Hacker News
date: 2025-07-03
fetch_date: 2025-10-07T00:00:29.311167
---

# That Network Traffic Looks Legit, But it Could be Hiding a Serious Threat

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

# [That Network Traffic Looks Legit, But it Could be Hiding a Serious Threat](https://thehackernews.com/2025/07/that-network-traffic-looks-legit-but-it.html)

**Jul 02, 2025**The Hacker NewsNetwork Security / Threat Detection

[![Network Traffic](data:image/png;base64... "Network Traffic")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYmXZg25AI9euid6yFoO777OuU3Np8qv-q8BeX6UsfJEi7-iFTNz12V1IXbq3sNE2aZrfLa8ULyfPu05wO5ro3gqltw6KUqhja7MsWg59afpI-LzhXvLxDdfqEEK7LUss2whbthQEGS9cQScJ0ZDJTCzSMIZ1v9OjLwV42ttK0xaj5PDnZqGiq7JWF7yo/s790-rw-e365/main.jpg)

*With nearly 80% of cyber threats now mimicking legitimate user behavior, how are top SOCs determining what's legitimate traffic and what is potentially dangerous?*

Where do you turn when firewalls and endpoint detection and response (EDR) fall short at detecting the most important threats to your organization? Breaches at edge devices and VPN gateways have risen from 3% to 22%, according to Verizon's latest Data Breach Investigations report. EDR solutions are struggling to catch zero-day exploits, living-off-the-land techniques, and malware-free attacks. Nearly 80% of detected threats use malware-free techniques that mimic normal user behavior, as highlighted in CrowdStrike's 2025 Global Threat Report. The stark reality is that conventional detection methods are no longer sufficient as threat actors adapt their strategies, using clever techniques like credential theft or DLL hijacking to avoid discovery.

In response, security operations centers (SOCs) are turning to a **[multi-layered detection](https://corelight.com/cp/evasive-threats?utm_source=thehackernews&utm_medium=article-3&utm_campaign=awareness-wave-1)** approach that uses network data to expose activity adversaries can't conceal.

Technologies like network detection and response (NDR) are being adopted to provide visibility that complements EDR by exposing behaviors that are more likely to be missed by endpoint-based solutions. Unlike EDR, NDR operates without agent deployment, so it effectively identifies threats that use common techniques and legitimate tools maliciously. The bottom line is evasive techniques that work against edge devices and EDR are less likely to succeed when NDR is also on the lookout.

## **Layering up: The faster threat detection strategy**

Much like layering for unpredictable weather, elite SOCs boost resilience through a multi-layered detection strategy centered on network insights. By consolidating detections into a single system, NDR streamlines management and empowers teams to focus on high-priority risks and use cases.

Teams can adapt quickly to evolving attack conditions, detect threats faster, and minimize damage. Now, let's gear up and take a closer look at the layers that make up this dynamic stack:

#### THE BASE LAYER

Lightweight and quick to apply, these easily catch known threats to form the basis for defense:

* **Signature-based network detection** serves as the first layer of protection due to its lightweight nature and quick response times. Industry-leading signatures, such as those from Proofpoint ET Pro running on Suricata engines, can rapidly identify known threats and attack patterns.
* **Threat intelligence***,* often composed of indicators of compromise (IOCs), looks for known network entities (e.g., IP addresses, domain names, hashes) observed in actual attacks. As with signatures, IOCs are easy to share, light-weight, and quick to deploy, offering quicker detection.

#### THE MALWARE LAYER

Think of **malware detection** as a waterproof barrier, protecting against "drops" of malware payloads by identifying malware families. Detections such as YARA rules — a standard for static file analysis in the malware analysis community — can identify malware families sharing common code structures. It's crucial for detecting polymorphic malware that alters its signature while retaining core behavioral characteristics.

#### THE ADAPTIVE LAYER

Built to weather evolving conditions, the most sophisticated layers use behavioral detection and machine learning algorithms that identify known, unknown, and evasive threats:

* **Behavioral detection** identifies dangerous activities like domain generation algorithms (DGAs), command and control communications, and unusual data exfiltration patterns. It remains effective even when attackers change their IOCs (or even components of the attack), since the underlying behaviors don't change, enabling quicker detection of unknown threats.
* **ML** models, both supervised and unsupervised, can detect both known attack patterns and anomalous behaviors that might indicate novel threats. They can target attacks that span greater lengths of time and complexity than behavioral detections.
* **Anomaly detection** uses unsupervised machine learning to spot deviations from baseline network behavior. This alerts SOCs to anomalies like unexpected services, unusual client software, suspicious logins, and malicious management traffic. It helps organizations uncover threats hiding in normal network activity and minimize attacker dwell time.

#### THE QUERY LAYER

Finally, in some situations, there is simply no faster way to generate an alert than to query the existing network data. **Search-based detection** *—* log search queries that generate alerts and detections — functions like a snap-on layer that's at the ready for short-term, rapid response.

## **Unifying threat detection layers with NDR**

The true strength in multi-layered detections is how they work together. Top SOCs are deploying Network Detection and Response (NDR) to provide a unified view of threats across the network. NDR correlates detections from multiple engines to deliver a complete threat view, centralized network visibility, and the context that powers real-time incident response.

Beyond layered detections, **[advanced NDR solutions](https://corelight.com/products/open-ndr/?utm_source=thehackernews&utm_medium=article-3&utm_campaign=awareness-wave-1)** can also offer severa...