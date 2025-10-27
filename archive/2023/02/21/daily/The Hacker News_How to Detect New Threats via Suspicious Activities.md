---
title: How to Detect New Threats via Suspicious Activities
url: https://thehackernews.com/2023/02/how-to-detect-new-threats-via.html
source: The Hacker News
date: 2023-02-21
fetch_date: 2025-10-04T07:39:22.006991
---

# How to Detect New Threats via Suspicious Activities

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

# [How to Detect New Threats via Suspicious Activities](https://thehackernews.com/2023/02/how-to-detect-new-threats-via.html)

**Feb 20, 2023**The Hacker NewsMalware Analysis / Threat Detection

[![Malware analysis](data:image/png;base64... "Malware analysis")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTyL6hUHGq19Zj9TFm5gfuj8tBr3YIFc38LyWJWMTjj94f2z492vKaDvzvQNhkn3Tp1XxrOtmMu6ceDzseUWfTfH04xGhLbn5Hpk4IYdzkzQUPcygWLUShOJH5fq4Ep-LOLj0m1y7bPyJ7d-NVIRW-7xFmVUgmaFRWV_GYufF5Uo7titGTiKj6Y9iJ/s790-rw-e365/anyrun.png)

Unknown malware presents a significant cybersecurity threat and can cause serious damage to organizations and individuals alike. When left undetected, malicious code can gain access to confidential information, corrupt data, and allow attackers to gain control of systems. Find out how to avoid these circumstances and detect unknown malicious behavior efficiently.

## Challenges of new threats' detection

While known malware families are more predictable and can be detected more easily, unknown threats can take on a variety of forms, causing a bunch of challenges for their detection:

1. Malware developers use polymorphism, which enables them to modify the malicious code to generate unique variants of the same malware.
2. There is malware that is still not identified and doesn't have any rulesets for detection.
3. Some threats can be Fully UnDetectable (FUD) for some time and challenge perimeter security.
4. The code is often encrypted, making it difficult to detect by signature-based security solutions.
5. Malware authors may use a "low and slow" approach, which involves sending a small amount of malicious code across a network over a long time, which makes it harder to detect and block. This can be especially damaging in corporate networks, where the lack of visibility into the environment can lead to undetected malicious activity.

## Detection of new threats

When analyzing known malware families, researchers can take advantage of existing information about the malware, such as its behavior, payloads, and known vulnerabilities, in order to detect and respond to it.

But dealing with new threats, researchers have to start from scratch, using the following guide:

**Step 1.** Use reverse engineering to analyze the code of the malware to identify its purpose and malicious nature.

**Step 2**. Use static analysis to examine the malware's code to identify its behavior, payloads, and vulnerabilities.

**Step 3.** Use dynamic analysis to observe the behavior of the malware during execution.

**Step 4.** Use sandboxing to run the malware in an isolated environment to observe its behavior without harming the system.

**Step 5.** Use heuristics to identify potentially malicious code based on observable patterns and behaviors.

**Step 6.** Analyze the results of reverse engineering, static analysis, dynamic analysis, sandboxing, and heuristics to determine if the code is malicious.

There are plenty of tools from Process Monitor and Wireshark to ANY.RUN to help you go through the first 5 steps. But how to draw a precise conclusion, what should you pay attention to while having all this data?

The answer is simple - focus on indicators of malicious behavior.

## Monitor suspicious activities for effective detection

Different signatures are used to detect threats. In computer security terminology, a signature is a typical footprint or pattern associated with a malicious attack on a computer network or system.

Part of these signatures is behavioral ones. It's impossible to do something in the OS and leave no tracing behind. We can identify what software or script it was via their suspicious activities.

You can run a suspicious program in a sandbox to observe the behavior of the malware and identify any malicious behavior, such as:

* abnormal file system activity,
* suspicious process creation and termination
* abnormal networking activity
* reading or modifying system files
* access system resources
* create new users
* connect to remote servers
* execute other malicious commands
* exploit known vulnerabilities in the system

Microsoft Office is launching PowerShell – looks suspicious, right? An application adds itself to the scheduled tasks – definitely pay attention to it. A svchost process runs from the temp registry – something is definitely wrong.

You can always detect any threat by its behavior, even without signatures.

Let's prove it.

### Use case #1

Here is a [sample of the stealer](https://app.any.run/tasks/bfa067f3-5a5c-4188-85ca-dfe51ee0016b/?utm_source=hacker_news&utm_medium=article&utm_campaign=detect_new_threats0223&utm_content=task1). What does it do? Steals user data, cookies, wallets, etc. How can we detect it? For example, it reveals itself when the application opens the Chrome browser's Login Data file.

|  |
| --- |
| [![Malware analysis](data:image/png;base64... "Malware analysis")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlklwNGl8RCtEZtmTx2N3Pl56ZrBK53ck7Q0StkggMyr-fBget6aWNMVCRLCLiE1H1-DJqxoWVfTiowI9VwAlONYDg3qWQabccl2797gresJEZYMQdBLavU6f3A1KlhDc0EKh1an8TirGYbPws2oH6Ikvslr3-F4hsd2paWUT0dJJM_E3KuTFQ8rI1-Q/s790-rw-e365/1.png) |
| Stealer's suspicious behavior |

The activity in the network traffic also announces the threat's malicious intentions. A legitimate application would never send credentials, OS characteristics, and other sensitive data collected locally.

In the case of traffic, malware can be detected by well-known features. [Agent Tesla](https://any.run/malware-trends/agenttesla?utm_source=hacker_news&utm_medium=article&utm_campaign=detect_new_threats0223&utm_content=mtt) in some cases does not encrypt data sent from an infected system like in this [sample](https://app.any.run/tasks/98ba59ed-0256-4b0b-bd5f-c54e1d2fe893/?utm_source=hacker_news&utm_medium=article&utm_campaign=detect_new_threats0223&utm_content=task2).

|  |
| --- |
| [![Malware analysis](data:image/png;base64... "Malware analysis")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXs...