---
title: How Breaches Start: Breaking Down 5 Real Vulns
url: https://thehackernews.com/2025/04/how-breaches-start-breaking-down-5-real.html
source: The Hacker News
date: 2025-04-29
fetch_date: 2025-10-06T22:08:56.695382
---

# How Breaches Start: Breaking Down 5 Real Vulns

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

# [How Breaches Start: Breaking Down 5 Real Vulns](https://thehackernews.com/2025/04/how-breaches-start-breaking-down-5-real.html)

**Apr 28, 2025**The Hacker NewsCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5EpqCBIiD5Pew4QRf4QB1mFqVdA0fFfTs3mUbwENVou4wO7kQZKT5OvX1sCT0URBmEGEUPnJhQof-vECbfrxO6crvTHSTBYp3LJuaKbh3NBEKtaGmMylcMk1wyKfOeZl3DPbTTjZmQLbgpiA2ZfJCazWKlfwW7OVocead6DzQ31ub-GvXgHOp1_YWgfc/s790-rw-e365/main.jpg)

Not every security vulnerability is high risk on its own - but in the hands of an advanced attacker, even small weaknesses can escalate into major breaches. These five real vulnerabilities, uncovered by [Intruder's](https://www.intruder.io/?utm_source=thehackernews&utm_medium=p_referral&utm_campaign=global%7Cfixed%7C5_vulns_explained) bug-hunting team, reveal how attackers turn overlooked flaws into serious security incidents.

## **1. Stealing AWS Credentials with a Redirect**

Server-Side Request Forgery (SSRF) is a common vulnerability that can have a significant impact, especially in cloud-hosted applications. If a web application fetches resources from user-supplied URLs, care should be taken to ensure attackers can't manipulate requests to access unintended resources.

While assessing a home-moving app running in AWS, our team tested common SSRF bypass techniques.

The attack chain was as follows: the app sent a webhook request to the attacker's web server, which responded with a 302 redirect to AWS's metadata service. The app followed the redirect and logged the response, which exposed sensitive metadata - including AWS credentials.

With these credentials, an attacker could enumerate IAM permissions and attempt to pivot deeper into the cloud environment.

This attack would not have been possible if the metadata service was [enforcing IMDSv2](https://repost.aws/knowledge-center/ssm-ec2-enforce-imdsv2) - a best practice that a good [cloud security scanner](https://www.intruder.io/cloud-security) would have flagged. While automated tools might not have detected the full attack chain, breaking just this part of the chain could have prevented exploitation.

## **2. From Exposed .git Repo to Full Database Access**

While investigating an unintentionally exposed .git repository flagged by a vulnerability scan, our team discovered it belonged to a publicly accessible web application.

Reviewing the application's source code, we uncovered an authentication bypass - the login page could be accessed by supplying a hidden parameter.

Our team gained access to a management tool, where further analysis revealed a blind SQL injection vulnerability in an authenticated page.

Exploiting this vulnerability granted access to a university's database, which, if leveraged by an attacker, could have exposed sensitive personal information of students and staff - showing how a small misconfiguration can quickly escalate into a major security risk.

## **3. How a Tiny Detail Led to Remote Code Execution**

While hunting for bugs in a document signing app, our team noticed that, after signing a PDF, the metadata listed "ExifTool" as the document creator. Given ExifTool's history of critical vulnerabilities, we dug deeper.

Although the application didn't disclose the tool's version, testing for recent known vulnerabilities confirmed it was vulnerable to [CVE-2021-22204](https://intel.intruder.io/cves/CVE-2021-22204). By creating and uploading a malicious PDF, our team successfully gained remote command execution as the www-data user.

This foothold could have allowed an attacker to leverage additional vulnerabilities on the affected server, enabling them to gain root access and pivot to other machines on the network, causing extensive damage.

## **4. From Self-XSS to Site-Wide Account Takeover**

Cross-site scripting (XSS) is a powerful attack vector for session hijacking attacks, especially when no user interaction is required. While a 'Self-XSS' vulnerability is typically low risk, it can become dangerous when combined with another vulnerability.

Our team uncovered this exact scenario while assessing an auction application. A Self-XSS vulnerability was discovered where a user-supplied HTTP request header was reflected in the application's response.

Normally, this would be harmless since an attacker can't force a victim's browser to send a malicious header - but further testing uncovered a cache-poisoning vulnerability.

By chaining these two weaknesses, our team tricked the app into caching and serving the Self-XSS payload to all site visitors, escalating it to a site-wide persistent XSS attack.

This would have allowed an attacker to hijack any user account - including admin accounts.

## **5. Changing a Number to Expose Sensitive Data**

API weaknesses are more common than you'd think. Among them, IDOR vulnerabilities require little effort to exploit beyond modifying an identifier in a request.

The real challenge for an attacker isn't execution but discovery - finding a vulnerable endpoint that can be used without proper authentication or authorization, and recognizing that it exposes sensitive data. Once found, exploitation can be as simple as changing the identifier to a resource that the user does not own, or just making a request to an endpoint that should be reserved for administrators.

Our team frequently identifies IDOR, missing authentication, and broken authorization weaknesses in APIs. Here are some snippets from real HTTP requests and paths we found that exposed highly sensitive data:

* **GET /organisations/edit\_user?user\_id=1001**: The attacker could modify user profiles and hijack accounts
* **GET /prod-applicantresumes/12031.pdf**: The attacker could access job seekers' CVs.
* **POST /Order/Download, OrderNo=10202**: The attacker could access customer order information.

These examples are about as simple as API weaknesses get, but the consequences are far-reaching. By simply changing one number and enumerating through thousands ...