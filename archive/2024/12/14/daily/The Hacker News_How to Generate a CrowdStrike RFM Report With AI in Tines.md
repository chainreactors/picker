---
title: How to Generate a CrowdStrike RFM Report With AI in Tines
url: https://thehackernews.com/2024/12/how-to-generate-crowdstrike-rfm-report.html
source: The Hacker News
date: 2024-12-14
fetch_date: 2025-10-06T19:43:42.278249
---

# How to Generate a CrowdStrike RFM Report With AI in Tines

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

# [How to Generate a CrowdStrike RFM Report With AI in Tines](https://thehackernews.com/2024/12/how-to-generate-crowdstrike-rfm-report.html)

**Dec 13, 2024**The Hacker NewsAutomation / Endpoint Security

[![CrowdStrike RFM Report](data:image/png;base64... "CrowdStrike RFM Report")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6d0JsQ7LopWZcrpDdThb18DfRcFRe12dFj-0y-tsN8AmD-2wgLL3KLa6TfUZN911KOhiobWpGlIUjNtIuRYJS8HNNpNP6Ikjky8daRUJMgEAdXs2MJ6U5v5JKL35oVSJOjHsK_qPLAUFa8nrlbICE-dZzSRpRDSU8mQiK2DYtHMFiDB1sGk3USRrGq0c/s790-rw-e365/main.png)

Run by the team at orchestration, AI, and automation platform Tines, the Tines library contains pre-built workflows shared by real security practitioners from across the community, all of which are free to import and deploy via the [Community Edition](https://tines.com/community-edition?utm_source=paid&utm_medium=media&utm_campaign=thehackernews-organicarticle-dec13) of the platform.

Their bi-annual "You Did What with Tines?!" competition highlights some of the most interesting workflows submitted by their users, many of which demonstrate practical applications of large language models (LLMs) to address complex challenges in security operations.

One recent winner is a workflow designed to automate CrowdStrike RFM reporting. Developed by Tom Power, a security analyst at The University of British Columbia, it uses orchestration, AI and automation to reduce the time spent on manual reporting.

Here, we'll share an overview of the workflow, plus a step-by-step guide for getting it up and running.

## The problem - time-consuming reporting

The workflow's builder, Tom Power, explains, "The CrowdStrike Falcon sensor goes into Reduced Functionality Mode (RFM), usually because the operating system (OS) or kernel version is too old or too new for the sensor to support in kernel mode. Every week, SecOps would log into the Falcon console, and filter the host management console for endpoints in RFM for the last week. We would generate the report and download it."

This process provided critical data for identifying kernel updates causing RFM, particularly for Linux endpoints. However, it required the team to manually check whether CrowdStrike had released a new sensor version compatible with the latest kernel updates.

"The entire process took about 30 minutes each week," Tom adds. "Over the course of a year, that added up to more than 25 hours of time we could have spent on other cybersecurity priorities."

## The solution - automated RFM reporting with AI

[![CrowdStrike RFM Report](data:image/png;base64... "CrowdStrike RFM Report")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi27WPTa6oP-owJyz4JciS9lWFXd7R6rD2ny-O7nCvTv6s9bCH67XKT-jn5alQJew_9hGb0BfJLihCuKARK3EpaHSjeIExOO0d26VpmrhH2stU2FXHiLQbs-UeUI6UET3M5Wz1x7LUyJ8I4darmAN07xtNb1_Q1J7X3pg33c23GzOUHwZZ-P3W-z2Jksv4/s790-rw-e365/1.png)

Tom's workflow automates the tracking and reporting of Falcon Sensor RFM across hosts. By leveraging Tines' AI-driven Automatic Mode, it generates custom code to streamline report creation. The workflow not only produces regular, consistent reports but also enables management to monitor trends in RFM occurrences, supporting proactive system health management and faster decision-making.

The automated workflow eliminates the need for manual reporting by allowing analysts to submit requests via a simple web form. Within minutes, the workflow retrieves data, processes it, and delivers an actionable email report, complete with detailed insights and a CSV attachment.

#### **Example output:**

Here's a sample of the auto-generated email and report received by the team:

[![CrowdStrike RFM Report](data:image/png;base64... "CrowdStrike RFM Report")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgixw1hSbhxGIOqz50bIyJORX4ckduMlZ4GVlI7NdvNqCYPMQ6bpE_GmOaJM7MkRNWAyqVzfr6FWGlY_JwClvZB71mUhgU9HW3X_G24NGxSXwpaOefN7bclBskvkQSupOPchXv0XXARD4pb-YUealIyitQQhToBxYz2kdMQKDnt7yhgYnUKdos-j_qTSYk/s790-rw-e365/2.png)

[![CrowdStrike RFM Report](data:image/png;base64... "CrowdStrike RFM Report")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZ-xUv9powPEiLr6NAknXiSDHLjh-9ObllQGd822aAj95UscHsw-H8rbyWRaAheZdZ22hzNpMEbrGN-zbWSbfPoE-oB24UKKHpiQiCgGBXa1nmS6-RCrGN1CJpg3Y-FJYWu6Ktpn2Cytf63UTKl7rgNGmXMLM8Rb9ImY5RsYojXDDUMwFwIz9vCxhZjJw/s790-rw-e365/3.png)

Here are some of the key benefits of using this workflow:

* Frees analysts to focus on high-priority cybersecurity tasks.
* Reduces manual effort and the potential for human error.
* Delivers consistent, reliable reports for improved productivity.
* Enhances decision-making by providing real-time insights.
* Boosts morale by removing a tedious and repetitive task.

[![CrowdStrike RFM Report](data:image/png;base64... "CrowdStrike RFM Report")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1EXuXwuPfDRs14oJFc00WgnJUu28dmp9ABulEYqTaXTwuEkHkwOEmfvifoH1fLm-ZzghYMI_W8u_oD38BMQ38PnV5F0UZR6FR5DGFNrgaLxuCjKrjv29KCCmqzr8nNy4AkuoX7MOPZCSueEAFBfQpNExZemoCX_RSs9w8cdl4N51XphlYT6wnjkQKOwA/s790-rw-e365/4.png)

## Workflow overview

Tools used:

* Tines - a workflow orchestration, AI and automation platform that's popular with security teams. It's possible to use the free Community Edition of Tines to build and run this workflow if you don't have a paid account. AI must be enabled on your tenant.
* CrowdStrike - endpoint detection and response (EDR) platform. This workflow integrates with CrowdStrike Falcon's API to retrieve data about endpoints in Reduced Functionality Mode (RFM). While Falcon provides robust endpoint visibility, it lacks native automation for recurring RFM reports.

The workflow is initiated when a web form is submitted, triggering the process to generate CrowdStrike RFM reports.

The first action retrieves a list of device IDs from CrowdStrike Falcon's API. If the list is larger than what CrowdStrike returns in the first batch, multiple calls are made to paginate through the full list.

Once all the device details are retrieved, the...