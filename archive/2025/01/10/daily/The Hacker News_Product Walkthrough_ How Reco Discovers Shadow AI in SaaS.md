---
title: Product Walkthrough: How Reco Discovers Shadow AI in SaaS
url: https://thehackernews.com/2025/01/product-review-how-reco-discovers.html
source: The Hacker News
date: 2025-01-10
fetch_date: 2025-10-06T20:12:43.931116
---

# Product Walkthrough: How Reco Discovers Shadow AI in SaaS

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

# [Product Walkthrough: How Reco Discovers Shadow AI in SaaS](https://thehackernews.com/2025/01/product-review-how-reco-discovers.html)

**Jan 09, 2025**The Hacker NewsAI Security / SaaS Security

[![Discovers Shadow AI in SaaS](data:image/png;base64... "Discovers Shadow AI in SaaS")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0FtrJbu9P2mmBDaVBwQoX11IH-sTLyxMzqYS-5Oj_AbpNQ6se6_byE6NhJAz8a-ESIvthlnXlhtjBdyFBJ_97LRy-zndKD4dMABKxgNWEPar0GVbkfCzi27GlhcXfFZ_kv_uCEQsGTTF6EOa0486D0SkazwXLtt8spV7E_8KD21eDJjhANINZsSXkVTQ/s790-rw-e365/shadow_ai_shadow_saas_discovery_reco.jpg)

As SaaS providers race to integrate AI into their product offerings to stay competitive and relevant, a new challenge has emerged in the world of AI: shadow AI.

Shadow AI refers to the unauthorized use of AI tools and copilots at organizations. For example, a developer using ChatGPT to assist with writing code, a salesperson downloading an AI-powered meeting transcription tool, or a customer support person using Agentic AI to automate tasks – without going through the proper channels. When these tools are used without IT or the Security team's knowledge, they often lack sufficient security controls, putting company data at risk.

## Shadow AI Detection Challenges

Because shadow AI tools often embed themselves in approved business applications via AI assistants, copilots, and agents they are even more tricky to discover than traditional shadow IT. While traditional shadow apps can be identified through network monitoring methodologies that scan for unauthorized connections based on IP addresses and domain names, these AI assistants can fly under the radar because they share an IP address or domain with approved applications.

Additionally, some employees utilize standalone AI tools tied to personal accounts, like personal ChatGPT instances, to assist with work-related tasks. While these AI apps aren't connected to corporate infrastructure, there's still the risk that employees will input sensitive data into them, increasing the chance of data leaks.

## Shadow AI Security Risks

Like any shadow apps, shadow AI apps expand the attack surface through unmonitored integrations and APIs. They're often set up with weak configurations like excessive permissions, duplicative passwords, and no multi-factor identification (MFA), increasing the risk of exploitation and lateral movement within the network.

However, shadow AI tools are even more dangerous than traditional shadow apps because of their ability to ingest and share information. [One study](https://www.infosecurity-magazine.com/news/third-employees-sharing-work-info/) found that as many as 15% of employees post company data in AI tools. Since GenAI models learn from every interaction, there's a risk they will expose sensitive information to unauthorized users or spread misinformation.

## How Reco Discovers Shadow AI in SaaS

[Reco](https://www.reco.ai/), a SaaS security solution, uses AI-based graph technology to discover and catalog shadow shadow AI. Here's how Reco works:

1. **Active Directory Integration:** Reco begins by integrating with your organization's Active Directory, such as Microsoft Azure AD or Okta, to gather a list of approved and known applications and AI tools.
2. **Email Metadata Analysis:** Reco analyzes email metadata from platforms like Gmail and Outlook to detect communications with unauthorized tools. It filters out internal apps and marketing emails and focuses on usage indicators, like account confirmations and download requests.
3. **GenAI Module Matching:** Using a proprietary, fine-tuned model based on interactions and NLP, Reco consolidates and cleans the list, matching identities with corresponding apps and AI tools. Then, it creates a list of all SaaS apps and AI tools being used, who is using them, and what authentication mechanisms are being used.
4. **Shadow Application Detection:** By comparing this list against a list of known applications and AI tools, Reco produces a list of unauthorized applications and shadow AI tools.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtcLXxa6X4rBXJUav-oYCLXzOpCPWl8-yf1cgafSQHdym3kRMwOld__3F1obaSbYpxYpwIuEDekMCZtvQHTz0JMAoiQv5iYJrT8y5_w3Eij3AL-f5PQWdISCrAvDzR_wAP64OKNo0HwYkSKWS95qvCBqBhd6SBTojCZLqS__pQqFkERQ20beCGygk6qG4/s790-rw-e365/1.gif)

## What Reco Can Tell You About Shadow AI Tools

After Reco produces the list of shadow AI tools and apps, Reco can answer questions like:

### **Which SaaS apps are currently in use across your organization? Of these apps, which are utilizing AI assistants and copilots?**

Reco inventories all applications running in your environment that are associated with your business email. It creates a list of who is using what, how they're authenticating, and produces activity logs in order to understand their behavior. That way, it can alert to suspicious activity, like excessive downloads, external file sharing, or permission changes. It also provides a Vendor Risk Score so security teams can prioritize riskier apps.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCjuJKIYyjsoJoMAsvnReUBPOYo0HEX2VrRCIeSm5W-HrB5Jy6KEgwUnanS4xbidTtFdkS3b_5hQrNlnzn5eg-MxssnfDq02zpwBwbhBwVWrjdhS9jxtkO2lEnOQtC6gkKi8_suIdWJspbirWzmmW3WlsKaImIQ7Sk_kyFBaKbL0mxzIH2aeFw98SCpFo/s790-rw-e365/2.png)

### **What app-to-app connections exist?**

SaaS applications don't operate as islands. You need to understand how they're interacting with other applications to effectively manage risk. Reco shows you all the app-to-app integrations discovered within your environment. For example, you can see if an AI tool has been connected to a business-critical application like Gmail or Snowflake, and what permissions each AI application has.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRuGUwZvOm0IYYyCDPMU3xj6Pfy4bN85V5mj3deOh5nI8nZaZt0aPTwVvll7veOKIPOQHtkluC_vdZOoCwrKnCpP3TX4Y3rBA6qRFspglkYbvVjRQCAQ1oCt9...