---
title: Cyber Story Time: The Boy Who Cried "Secure!"
url: https://thehackernews.com/2024/11/cyber-story-time-boy-who-cried-secure.html
source: The Hacker News
date: 2024-11-22
fetch_date: 2025-10-06T19:20:20.441511
---

# Cyber Story Time: The Boy Who Cried "Secure!"

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

# [Cyber Story Time: The Boy Who Cried "Secure!"](https://thehackernews.com/2024/11/cyber-story-time-boy-who-cried-secure.html)

**Nov 21, 2024**The Hacker NewsThreat Detection / Pentesting

[![Cyber Story Time](data:image/png;base64... "Cyber Story Time")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiRAINlv9vlVheY9hpFbDMOg6zInMZanuLRxb0GDmLAhkBUC3bGcnltkWqiaDJuxEEwvfMD3-G5uplcnVuVdquF9kD4UvvMnIZqyTDMy_yCYP4b9XqNsMic4Jo0Zi023Hrqpx83MpdBaNxmzuSaAESSJm-YZhpfhr8cz7P7k7HlDpXUKF3Vmpm88Xgvwnk/s790-rw-e365/penter.png)

As a relatively new security category, many security operators and executives I've met have asked us "What are these Automated Security Validation (ASV) tools?" We've covered that pretty extensively in the past, so today, instead of covering the "*What is ASV?"* I wanted to address the "*Why ASV?"* question. In this article, we'll cover some common use cases and misconceptions of how people misuse and misunderstand ASV tools daily (because that's a lot more fun). To kick things off, there's no place to start like the beginning.

Automated security validation tools are designed to provide continuous, real-time assessment of an organization's cybersecurity defenses. These tools are continuous and use exploitation to validate defenses like EDR, NDR, and WAFs. They're more in-depth than vulnerability scanners because they use tactics and techniques that you'll see in manual penetration tests. Vulnerability scanners won't relay hashes or combine vulnerabilities to further attacks, which is where ASVs shine. Their purpose is in the name: to "validate" defenses. When issues or gaps are addressed, we need to validate that they really are fixed.

## **Why is ASV needed?**

And that brings us to the *showing* part of this, and our teacher for this is Aesop, the Greek storyteller who lived around 600 BC. He wrote a story called The Boy Who Cried Wolf that I know you've heard before, but I'll share it again in case you need a refresher:

The fable tells the story of a shepherd boy who keeps fooling the village into believing that he's seen a wolf. Whether he was motivated by attention, fear, or terrible eyesight? I don't know. The point is that he repeatedly waves his hands in the air and cries "Wolf!" when there's no wolf in sight. He does this so often that he desensitizes the townspeople to his calls so that when there really is a wolf, the town doesn't believe him, and the shepherd boy gets eaten. It's a very heartwarming story, like most Greek tales.

## **The Sys Admin Who Cried Remediated**

In modern cybersecurity, the false positive is the equivalent of "crying wolf.". A common practice issue, where threats get alerted despite not having any chance of being exploited. But let's rescope this story because the only thing worse than a false positive, is a false negative.

Imagine, if instead of "crying wolf" when there was no wolf, the boy said "all's clear," never realizing the wolf was hiding among the sheep This is a false negative, not getting alerted when a threat is prevalent. Once the boy had set up the traps, he was convinced that there was no longer a threat, but he didn't validate that the traps actually worked to block the wolf. So the rescoped version of Crying Wolf went something like this:

"Ah, I figured we had a wolf lurking around. I'll take care of it," says the boy.

So the shepherd follows the instructions: He sets up wolf traps, buys a wolf-killing security tool, he even puts in a Group Policy Object (GPO) to get that wolf out of his field. Then he goes to the town proud of his work.

"They told me there was a wolf, so I took care of it," he tells his shepherd friends while having a beer at the local tavern.

Meanwhile, the reality is that the wolf is able to dodge the traps, saunter past the misconfigured wolf-killing tool, and set new policies at the application level so he doesn't care about the GPO. He captures a set of the town's Domain Admin (DA) credentials, relays them, declares himself mayor, and then holds the town to a ransomware attack. Before they know it, the town owes 2 Bitcoin to some wolf, or else they'll lose their sheep and a truckload of PII.

What the shepherd boy did is called a false negative. He thought there was no wolf, living in a false sense of security when the threat was never truly neutralized. And he's now trending on Twitter for all the wrong reasons.

## **Real-life scenario time!**

Wolves are rarely a threat to information security, but do you know who is? That bad actor with a backdoor, a foothold in your network, listening for credentials. All of it is made possible through their very good friends, legacy name resolution protocols.

Name resolution poisoning attacks are a tough bug to squash as far as remediation goes. If your DNS is configured improperly (which is surprisingly common) and you haven't disabled good ol' LLMNR, NetBIOS NS, and mDNS protocols used in man-in-the-middle attacks via GPO, start-up scripts, or your own special sauce, then you might be in some trouble. And where the wolf might have helped himself to a glass of milk—your attacker will be helping himself to sensitive data.

If an attacker sniffs credentials and you don't have SMB signing enabled *and* required on all your domain-joined machines (if you're wondering if you do, then you probably don't) then that attacker may relay the hash. This will gain access to the domain-joined machine without even cracking the captured hash.

Yikes!

Now your friendly village pentester finds this issue and tells the sys admin, AKA our shepherd, to do one of the aforementioned fixes to prevent this whole string of attacks. He remediates this to the best of their ability. They put in the GPOs, they get the fancy tools, they do ALL the things. But has the dead wolf been seen? Do we KNOW the threat has been fixed?

Through a montage-worthy set of corner cases, the attacker can still get in, because there will almost always be corner cases. You'll have a Linux server that isn't domain-joined, an a...