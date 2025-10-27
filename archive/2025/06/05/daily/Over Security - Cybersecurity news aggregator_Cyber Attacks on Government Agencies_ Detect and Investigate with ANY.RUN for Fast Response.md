---
title: Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response
url: https://any.run/cybersecurity-blog/how-to-investigate-government-cyber-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-05
fetch_date: 2025-10-06T22:55:14.098010
---

# Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response](/cybersecurity-blog/wp-content/uploads/2025/06/gov_attacks_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response

June 4, 2025

[Add comment](#comments-14055)
4744 views
9 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1637
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3168
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3197
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Cyber Attacks on Government Agencies: Detect and Investigate with ANY.RUN for Fast Response

Government institutions worldwide face a growing number of sophisticated cyberattacks. This case study examines how [ANY.RUN’s solutions](http://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=government_investigations&utm_term=040625&utm_content=linktolanding) can be leveraged to detect, analyze, and mitigate cyber threats targeting government organizations.

By analyzing real-world threats, we demonstrate how ANY.RUN’s [Threat Intelligence Lookup](https://intelligence.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=government_investigations&utm_term=040625&utm_content=linktolookup), [Interactive Sandbox](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=government_investigations&utm_term=040625&utm_content=linktoservice), and [YARA Search](https://any.run/cybersecurity-blog/yara-search-guide/) assist cybersecurity teams in identifying attack vectors, tracking malicious activities, and enhancing organizational resilience.

## Case Studies

We will explore several attack scenarios where adversaries impersonate government structures to gain initial access:

* A phishing email sent to the Department of Employment and Workforce (a U.S. government agency responsible for helping with employment and paying unemployment insurance benefits).

* A domain imitating the official website of the U.S. Social Security Administration.

* A malicious PDF disguised as a court notice from the South African Judiciary.

## 1. Phishing Email Targeting South Carolina Department of Employment and Workforce

Let’s take up the role of a cybersecurity officer at the department and try to understand who is targeting the organization, what malware is used, and what delivery methods are applied.

A YARA rule is created to search emails with recipients from the domain dew.sc.gov analyzed in ANY.RUN sandbox. It identified 33 files and their analyses featuring email addresses on dew.sc.gov.

![](/cybersecurity-blog/wp-content/uploads/2025/06/image2-1024x523.png)

These results help to better understand threats targeting the agency:

* Study subject lines, attachment types, and delivery methods.

* Identify malware and tools used for attacks.

* Collect artifacts (hashes, URLs, IPs) for filtering and monitoring.

* Detect recurring techniques to improve protection.

Let’s [view one of the sandbox analyses](https://app.any.run/tasks/583e3d2f-876e-4b57-8bee-879d4cdbb45c/?utm_source=anyrunblog&utm_medium=article&utm_campaign=government_investigations&utm_term=040625&utm_content=linktoservice) linked to the detected files:

In April 2025, a phishing email was uploaded to ANY.RUN, targeting an employee at the South Carolina DEW. The email, sent from @163.com domain, contained a malicious ZIP attachment named “Quotation.zip” (658 KB).

![](/cybersecurity-blog/wp-content/uploads/2025/06/image3-2-1024x596.png)

We can run a [separate analysis of the email in the Sandbox.](https://app.any.run/tasks/0e98323b-9eda-462e-9e02-222e03ced6e6) First of all, header analysis shows that the email failed SPF, DKIM, and DMARC checks — the IP address wasn’t authorized for sending from 163.com, and no DKIM signature was present.

Detect phishing and malware threats faster
with ANY.RUN’s Interactive Sandbox

[Sign up with business email](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=government_investigations&utm_term=040625&utm_content=linktoregistration#register/)

The IP can be used as an IOC and subjected to reputation checks.

![](/cybersecurity-blog/wp-content/uploads/2025/06/image4-1-1024x628.png)

The email attachment that includes an executable file, “Quotation.exe”, has been flagged as a stealer by ANY.RUN’s signatures even before execution. The malware was identified as [FormBook](https://any.run/malware-trends/formbook/), wi...