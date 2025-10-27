---
title: How Long Does It Take Hackers to Crack Modern Hashing Algorithms
url: https://thehackernews.com/2025/01/how-long-does-it-take-hackers-to-crack.html
source: Instapaper: Unread
date: 2025-01-30
fetch_date: 2025-10-06T20:14:26.469073
---

# How Long Does It Take Hackers to Crack Modern Hashing Algorithms

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

# [How Long Does It Take Hackers to Crack Modern Hashing Algorithms?](https://thehackernews.com/2025/01/how-long-does-it-take-hackers-to-crack.html)

**Jan 28, 2025**The Hacker NewsCybersecurity / Encryption

[![Crack Modern Hashing Algorithms](data:image/png;base64... "Crack Modern Hashing Algorithms")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbt6F2E2A8_A7V9HB4kxx9tKna5OLNmJcCURr__tX2dFKChpCbpkBPOPYN3X9UiGUcVZ5Ue4V0NA9siiKjwsKQtLN5kk9nBGVU8eAJkOay8EEvrkMCsfuMSgo1JnVxDH2lEG_zJGzHRuBHQj0M-S_0imVDL0jq00THZUWe3aRtMj2bB0uTQn9q7ggYfZA/s790-rw-e365/passwords.jpg)

While passwords remain the first line of defense for protecting user accounts against unauthorized access, the methods for creating strong passwords and protecting them are continually evolving. For example, [NIST password recommendations](https://specopssoft.com/blog/nist-password-guidelines/?utm_source=thehackernews&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=article) are now prioritizing password length over complexity. Hashing, however, remains a non-negotiable. Even long secure passphrases should be hashed to prevent them from being completely exposed in the event of a data breach – and never stored in plaintext.

This article examines how today's cyber attackers attempt to crack hashed passwords, explores common hashing algorithms and their limitations, and discusses measures you can take to protect your hashed passwords, regardless of which algorithm you are using.

## Modern password cracking techniques

Malicious actors have an array of tools and methods at their disposal for cracking hashed passwords. Some of the more widely used methods include brute force attacks, password dictionary attacks, hybrid attacks, and mask attacks.

### Brute force attacks

A [brute force attack](https://specopssoft.com/blog/brute-force-attack/?utm_source=thehackernews&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=article) involves excessive, forceful trial and error attempts to gain account access. Malicious actors employ specialized tools to systematically test password variations until a working combination is discovered. Although unsophisticated, brute force attacks are highly effective using password cracking software and high-powered computing hardware like graphics processing units (GPUs).

### Password dictionary attack

As its name implies, a password dictionary attack systematically draws words from a dictionary to brute force password variations until finding a working combination. The dictionary contents may contain every common word, specific word lists, and word combinations, as well as word derivatives and permutations with alphanumeric and non-alphanumeric characters (e.g., substituting an "a" with a "@"). Password dictionary attacks may also contain previously leaked passwords or key phrases exposed in data breaches.

### Hybrid attacks

A [hybrid password attack](https://specopssoft.com/blog/hybrid-password-attacks/?utm_source=thehackernews&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=article) combines brute force with dictionary-based methods to achieve better attack agility and efficacy. For example, a malicious actor may use a dictionary word list of commonly used credentials with techniques that integrate numerical and non-alphanumeric character combinations.

### Mask attacks

In some cases, malicious actors may know of specific password patterns or parameters/requirements. This knowledge allows them to use mask attacks to reduce the number of iterations and attempts in their cracking efforts. Mask attacks use brute force to check password attempts that match a specific pattern (e.g., eight characters, start with a capital letter, and end with a number or special character).

## How hashing algorithms protect against cracking methods

Hashing algorithms are a mainstay across a myriad of security applications, from file integrity monitoring to digital signatures and password storage. And while it's not a foolproof security method, hashing is vastly better than storing passwords in plaintext. With hashed passwords, you can ensure that even if cyber attackers gain access to password databases, they cannot easily read or exploit them.

By design, hashing significantly hampers an attacker's ability to crack passwords, acting as a critical deterrent by making password cracking so time and resource intensive that attackers are likely to shift their focus to easier targets.

## Can hackers crack hashing algorithms?

Because hashing algorithms are one-way functions, the only method to compromise hashed passwords is through brute force techniques. Cyber attackers employ special hardware like GPUs and cracking software (e.g., Hashcat, L0phtcrack, John The Ripper) to execute brute force attacks at scale—typically millions or billions or combinations at a time.

Even with these sophisticated purpose-built cracking tools, password cracking times can vary dramatically depending on the specific hashing algorithm used and password length/character combination. For example, long, complex passwords can take thousands of years to crack while short, simple passwords can be cracked immediately.

The following cracking benchmarks were all found by [Specops](https://specopssoft.com/?utm_source=thehackernews&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=article) on researchers on a Nvidia RTX 4090 GPU and used Hashcat software.

### MD5

Once considered an industrial strength hashing algorithm, MD5 is now considered cryptographically deficient due to its various security vulnerabilities; that said, it remains one of the most widely used hashing algorithms. For example, the popular CMS Wordpress still uses MD5 by default; this accounts for approximately [43.7%](https://www.wpzoom.com/blog/wordpress-statistics/) of CMS-powered websites.

With readily available GPUs and cracking software, attackers can instantly crack numeric passwords of 13 characters or fewer secured by MD5's 128-bit hash; on the other...