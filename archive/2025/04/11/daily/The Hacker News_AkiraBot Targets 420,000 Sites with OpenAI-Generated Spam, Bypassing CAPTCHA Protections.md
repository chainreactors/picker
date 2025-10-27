---
title: AkiraBot Targets 420,000 Sites with OpenAI-Generated Spam, Bypassing CAPTCHA Protections
url: https://thehackernews.com/2025/04/akirabot-targets-420000-sites-with.html
source: The Hacker News
date: 2025-04-11
fetch_date: 2025-10-06T22:07:20.140841
---

# AkiraBot Targets 420,000 Sites with OpenAI-Generated Spam, Bypassing CAPTCHA Protections

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

# [AkiraBot Targets 420,000 Sites with OpenAI-Generated Spam, Bypassing CAPTCHA Protections](https://thehackernews.com/2025/04/akirabot-targets-420000-sites-with.html)

**Apr 10, 2025**Ravie LakshmananWebsite Security / Cybercrime

[![OpenAI-Generated Spam](data:image/png;base64... "OpenAI-Generated Spam")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizh0qywT1Ho701o9p8OyxDccCj_8A0KGHjG2x1m3ls__pZLcBzFhP9ZznBLPNDUneOpbqh2PfaGWzObR-4a36_NJNcMxq_2Gpp0sRhyiB8_85dvCAuHDB_IuKvi9N50RReW-y15yhdHEVexmYaAtaXJvH7v5jMFUVOnjnpyc0y64Bs_UCHhigbd7k0F_Ti/s790-rw-e365/akira.jpg)

Cybersecurity researchers have disclosed details of an artificial intelligence (AI) powered platform called **AkiraBot** that's used to spam website chats, comment sections, and contact forms to [promote](https://www.google.com/search?q=%22Visit+useakira.com+if+you+want+your+website+to+be+at+the+TOP+of+Google,+Yahoo+and+Bing%22&sca_esv=133ef026d08bc3d4&ei=NlP3Z9nvKfGD4-EPpPG0iAc&start=10&sa=N&sstk=Af40H4Wg28oHr_it3cKiWRS5V_ZqjHXWdrQdnS3_SG2Eb6336ZRRgwLR983IZmgN3DUl6CERg-LBNnnjO-bM2xlBf7iot1MCum9owg&ved=2ahUKEwjZ4vSL2syMAxXxwTgGHaQ4DXEQ8NMDegQIBhAW&biw=1470&bih=756&dpr=2) dubious search engine optimization (SEO) services such as Akira and ServicewrapGO.

"AkiraBot has targeted more than 400,000 websites and successfully spammed at least 80,000 websites since September 2024," SentinelOne researchers Alex Delamotte and Jim Walter [said](https://www.sentinelone.com/labs/akirabot-ai-powered-bot-bypasses-captchas-spams-websites-at-scale/) in a report shared with The Hacker News. "The bot uses OpenAI to generate custom outreach messages based on the purpose of the website."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Targets of the activity include contact forms and chat widgets present in small to medium-sized business websites, with the framework sharing spam content generated using OpenAI's large language models (LLMs). What makes the "sprawling" Python-based tool stand apart is its ability to craft content such that it can bypass spam filters.

It's believed that the bulk messaging tool has been put to use since at least September 2024, starting off under the name "Shopbot" in what appears to be a reference to websites using Shopify.

Over time, AkiraBot has expanded its targeting footprint to include sites developed using GoDaddy, Wix, and Squarespace, as well as those that have generic contact forms and live chat widgets built using Reamaze.

There is evidence to suggest that the promotion of the SEO service has occurred since at least 2023, although Delamotte told The Hacker News that it may have been pulled off using a different vector. "We believe the actor used more static content until September 2024, the dates of their earliest LLM-enabled content tools," the researcher added.

The crux of the operation – which is to generate the spam content – is facilitated by leveraging the OpenAI API. The tool also offers a graphical user interface (GUI) to choose the list of websites to be targeted and customize how many of them can be targeted in a concurrent fashion.

"AkiraBot creates custom spam messages for targeted websites by processing a template that contains a generic outline of the type of message the bot should send," the researchers said. "The template is processed by a prompt sent to the OpenAI chat API to generate a customized outreach message based on the contents of the website."

[![OpenAI-Generated Spam](data:image/png;base64... "OpenAI-Generated Spam")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiifBeiHz86HN4fzF0pNut3gCRuavxKmH8MsJ5aBV5uChtdDzu4A1UPbAzcvck8bDlLWYzQQGU-eQSqs-TYe8Ga4kUIdIPiQG9gtQsDLp_q9XV6dcBwOnpYZhGPy7lgOoHSS5qNs8Wh8WBB6AIFgSGNeIBxJ53Y70oEeUooBMInzwEyAutWLs159aJBFlTd/s790-rw-e365/spam.jpg)

An analysis of the source code reveals that the OpenAI client uses the gpt-4o-mini model and is assigned the role of a "helpful assistant that generates marketing messages."

Another notable aspect of the service is that it can get around CAPTCHA barriers to spam websites at scale and evades network-based detections by relying on a proxy service that's typically offered to advertisers. The targeted CAPTCHA services consist of hCAPTCHA, reCAPTCHA, and Cloudflare Turnstile.

To accomplish this, the bot's web traffic is designed to mimic a legitimate end user and makes use of different proxy hosts from SmartProxy to obscure the source of the traffic.

AkiraBot is also configured to log its activities in a file named "submissions.csv" that records both successful and failed spam attempts. An examination of these files has revealed that more than 420,000 unique domains have been targeted to date. Furthermore, success metrics related to CAPTCHA bypass and proxy rotation are collected and posted to a Telegram channel via API.

In response to the findings, OpenAI has disabled the API key and other associated assets used by the threat actors.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The author or authors have invested significant effort in this bot's ability to bypass commonly used CAPTCHA technologies, which demonstrates that the operators are motivated to violate service provider protections," the researchers said. "AkiraBot's use of LLM-generated spam message content demonstrates the emerging challenges that AI poses to defending websites against spam attacks."

The development coincides with the emergence of a cybercrime tool referred to as Xanthorox AI that's marketed as an all-in-one chatbot to handle code generation, malware development, vulnerability exploitation, and data analysis. The platform also supports voice-based interaction via real-time voice calls and asynchronous voice messaging.

"Xanthorox AI is powered by five distinct models, each optimized for different operational tasks," SlashNext [said](https://slashnext.com/blog/xanthorox-ai-the-next-generation-of-malicious-ai-threats-emerges/). "These models run ent...