---
title: Obfuscation: There Are Two Sides To Everything
url: https://thehackernews.com/2024/08/obfuscation-there-are-two-sides-to.html
source: The Hacker News
date: 2024-08-02
fetch_date: 2025-10-06T18:07:32.575670
---

# Obfuscation: There Are Two Sides To Everything

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

# [Obfuscation: There Are Two Sides To Everything](https://thehackernews.com/2024/08/obfuscation-there-are-two-sides-to.html)

**Aug 01, 2024**The Hacker NewsSoftware Security / Threat Detection

[![Obfuscation](data:image/png;base64... "Obfuscation")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuibIKr_EZglopVDflWwLwmqAdebgA4HhUECXzmvNoEqlYodvNTEkzcE5MtFmZJQeoBeAa5RGtiLhGy5kgmvx2hkspSSyJWDk-Xjg6VnNuP2QX46JfczLNvu3VBwAwlygjxTDwp5h_b2j1Kj5yYNsggMAVDMDIJcdOxRQd2KsVzrOTmga6IcARWarSzDQ/s790-rw-e365/main.png)

## How to detect and prevent attackers from using these various techniques

Obfuscation is an important technique for protecting software that also carries risks, especially when used by malware authors. In this article, we examine obfuscation, its effects, and responses to it.

## What Is Obfuscation?

Obfuscation is the technique of intentionally making information difficult to read, especially in computer coding. An important use case is data obfuscation, in which sensitive data is made unrecognizable to protect it from unauthorized access. Various methods are used for this.

For example, only the last four digits of a credit card number are often displayed, while the remaining digits are replaced by Xs or asterisks. In contrast, encryption involves converting data into an unreadable form that can only be decrypted using a special key.

## Obfuscation In Code

When computer code is obfuscated, complex language and redundant logic are used to make the code difficult to understand. The aim? To deceive both human readers and programs such as decompilers. To do this, parts of the code are encrypted, metadata is removed, or meaningful names are replaced by meaningless ones. Inserting unused or meaningless code is also a common practice to disguise the actual code.

A so-called obfuscator can automate these processes and modify the source code so that it still works but is more difficult to understand.

Other methods of obfuscation include compressing the entire program, making the code unreadable, and changing the control flow to create unstructured, difficult-to-maintain logic.

Inserting dummy code that does not affect the logic or the program's result is also common.

Several techniques are often combined to achieve a multi-layered effect and increase security.

## The Flip Side

Unfortunately, obfuscation is not only a protection, it is also a challenge. Obfuscation is not only used by legitimate software developers, but also by malicious software authors. The goal of obfuscation is to anonymize cyber attackers, reduce the risk of detection, and hide malware by changing the overall signature and fingerprint of the malicious code – even if the payload is a known threat. The signature is a hash, a unique alphanumeric representation of a malware element. Signatures are very often hashed, but they can also be another short representation of a unique code within a malware element.

Rather than trying to create a new signature by modifying the malware itself, obfuscation focuses on deployment mechanisms to fool antivirus solutions that rely on signatures. Compare this to the use of machine learning, predictive analysis, and artificial intelligence to improve defenses.

Obfuscation, or the disguising of code, can be both "good" and "bad". In the case of "bad" obfuscation, hackers combine various techniques to hide malware and create multiple layers of disguise. One of these techniques is packers. These are software packages that compress malware to hide its presence and make the original code unreadable. Then there are cryptographers who encrypt malware or parts of software to restrict access to code that could alert antivirus programs.

Another method is the insertion of dead code. This involves inserting useless code into the malware to disguise the program's appearance. Attackers can also use command modification, which involves changing the command codes in malware programs. This changes the appearance of the code, but not its behavior.

[![Obfuscation](data:image/png;base64... "Obfuscation")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYWmDNgNqMoSgsBfU9rcbCwWvsW5QKsSSbCHBPkTQO-wQga_shyjDHY80Y9SLHRcIz7zZfwS2T_XvkZvwdPCwDUJpP7TbkoRQsIkj1q3_fZSXei568bKw-buH6fo7qo_38XFPSym5hD2uNubTUJoXHoScUzRGq3V9fYKoyojuMP0m1coMO3PQI7y1Bmvs/s790-rw-e365/Obfuscation-programmer.png)

Obfuscation in the code is, as we have seen, only the first step because no matter how much work the hacker puts into obfuscating the code to bypass EDR, malware must communicate within the network and to the outside world to be "successful". This means that communication must also be obfuscated. In contrast to the past, when networks were scanned quickly, and attempts were immediately made to extract data in the terabyte range at once, attackers today communicate more quietly so that the sensors and switches for the monitoring tools do not strike.

The aim to get IP addresses via scanning, for example, is now followed more slowly to stay under the radar. Reconnaissance, in which the threat actors try to collect data about their targeted victims, e.g. via their network architecture, is also becoming slower and more obscure.

A common obfuscation method is Exclusive OR (XOR). This method hides data in such a way that it can only be read by people who link the code with 0x55 XOR. ROT13 is another trick in which letters are replaced by a code.

### **Blasts From The Past:**

* A well-known example of obfuscation is the SolarWinds attack in 2020. Hackers used obfuscation to bypass defenses and hide their attacks.
* Another interesting example is PowerShell, a Microsoft Windows tool that attackers are abusing. Malware that uses PowerShell obscures its activities through techniques such as string encoding, command obfuscation, dynamic code execution, and more.
* Another example is the XLS.HTML attack. Here, hackers used elaborate obfuscation techniques to hide their malicious activities. They changed their encryption methods at least ten times...