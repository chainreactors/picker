---
title: Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats
url: https://thehackernews.com/2025/12/featured-chrome-browser-extension.html
source: The Hacker News
date: 2025-12-15
fetch_date: 2025-12-16T03:24:39.984076
---

# Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)

**Dec 15, 2025**Ravie LakshmananAI Security / Browser Security

[![Featured Chrome Browser Extension](data:image/png;base64... "Featured Chrome Browser Extension")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXHTpJtgXoQfYQN62WgKv5VQG11DDmx38k3E0UeuLONeGHcNFQXzppCq-HGBEG9kJNyW_2O5q7VAuvoR7aEzUpW1i3iC4PWFxF31qypiXtp8zJqKVCDF6FyxVU8_UTZUU2OKeO6lA-KkXXOk6ASt3KVG4jQ0vuwldlLYHrkeZyoVVr64i5o_nC3Jkpcqyt/s790-rw-e365/chat-stealer.jpg)

A Google Chrome extension with a "Featured" badge and six million users has been [observed](https://www.koi.ai/blog/urban-vpn-browser-extension-ai-conversations-data-collection) silently gathering every prompt entered by users into artificial intelligence (AI)-powered chatbots like OpenAI ChatGPT, Anthropic Claude, Microsoft Copilot, DeepSeek, Google Gemini, xAI Grok, Meta AI, and Perplexity.

The extension in question is [Urban VPN Proxy](https://chromewebstore.google.com/detail/Urban%20VPN%20Proxy/eppiocemhmnlbhjplcgkofciiegomcon), which has a 4.7 rating on the Google Chrome Web Store. It's advertised as the "best secured Free VPN access to any website, and unblock content." Its developer is a Delaware-based company named [Urban Cyber Security Inc](https://www.dnb.com/business-directory/company-profiles.urban_cyber_security_inc.ca25c0768d2e7d4586619e12e921bd9d.html). On the Microsoft Edge Add-ons marketplace, it has [1.3 million installations](https://microsoftedge.microsoft.com/addons/detail/urban-vpn-proxy/nimlmejbmnecnaghgmbahmbaddhjbecg).

Despite claiming that it allows users to "protect your online identity, stay protected, and hide your IP," the extension was updated on July 9, 2025, when version 5.5.0 was released with the AI data harvesting enabled by default using hard-coded settings.

Specifically, this is achieved by means of a tailored executor JavaScript that's triggered for each of the AI chatbots (i.e., chatgpt.js, claude.js, gemini.js) to intercept and gather the conversations every time a user who has installed the extension visits any of the targeted platforms.

Once the script is injected, it overrides the browser APIs used to handle network requests – fetch() and XMLHttpRequest() – to make sure that every request is first routed through the extension's code so as to capture the conversation data, including users' prompts and the chatbot's responses, and exfiltrate them to two remote servers ("analytics.urban-vpn[.]com" and "stats.urban-vpn[.]com").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

The exact list of data captured by the extension is as follows -

* Prompts entered by the user
* Chatbot responses
* Conversation identifiers and timestamps
* Session metadata
* AI platform and model used

"Chrome and Edge extensions auto-update by default," Koi Security's Idan Dardikman said in a report published today. "Users who installed Urban VPN for its stated purpose – VPN functionality – woke up one day with new code silently harvesting their AI conversations."

It's worth mentioning that Urban VPN's updated privacy policy, as of June 25, 2025, mentions that it collects this data to enhance Safe Browsing and for marketing analytics purposes, and that any other secondary use of the gathered AI prompts will be carried out on de-identified and anonymized data -

*As part of the Browsing Data, we will collect the prompts and outputs quired [sic] by the End-User or generated by the AI chat provider, as applicable. Meaning, we are only interested in the AI prompt and the results of your interaction with the chat AI.*

*Due to the nature of the data involved in AI prompts, some sensitive personal information may be processed. However, the purpose of this processing is not to collect personal or identifiable data, we cannot fully guarantee the removal of all sensitive or personal information, we implement measures to filter out or eliminate any identifiers or personal data you may submit through the prompts and to de-identify and aggregate the data.*

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwd5skUX1qUNdglyQlpj22zrixRA673aV9H_t58XuKq1lmKU9qwEORIZDi5xlssmraWTjYRguA2XS-GIXy7IFiGBqLhGefpse7PGeOUeutFMXW4YXGj1ARGljJrbACnNFQS-oh2WI7F4BhiO5vk4c-gGJQ5pb-f_f7Zv6QIpVHSemrD7kB5BO2U0Wl_bRi/s2600/code.png)

One of the third-parties it shares "Web Browsing Data" with is an affiliated ad intelligence and brand monitoring firm named [BIScience](https://infosec.exchange/%40WPalant/113744609630895910). The company uses the raw (not anonymized) data to create insights that are "commercially used and shared with Business Partners," the VPN software maker notes.

It's worth noting BiScience, which also happens to own Urban Cyber Security Inc., was [called out](https://palant.info/2025/01/13/biscience-collecting-browsing-history-under-false-pretenses/) by an anonymous researcher earlier this January for collecting users' browsing history, or clickstream data, as it's called, under misleading privacy policy disclosures.

The company is alleged to provide a software development kit (SDK) to partner third-party extension developers to collect clickstream data from users, which is [transmitted](https://secureannex.com/blog/sclpfybn-moneitization-scheme/) to the [sclpfybn[.]com](https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html) and other endpoints under its control.

"BIScience and partners take advantage of loopholes in the Chrome Web Store policies, mainly exceptions listed in the [Limited Use policy](https://developer.chrome.com/docs/webstore/program-policies/limited-use/), which are the 'approved use cases,'" the researcher noted, adding they "develop user-facing features that allegedly require access to browsing history, to claim the 'necessary to providing or improving your single purpose' exception."

On the extension listing page, Urban VPN also...