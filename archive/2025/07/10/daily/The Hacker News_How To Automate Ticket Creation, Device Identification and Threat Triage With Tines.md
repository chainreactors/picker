---
title: How To Automate Ticket Creation, Device Identification and Threat Triage With Tines
url: https://thehackernews.com/2025/07/how-to-automate-ticket-creation-device.html
source: The Hacker News
date: 2025-07-10
fetch_date: 2025-10-06T23:54:48.987764
---

# How To Automate Ticket Creation, Device Identification and Threat Triage With Tines

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

# [How To Automate Ticket Creation, Device Identification and Threat Triage With Tines](https://thehackernews.com/2025/07/how-to-automate-ticket-creation-device.html)

**Jul 09, 2025**The Hacker NewsSecurity Operations / Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX3KbLJ-K8IdOF3TNcFC2SbxQjigss1W8huUT_3v0DjBeFjJpA69VLWJ9sqAKUmxOMNEAeO-9itP3zZ8BgoI8dNr1Uh-8SLL88H86FmWJvu16ryiT0iBU0gpgozJocJfVuI-_dZP3wPwj6pVmMcZdhj4LR1Rpw3fAXNxRC9kAjKbRWkobpPYBKXVjytro/s790-rw-e365/tines-main.png)

Run by the team at workflow orchestration and AI platform Tines, the Tines library features over 1,000 pre-built workflows shared by security practitioners from across the community - all free to import and deploy through the platform's [Community Edition.](https://login.tines.com/saml_idp/signup?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=organicarticle-May2)

A recent standout is a workflow that handles malware alerts with CrowdStrike, Oomnitza, GitHub, and PagerDuty. Developed by Lucas Cantor at Intercom, the creators of [fin.ai](https://fin.ai/), the workflow makes it easier to determine the severity of a security alert and escalate it seamlessly, depending on the device owner's response. "It's a great way to reduce noise and add context to security issues that are added on our endpoints as well," Lucas explains.

In this guide, we'll share an overview of the workflow, plus step-by-step instructions for getting it up and running.

## The problem - lack of integration between security tools

For security teams, responding to malware threats, analyzing their severity, and identifying the device owner so they can be contacted to resolve the threat, can take up a lot of time.

From a workflow perspective, teams often have to:

* Manually respond to CrowdStrike events
* Enrich the alert with additional metadata
* Document and alert the device owner in Slack
* Notify on call teams via PagerDuty

Going through this process manually can result in delays and increase the chances of human error.

## The solution - automated ticket creation, device identification, and threat triage

Lucas's prebuilt workflow automates the process of taking the malware alert and creating the case - while crucially notifying the device owner and the on-call team. This workflow helps security teams accurately identify the level of threat faster by:

* Detecting new alerts from Crowdstrike
* Identifying and notifying the device owner
* Escalating critical issues

The result is streamlined response to malware security alerts that ensures they are dealt with quickly, no matter what the severity.

Key benefits of this workflow:

* Reduced remediation time
* Device owner is kept informed
* Clear remediation and escalation pathways
* Centralized management system

## Workflow overview

### **Tools used:**

* Tines - workflow orchestration and AI platform (free Community Edition available)
* Crowdstrike - threat intelligence and EDR platform
* Oomnitza - IT asset management platform
* Github - developer platform
* PagerDuty - incident management platform
* Slack – team collaboration platform

### **How it works**

#### **Part 1**

* Get a security alert from CrowdStrike
* Find the device that the alert was triggered and look up its details
* Create a ticket in GitHub for the alert and raise the issue in a Slack message
* If the device is owned by a user and it is a low priority,
  + Send the owner a message requesting escalation
* If the device is owned by a user and it is a high priority,
  + Create a PagerDuty Event to notify the on-call analyst
  + Informing the owner of the ongoing issue

#### **Part 2**

* Get a user interaction with the Slack message
* Enrich the GitHub issue with the users response
* If the owner escalates the issue
  + Create a PagerDuty Event to notify the on-call analyst

## Configuring the workflow - step-by-step guide

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAm3VtJku2_xjOgn9QZdpH3BOTahrlHhA7NAuSp6wtvhbzCnoJOQK0QBYqE5Nex_cgJsxowzN7kLIGpE-fKlWnKZnb49_ujHgoNP5uYM-uLK4YFKEBrTno2_M4JFesnV-DE9sJShVkyfLhEz7VLMY636TUv9BjCaHXGY0_km9o_QKJAPJIAQvBdW1JaN0/s790-rw-e365/image2.png)

**1.** Log into Tines or create a new account.

**2.** Navigate to the [pre-built workflow in the library.](https://www.tines.com/library/stories/1213236/?name=handle-malware-alerts-with-crowdstrike-oomnitza-github-and-pagerduty&redirected-from=%2Flibrary%2Fcommunity%2F%3Fview%3Dall&sort=popularity&s=Luc) Select import. This should take you straight to your new pre-built workflow.

**3.** Set up your credentials

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixZWVuAXw65CddqangZ97UIIJn5Wm7IaOwVo1RNo2e6QLPYEPreUNZ8DTNR3XcCw-xuhd8cSUva30LMj_um93MOCgogGPUzMrGPT13-1PNhSWFA6I7-ohARLpsGzqe0D13nuNU7RilwlhIJyWpYr0a19oQ2x_k3PqaW3BzseQcu2kGNMiiPyUTb20OF7w/s790-rw-e365/image1.png)

You'll need five credentials added to your Tines tenant:

* CrowdStrike
* Oomnitza
* Github
* PagerDuty
* Slack

Note that similar services to the ones listed above can also be used, with some adjustments to the workflow.

From the credentials page, select New credential, scroll down to the relevant credential and complete the required fields. Follow the CrowdStrike, Oomnitza, Github, PagerDuty, and Slack credential guides at explained.tines.com if you need help.

**4.** Configure your actions.

* Set your environment variables. This includes your:
  + Slack IT channel alerting webhook (`slack\_channel\_webhook\_urls\_prod`)
  + CrowdStrike/GitHub severity priority mapping (`crowdstrike\_to\_github\_priority\_map`)
* Configure CrowdStrike to alert the New CrowdStrike Detection webhook when a detection is created
* Configure your SlackBot interactivity URL to the Receive Slack Button Push webhook

**5.** Test the workflow.

**6.** Publish and operationalize

Once tested, publish the workflow.

If you'd like to test this workflow, you can sign up for a [free T...