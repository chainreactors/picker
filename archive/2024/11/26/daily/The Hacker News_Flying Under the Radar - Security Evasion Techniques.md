---
title: Flying Under the Radar - Security Evasion Techniques
url: https://thehackernews.com/2024/11/flying-under-radar-security-evasion.html
source: The Hacker News
date: 2024-11-26
fetch_date: 2025-10-06T19:26:25.029143
---

# Flying Under the Radar - Security Evasion Techniques

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

# [Flying Under the Radar - Security Evasion Techniques](https://thehackernews.com/2024/11/flying-under-radar-security-evasion.html)

**Nov 25, 2024**The Hacker NewsThreat Intelligence / Security Awareness

[![Security Evasion Techniques](data:image/png;base64... "Security Evasion Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTSxqMwFavaipnKy8Z-PdBGEcX7EQSTOjEI_Vt8d_HeR8g84uwaxKZRnJIxhSElbTgAzkBjAA_N1QpP0UJ3OTKE2mzJ1JIbt1SJF8tYqGdbpzMtVXU7sIj-p1NZ-8OdY7fSXgn1vxFYFy__hyphenhyphenU-TlZLlgeCDPXVi6zfdBaNxVyZXz5mAb06ZR8p70_j3g/s790-rw-e365/main.png)

*Dive into the evolution of phishing and malware evasion techniques and understand how attackers are using increasingly sophisticated methods to bypass security measures.*

## The Evolution of Phishing Attacks

*"I really like the saying that 'This is out of scope' said no hacker ever. Whether it's tricks, techniques or technologies, hackers will do anything to evade detection and make sure their attack is successful,"* says Etay Maor, Chief Security Strategist at Cato Networks and member of [Cato CTRL](https://www.catonetworks.com/cato-ctrl/?utm_source=hackernews&utm_medium=referral). Phishing attacks have transformed significantly over the years. 15-20 years ago, simple phishing sites were sufficient for capturing the crown jewels of the time - credit card details. Today, attacks and defense methods have become much more sophisticated, as we'll detail below.

*"This is also the time where the "cat-and-mouse" attack-defense game began,"* says Tal Darsan, Security Manager and member of Cato CTRL. At the time, a major defense technique against credit card phishing sites involved flooding them with large volumes of numbers, in hopes of overwhelming them so they couldn't identify the real credit card details.

But threat actors adapted by validating data using methods like the Luhn algorithm to verify real credit cards, checking issuer information via Bank Identification Numbers (BIN), and performing micro-donations to test if the card was active.

Here's an example of how attackers validated credit card numbers inputted to phishing sites:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizezJhZJuOrSUMzLq0e-O3fuMBsCoi-lWfy3ts1t_yxjeYiEP6zokQIMHRtYv3abF_WfpZ0jzQZ3zGx3in6wLymkXGKnj8Rfyov9x4uJtI_vNzJ3-WcMQ1XPpKxn3N3UBuSEkdD3D6N49T8OuDgalndj_iW1zR12rtEFaQm_5An2Nq21L3OBmWKujjZNE/s790-rw-e365/1.png)

## Anti-Researcher Techniques

As phishing grew more advanced, attackers added anti-research techniques to prevent security analysts from studying and shutting down their operations. Common strategies included IP blocking after one-time access to create a false pretense that the phishing site was shut down, and detecting proxy servers, as researchers often use proxies when investigating.

The attacker code for one-time IP address access:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8s6O-WzQfdp8jt4TJQ0JQObn1bwe9sHUkmB5TJXicYYkDCUACYrBJCvot9-jBfjCFj7tm8AIAWPqwgA0CThh-td5xbvWvgqoEJGOgkVQiqlM-5aquqLL1xOrc7oi9NJg7xJ-H6Vr9QRYYcp5BeROpGEPiE88tvkCN4ZzOomUwaejxPNg59x05l3FZgHI/s790-rw-e365/2.png)

The attacker code for proxy identification:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_gOfjuBq-NxsEQONfhoElhUz-2mgiRAsGr9H6b8LxV3a2t1TzM-NbjNuN-NN8NebGtd1pilZOO5hRCbc9Z5scQD7Pp6YPdiuawS-IkYtg26TleV7R_1A8xKrRj84Zbc9MhkGx6UqPi4G-Gw5il4-Sp5RtUhEA98zJy_BdEbVejxfGrjBUjauhmtwQUUs/s790-rw-e365/3.png)

Attackers have also been randomizing folder structures in their URLs during the past decades, deterring researchers from tracking phishing sites based on common directory names used in phishing kits. This can be seen in the image below:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5SsRWHYhzBzJoStLGQDthpuuM0PRnyCcdKHOYlptKtun6pDy_UHQEkCCCiBefNs0bSnP-BUP9rdaMEY29PMNgoB_dr9vZtNEkHWpieb3_RvX3bs7t-od43WR92gzUSlTLyeM4o40mzm4mjBd4cxzaZ7OmKTwb5Erf-E3r2bs7U1YG2VGNL12cWsOaI_c/s790-rw-e365/4.png)

## Evading Anti-Virus

Another way to evade security controls in the past was to modify [malware](https://www.catonetworks.com/glossary/what-is-malware?utm_source=hackernews&utm_medium=referral) signatures with crypting services. This made it undetectable by signature-based antivirus systems. Here's an example of such a service that was once very popular:

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOxjxjdir4tkFx_N8rM02fyIkNyEQLwI5eSTjweRaNbISqNnyKDxCJYZdiSa3KAr3yeXaSVwt0bKFJn8pj5SLAqc3f-B4onzKY-t9anQPflfgXVHMLvZk8KXhoOjx6MT8VhAImTh8TPsUCIGAOynLn2vVNGoGeVfqJskqVZsJX_HXjsJqAztdGBZAkURM/s790-rw-e365/5.png)

## Evading Device Verification

Let's move on to other modern evasion techniques. First, a phishing attack that targets victims by gathering detailed device information—such as Windows version, IP address, and antivirus software—so attackers can better impersonate the victim's device.

This data helps them bypass security checks, like device ID verification, which organizations, like banks, use to confirm legitimate logins. By replicating the victim's device environment (e.g., Windows version, media player details, hardware specs), attackers can avoid suspicion when logging in from different locations or devices.

Some dark web services even provide pre-configured virtual machines that mirror the victim's device profile (see image below), adding an extra layer of anonymity for attackers and enabling safer access to compromised accounts. This demonstrates how data science and customization have become integral to criminal operations.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEje4RiE5-sTBuU4JfiRnhsOY3cjzOTFmZD21pIWaX2Nv7R_lxUrQ1JVwyhom3_2eXsvWyGrMiVlwSKQRp0CXMJ0z7X3UUpDL6sXjTfnkBpregWNe5uMd77dzGQuyZOFl0k57H3kVa2N1J1ff81T-khcfdReVrL1v4L_cXXDaM5yTXlfrcNNvRYA8alqRyY/s790-rw-e365/6.png)

## Evading Anomaly Detection

Another case is when d...