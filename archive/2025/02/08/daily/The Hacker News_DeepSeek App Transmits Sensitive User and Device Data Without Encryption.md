---
title: DeepSeek App Transmits Sensitive User and Device Data Without Encryption
url: https://thehackernews.com/2025/02/deepseek-app-transmits-sensitive-user.html
source: The Hacker News
date: 2025-02-08
fetch_date: 2025-10-06T20:47:18.427523
---

# DeepSeek App Transmits Sensitive User and Device Data Without Encryption

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

# [DeepSeek App Transmits Sensitive User and Device Data Without Encryption](https://thehackernews.com/2025/02/deepseek-app-transmits-sensitive-user.html)

**Feb 07, 2025**Ravie LakshmananMobile Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgE3vY3R2OtrX1tKEjWavET-Vgs4a7DM_adgg14YlWBO1kGLa1rjjhVQG9Mf6DeeCFTXKxal-pNLjzFtLBNJJ1XL_1si-arFZ3dLjeEsjgBY37n8mBLUiMohaS5BvLXYdTRDi3NtNssJ13MHLmMb8JedhtgO-_MqkkUPUWZIVeedsyKcb8mN06HKO_GgSOo/s790-rw-e365/deepseek-ios-app.png)

A new audit of DeepSeek's mobile app for the Apple iOS operating system has found glaring security issues, the foremost being that it sends sensitive data over the internet sans any encryption, exposing it to interception and manipulation attacks.

The assessment comes from NowSecure, which also found that the app fails to adhere to best security practices and that it collects extensive user and device data.

"The DeepSeek iOS app sends some mobile app registration and device data over the Internet without encryption," the company [said](https://www.nowsecure.com/blog/2025/02/06/nowsecure-uncovers-multiple-security-and-privacy-flaws-in-deepseek-ios-mobile-app/). "This exposes any data in the internet traffic to both passive and active attacks."

The teardown also revealed several implementation weaknesses when it comes to applying encryption on user data. This includes the use of an insecure symmetric encryption algorithm ([3DES](https://en.wikipedia.org/wiki/Triple_DES)), a hard-coded encryption key, and the reuse of [initialization vectors](https://en.wikipedia.org/wiki/Initialization_vector).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

What's more, the data is sent to servers that are managed by a cloud compute and storage platform named [Volcano Engine](https://www.volcengine.com), which is owned by ByteDance, the Chinese company that also operates TikTok.

"The DeepSeek iOS app globally disables App Transport Security (ATS) which is an iOS platform level protection that prevents sensitive data from being sent over unencrypted channels," NowSecure said. "Since this protection is disabled, the app can (and does) send unencrypted data over the internet."

The findings add to a [growing](https://thehackernews.com/2025/02/taiwan-bans-deepseek-ai-over-national.html) [list](https://thehackernews.com/2025/02/thn-weekly-recap-top-cybersecurity.html) of [concerns](https://blogs.cisco.com/security/evaluating-security-risk-in-deepseek-and-other-frontier-reasoning-models) that have been raised around the artificial intelligence (AI) chatbot service, even as it skyrocketed to the top of the app store charts on both Android and iOS in several markets across the world.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3GIowjce1ZclFe8NYchg49whFVJpiVkhggBdcEZUsjzBkmwlGU2PC62wLOpRKBEx0ZTM2cnIwYezGEKT9Rt_64hHsJnWXuATZYASw30Nrpj_W7RVwEaBy4sfMoVlyZlDg1GX1NrYfIEUiC08thfCASrXDZdetqIsIHLTWAtr0s-hWmEaoCZmjp9JsjAb1/s790-rw-e365/secure.png)

Cybersecurity company Check Point said that it observed instances of threat actors leveraging AI engines from DeepSeek, alongside Alibaba Qwen and OpenAI ChatGPT, to develop information stealers, generate uncensored or unrestricted content, and optimize scripts for mass spam distribution.

"As threat actors utilize advanced techniques like jailbreaking to bypass protective measures and develop info stealers, financial theft, and spam distribution, the urgency for organizations to implement proactive defenses against these evolving threats ensures robust defenses against potential misuse of AI technologies," the company [said](https://blog.checkpoint.com/artificial-intelligence/cpr-finds-threat-actors-already-leveraging-deepseek-and-qwen-to-develop-malicious-content/).

Earlier this week, the Associated Press [revealed](https://apnews.com/article/deepseek-china-generative-ai-internet-security-concerns-c52562f8c4760a81c4f76bc5fbdebad0) that DeepSeek's website is configured to send user login information to China Mobile, a state-owned telecommunications company that has been banned from operating in the United States.

The app's Chinese links, much like [TikTok](https://thehackernews.com/2025/01/tiktok-goes-dark-in-us-as-federal-ban.html), have prompted U.S. lawmakers to [push for a nation-wide ban](https://gottheimer.house.gov/posts/release-gottheimer-lahood-introduce-new-bipartisan-legislation-to-protect-americans-from-deepseek) on DeepSeek from government devices over risks that it could provide user information to Beijing.

It's worth noting that several countries, including [Australia](https://www.bbc.com/news/articles/c8d95v0nr1yo), [Italy](https://thehackernews.com/2025/01/italy-bans-chinese-deepseek-ai-over.html), [the Netherlands](https://www.dutchnews.nl/2025/02/deepseek-banned-from-civil-servants-computers-over-spy-concerns/), [Taiwan](https://thehackernews.com/2025/02/taiwan-bans-deepseek-ai-over-national.html), and [South Korea](https://www.reuters.com/technology/artificial-intelligence/south-koreas-industry-ministry-temporarily-bans-access-deepseek-security-2025-02-05/), and [government agencies in India](https://www.reuters.com/technology/artificial-intelligence/indias-finance-ministry-asks-employees-avoid-ai-tools-like-chatgpt-deepseek-2025-02-05/) and the United States, such as the Congress, NASA, Navy, Pentagon, and Texas, have instituted bans on DeepSeek from government devices.

DeepSeek's explosion in popularity has also led to it battling malicious attacks, with Chinese cybersecurity firm XLab [telling](https://www.globaltimes.cn/page/202501/1327697.shtml) Global Times that the service has been subjected to sustained distributed denial-of-service (DDoS) attacks originating from Mirai botnets [hailBot](https://thehackernews.com/2023/11/mirai-based-botnet-exploiting-zero-day.html) and [RapperBot](https://thehackernews.com/2022/11/warning-new-rapperbot-campaign-a...