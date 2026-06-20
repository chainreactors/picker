---
title: Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data
url: https://thehackernews.com/2026/06/salesforce-disables-klue-app.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:43.319688
---

# Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Salesforce Disables Klue App Integration After OAuth Token Abuse Exposes Customer Data](https://thehackernews.com/2026/06/salesforce-disables-klue-app.html)

**Ravie Lakshmanan**Jun 19, 2026Data Breach / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI7q_DYP5ExkNSDd8Y10rOfYtTIs6sNXxdE6X55nsvKVllZZ14U9mqUY23nzGGPhXx515NVPMI5Btp4MM5qUx0V1lKDvURtKBICbblPPYuN1VSCN12-J0RmpBKCSM0veZc_9hNt1TnD9PdkNTQi8x337E9cPmLn7uyHOPw0_HshcbxKqVnmgOAjJHOOw6g/s1700-e365/salesforce.jpg)

Salesforce has revealed that it disabled the Klue Battlecards app integration within its platform in response to a security incident impacting the competitive intelligence company on June 11, 2026.

To that end, organizations will be unable to connect to Salesforce via the app until further notice, the American cloud-based software company noted in an alert published this week.

"Salesforce took this action because our security teams recently detected unusual activity involving the app that may have resulted in unauthorized access to a subset of customer data via the app's connection to Salesforce," it [noted](https://status.salesforce.com/generalmessages/20000257). "This issue is limited to Klue's app connection and does not arise from a vulnerability within the Salesforce platform."

The development comes as an extortion group dubbed Icarus compromised and exfiltrated data from customers of Klue, including cybersecurity company Huntress.

"The data that was copied from our Salesforce account includes business contacts, price quotes, and other sales-related data and messaging," Huntress [said](https://www.huntress.com/blog/klue-breach-investigation). "No threat data, passwords, payment card information, or engineering data relating to the Huntress agent or telemetry we collect was affected."

In its own update, Klue said it detected unauthorized activity affecting a portion of Klue's integration infrastructure on June 12, 2026, adding the attackers gained access through a compromised legacy credential associated with an integration service.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"The attacker used that access to obtain OAuth tokens used to connect Klue with certain third-party platforms, including Salesforce, and subsequently accessed data within a number of connected customer environments," Klue CEO Jason Smith [said](https://klue.com/blog/an-update-on-recent-klue-security-incident). "Based on our investigation to date, the incident was limited to the affected third-party platforms, and there is no evidence that customer content stored within the Klue platform was impacted."

Specifically, the intrusion is said to have allowed the threat actor to push a code update capable of collecting OAuth tokens that its customers use to connect Klue to their own systems. In response to the breach, Klue has taken steps to revoke affected credentials and tokens, remove unauthorized code, stop remote access, disable potentially impacted integrations, and launch a comprehensive investigation.

As of June 16, 2026, some of Huntress employees have received an email with the subject line "top secret email" and a warning that states: "Your Salesforce data has been downloaded ... You have 48 hours to communicate with us. Do the right decision."

"The threat actor seems to have leveraged a long-disused but still active credential to conduct the initial compromise – one that was originally created by Klue for them to prototype a third-party integration they later abandoned," the company said. "The threat actor then pivoted into Klue's infrastructure to steal the tokens used by Klue's customers, then used those stolen credentials to query those customers' CRM tools directly and, eventually, to exfiltrate the data."

Not much is known about the Icarus actor other than the fact that they have been active since April 28, 2026, and have claimed a total of two victims to date. That said, the data theft campaign mirrors prior attack waves mounted by ShinyHunters and UNC6395.

ReliaQuest, in its own analysis of the Klue integration abuse, said the activity shares similarities with the third-party OAuth-abuse playbook associated with the [Salesloft Drift](https://thehackernews.com/2025/09/github-account-compromise-led-to.html) and [Gainsight](https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html) compromises that targeted Salesforce environments last year.

"In the attacks we observed, the adversary first authenticated through a compromised Klue integration service account, generated OAuth tokens, and ran automated Python scripts (identifiable by Python-urllib user-agent strings)," ReliaQuest researchers Thassanai McCabe and Alexa Feminella [said](https://reliaquest.com/blog/threat-spotlight-integration-abused-in-crm-data-theft).

"These scripts first enumerated the org's object catalog via GET /services/data/v59.0/sobjects, then looped REST API queries against the Salesforce query endpoint (/services/data/v59.0/query) and paginated results via the QueryMore cursor for almost 24 hours."

These are assessed to be bulk data retrieval actions designed to pull large volumes of CRM records through the Salesforce REST API. This included a "concentrated burst" of nearly a thousand queries in 15 minutes against at least one environment and an extraction window that lasted more than six hours in another case.

It's unclear how many Salesforce customers were affected by the latest attacks, although Klue said it has been communicating directly with impacted customers, sharing investigative findings, and assisting with their response efforts.

"The common thread is the abuse of OAuth tokens or credentials from a trusted third-party vendor," ReliaQuest said. "These integrations are non-human identities with persistent, often broad access to sensitive data, yet they are typically monitored far less closely than employee accounts. That gap is why a 24-hour...