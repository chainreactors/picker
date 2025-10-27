---
title: Not Your Old ActiveState: Introducing our End-to-End OS Platform
url: https://thehackernews.com/2024/12/not-your-old-activestate-introducing.html
source: The Hacker News
date: 2024-12-19
fetch_date: 2025-10-06T20:00:43.180211
---

# Not Your Old ActiveState: Introducing our End-to-End OS Platform

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

# [Not Your Old ActiveState: Introducing our End-to-End OS Platform](https://thehackernews.com/2024/12/not-your-old-activestate-introducing.html)

**Dec 18, 2024**The Hacker NewsSoftware Security / DevSecOps

[![End-to-End OS Platform](data:image/png;base64... "End-to-End OS Platform")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwoGtVmQHeep3ZfuaHjv8ABSWY67TcjsFxBdTO_7BcvRareCrjXtNgHpM_nWssTQ-kriZbsZ3PIpasp1BI__plq81JEVmXClBewPpc4nxg3Jw1oAwhKJNFsLy5Capw5KZlvbXtV1fHA__kJNqOrFc1x3wBpoNtfUtTW8VTeOk7tR3KSA7ru0VE8qVCsNE/s790-rw-e365/activestate.png)

Having been at ActiveState for nearly eight years, I've seen many iterations of our product. However, one thing has stayed true over the years: Our commitment to the open source community and companies using open source in their code.

ActiveState has been helping enterprises manage open source for over a decade. In the early days, open source was in its infancy. We focused mainly on the developer case, helping to get open source on platforms like Windows.

Over time, our focus shifted from helping companies run open source to supporting enterprises managing open source when the community wasn't producing it in the way they needed it. We began managing builds at scale, and supporting enterprises in understanding what open source they're using and if it's compliant and safe.

Managing open source at scale in a large organization can be complex. To help companies overcome this and bring structure to their open source DevSecOps practice, we're unveiling our end-to-end platform to help manage open source complexity.

## The current state of open source and supply chain security

It's inevitable that with the soaring popularity of open source comes an influx of security issues. Open source adoption in modern software applications is significant. Over [90% of applications contain open source components](https://www.sonatype.com/blog/the-transformation-of-open-source-lessons-from-the-past-decade#:~:text=The%20rise%20of%20open%20source%3A%20A%20double%2Dedged%20sword&text=Today%2C%20open%20source%20components%20make,downloads%20to%20exceed%206.6%20trillion.). Open source is now at the core of how we produce software, and we've hit a point where it's the primary vector for bad actors to get access to nearly any piece of software.

Attacks have been around forever, but there's been an increasing number of incidents in recent years. The pandemic surfaced new opportunities for bad actors. When people were using their own home networks and VPNs with less stringent security measures, it started to allow for more risk. Despite return to office efforts, many IT workers are still at home, so these opportunities still exist.

Additionally, many enterprises don't have processes in place for how they choose and procure open source software, so devs blindly find and incorporate it. The challenge is companies then don't know where open source code is coming from, who built it, and with what intentions. This creates multiple opportunities for attacks to happen throughout the open source software supply chain process.

Open source is an open ecosystem, which makes it vulnerable 'by design.' It needs to be as open as possible to not hinder authors from contributing, but there's a real challenge of keeping it secure throughout the entire development process.

Risks don't just exist when you're importing. If your build service isn't secure when you start building, you can be at risk. Many of the most recent attacks we've seen are open source software supply chain attacks not vulnerabilities. This requires a whole new approach to open source security.

## Reimagining the open source management process

At ActiveState, it's our mission to bring rigor to the open source supply chain. Companies can get better visibility and control over their open source code across DevSecOps by focusing on a four-step management cycle.

### Step 1: Discovery

Before you can even begin to remediate vulnerabilities, you need to know what you're using in your code. It's important to take inventory of all the open source that's running within your organization. An artifact of this effort could look like a dashboard.

### Step 2: Prioritization

Once you have the dashboard, you can start analyzing for vulnerabilities and dependencies and prioritize which to focus on first. Understanding where the risks are in your codebase and triaging them will help you make informed decisions about next steps.

### Step 3: Upgrading and curating

Now comes the remediation and change management phase. You'll want to establish governance and policies for managing open source across your org to keep everyone aligned across functions and teams.

You should also closely manage what dependencies are used in both production and development environments to minimize risk.

In our platform, we maintain a large immutable catalogue of open source software. We keep a consistent, reproducible record of around 50 million version components, and we are constantly adding to it. It helps our users make sure they can always get back to reproducible builds. It means you can curate the entire internet for open source while trusting it's secure.

### Step 4: Build and deploy

The build and deploy phase involves incorporating secure and safe open source components into your code - because you're not really remedied and secure until the fixes are deployed. At ActiveState, we build and track everything. From when we ingest source code to when we build it into a secure cluster. We then give it to you in a variety of formats to be deployed depending on your needs. We're the only solution (that we know of) that truly helps companies remediate and deploy, completing the full lifecycle of ensuring software supply chain security.

## A new ActiveState: tackling open source security challenges head-on

Through our work in open source over the past decade, we've discovered there's a gap between the passionate communities producing open source and the enterprises that ...