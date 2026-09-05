---
title: Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters
url: https://thehackernews.com/2026/09/phishing-campaign-sends-millions-of.html
source: The Hacker News
date: 2026-09-04
fetch_date: 2026-09-05T06:30:35.874344
---

# Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Phishing Campaign Sends Millions of Emails Using Invisible Unicode to Evade Filters](https://thehackernews.com/2026/09/phishing-campaign-sends-millions-of.html)

**Ravie Lakshmanan**Sep 04, 2026Email Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoD4eMYuhLT8HvcHbYe8A4hkhmDH1f4pIWTIm5AXKueqdpY1NS8yNiTtlzS4mdIS8PLY8_zM1uQDNpO1U49HCUoJT8nn2Bpb6krpcYpOSQ3H3Z6fUsm-UkoFvj8fk8oShK0eUhO6px8hox_ZzlnX8tu0pJKpJ3UAF2Vcb3XyBXjCt_8uD8OOkMMgUjv8Pc/s1700-nu-rw-lo-l85-e365/emails.jpg)

Microsoft is alerting of a "high-volume phishing campaign" that's using invisible Unicode tag characters to bypass email filters.

"Instead of using these characters to hide instructions from people while exposing them to AI models, the attacker used them to split financial lure words such as 'funding' to prevent email filters from parsing them," the Microsoft Security Research team [said](https://www.microsoft.com/en-us/security/blog/2026/09/03/ascii-smuggling-crosses-over-from-ai-prompt-injection-to-phishing-evasion/).

The Windows maker said the findings show AI-era evasion techniques can be adapted by threat actors in traditional phishing and spam campaigns. Attacks exploiting this approach are said to have first emerged in early February 2026.

ASCII Smuggling refers to a technique where invisible or non-rendering Unicode characters are used to conceal messages or instructions inside seemingly-harmless text. As a result, human user interfaces do not render them, making the text appear completely normal to the user.

However, such content can be ingested by email filters or AI language models, mistakenly treating it as real text. This, in turn, can open the door to prompt injection by taking advantage of the fact that large language models (LLMs) cannot draw a reliable boundary between genuine user instructions entered directly into a prompt and content embedded into benign-looking text or other third-party sources such as web pages, documents, or emails.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"The most abused range is the Unicode Tags block, U+E0000 to U+E007F," Microsoft said. "This block contains a shadow copy of the printable ASCII characters (for example, U+E0041 mirrors 'A,' U+E0061 mirrors 'a'). The block was originally intended for language tagging and is now largely deprecated."

According to the Windows maker, the ASCII smuggling-oriented phishing campaign entered into a high-volume phase for roughly three months before dropping sharply post May 15, 2026. The activity is said to have followed a weekly cadence, with the campaign almost going radio silent on weekends and resuming in full swing on Mondays.

Weekday volumes are estimated to reach anywhere between 1 to 2.37 million messages, hitting a peak on February 26, 2026. The campaign is assessed to be tied to a broader phishing campaign that weaponized the ActiveCampaign marketing and automation platform to distribute thousands of AI-generated phishing emails targeting Small Business Administration (SBA) loan applicants.

Details of the phishing campaign were disclosed by the Fortra Intelligence and Research Experts (FIRE) team in September 2025, stating the operation focuses on collecting detailed business and financial information, likely to enable highly targeted spear‑phishing in future attacks.

"The campaign's sophistication and uniqueness lies in the ability to mass‑produce convincing, tailored websites that adapt to different illegitimate or impersonated domains," Fortra [noted](https://www.fortra.com/blog/attackers-exploit-activecampaign-deliver-thousands-ai-generated-sba-phish) at the time. "Threat actors are able to scale sophisticated phishing by using ActiveCampaign's AI-powered marketing automation features to vary the design, content, and flow, ultimately creating more convincing phishing campaigns, quicker."

The latest set of phishing emails, per Microsoft, leverages the invisible tag characters as an obfuscation pattern, inserting them inside common financial keywords so as to split them apart and get around email filters looking for keyword or literal signature matches.

For instance, a finance-related lure term such as "funding" becomes "fun⟨U+E0020⟩ding," so that it looks normal to the email recipient while having the side effect of bypassing email security controls.

"To a recipient, and to parsing pipelines that drop or normalize these characters, the word still reads as funding," Microsoft explained. "To a detector matching the literal string funding, or a regex that does not account for interleaved invisible code points, the byte sequence no longer contains the contiguous keyword."

While the use of invisible or look-alike characters is not a new technique in phishing and [homoglyph attacks](https://thehackernews.com/2025/10/fake-nethereum-nuget-package-used.html), what's novel is the choice of the characters used – namely, the Unicode Tags block – and the scale of the campaign itself, which has generated multi-million messages on a daily basis.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

The campaign has been found to leverage hundreds of disposable, finance-themed sender domains using lures that mimicked business loan, line-of-credit, and advance-funding phishing patterns that are typically associated with fraud or credential-harvesting schemes. The top 10 sender domains by the most hits are listed below -

* guardiangrowthfunding[.]com
* digitalcapitalboost[.]com
* thebusinessloanexpress[.]com
* yourlocfunding[.]com
* advancefundingboost[.]com
* guardiancapitalway[.]com
* harboradvancefunding[.]com
* unitedfundingwave[.]com
* directcapitalboost[.]com
* onlinedirectfinance[.]com

What's more, these emails from these finance-themed domains are relayed through ActiveCampaign, causing every outbound link in the message body to be routed vi...