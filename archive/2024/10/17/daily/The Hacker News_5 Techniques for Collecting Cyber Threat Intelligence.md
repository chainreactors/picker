---
title: 5 Techniques for Collecting Cyber Threat Intelligence
url: https://thehackernews.com/2024/10/5-techniques-for-collecting-cyber.html
source: The Hacker News
date: 2024-10-17
fetch_date: 2025-10-06T18:59:34.272317
---

# 5 Techniques for Collecting Cyber Threat Intelligence

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

# [5 Techniques for Collecting Cyber Threat Intelligence](https://thehackernews.com/2024/10/5-techniques-for-collecting-cyber.html)

**Oct 16, 2024**The Hacker NewsThreat Intelligence / Malware Analysis

[![Cyber Threat Intelligence](data:image/png;base64... "Cyber Threat Intelligence")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6ETfjYQZTzK6aSxlVmDpisuL0SuJoS0DQbeGgiuseN7WHqt6ajYfz-LZAL3_4j6PcLzDmmiU4DIob2lrW1ltRf-pi4ifYppx-tTtWsWvX8cQV0MvZPUyjeh3pNX6gxaC7Uj0V9iv3lFqnaIH1aUYjXXu56VmYglbzwTSykhD1CVkHpvBQEiej2ERUNnY/s1700/cyber.png)

To defend your organization against cyber threats, you need a clear picture of the current threat landscape. This means constantly expanding your knowledge about new and ongoing threats.

There are many techniques analysts can use to collect crucial cyber threat intelligence. Let's consider five that can greatly improve your threat investigations.

## Pivoting on С2 IP addresses to pinpoint malware

IP addresses used by malware to communicate with its command and control (C2) servers are valuable indicators. They can help not only update your defenses, but also identify related infrastructure and tools belonging to threat actors.

This is done using the pivoting method, which lets analysts find additional context on the threat at hand with an existing indicator.

To perform pivoting, analysts use various sources, including threat intelligence databases that store large volumes of fresh threat data and offer search capabilities.

One useful tool is [Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=thehackernews&utm_medium=article&utm_campaign=5-techniques-for-collecting&utm_content=landing-lookup&utm_term=161024) from ANY.RUN. This service allows you to search its database using over 40 different query parameters, such as:

* Network indicators (IP addresses, domain names)
* Registry and file system paths
* Specific threat names, file names, and hashes

[ANY.RUN](https://any.run/?utm_source=thehackernews&utm_medium=article&utm_campaign=5-techniques-for-collecting&utm_content=landing&utm_term=161024) provides data associated with the indicators or artifacts in your query, along with sandbox sessions where the data was found. This helps analysts pin down a certain indicator or their combination to a specific attack, discover its context, and collect essential threat intelligence.

To demonstrate how it works, let's use the following IP address as part of [our query: 162[.]254[.]34[.]31](https://intelligence.any.run/analysis/lookup?utm_source=thehackernews&utm_medium=article&utm_campaign=5-techniques-for-collecting&utm_content=analysis-lookup1&utm_term=161024#%7B%2522query%2522:%2522destinationIP:%255C%2522162.254.34.31%255C%2522%2522,%2522dateRange%2522:180%7D). In your case, the initial indicator may come from an alert generated by an SIEM system, a threat intelligence feed, or research.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkH8MgdqHIS0-JWa6d_hC72WQ2L9rfatLYf1ZgQz1WPU38twrE6lb4O6NS5j-cFgWGzlKFNjhblCmHJ5O1QwD1BuvwUJsaCkWcrO1z8vfNZszpLhyphenhyphen5xTZjjQhhwsuh_qc7xCgFQi-H4MH7lkX_k3qDVC2wmhQlVl-ywZwe4-OrCHMn-J1BetpNcZ5RLgI/s1700/1.png) |
| The overview tab shows the key results of our search |

Submitting the IP address to TI Lookup instantly allows us to see that his IP has been linked to malicious activity. It also lets us know that the specific threat used with this IP is AgentTesla.

The service displays domains related to the indicator, as well as ports used by malware when connecting to this address.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCPlRBqWz9jF7_ywPo8f7IbIY7SLABUvpzdtfTFZCfjBiJ1qxs-zXuidKSpvPH-sTzydp_JydTEkc6rGn2ZoJHwsryphub7jYZjYsXH3ocD_CetyJRj5yec9XYIA3sCUB1Qkm4-PH-g0t5KbDE1tAzrdFzJpWIatM86GhYAB_eUJ1NmILb3n0Cj2pyn4Q/s1700/2.png) |
| Suricata IDS rule linked to the queried IP indicates data exfiltration via SMTP |

Other information available to us includes files, synchronization objects (mutexes), ASN, and triggered Suricata rules that were discovered in sandbox sessions involving the IP address in question.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7VFQi5H5sMhfzUvrJzMptx7L63jwSPeoE4uIxbzmVhaV2OnPO5t5IojX5Ijd8UveUH1EB4OEudpSk30w66SoVsOReD2H5L7GxBD9kfrjp6qsUwq__FOEEoIw6QDgvO_VC6BbuB1G0KxJNyOTOnQQktU45gCphlBELuSAUS76J0Bz27pe7SVjpVPyUcVo/s1700/3.png) |
| Sandbox session listed as one of the results in TI Lookup |

We can also navigate to [one of the sandbox sessions](https://app.any.run/tasks/2701e566-8638-4beb-9543-8d99e06749cb/?utm_source=thehackernews&utm_medium=article&utm_campaign=5-techniques-for-collecting&utm_content=tasks1&utm_term=161024) where the IP was spotted to see the entire attack and collect even more relevant information, as well as rerun the analysis of the sample to study it in real-time.

Test TI Lookup to see how it can improve your threat investigations. [Request a 14-day free trial](https://intelligence.any.run/plans?utm_source=thehackernews&utm_medium=article&utm_campaign=5-techniques-for-collecting&utm_content=plans&utm_term=161024).

## Using URLs to expose threat actors' infrastructure

Examining the domains and subdomains can provide valuable information on URLs used for hosting malware. Another common use case is identifying websites used in phishing attacks. Phishing websites often mimic legitimate sites to trick users into entering sensitive information. By analyzing these domains, analysts can uncover patterns and discover broader infrastructure employed by attackers.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmbpCmer3bR8FafEzTKdjlzQlKhEEDU6KShEJaalUezcG2VzjWgTzC6Uv1967Tg7qZVxx0BZEERrIJYCo3a3VWu8hkMmKotX_IZvK8i7w4LsymQwW-nMsv6CHCvaPnFX9Jok0nlyPWiIXcDy_ONVkdKf3cqgN6RjxRv72T0zM3MvaOXE3QqyMxkNfW4Y8/s1700/4.png) |
| URLs matching our search query f...