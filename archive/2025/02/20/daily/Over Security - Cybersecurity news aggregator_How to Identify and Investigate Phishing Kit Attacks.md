---
title: How to Identify and Investigate Phishing Kit Attacks
url: https://any.run/cybersecurity-blog/how-to-track-phishkits/
source: Over Security - Cybersecurity news aggregator
date: 2025-02-20
fetch_date: 2025-10-06T20:38:09.932729
---

# How to Identify and Investigate Phishing Kit Attacks

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

![How to Identify and Investigate Phishing Kit Attacks](/cybersecurity-blog/wp-content/uploads/2025/02/phishkits_blog.jpg)

[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

# How to Identify and Investigate Phishing Kit Attacks

February 19, 2025

[Add comment](#comments-11659)
3131 views
8 min read

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How to Identify and Investigate Phishing Kit Attacks

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1441
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3041
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3084
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)

How to Identify and Investigate Phishing Kit Attacks

Phishing kits have invested greatly in the popularity of phishing. They drop the entry threshold for cybercriminals enabling even low-skilled hackers to conduct successful attacks.

In general, a phishing kit is a set of tools for creating convincing fake webpages, sites, or emails that trick users into divulging sensitive information like passwords or credit card credentials. Security specialists should never underestimate this type of malware and fail to be ready to counter its users.

## What Phishkits are made of

These ready-to-use packages can be basic, with some pre-written code and website and email templates, and they can be advanced phishing-as-a-service (PHaaS) kits that offer more sophisticated and customizable features. These may even contain automated updates or encryption features.

A typical kit includes:

* Website (email, social network pages) templates mimicking legitimate brands (banks, email providers, cloud services, etc.)
* Data harvesting scripts that capture input in webpage forms
* Automated deployment tools for quick setup
* Bypass techniques such as reverse proxies that intercept multi-factor authentication
* Server-side components that manage the data collected from victims

## Some notable Phishkits

* **16Shop**: targeted Apple, PayPal, and Amazon users and was distributed as a subscription service.
* **Evilginx2**: a framework to intercept authentication tokens that helped to bypass MFA.
* **BulletProofLink**: a PHaaS platform that offered pre-hosted phishing pages and even reused stolen credentials to maximize profit.

![](/cybersecurity-blog/wp-content/uploads/2025/02/greatness_phishkit-1024x578.png)

* **Greatness**: targets Microsoft 365 users and can dynamically generate fake login pages customized for the victim.
* **GoPhish**: an open-source framework meant for businesses to test their exposure to phishing by imitating attacks but also used maliciously.
* **King Phisher**: offers advanced features like campaign management and cloning of websites.
* **Blitz**: known for its simplicity and quick creation of phishing webpages.

## Why Phishkits are a serious issue for businesses

Phishing kits are employed to attack both individuals and organizations, but they represent a specific threat to businesses by inviting wider audience of would-be hackers to the industry, multiplying risks and providing an increased workload to security systems.

Besides, phishing kit attacks make it easier to turn any employee into a soft spot of the cyber security perimeter. Even targeted at people, such attacks are a headache for SOC teams.

The features of phishkits that pose increased risks for organizations are:

**Scalability**: They allow attackers to automate and run phishing campaigns against thousands of employees simultaneously.

**MFA Bypass**: Modern phishkits integrate Adversary-in-the-Middle (AiTM) techniques to steal session cookies, bypassing multi-factor authentication.

**Brand Abuse & Reputation Damage**: Phishing pages tend to impersonate well-known brands, leading to loss of their customer trust when credentials are stolen.

**Supply Chain Attacks**: Phishkits can be used to target third-party vendors and gain access to corporate networks via compromised partners.

## Defusing Phishkits with Threat Intelligence

[Cyber threat intelligence](https://any.run/cybersecurity-blog/threat-intelligence-explained/) has long proven useful in countering phishkit-based attacks. It involves gathering, analyzing, and acting upon information about current and emerging threats. For countering phishkits, it enforces:

* **Early detection**: TI helps to collect the indicators of compromise associated with the use of certain phishkits and set up network monitoring for detecting the elements of phishkit infrastructure.
* **Behavioral Analysis**: TI is used to analyze patterns and behaviors of phishing campaigns, to identify new kits or variations of known ones before they cause harm.
* **Proactive...