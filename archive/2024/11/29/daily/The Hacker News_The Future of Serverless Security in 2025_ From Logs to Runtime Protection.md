---
title: The Future of Serverless Security in 2025: From Logs to Runtime Protection
url: https://thehackernews.com/2024/11/the-future-of-serverless-security-in.html
source: The Hacker News
date: 2024-11-29
fetch_date: 2025-10-06T19:19:55.399465
---

# The Future of Serverless Security in 2025: From Logs to Runtime Protection

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

# [The Future of Serverless Security in 2025: From Logs to Runtime Protection](https://thehackernews.com/2024/11/the-future-of-serverless-security-in.html)

**Nov 28, 2024**The Hacker NewsCloud Security / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoGgzo88ukrMwt-zZVyghhUZGAO3SrZVGzK8tCqUmII0J7HjlRnhupHMP8-los0Xwd29N4yBTs19wX5KoaLLpK98gHfvk8LPv-vypoHruHGVL0xa2JyA3o6_5mJ2YMWQ8Xe4wpNkwUy4mkPcz25tuk9E-t6qPGBx15d0NmCNTrHLcpKnkyVmZ12peSgvk/s790-rw-e365/serverless.png)

Serverless environments, leveraging services such as AWS Lambda, offer incredible benefits in terms of scalability, efficiency, and reduced operational overhead. However, securing these environments is extremely challenging. The core of current serverless security practices often revolves around two key components: log monitoring and static analysis of code or system configuration. But here is the issue with that:

### **1. Logs Only Tell Part of the Story**

Logs can track external-facing activities, but they don't provide visibility into the internal execution of functions. For example, if an attacker injects malicious code into a serverless function that doesn't interact with external resources (e.g., external APIs or databases), traditional log-based tools will not detect this intrusion. The attacker may execute unauthorized processes, manipulate files, or escalate privileges—all without triggering log events.

### **2. Static Misconfiguration Detection is Incomplete**

Static tools that check for misconfigurations are great for detecting issues such as overly permissive IAM roles or sensitive environment variables exposed to the wrong parties. However, these tools cannot account for what happens in real-time, detect exploitations as they happen, or detect deviations from expected behavior.

## Real-World Implications of the Limited Cloud Security Available for Serverless Environments

### **Example 1: Malicious Code Injection in a Lambda Function**

An attacker successfully injects malicious code into a Lambda function, attempting to spawn an unauthorized subprocess or establish a connection to an external IP address.

* **Problem**: Traditional security tools relying on log monitoring will likely miss this attack. Logs typically track external-facing events like API calls or network connections, but they won't capture internal actions, such as code execution within the function itself. As a result, the attacker's actions—whether manipulating files, escalating privileges, or executing unauthorized processes—remain invisible unless they trigger an external event like an outbound API call.
* **Solution**: To effectively detect and prevent this attack, security teams need tools that provide visibility into the function's internal operations in real time. [A sensor monitoring runtime activity](https://hubs.li/Q02ZGMnN0) can identify and terminate rogue processes before they escalate, offering proactive, real-time protection.

### **Example 2: Exploiting Vulnerable Open-Source Libraries**

A Lambda function relies on an open-source library with a known vulnerability, which an attacker can exploit to execute remote code.

* **Problem**: While static analysis tools can flag known vulnerabilities in the library itself, they don't have visibility into how the library is used in the runtime environment. This means that even if a vulnerability is identified in code scans, the real-time exploitation of that vulnerability might go undetected if it doesn't involve an external event (such as a network request or API call).
* **Solution**: A sensor designed to monitor the function's internal operations can detect when the library is being misused or actively exploited at runtime. By continuously analyzing function behavior, the sensor can identify anomalous actions and block the exploit before it compromises the system.

## The Shift that Needs to Happen for 2025

Cloud security is expanding rapidly, providing organizations with increased protection and detection and response measures against sophisticated cloud attacks. Serverless environments need this same type of protection because they are built on the cloud.

By shifting from reactive, log-based security measures to proactive, runtime-focused protection, security teams can begin to implement modern cloud security practices into their serverless environments.

## Introducing Sweet's AWS Lambda Serverless Sensor

Recognizing the limitations of traditional security tools, [Sweet Security](https://hubs.li/Q02ZGMpR0) has developed a groundbreaking sensor for serverless environments running AWS Lambda. This sensor addresses the blind spots inherent in log-based and static analysis methods by offering deep, real-time monitoring of Lambda functions.

### **Runtime monitoring and visibility**

Sweet's sensor monitors the runtime activity of serverless functions. By observing system calls, internal function behavior, and interactions within the Lambda environment, the sensor provides full visibility into how the function is behaving at any given moment.

### **Blocking malicious behavior in real-time**

Sweet identifies suspicious activity, such as spawning unauthorized processes or connecting to external IPs, and blocks them before harm is done.

### **Detecting anomalies in function behavior**

Sweet's Lambda sensor monitors the function's internal operations in real-time, detects any misuse of the library, and blocks the exploit before it can compromise the system.

In an age where serverless computing is becoming the backbone of cloud-native architectures, the ability to secure these environments in real time is paramount. Traditional log-based and static security tools are no longer enough to safeguard against sophisticated, dynamic attacks. With Sweet Security's innovative sensor, organizations now have the ability to proactively monitor, detect, and prevent threats in real time—giving them the confidence to embrace serverless computing while keeping their envir...