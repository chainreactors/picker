---
title: How to Investigate ChatGPT activity in Google Workspace
url: https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html
source: The Hacker News
date: 2024-09-18
fetch_date: 2025-10-06T18:29:38.777588
---

# How to Investigate ChatGPT activity in Google Workspace

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

# [How to Investigate ChatGPT activity in Google Workspace](https://thehackernews.com/2024/09/how-to-investigate-chatgpt-activity-in.html)

**Sep 17, 2024**The Hacker NewsGenAI Security / SaaS Security

[![Google Workspace](data:image/png;base64... "Google Workspace")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1jilvDJHd2bwsb_Ofx0gjEF79L6v4D10VHAmrVVK0NM3iRqerSez398zBuf0Ned7KVuFXDsi58BuaZM8ZrGU2kZYMea0KR-03CXsKtKdopGghC_xRXEQb9_kffJ6oiV-mky7Di2sjTzr3ueaHF6Ihv0ZBMlvU8Ceke-f9nH5kWfzAMUnuAVqNp2Lu2y4/s1500/nudge.png)

When you connect your organization's Google Drive account to ChatGPT, you grant ChatGPT extensive permissions for not only your personal files, but resources across your entire shared drive. As you might imagine, this introduces an array of cybersecurity challenges. This post outlines how to see ChatGPT activity natively in the Google Workspace admin console, and how Nudge Security can provide full visibility into all genAI integrations.

Since launching ChatGPT in 2022, OpenAI has defied expectations with a steady stream of product announcements and enhancements. One such announcement came on May 16, 2024, and for most consumers, it probably felt innocuous. Titled **["Improvements to data analysis in ChatGPT,"](https://openai.com/index/improvements-to-data-analysis-in-chatgpt/)** the post outlines how users can add files directly from Google Drive and Microsoft OneDrive. It's worth mentioning that other genAI tools like Google AI Studio and Claude Enterprise have also added similar capabilities recently. Pretty great, right? Maybe.‍

When you connect your organization's Google Drive or OneDrive account to ChatGPT (or other genAI tools), you grant it extensive permissions for not only your personal files, but resources across your entire shared drive. As you might imagine, the benefits of this kind of extensive integration come with an array of cybersecurity challenges.

So, how can you find out if employees have enabled the integration between ChatGPT and Google Drive, and how can you monitor which files have been accessed? This post walks through how to do this natively in Google Workspace, and how [Nudge Security](https://www.nudgesecurity.com/) can help you discover all genAI apps in use, and what other apps they've been integrated with.

## ‍**Where to see ChatGPT activity in Google Workspace**

In Google Workspace, there are a couple ways to identify and investigate activity associated with the ChatGPT connection.

From Google Workspace's Admin Console, navigate to Reporting > Audit and investigation > Drive log events. Here you'll see a list of Google Drive resources accessed.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrD7yoo_DIA6kzXxazt1izRrG1ft6kKtgHOz7L5wWcEA4TdiD7YH6j7wvbyRn_hBXuJhBthFbCJBUEbBn1wmu-G7Gqlhx26l4U9LdNmpSMFilA-gLRioZRn_oX1VNLqeAE4OJzDJ2cH1f6HQ8ajAyOHfYvwPZlLxDco6l52ynDRymmDxJjk3RCHwcr3zE/s1500/1.png)

You can also investigate the activity via API calls under Reporting→Audit and investigation→ Oauth log events.

[![Google Workspace](data:image/png;base64... "Google Workspace")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjE1RcWttJZumvDj-24EewQVHuWflwP1_4Rw7SkKVljPvaTgO77xHU6TjNjCfk-GkCV1Ob6tCd8GdqmaEa5mK6DCDbl6Y4ZO1SAO6jCOWPDDqFpoSlWbv3eu0RisogVQ_2VZ_N8sNr5a41DsMossh0yTvE2db6n-fNeYBc2UwOJsu2KeY_s50fofhKme9U/s1500/2.png)

‍So, periodically checking your Google Workspace admin console can help you understand what resources are being accessed by ChatGPT, but seeing this activity after it has already happened is of course less valuable than getting alerted as soon as new integrations are created with ChatGPT. This is where Nudge security can help.

## **How to see all genAI integrations with Nudge Security**

Nudge Security discovers all accounts ever created by anyone in your organization for any SaaS application, including ChatGPT and the rapidly expanding list of newly created genAI tools, without requiring any prior knowledge of the tool's existence. With the built-in AI dashboard, customers can keep up with AI adoption and proactively [mitigate AI security risks](https://www.nudgesecurity.com/use-cases/mitigate-ai-risks).

[![genAI integrations](data:image/png;base64... "genAI integrations")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjJVOR6dlcNYQDplImAzhdck8fAS43R07HtfSdoNCM_ZfoxMrm6lGAHde8LPyGQNiqmcYCVbHFLhQf0WWQhmciYGnVdITtzuyUudAnXO-hKSNh5ib81236BvvGUvTUS2EGigqlX_CyWKy5339m1uGoPuNsWQipVjaS8AKTiYsKxeW8sSWnEKkyefJFEpk/s1500/3.png)

Additionally, Nudge Security surfaces your entire organization's OAuth grants, such as those granted to ChatGPT, within a filterable OAuth dashboard that includes grant type (sign-in or integration), activity, and risk insights. Filter by category to see all grants associated with AI tools:

[![genAI integrations](data:image/png;base64... "genAI integrations")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNO79fxfK-9oUCk-34J1bFdSQ5nsKyKcNvt1BaZ4DUGdCPstYQMcFOjK7XJzmR7uEfnsKK38lWXtxp_rPznJnx1KP8Z79UGzAOv2DI4PRjKRJeykztZzqYG22a1Ta0xLhFV_QGna2yLrNpvbNGW_y587WTLHaHY0ZqOPrW6G_w07pH9mrM04xxPY5iOzc/s1500/4.png)

Click on a grant to open a detail screen, where you can review a risk profile, details on who created the grant and when, access details, scopes granted, and more:

[![genAI integrations](data:image/png;base64... "genAI integrations")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiesYQkymtw79tsv42NRTKY_KTCxGJghPldnE93c5VCmEA_xX5p1VZO3zNQwDLNTQeFEBoVivGayu2Tu_CmGXqWdlMim1ceZleHTalZjfohPTRmPrQTT7Rht1I0L8BhtszFoHG-0se-4BQzy7NSAxGbc8fKgBhju1D29aysjN7kP2rPLTL94PgibwCuZ9E/s1500/5.png)

You can then send a "nudge" to the creator of the grant via Slack or email to take a certain action, like limiting the scope of the grant, or you can immediately revoke the grant from within the Nudge Security user interface.

Finally, you can set up a custom rule to ensure that you are notified when a user at your organization creates an OAuth grant for ChatGPT—...