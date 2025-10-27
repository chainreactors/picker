---
title: How Adversary Telegram Bots Help to Reveal Threats: Case Study
url: https://any.run/cybersecurity-blog/adversary-telegram-bot-abuse/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-21
fetch_date: 2025-10-06T22:29:00.554180
---

# How Adversary Telegram Bots Help to Reveal Threats: Case Study

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![How Adversary Telegram Bots Help to Reveal Threats: Case Study ](/cybersecurity-blog/wp-content/uploads/2025/05/adversary_bots_blog.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# How Adversary Telegram Bots Help to Reveal Threats: Case Study

May 20, 2025

[Add comment](#comments-13690)
27931 views
15 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

How Adversary Telegram Bots Help to Reveal Threats: Case Study

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1616
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3163
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3181
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

How Adversary Telegram Bots Help to Reveal Threats: Case Study

Are Telegram bots safe? While analyzing malware samples uploaded to [ANY.RUN’s Interactive Sandbox](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=adversary_bot_abuse&utm_term=200525&utm_content=linktoservice), one particular case marked as “phishing” and “Telegram” drew the attention of our security analysts.

Although this [analysis session](https://app.any.run/tasks/6e05ff83-09e4-4eaf-9b5f-b6628b3919f1/?utm_source=anyrunblog&utm_medium=article&utm_campaign=adversary_bot_abuse&utm_term=200525&utm_content=linktoservice) wasn’t attributed to any known malware family or threat actor group, the analysis revealed that Telegram bots were being used for data exfiltration. This led us to apply a message interception technique for Telegram bots, previously described on the [ANY.RUN blog](https://any.run/cybersecurity-blog/intercept-stolen-data-in-telegram/).

The investigation resulted in a clear and practical case study demonstrating how intercepting Telegram bot communications can aid in profiling the threat actor behind a relatively obscure phishing campaign.

Key outcomes of this analysis include:

* Examination and technical analysis of a lesser known phishing campaign

* Demonstration of [Telegram API-based](https://any.run/cybersecurity-blog/intercept-stolen-data-in-telegram/) data interception techniques

* Collection of [threat](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) [i](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/)[ntelligence](https://any.run/cybersecurity-blog/introducing-any-run-threat-intelligence-lookup/) (TI) indicators to help identify the actor

* Recommendations for detecting this type of threat

Let’s dive in.

## Technical Analysis of Attack with Telegram Bot

Let’s take a closer look at the analysis session:

[View analysis session](https://app.any.run/tasks/6e05ff83-09e4-4eaf-9b5f-b6628b3919f1/?utm_source=anyrunblog&utm_medium=article&utm_campaign=adversary_bot_abuse&utm_term=200525&utm_content=linktoservice)

The subject of the analysis is a phishing page hosted on a Notion workspace. The page content is in Italian, which, combined with the subdomain name, suggests this is a targeted campaign aimed at Italian-speaking users or organizations.

The URL submitted for analysis was:

**hxxps[:]//studiosperandio.notion[.]site/1c37ff25a354805f8dd0eed23673d4e8?pvs=4**

Here’s how the page appeared inside ANY.RUN’s Interactive Sandbox:

![](/cybersecurity-blog/wp-content/uploads/2025/05/image24.png)

It’s worth noting that the use of Notion workspaces as easily accessible infrastructure for phishing activity is not new.

This is supported by the number and frequency of related samples uploaded to ANY.RUN sandbox, as seen in the following [TI Lookup query](https://intelligence.any.run/analysis/lookup#{%22query%22:%22domainName:%5C%22notion%5C%22%20and%20threatName:%5C%22phishing%5C%22%22,%22dateRange%22:180}).

![](/cybersecurity-blog/wp-content/uploads/2025/05/image25-1-1024x395.png)

The targeted user is prompted to view a document that was allegedly shared with them.

Level up your team’s malware analysis and threat intelligence capabilities
See all ANY.RUN’s 9th Birthday offers

[Check out offers](https://app.any.run/plans/?utm_source=anyrunblog&utm_medium=article&utm_campaign=adversary_bot_abuse=200525&utm_content=linktoplans)

To do so, they are asked to sign in using their Microsoft credentials via the following link:

**hxxps[:]//gleaming-foregoing-quicksand[.]glitch[.]me/noter.html**

Clicking the link opens a hastily crafted phishing page designed to mimic a Microsoft OneNote login prompt. The page presents multiple authentication options, including:

* Office365

* Outlook

* Rackspace

* Aruba Mail

* PEC

* Altra Posta

![](/cybersecurity-blog/wp-content/uploads/2025/05/image26-1024x553.png)

After selecting a login method, the user is prompte...