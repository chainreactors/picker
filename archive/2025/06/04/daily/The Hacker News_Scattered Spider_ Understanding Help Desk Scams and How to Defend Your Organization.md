---
title: Scattered Spider: Understanding Help Desk Scams and How to Defend Your Organization
url: https://thehackernews.com/2025/06/scattered-spider-understanding-help.html
source: The Hacker News
date: 2025-06-04
fetch_date: 2025-10-06T22:56:43.008169
---

# Scattered Spider: Understanding Help Desk Scams and How to Defend Your Organization

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

# [Scattered Spider: Understanding Help Desk Scams and How to Defend Your Organization](https://thehackernews.com/2025/06/scattered-spider-understanding-help.html)

**Jun 03, 2025**The Hacker NewsIdentity Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjc15iZeRVqbNA9wEoCUqiFNDQw9YQ24wji3kmymfoO671lPOxc9U0Xb_1nw_Hy0Vu6WHRHzgQ3WdeKXWZZj989lnbUnwF_cL66U9WyMk4-t_pNSPZVHo-GmpGMeeBuxEfVQA2O4GXhzoUGRoE9QxiytCBL9JjwlmXiDddWR6Bc-UCJ1wrA9FqMHAtQdk/s790-rw-e365/main.png)

In the wake of high-profile attacks on UK retailers Marks & Spencer and Co-op, Scattered Spider has been all over the media, with coverage spilling over into the mainstream news due to the severity of the disruption caused — currently looking like hundreds of millions in lost profits for M&S alone.

This coverage is extremely valuable for the cybersecurity community as it raises awareness of the battles that security teams are fighting every day. But it's also created a lot of noise that can make it tricky to understand the big picture.

The headline story from the recent campaign against UK retailers is the use of help desk scams. This typically involves the attacker calling up a company's help desk with some level of information — at minimum, PII that allows them to impersonate their victim, and sometimes a password, leaning heavily on their native English-speaking abilities to trick the help desk operator into giving them access to a user account.

## Help Desk Scams 101

The goal of a help desk scam is to get the help desk operator to reset the credentials and/or MFA used to access an account so the attacker can take control of it. They'll use a variety of backstories and tactics to get that done, but most of the time it's as simple as saying "I've got a new phone, can you remove my existing MFA and allow me to enroll a new one?"

From there, the attacker is then sent an MFA reset link via email or SMS. Usually, this would be sent to, for example, a number on file — but at this point, the attacker has already established trust and bypassed the help desk process to a degree. So asking "Can you send it to this email address" or "I've actually got a new number too, can you send it to…" gets this sent directly to the attacker.

At this point, it's simply a case of using the self-service password reset functionality for Okta or Entra (which you can get around because you now have the MFA factor to verify yourself), and *voila*, the attacker has taken control of the account.

And the best part? Most help desks have the same process for every account — it doesn't matter who you're impersonating or which account you're trying to reset. So, attackers are specifically targeting accounts likely to have top-tier admin privileges — meaning once they get in, progressing the attack is trivial, and much of the typical privilege escalation and lateral movement is removed from the attack path.

So, help desk scams have proved to be a reliable way of bypassing MFA and achieving account takeover — the foothold from which to launch the rest of an attack, such as stealing data, deploying ransomware, etc.

## Don't be fooled — this isn't a new development

But something that's not quite coming across in the reporting is that Scattered Spider has been doing this successfully since 2022, with the M&S and Co-op attacks merely the tip of the iceberg. Vishing (calling a user to get them to give up their MFA code) has been a part of their toolkit since the beginning, with the early attacks on Twilio, LastPass, Riot Games, and Coinbase involving some form of voice-based social engineering.

Notably, the high-profile attacks on Caesars, MGM Resorts, and Transport for London all involved calling a help desk to reset credentials as the initial access vector.

* **Caesars** in August 2023 where hackers impersonated an IT user and convinced an outsourced help desk to reset credentials, after which the attacker stole the customer loyalty program database and secured a $15m ransom payment.
* **MGM Resorts** in September 2023, where the hacker used LinkedIn information to impersonate an employee and reset the employee's credentials, resulting in a 6TB data theft. After MGM refused to pay, the attack eventually resulted in a 36-hour outage, a $100m hit, and a class-action lawsuit settled for $45m.
* **Transport for London** in September 2024 resulted in 5,000 users' bank details being exposed, 30,000 staff required to attend in-person appointments to verify their identities and reset passwords, and significant disruption to online services lasting for months.

So not only have Scattered Spider (and other threat groups) been using these techniques for some time, but the severity and impact of these attacks have been ramping up.

## Avoiding help desk gotchas

There's lots of advice for securing help desks being circulated, but much of the advice still results in a process that is either phishable or difficult to implement.

Ultimately, organizations need to be prepared to introduce friction to their help desk process and either delay or deny requests in situations where there's significant risk. So, for example, having a process for MFA reset that recognizes the risk associated with resetting a high-privileged account:

* Require multi-party approval/escalation for admin-level account resets
* Require in-person verification if the process can't be followed remotely
* Freeze self-service resets when suspicious behavior is encountered (this would require some kind of internal process and awareness training to raise the alarm if an attack is suspected)

And watch out for these gotchas:

* If you receive a call, good practice is to terminate the call and dial the number on file for the employee. But, in a world of SIM swapping, this isn't a foolproof solution — you could just be re-dialing the attacker.
* If your solution is to get the employee on camera, increasingly sophisticated deepfakes can thwart this approach.

But, help desks are a...