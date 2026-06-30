---
title: Malicious Perplexity Chrome Extension Intercepted Searches and Address Bar Input
url: https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html
source: The Hacker News
date: 2026-06-29
fetch_date: 2026-06-30T06:10:12.659016
---

# Malicious Perplexity Chrome Extension Intercepted Searches and Address Bar Input

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

# [Malicious Perplexity Chrome Extension Intercepted Searches and Address Bar Input](https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html)

**Swati Khandelwal**Jun 29, 2026Browser Security / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOcObOpyIQZzuiNoFu6Lv4jCDh64o1WYrC3stGdk58mMRg69RT56svVrXVwu618f6szk2lj_Tqbt6b7Rg25yV0cauxIDTbMAI8cbftKVYibIt5SMeaOT2zE3oeuu-RLI7M1mkEV3zirqDiO-nLMikX7QixM2EpVIdKQERGc7I_0p58L4J-s5mBjSCpgHc/s1700-e365/pp-ai.jpg)

Microsoft has found a malicious Chrome extension that posed as the AI search engine Perplexity and quietly logged what people searched for. It routed every query and every character typed into the address bar through an attacker-controlled server before redirecting users to real results.

Microsoft says Google removed it from the store after responsible disclosure. The extension was called "Search for perplexity ai" (ID flkebkiofojicogddingbdmcmkpbplcd) and used a look-alike domain, perplexity-ai[.]online, to pass for the real service at perplexity.ai.

[Microsoft's Defender research team](https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/) says the point was to intercept searches and collect data. It found no proof of password theft, but far more access than a search box should ever need.

Once installed, the extension sets itself as the browser's default search engine. When you searched, the query went first to perplexity-ai[.]online, where the attacker's server logged it with your browser headers, IP address, and user agent.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

A rule then bounced you to a real search engine (Perplexity, Google, or Bing), so the results looked normal. The theft happened on that first stop, before the redirect.

The address bar made it worse. The extension also pointed the browser's live search suggestions (the suggest\_url) to the same attacker domain. So your input went to the attacker's server before you pressed Enter. Not just finished searches, but every character as you typed it.

[Chrome permits search-provider overrides](https://developer.chrome.com/docs/extensions/reference/manifest/chrome-settings-override), and legitimate extensions use them. Rewriting and redirecting your traffic is the part a search box has no business doing. This one asked for the declarativeNetRequest family of permissions to do exactly that, then shipped server-side code that logged every request. Microsoft calls that proof the collection was deliberate, not a side effect of the redirect.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqHW3E71Es3U6eAi9XuW_qcryhIUnObxunOS8DdoLk8u7IC4urSUHr_2G7bO9HDM3LJLZLoTzcahEg7sVRiD7sdfd6pj46qJLsbZVqK1ex-eCMEezhOLPETeQqPjPdCzpni_aX3Uz7NMjubtHhTWmn-ZIC8Y5npG98rlsKQC1bhgZudaiEdS_Pq5xB5Z0/s1700-e365/ai-code.jpg)

The extension also shipped disabled redirect rules for Google and Bing, so the same setup could be switched on for those engines too. It even left room to run WebAssembly code later, which a simple search tool has no reason to do.

This fits a steady run of malicious extensions that hide behind AI branding. Some [swap the default search engine to capture what you type](https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html). Others [hijack the search provider](https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html) or [skim ChatGPT and DeepSeek chats](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html). Microsoft's [own research](https://www.microsoft.com/en-us/security/blog/2026/03/05/malicious-ai-assistant-extensions-harvest-llm-chat-histories/) tied that chat-skimming wave to roughly 900,000 installs across more than 20,000 company networks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

The difference here is the target: not your AI chats, but your searches and the characters you type into the address bar, collected through Chrome's own extension machinery.

If you installed "Search for perplexity ai," remove it and check that your default search engine has not been changed. For teams, Microsoft suggests the basics:

* Allow only approved extensions through the browser or company policy.
* Watch for changed search settings, strange extension permissions, and traffic to unfamiliar domains.
* Treat AI-branded tools with extra suspicion, and check the publisher and domain before installing.

No one has been named as the operator, and Microsoft did not say how many people installed it before the takedown. The AI branding got the install. The search override did the collecting.

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [browser security](https://thehackernews.com/search/label/browser%20security), [chrome extension](https://thehackernews.com/search/label/chrome%20extension), [data theft](https://thehackernews.com/search/label/data%20theft), [Malware](https://thehackernews.com/search/label...