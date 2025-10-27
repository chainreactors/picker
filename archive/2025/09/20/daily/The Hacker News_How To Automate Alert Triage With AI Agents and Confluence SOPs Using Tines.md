---
title: How To Automate Alert Triage With AI Agents and Confluence SOPs Using Tines
url: https://thehackernews.com/2025/09/how-to-automate-alert-triage-with-ai.html
source: The Hacker News
date: 2025-09-20
fetch_date: 2025-10-02T20:27:23.412809
---

# How To Automate Alert Triage With AI Agents and Confluence SOPs Using Tines

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

# [How To Automate Alert Triage With AI Agents and Confluence SOPs Using Tines](https://thehackernews.com/2025/09/how-to-automate-alert-triage-with-ai.html)

**Sep 19, 2025**The Hacker NewsAI Automation / Security Operations

[![AI Agents and Confluence SOPs Using Tines](data:image/png;base64... "AI Agents and Confluence SOPs Using Tines")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJXsjGv0y0H3FOuoYZQkkLtvp92R9RT19QuTlrFmp2m_bBVodd1CdpzsoH2vmjvz9ewJ5HDYA96qcr4FpnudXI_eVzCSk9kXomkkrvBSJmaV0q2Ojsv3tTASghV2lFjkwPJ9wsrGvr089zH7MjWq4uqSEeg_Nuzq7u5kKo3l2ffC6jl_v-Qp1CMtGdgbU/s790-rw-e365/main-a.jpg)

Run by the team at workflow orchestration and AI platform Tines, the Tines library features over 1,000 pre-built workflows shared by security practitioners from across the community - all free to import and deploy through the platform's [Community Edition.](https://login.tines.com/saml_idp/signup?utm_source=TheHackerNews&utm_medium=paid_media&utm_content=article-1909)

The workflow we are highlighting streamlines security alert handling by automatically identifying and executing the appropriate Standard Operating Procedures (SOPs) from Confluence. When an alert triggers, AI agents analyze it, locate relevant SOPs, and perform required remediation steps - all while keeping the on-call team informed via Slack.

It was created by Michael Tolan, Security Researcher L2 at Tines, and Peter Wrenn, Senior Solutions Engineer at Tines.

In this guide, we'll share an overview of the workflow, plus step-by-step instructions for getting it up and running.

## The problem - manual alert triage and SOP execution

For security teams, responding to alerts efficiently requires quickly identifying the threat type, locating the appropriate SOP, and executing the required remediation steps.

From a workflow perspective, teams often have to:

* Manually analyze incoming security alerts
* Search through Confluence for relevant SOPs
* Document findings and actions in case management systems
* Execute multiple remediation steps across different security tools
* Update the case management system again after the fact
* Notify stakeholders about incidents and actions taken

This manual process is time-consuming, prone to human error, and can lead to inconsistent handling of similar alerts.

## The solution - AI-powered alert triage with automated SOP execution

This prebuilt workflow automates the entire alert triage process by leveraging AI agents and Confluence SOPs. The workflow helps security teams respond faster and more consistently by:

* Using AI to analyze and classify incoming alerts
* Automatically locating relevant SOPs in Confluence
* Creating structured case records for tracking
* Deploying a second AI agent (subagent) to execute remediation steps
* Documenting all actions and notifying the on-call team via Slack

The result is a streamlined response to security alerts that ensures consistent handling according to established procedures.

## Key benefits of this workflow

* Reduced mean time to remediation (MTTR)
* Consistent application of security procedures
* Comprehensive documentation of all actions taken
* Reduced analyst fatigue from repetitive tasks
* Improved visibility through automated notifications

## Workflow overview

### **Tools used:**

* Tines - workflow orchestration and AI platform (free Community Edition available)
* Confluence - knowledge management platform for SOPs

*This specific workflow also* uses *the following pieces of software. However, you can use whatever enrichment/*remediation *tools currently* existing within *your technology stack alongside Tines and Confluence.*

* CrowdStrike - threat intelligence and EDR platform
* AbuseIPDB - IP reputation database
* EmailRep - email reputation service
* Okta - identity and access management
* Slack - team collaboration platform
* Tavily - AI research tool
* URLScan.io - URL analysis service
* VirusTotal - file and URL scanning service

## How it works

### Part 1: Alert Ingestion and Analysis

* Receive security alert from integrated security tools
* AI agent analyzes the alert to determine type and severity
* System searches Confluence for relevant SOPs based on alert classification
* Create a case record with alert details and identified SOP

### Part 2: Remediation and Documentation

* Second AI agent reviews the case and SOP instructions
* AI agent orchestrates remediation actions across appropriate security tools
* All actions are documented in the case history
* Slack notification is sent to the on-call team with alert details and actions taken

## Configuring the workflow - step-by-step guide

1. Log into Tines or create a new account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaCOG_T5J3Lwh6rmD-myHvPNsL01gM-ROdZufvKMMjPHRPIVwaEBtPyRonxucNwOoyvq0_bsIIadmGFNRyip7EYwZxvaZ-NEOok0VuRNDfN7bjOWbRUy3w8HVLFtij5NTbLBIJxIIDhhi55wZXkVOC4rbc_s6YVHz37m-JvjIZvqbBUwfG5kPtq7ICo70/s790-rw-e365/1.png)

2. Navigate to [the pre-built workflow](https://www.tines.com/library/stories/1318807/?name=triage-alerts-with-agents-using-sops-in-confluence) in the library. Select import.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqB_RCxucP8TMJxxbR-GExrx9yUDvsm6gh3Q1p0h4OcDEhot7eJTQ_04EKlHmw9yshwdTSpzGJ2jHZCedfsTVB1UnGfA5E2NWpSp-rsJMKtp4owyabRVUmMpmXdOQBCSVgl7TQ8IvjAuJ6wgiW-kdGjevWuZS7C31hynIBi_hEinYbYoOl32iAjz14ARU/s790-rw-e365/2.png)

#### 3. Set up your credentials

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8v8kBQhCM_NdyNPF8FB58lSNH6Qeo2Kk8weGUK21ER61Ted1uz4N8IYMI5Ys0lO1LTUM2kyWQFTBnPqRF0yJap9_PKIgZ9h9q6A9gzMie8uqcK-1uTr_4ZUIX2p8D2w19_nO7uPSLF9gZd05aLkhI2Hjy2HvwUpRUdXGV4OUDCppsjNjmwCrcDSMg-Ik/s790-rw-e365/3.png)

You'll need credentials for all the tools used in this workflow. You can add or remove whatever tools you wish to suit your environment.

* Confluence
* CrowdStrike
* AbuseIPDB
* EmailRep
* Okta
* Slack
* Tavily
* URLScan.io
* ...