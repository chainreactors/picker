---
title: Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA Codes
url: https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:34.910889
---

# Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA Codes

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Fake ChatGPT, Gemini, and Claude Ad Portals Capture Credentials and MFA Codes](https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html)

**Ravie Lakshmanan**Oct 06, 2026Phishing / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0zSahkV9zcg01XiHIrV4cYRCzxV9MLlvvX9vRW5e0Nd5Kg0aXGPgWR2oqqdHAAcrmm5r66m5Aj8VF9HYZtgTJv_X1HOaijWEoB_6m8ieYd-F9ytUtmn-1GgX4B-BWo6LXQgzVzr0nTiXsicD-3eTf02ZvrTwPsOCFt8yYGvuxTHfIYxwErOI1w99uekRz/s1700-nu-rw-lo-l85-e365/muse-ai.jpg)

Cybersecurity researchers have disclosed details of a "human-operated phishing platform" that impersonates advertising products for artificial intelligence (AI) chatbots like Google Gemini, Anthropic Claude, OpenAI ChatGPT, Perplexity, Meta Muse, and Manus.

The products, which claim to offer campaign optimization, spend audits, and business-account connections, are designed with one goal in mind: to capture credentials and multi-factor authentication (MFA) codes via spoofed login windows using the browser-in-the-browser ([BitB](https://thehackernews.com/2022/03/new-browser-in-browser-bitb-attack.html)) trick.

"Each product was built around the same action: Connect," Island researchers Oleg Zaytsev and Ofek Ronen [said](https://www.island.io/blog/behind-the-connect-button-the-fake-ai-ads-campaign) in a report shared with The Hacker News. "Clicking it opened a browser drawn inside the real browser. The fake address bar displayed trusted origins such as accounts.google.com or an Okta tenant, while the real browser remained on the phishing domain."

"Behind the interface, the platform kept every password attempt, fingerprinted the device, and let an operator pick which MFA challenge the victim saw next."

One of the websites in question is "museads.ai," which emerged on September 16, 2026, a little over a week after Meta launched [Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/), its AI agent designed for personal workflows. Described as "Your AI ads manager for paid media workflows," the platform claimed to help customers reach buyers, connect their ad accounts, and run sponsored placements.

Prominently placed in the spoofed web page is a Prompt Box with a "Connect" button, clicking which triggers a BitB attack to capture a visitor's account credentials for Google, Meta, TikTok, and Okta workflows. This is accomplished by drawing a fake window displaying a bogus account sign-in form with the address bar pointing to a legitimate domain (e.g., accounts.google[.]com).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

In the background, the victim's device is fingerprinted, and the information is transmitted to the attacker at the endpoint "/api/send/ip" over Socket.IO, after which operator commands and victim data are exchanged based on the login workflow. Armed with the account credentials, the attacker attempts to sign in to the account in real-time.

Commands to the phishing page are delivered through two Socket.IO events named operator-command and telegram-command. These commands drive the sign-in process, while the human operator can view what steps the victims are taking and decide the next course of action.

"In the inspected code, both pass the received command text to the same parser, so they don’t represent separate sets of page actions," Zaytsev, Lead Security Researcher at Island, told The Hacker News.

"The commands let the operator steer the victim through authentication in real time: request another password (/password), show an SMS or authenticator challenge (/2fa, /authApp), display Google prompts such as approval, QR, or number matching (/googlePrompt, /googleQrVerify, /verifyTap), or select Okta username, password, SMS, push, authenticator, and number-matching screens (/oktaUsername, /oktaPassword, /oktaSms2fa, /oktaApprove, /oktaAuthApp, /oktaVerifyTap). The operator can also reject a submitted code (/wrong2fa), keep the visitor waiting, or end or suppress the flow (/done, /ban)."

"Every brand gets its own pitch," the researchers explained. "ChatGPT promises a Monday Google Ads brief. Gemini promises MCC (manager account) and linked-client support. Claude gets its own advertising portal, Perplexity offers campaign planning and spend audits, and Manus offers a private Meta integration."

Users are [assessed](https://ironscales.com/threat-intelligence/gemini-ads-beta-invite-attacker-built-bulk-mail-compliance-kit) to be [directed](https://research.intezer.com/blog/2026/08/when-the-whole-company-adopts-ai/) to these landing pages via fake invitation emails that impersonate these trusted brands to lend the attacks a veneer of legitimacy.

"Each one in this campaign poses as a believable product, with its own brand, pitch, and sign-in flow," the researchers pointed out. "They also move with the news."

Island said the AI ads pages are part of a broader phishing platform that supports a three-pronged operation, the two others being Google Ads-themed refund claims and payment confirmation, as well as recruitment-related sites for Tesla, Louis Vuitton, Nike, and Adecco.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9IIlSeN6Dr7SYst1FSzi-IpwRXWV44Yf3Bs8HSzXuU4eKQdEJskC78-wpNd1TiM5_aAPuGQgz4w93NShE9jZhIn-JYVwlECCcf2iHuT0l8lYIQhi6ijBteUuSbRVxttJrSGMOcduJkZkoFDwZEkJpTETzo_BHFBlrswaa7oTWuw3khC0V3DWCzXm_LGTo/s1700-nu-rw-lo-l85-e365/flow.png)

All the identified websites have been found to share the same technology stack comprising Next.js and Socket.IO, and communicate with the same endpoints. What's more, the threat actors behind the operation have exposed source code for earlier versions of the platform through misconfigured public GitHub repositories.

The AI ads-focused campaign is designed to target agency staff, media buyers, and manager-account administrators, likely with the end goal of monetizing th...