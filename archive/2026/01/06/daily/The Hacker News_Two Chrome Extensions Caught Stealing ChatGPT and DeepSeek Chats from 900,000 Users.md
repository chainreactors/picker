---
title: Two Chrome Extensions Caught Stealing ChatGPT and DeepSeek Chats from 900,000 Users
url: https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html
source: The Hacker News
date: 2026-01-06
fetch_date: 2026-01-07T03:30:45.012301
---

# Two Chrome Extensions Caught Stealing ChatGPT and DeepSeek Chats from 900,000 Users

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Two Chrome Extensions Caught Stealing ChatGPT and DeepSeek Chats from 900,000 Users](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html)

**Jan 06, 2026**Ravie LakshmananArtificial Intelligence / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEilyYADOHMjVaRNmtGaBfZPuBBjV_zLAAmQ5LxnNXcpM_sHfQYws0W0gowwIgUC9-LBYr-y4eb5HK1cyqC857lCqKz1M_EHugfrzmkAL2vW-0SoRCdJpYsbZv8fd6-5EK8awrdD7a4eCaTZTJB9BLLDdYZlKNZQJ4Pwp7aok-jQ793kB7ft_A5pIgtCqvuQ/s790-rw-e365/chrome.jpg)

Cybersecurity researchers have [discovered](https://www.ox.security/blog/malicious-chrome-extensions-steal-chatgpt-deepseek-conversations/) two new malicious extensions on the Chrome Web Store that are designed to exfiltrate OpenAI ChatGPT and DeepSeek conversations alongside browsing data to servers under the attackers' control.

The names of the extensions, which collectively have over 900,000 users, are below -

* Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI (ID: fnmihdojmnkclgjpcoonokmkhjpjechg, 600,000 users)
* AI Sidebar with Deepseek, ChatGPT, Claude, and more. (ID: inhcgfpbfdjbjogdfjbclgolkmhnooop, 300,000 users)

The findings follow weeks after [Urban VPN Proxy](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html), another extension with millions of installations on Google Chrome and Microsoft Edge, was [caught spying](https://moonlock.com/chrome-extension-spying-ai-chats) on users' chats with artificial intelligence (AI) chatbots. This tactic of using browser extensions to stealthily capture AI conversations has been [codenamed](https://secureannex.com/blog/prompt-poaching/) **Prompt Poaching** by Secure Annex.

The two newly identified extensions "were found exfiltrating user conversations and all Chrome tab URLs to a remote C2 server every 30 minutes," OX Security researcher Moshe Siman Tov Bustan said. "The malware adds malicious capabilities by requesting consent for 'anonymous, non-identifiable analytics data' while actually exfiltrating complete conversation content from ChatGPT and DeepSeek sessions."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The malicious browser add-ons have been found to impersonate a [legitimate extension](https://chromewebstore.google.com/detail/chat-with-all-ai-models-g/becfinhbfclcgokjlobojlnldbfillpf) named "Chat with all AI models (Gemini, Claude, DeepSeek...) & AI Agents" from AITOPIA that has about 1 million users. They are still available for download from the Chrome Web Store as of writing, although "Chat GPT for Chrome with GPT-5, Claude Sonnet & DeepSeek AI" has since been stripped of its "Featured" badge.

Once installed, the rogue extensions request that users grant them permissions to collect anonymized browser behavior to purportedly improve the sidebar experience. Should the user agree to the practice, the embedded malware begins to harvest information about open browser tabs and chatbot conversation data.

To accomplish the latter, it looks for specific DOM elements inside the web page, extracts the chat messages, and stores them locally for subsequent exfiltration to remote servers ("chatsaigpt[.]com" or "deepaichats[.]com").

What's more, the threat actors have been found to leverage Lovable, an artificial intelligence (AI)-powered web development platform, to host their privacy policies and other infrastructure components ("chataigpt[.]pro" or "chatgptsidebar[.]pro") in an attempt to obfuscate their actions.

The consequences of installing such add-ons can be severe, as they have the potential to exfiltrate a wide range of sensitive information, including data shared with chatbots like ChatGPT and DeepSeek, and web browsing activity, including search queries and internal corporate URLs.

"This data can be weaponized for corporate espionage, identity theft, targeted phishing campaigns, or sold on underground forums," OX Security said. "Organizations whose employees installed these extensions may have unknowingly exposed intellectual property, customer data, and confidential business information."

### Legitimate Extensions Join Prompt Poaching

The disclosure comes as Secure Annex said it identified legitimate browser extensions such as [Similarweb](https://chromewebstore.google.com/detail/similarweb-website-traffi/hoklmmgfnpapgjgcpechhaamimifchmp) and Sensor Tower's [Stayfocusd](https://chromewebstore.google.com/detail/stayfocusd-%E2%80%93-website-bloc/laankejkbhbdhmipfmgcngdelahlfoji) – each with 1 million and 600,000 users, respectively – engaging in prompt poaching.

Similarweb is said to have introduced the ability to monitor conversations in May 2025, with a January 1, 2026, update adding a full terms of service pop-up that makes it explicit that data entered into AI tools is being collected to "provide the in-depth analysis of traffic and engagement metrics." A December 30, 2025, [privacy policy update](https://www.similarweb.com/corp/legal/extension-privacy-policy/) also spells this out -

*This information includes prompts, queries, content, uploaded or attached files (e.g., images, videos, text, CSV files) and other inputs that you may enter or submit to certain artificial intelligence (AI) tools, as well as the results or other outputs (including any attached files included in such outputs) that you may receive from such AI tools ("AI Inputs and Outputs").*

*Considering the nature and general scope of AI Inputs and Outputs and AI Metadata that is typical to AI tools, some Sensitive Data may be inadvertently collected or processed. However, the aim of the processing is not to collect Personal Data in order to be able to identify you. While we cannot guarantee that all Personal Data is removed, we do take steps, where possible, to remove or filter out identifiers that you may enter or submit to these AI tools.*

Further analysis has revealed that Similarweb uses DOM scraping or hijacks native browser APIs like fetch() and XMLHttpRequest() –...