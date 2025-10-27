---
title: Last Years Open Source - Tomorrow's Vulnerabilities
url: https://thehackernews.com/2022/11/last-years-open-source-tomorrows.html
source: The Hacker News
date: 2022-11-02
fetch_date: 2025-10-03T21:34:56.962444
---

# Last Years Open Source - Tomorrow's Vulnerabilities

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

# [Last Years Open Source - Tomorrow's Vulnerabilities](https://thehackernews.com/2022/11/last-years-open-source-tomorrows.html)

**Nov 01, 2022**The Hacker News

[![Open Source Vulnerabilities](data:image/png;base64... "Open Source Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHCMnqhwqPtQNSBXsZfmX7LEVj5u6v9J0m0PEJfwCxouhiIhao2Vs5MVncWuJ98NuxpWT7NguZoYl9dp9C4CsQNISQjl1ik3-HeBH_0aR7VPGsot16xib61mh4OHw6O8pbWPihBxdOnhJUpQ7H8hm9OS6DpuBY_aUAr7qYoai0rNSCjr6TtjWFr_JO/s790-rw-e365/open-source-hacking.jpg)

Linus Torvalds, the creator of Linux and Git, has his own law in software development, and it goes like this: "*given enough eyeballs, all bugs are shallow*." This phrase puts the finger on the very principle of open source: the more, the merrier - if the code is easily available for anyone and everyone to fix bugs, it's pretty safe. But is it? Or is the saying "all bugs are shallow" only true for *shallow* bugs and not ones that lie deeper? It turns out that security flaws in open source can be harder to find than we thought. Emil Wåreus, Head of R&D at [Debricked](https://debricked.com), took it upon himself to look deeper into the community's performance. As the data scientist he is, he, of course, asked the data: *how good is the open source community at finding vulnerabilities in a timely manner*?

## **The thrill of the (vulnerability) hunt**

Finding open source vulnerabilities is typically done by the maintainers of the open source project, users, auditors, or external security researchers. But despite these great code-archaeologists helping secure our world, the community still struggles to find security flaws.

On average, it takes *over 800 days* to discover a security flaw in open source projects. For instance, the infamous Log4shell (CVE-2021-44228) vulnerability was undiscovered for a whopping 2649 days.

[![Open Source Vulnerabilities](data:image/png;base64... "Open Source Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDV6UV2i1t5HF7EMQs8N5wywO9YTWCb3M_uB1ZqwVnkPDzieuVEda7tkHRQiw41mhCnz3SBVnaReHEMH2fUQNCCC_Z4S-6KYh_KH5nY-f0od8kkYPj9BWh2JjUSdnMcPRqovKz6tSxPy6tCA2_5c-bO52_9kby2Ci3hqk0g9VcmKTnSJUmn4KFxJgW/s790-rw-e365/FLAWS.jpg)

The analysis shows that 74% of security flaws are actually undiscovered for at least one year! Java and Ruby seem to have the most challenges here, as it takes the community more than 1000 days to find and disclose vulnerabilities. Our [white] hats go off to the PHP/Composer community, which slightly outperforms the others.

## **The needle in a techstack**

Other interesting factors are that some of the different weakness types (CWE) seem to be harder to find and disclose, which actually contradicts Linus's law. The weakness types CWE-400 (Uncontrolled Resource Consumption) and CWE-502 (Deserialization of Untrusted Data) typically aren't localized to a single function or may appear as intended logic in the application. In other words, it can't be considered "a shallow bug."

It also seems that the developer community is a bit better at finding CWE-20 (Improper Input Validation), where the flaw most of the time is just a few lines of code in a single function.

[![Open Source Vulnerabilities](data:image/png;base64... "Open Source Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMcHcgVAMCZdOLqkgBI2vwxfxloDUpyM00TN6hWNXm2XuP6xMEA6rxvm6SSzpLbxnWheflWn2NzzpG28KssHYhTkxqvgPCreYfJUptqQ466Jvgjav1oC_3pRbCDqLGVNtbUmUGhmdO_mv8yRBolaXWeQr91wJXBpvD3XjYa4h945ZbgYI8puChOJYh/s790-rw-e365/bugs.jpg)

## **Solve vulnerabilities with powerful remediation**

Why does this matter? As consumers of open source, and that's about every company in the whole world, the problem of vulnerabilities in open source is an important one. The data tells us that we can't fully trust Linus' Law - not because open source is less secure than other software, but because **not all bugs are shallow**.

Luckily, there are powerful tools to perform at-scale analysis of a lot of open source projects at once. There have been [[white knight hackers disclose 1000's](https://www.youtube.com/watch?v=WkdzWiNKzt8)] of vulnerabilities at once using these methods. It would be naive to not assume that ill-minded organizations and individuals do the same. As an ecosystem that lays the foundation for our software-centric world, the community must improve its ability to find, disclose, and fix security flaws in open source significantly.

Last year, [Google committed $10 billion](https://blog.google/technology/safety-security/why-were-committing-10-billion-to-advance-cybersecurity/) to an open source fund to help secure open source with a specific curator role to work alongside the maintainers with specific security efforts.

Furthermore, Debricked helps companies make these vulnerabilities actionable by scanning all your software, every branch, every push, and every commit, for new (open source) vulnerabilities. Debricked even continuously scans all your old commits for every new vulnerability, to make sure they bring up-to-date, accurate, and actionable intelligence on the open source you consume. Debricked even helps developers fix your security flaws with automated pull requests that won't cause dependency hell; pretty neat!

## The truth lies in the data

So, knowing all this, what is the best way to protect your project or company against open source vulnerabilities? As we've seen in the case of Log4j and Spring4shell as well as the numbers, we can never really trust that the community will find and fix all risks. There's a good chance that there are lots and lots of undiscovered and undisclosed vulnerabilities in your code today, and there's not much you can do about it.

According to Debricked, the best way to mitigate this is by implementing continuous vulnerability scanning to your SDLC. By automatically scanning at every push of code, in combination with the machine learning-powered [vulnerability database](https://debricked.com/vulnerability-databa...