---
title: Kerberoasting Detections: A New Approach to a Decade-Old Challenge
url: https://thehackernews.com/2025/07/kerberoasting-detections-new-approach.html
source: The Hacker News
date: 2025-07-24
fetch_date: 2025-10-06T23:56:01.388682
---

# Kerberoasting Detections: A New Approach to a Decade-Old Challenge

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

# [Kerberoasting Detections: A New Approach to a Decade-Old Challenge](https://thehackernews.com/2025/07/kerberoasting-detections-new-approach.html)

**Jul 23, 2025**The Hacker NewsThreat Detection / Identity Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiRqRK8FI49st9Cgvx9KkoNxlFIlZBIgLnC8BjxbtOasCLnTWeDeOxV1GQQrs1SH9YqnvGDzS5mtJTJtCQSN2iKGpxuHsWK5zOOeGy6wnCVDXG3SdNj1VAPYLVnU3A1G7oLbBe63qRGa0hUk5yYLUefPDMHEmKSM-On77FHqXwEdSPem0go_9ZmvJMmlc/s790-rw-e365/Kerberoasting.jpg)

Security experts have been talking about [Kerberoasting](https://www.beyondtrust.com/resources/glossary/kerberoasting?utm_source=partner&utm_medium=referral&utm_campaign=THN&utm_content=Kerberoasting-Detections) for over a decade, yet this attack continues to evade typical defense methods. Why? It's because existing detections rely on brittle heuristics and static rules, which don't hold up for detecting potential attack patterns in highly variable Kerberos traffic. They frequently generate false positives or miss "low-and-slow" attacks altogether.

Is there a better and more accurate way for modern organizations to detect subtle anomalies within irregular Kerberos traffic? [The BeyondTrust research team](https://www.beyondtrust.com/blog/entry/kerberoasting-detections?utm_source=partner&utm_medium=referral&utm_campaign=THN&utm_content=Kerberoasting-Detections) sought to answer this question by combining security research insights with advanced statistics. This article offers a high-level look into the driving forces behind our research and our process of developing and testing a new statistical framework for improving Kerberos anomaly detection accuracy and reducing false positives.

## An Introduction to Kerberoasting Attacks

Kerberoasting attacks take advantage of the Kerberos network authentication protocol within Windows Active Directory environments. The Kerberos authentication process works as follows:

**1. AS-REQ:** A user logs in and requests a Ticket Granting Ticket (TGT).

**2. AS-REP:** The Authentication Server verifies the user's credentials and issues a TGT.

**3. TGS-REQ:** When the user wants to request access to a service, they request a Ticket Granting Service Ticket (TGS) using the previously received TGT. This action is recorded as Windows Event 4769[1] on the domain controller.

**4. TGS-REP:** The TGS verifies the request and issues a TGS, which is encrypted using the password hash of the service account associated with the requested service.

**5. KRB-AP-REQ:** For the user to authenticate against a service using the TGS ticket, they send it to the application server, which then takes various actions to verify the user's legitimacy and allow access to the requested service.

Attackers aim to exploit this process because Kerberos service tickets are encrypted with the hash of the service account's password. To take advantage of Kerberos tickets, attackers first leverage LDAP (Lightweight Directory Access Protocol) to query the directory for any AD accounts that have Service Principal Names (SPNs) associated with them. An attacker will then request Ticket Granting Service (TGS) tickets for these accounts, which can be done without any administrative rights. Once they have requested these service tickets, they can crack the hash offline to uncover the credentials of the service account. Access to a service account can then enable the attacker to move laterally, escalate privileges, or exfiltrate data.

## The Shortcomings of Typical Heuristic Methods

Many organizations have heuristic-based detection methods in place to flag irregular Kerberos behavior. One common method is volume-based detection, which can flag a spike in TGS request activity from a single account. If an attacker requests TGS tickets for all service principal names they can find using LDAP, this detection method will likely identify this spike as suspicious activity. Another method, encryption-type analysis, can detect if an attacker attempts to downgrade the encryption of the requested TGS tickets from the default AES to a weaker type, such as RC4 or DES, in hopes of making their own job easier when they start to [crack the hash](https://www.beyondtrust.com/blog/entry/password-cracking-101-attacks-defenses-explained?utm_source=partner&utm_medium=referral&utm_campaign=THN&utm_content=Kerberoasting-Detections).

While both of these static rule-based methods can work in some cases, they produce a notorious number of false positives. Additionally, they don't factor in the user's behaviors and irregularities unique to each organization's domain configurations.

## A Statistical Model for Detecting Kerberoasting Attacks

With these limitations in mind, the BeyondTrust research team sought to find a method that would both improve anomaly detection capabilities and reduce false positives. We found statistical modeling to be the best method, in which a model would be created that could estimate probability distribution based on contextual data patterns. The ability to predict normal user behavior would be key to flagging any abnormalities.

Our team laid out four constraints for our prospective statistical model, based on existing Kerberoasting research[2, 3]:

1. **Explainability**: The ability to interpret the output with respect to a recognized, normalized, and easy to explain and track measure.
2. **Uncertainty**: The ability to reflect sample size and confidence in estimates, as opposed to the output being a simple binary indicator.
3. **Scalability**: The ability to limit the amount of cloud computing and data storage needed for updating model parameters per run.
4. **Nonstationarity**: The capacity to adapt to trends or other data changes over time, and incorporating these shifts into how anomalies are defined

The BeyondTrust research team worked to build out a model that aligned with the above constraints, eventually developing a model that groups similar ticket-request patterns into distinct clusters and then use...