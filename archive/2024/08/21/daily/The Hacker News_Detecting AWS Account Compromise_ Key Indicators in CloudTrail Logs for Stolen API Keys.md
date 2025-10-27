---
title: Detecting AWS Account Compromise: Key Indicators in CloudTrail Logs for Stolen API Keys
url: https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html
source: The Hacker News
date: 2024-08-21
fetch_date: 2025-10-06T18:08:44.591165
---

# Detecting AWS Account Compromise: Key Indicators in CloudTrail Logs for Stolen API Keys

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

# [Detecting AWS Account Compromise: Key Indicators in CloudTrail Logs for Stolen API Keys](https://thehackernews.com/2024/08/detecting-aws-account-compromise-key.html)

**Aug 20, 2024**The Hacker NewsCybersecurity / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjP1d3SbzIoJjAFg_97lxzDYqRjvEdA8tYkLBFaYQ_BaA4HOxoTByqgpkNabrsfwBPD8YlcvYv959I-LcsQ7AQxIPX8lXZreeQrcX6NImDNbiSS7Ew3f7F4qhml2715kzNrkwxUAn4ySav_ZQmjlR4-00HWaVkDA9OPMuyJYRK2wZfF9yjTL49kgEN9vkc/s790-rw-e365/sans-3.jpg)

As cloud infrastructure becomes the backbone of modern enterprises, ensuring the security of these environments is paramount. With AWS (Amazon Web Services) still being the dominant cloud it is important for any security professional to know where to look for signs of compromise. AWS CloudTrail stands out as an essential tool for tracking and logging API activity, providing a comprehensive record of actions taken within an AWS account. Think of AWS CloudTrail like an audit or event log for all of the API calls made in your AWS account. For security professionals, monitoring these logs is critical, particularly when it comes to detecting potential unauthorized access, such as through stolen API keys. These techniques and many others I've learned through the incidents I've worked in AWS and that we built into [SANS FOR509](https://www.sans.org/cyber-security-courses/enterprise-cloud-forensics-incident-response/?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_content=THN_FOR509_DC_AWS_Article&utm_campaign=SANS_Cyber_Defense_Initiative_2024&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events), Enterprise Cloud Forensics.

## 1. Unusual API Calls and Access Patterns

### A. Sudden Spike in API Requests

One of the first signs of a potential security breach is an unexpected increase in API requests. CloudTrail logs every API call made within your AWS account, including who made the call, when it was made, and from where. An attacker with stolen API keys might initiate a large number of requests in a short time frame, either probing the account for information or attempting to exploit certain services.

What to Look For:

* A sudden, uncharacteristic surge in API activity.
* API calls from unusual IP addresses, particularly from regions where legitimate users do not operate.
* Access attempts to a wide variety of services, especially if they are not typically used by your organization.

Note that Guard Duty (if enabled) will automatically flag these kinds of events, but you have to be watching to find them.

### B. Unauthorized Use of Root Account

AWS strongly recommends avoiding the use of the root account for day-to-day operations due to its high level of privileges. Any access to the root account, especially if API keys associated with it are being used, is a significant red flag.

What to Look For:

* API calls made with root account credentials, especially if the root account is not typically used.
* Changes to account-level settings, such as modifying billing information or account configurations.

## 2. Anomalous IAM Activity

### A. Suspicious Creation of Access Keys

Attackers may create new access keys to establish persistent access to the compromised account. Monitoring CloudTrail logs for the creation of new access keys is crucial, especially if these keys are created for accounts that typically do not require them.

What to Look For:

* Creation of new access keys for IAM users, particularly those who have not needed them before.
* Immediate use of newly created access keys, which could indicate an attacker is testing or utilizing these keys.
* API calls related to `CreateAccessKey`, `ListAccessKeys`, and `UpdateAccessKey`.

### C. Role Assumption Patterns

AWS allows users to assume roles, granting them temporary credentials for specific tasks. Monitoring for unusual role assumption patterns is vital, as an attacker might assume roles to pivot within the environment.

What to Look For:

* Unusual or frequent `AssumeRole` API calls, especially to roles with elevated privileges.
* Role assumptions from IP addresses or regions not typically associated with your legitimate users.
* Role assumptions that are followed by actions inconsistent with normal business operations.

## 3. Anomalous Data Access and Movement

### A. Unusual S3 Bucket Access

Amazon S3 is often a target for attackers, given that it can store vast amounts of potentially sensitive data. Monitoring CloudTrail for unusual access to S3 buckets is essential in detecting compromised API keys.

What to Look For:

* API calls related to `ListBuckets`, `GetObject`, or `PutObject` for buckets that do not typically see such activity.
* Large-scale data downloads or uploads to and from S3 buckets, especially if occurring outside of normal business hours.
* Access attempts to buckets that store sensitive data, such as backups or confidential files.

### B. Data Exfiltration Attempts

An attacker may attempt to move data out of your AWS environment. CloudTrail logs can help detect such exfiltration attempts, especially if the data transfer patterns are unusual.

What to Look For:

* Large data transfers from services like S3, RDS (Relational Database Service), or DynamoDB, especially to external or unknown IP addresses.
* API calls related to services like AWS DataSync or S3 Transfer Acceleration that are not typically used in your environment.
* Attempts to create or modify data replication configurations, such as those involving S3 cross-region replication.

## 4. Unexpected Security Group Modifications

Security groups control inbound and outbound traffic to AWS resources. An attacker might modify these settings to open up additional attack vectors, such as enabling SSH access from external IP addresses.

What to Look For:

* Changes to security group rules that allow inbound traffic from IP addresses outside your trusted network.
* API calls related to `AuthorizeSecurityGroupIngress` or `RevokeSecurityGroupEgress` th...