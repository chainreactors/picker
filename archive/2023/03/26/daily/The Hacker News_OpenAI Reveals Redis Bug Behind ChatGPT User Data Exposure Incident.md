---
title: OpenAI Reveals Redis Bug Behind ChatGPT User Data Exposure Incident
url: https://thehackernews.com/2023/03/openai-reveals-redis-bug-behind-chatgpt.html
source: The Hacker News
date: 2023-03-26
fetch_date: 2025-10-04T10:44:55.359162
---

# OpenAI Reveals Redis Bug Behind ChatGPT User Data Exposure Incident

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

# [OpenAI Reveals Redis Bug Behind ChatGPT User Data Exposure Incident](https://thehackernews.com/2023/03/openai-reveals-redis-bug-behind-chatgpt.html)

**Mar 25, 2023**Ravie LakshmananArtificial Intelligence / Data Security

[![ChatGPT](data:image/png;base64... "ChatGPT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjG1uawIB2kUUStMe6h5ReVpS5-DaaC80MnfdYRK0wiTQYTFocH6A85GVUrUyEYZ557x6HS69AykWzZ8vlHOMKZaVj43koutrRlRtHt_lHc4yJzsAba3asE1YIvykT90OjyrXEmLL2qY31HkEPWJgbd2zJHiw38uFPxpG3zZQsP89FKQiD-XjefPns8/s790-rw-e365/chatgpt.png)

OpenAI on Friday disclosed that a bug in the Redis open source library was responsible for the exposure of other users' personal information and chat titles in the upstart's ChatGPT service earlier this week.

The [glitch](https://www.vice.com/en/article/5d9zd5/chatgpt-users-report-being-able-to-see-random-peoples-chat-histories), which came to light on March 20, 2023, enabled certain users to view brief descriptions of other users' conversations from the chat history sidebar, prompting the company to temporarily shut down the chatbot.

"It's also possible that the first message of a newly-created conversation was visible in someone else's chat history if both users were active around the same time," the company [said](https://openai.com/blog/march-20-chatgpt-outage).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The bug, it further added, originated in the [redis-py library](https://github.com/redis/redis-py/issues/2624), leading to a scenario where canceled requests could cause connections to be corrupted and return unexpected data from the database cache, in this case, information belonging to an unrelated user.

To make matters worse, the San Francisco-based AI research company said it introduced a server-side change by mistake that led to a surge in request cancellations, thereby upping the error rate.

While the problem has since been addressed, OpenAI noted that the issue may have had more implications elsewhere, potentially revealing payment-related information of 1.2% of the ChatGPT Plus subscribers on March 20 between 1-10 a.m. PT.

This included another active user's first and last name, email address, payment address, the last four digits (only) of a credit card number, and credit card expiration date. It emphasized that full credit card numbers were not exposed.

The company said it has reached out to affected users to notify them of the inadvertent leak. It also said it "added redundant checks to ensure the data returned by our Redis cache matches the requesting user."

## **OpenAI Fixes Critical Account Takeover Flaw**

In another caching-related issue, the company also addressed a critical account takeover vulnerability that could be exploited to seize control of another user's account, view their chat history, and access billing information without their knowledge.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The flaw, which was [discovered](https://twitter.com/naglinagli/status/1639343866313601024) by security researcher Gal Nagli, bypasses protections put in place by OpenAI on chat.openai[.]com to read a victim's sensitive data.

[![ChatGPT Account Takeover](data:image/png;base64... "ChatGPT Account Takeover")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhRMjyk-fUTdF49wV65r_UfSB9oY3xfXcHN4eEzfJ75M7GEYhY9RjerJd08X1a64GwoMHbl1mrsrAPC4WwUq8GMAJUsqKDUCtSruOArlUMO5NfzMN4xWHDc_B84zX1G8RYfSFCamgZ5SSoa14pEcEP2yr7Rl-rkzXV39VKiojRhl-IalaGWVw-ZUnc4g/s790-rw-e365/openai.png)

This is achieved by first creating a specially crafted link that appends a .CSS resource to the "chat.openai[.]com/api/auth/session/" endpoint and tricking a victim to click on the link, causing the response containing a JSON object with the accessToken string to be cached in [Cloudflare's CDN](https://developers.cloudflare.com/cache/).

The cached response to the CSS resource (which has the [CF-Cache-Status header](https://developers.cloudflare.com/cache/about/default-cache-behavior/) value set to HIT) is then abused by the attacker to harvest the target's JSON Web Token ([JWT](https://thehackernews.com/2023/01/critical-security-flaw-found-in.html)) credentials and take over the account.

Nagli said the bug was fixed by OpenAI within two hours of responsible disclosure, indicative of the severity of the issue.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[ChatGPT](https://thehackernews.com/search/label/ChatGPT)[data breach](https://thehackernews.com/search/label/data%20breach)[OpenAI](https://thehackernews.com/search/label/OpenAI)[Redis](https://thehackernews.com/search/label/Redis)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-h...