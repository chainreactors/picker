---
title: Why 'Never Expire' Passwords Can Be a Risky Decision
url: https://thehackernews.com/2024/09/why-never-expire-passwords-can-be-risky.html
source: The Hacker News
date: 2024-09-24
fetch_date: 2025-10-06T18:33:56.030103
---

# Why 'Never Expire' Passwords Can Be a Risky Decision

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

# [Why 'Never Expire' Passwords Can Be a Risky Decision](https://thehackernews.com/2024/09/why-never-expire-passwords-can-be-risky.html)

**Sep 23, 2024**The Hacker NewsPassword Management / Data Breach

[![Password Management](data:image/png;base64... "Password Management")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhn37BeDnhO4_GNFDjmRou9iUw8L-1Q5SN-5dFgR2GlrR6mzCbVr2yipeX-c0jTtmn70t1VS7536cvQ3tUMQlhDYEtYdrsWReYZmcuJthpb-20iUb-6gB5R_-cSqmVt9V8S7OkM8DhyRqTv7LdTZrG3puA2iydlYVSl5fGvLdfEIZV8hixf4u_IInDkGQ0/s790-rw-e365/password.png)

Password resets can be frustrating for end users. Nobody likes being interrupted by the 'time to change your password' notification – and they like it even less when the new passwords they create are rejected by their organization's password policy. IT teams share the pain, with resetting passwords via service desk tickets and support calls being an everyday burden. Despite this, it's commonly accepted that all passwords should expire after a set period of time.

Why is this the case? Do you need password expiries at all? Explore the reason expiries exist and why setting passwords to 'never expire' might save some headaches, but not be the best idea for cybersecurity.

## Why do we have password expiries?

The traditional 90-day password reset policy stems from the need to protect against [brute-force attacks](https://specopssoft.com/blog/brute-force-attack/). Organizations typically store passwords as hashes, which are scrambled versions of the actual passwords created using cryptographic hash functions (CHFs). When a user enters their password, it's hashed and compared to the stored hash. Attackers attempting to crack these passwords must guess the correct one by running potential passwords through the same hashing algorithm and comparing the results. The process can further be complicated for attackers by techniques like salting, where random strings are added to passwords before hashing.

Brute-force attacks depend on several factors, including the computational power available to the attacker and the strength of the password. The 90-day reset period was considered a balanced approach to outpace brute-force attacks while not burdening users with too frequent changes. Advances in technology, however, have reduced the time required to crack passwords, prompting a re-evaluation of this policy. Despite this, the 90-day expiry remains a recommendation in many compliance standards, including PCI.

## Why have some organizations got rid of expiries?

One of the main arguments against regular password expiry is that it can lead to the reuse of weak passwords. Users often make slight changes to their existing passwords, such as changing 'Password1!' to 'Password2!'. This practice undermines the security benefits of password changes. The real issue here though is not the act of resetting passwords but rather the organization's policy that allows weak passwords in the first place.

The bigger reason organizations have opted for 'never expire' passwords is reducing IT and service desk burden. The cost and burden of password resets on IT help desks are significant. [Gartner estimates that 20-50%](https://www.bleepingcomputer.com/news/security/password-reset-calls-are-costing-your-org-big-money/?utm_source=thehackernews.com&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=guest-post) of IT help desk calls are related to password resets, with each reset [costing around $70 in labor](https://www.forrester.com/report/best-practices-selecting-deploying-and-managing-enterprise-password-managers/RES139333) according to Forrester. This adds up, especially when users frequently forget their passwords after being forced to create new ones.

Some organizations may therefore be tempted to force end users into creating one very strong password and then setting the passwords to 'never expire' in order to cut down on IT burden and reset costs.

## What are the risks with 'never expire' passwords?

Having a strong password and never changing it might give someone a false sense of security. A strong password isn't immune to threats; it can be vulnerable to phishing schemes, data breaches, or other types of cyber incidents without the user realizing it. The [Specops Breached Password Report](https://specopssoft.com/our-resources/most-common-passwords/?utm_source=thehackernews.com&utm_medium=referral&utm_campaign=na_thehackernews&utm_content=guest-post) found 83% of passwords that were compromised met the regulatory standards for length and complexity.

An organization might have a strong password policy where every end user is forced to create a strong password that's resistant to brute force attacks. But what happens if the employee decides to reuse their password for their Facebook, Netflix, and all other personal applications too? The risk of the password being compromised increases a lot, regardless of the internal security measures the organization has in place. [A survey by LastPass](https://www.darkreading.com/vulnerabilities-threats/password-reuse-abounds-new-survey-shows) found 91% of end users understood the risk of password reuse – but 59% did it anyway.

Another risk with 'never expire' passwords is that an attacker could use a set of compromised credentials for a long period of time. The Ponemon Institute found that it typically takes an organization about [207 days to identify a breach](https://www.ibm.com/reports/data-breach-action-guide). While mandating password expiration could be beneficial here, it's likely that an attacker would have already achieved their objectives by the time the password expires. Consequently, NIST and other guidelines advise organizations to only set passwords to never expire if they have mechanisms to identify compromised accounts.

## How to detect compromised passwords

Organizations must adopt a comprehensive password strategy that goes beyond regular expiry. This includes guiding users to [create strong passphrases](https://specopssoft.com/blog/passp...