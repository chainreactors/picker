---
title: OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms
url: https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html
source: The Hacker News
date: 2026-11-22
fetch_date: 2026-11-23T10:02:57.450126
---

# OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [OpenRouter Drops 3 Providers After Researchers Catch Months of Prompt Theft at AI Hosting Firms](https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html)

**Swati Khandelwal**Nov 22, 2026Artificial Intelligence / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEGP3P_elvK4C-QnSx5onZ67viDXCIgPCUYqtTF_RDNcLJfyQ4QMbegUmn8AJy5nEmnXfN4ACr6hHztG_DdqXlj54S21toacPQaZgRx2rgqZltN3lvREpZR2xlvgXF_iZ7zW0XT0b91mMiRDVaEB6TUvMFlWwaSa3_C7gwpxdKcNhLtIq15KqwaZrR3VI/s1700-nu-rw-lo-l85-e365/openrouter.png)

Attackers stole data from inside three AI inference providers for months, and none of the three knew until researchers told them, the industrial cybersecurity company Dragos said this week.

Some of the stolen requests were flagged as **Zero Data Retention**, the setting that is supposed to mean a prompt is never stored.

**OpenRouter**, a gateway that routes customers' AI requests to a pool of third-party providers, said today that it has removed three providers from its platform, removed 125 endpoints from eligibility for Zero Data Retention, and notified all potentially affected customers. The findings showed no breach of OpenRouter itself, the company said.

The earliest of the three breaches began in mid-July. The planted prompts were bait, but they were processed alongside real customer requests, and those were almost certainly copied too, the firm said.

The finding comes from [canary token research](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) that seeded about two million prompts with unique web links and credentials between July and November, then watched for anyone using them. A planted secret can only be learned in one place, so any use of it means someone read the prompt that carried it.

The largest of the three breaches involved a couple hundred AWS keys that were planted, each sent in exactly one request to one provider during a few short windows in late October. Every request sent during those windows was stolen, and some came from requests the provider had rejected before a model ever ran, indicating the attacker was copying traffic at the first point of arrival rather than deeper in the inference stack.

The thief tested keys within hours in some cases, listed S3 buckets, searched Secrets Manager and Parameter Store, and tried to create Bedrock API keys and add IAM users to keep access, driving tens of thousands of AWS API calls.

One attacker appears to have compromised two of the providers at once, using secrets from both from a single rented server.

On November 1, the same attacker brought in ARTEX, an AI-driven penetration testing framework, and used it only to confirm that keys it already held were still live. Two of its user agents, artex-agent and artex-judge-r121, appear in no public indicator list the firm could find and are worth adding to detections.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

"A privacy flag doesn't help when the attacker is already inside," wrote HD Moore, the firm's chief research officer.

The second finding needed no break-in. Sellers on an AI inference marketplace listed models at the lowest prices, enabled request logging, and collected what flowed through, the research found.

The people doing it looked like individuals on home internet connections. One, working from a Mac on home broadband in France, took passwords from two prompts and typed root SSH login attempts by hand, then used the same machine to test several planted AWS keys.

One of those keys had traveled through a different router that quietly forwarded some of its traffic to the marketplace, a hop that no customer was told about. That router has since told the firm it stopped, and route tracing across about 2,000 paths found several hundred unidentified systems, plus one seller that quietly adds about 1,000 hidden tokens to every prompt.

A Chinese AI lab, which the research does not name, fetched the secret links from more than half of the seeded prompts sent to its models between July and October, including about two-thirds of the requests marked no data collection or Zero Data Retention. Prompts sent to U.S. hosting providers that resell the lab's models triggered the same scraper, thereby flowing back to the lab.

A git client on another cloud later tried to clone private repositories referenced in the prompts, but only for that lab's models, and one large U.S. provider kept crawling a secret link more than two months after a single request to its search endpoint.

Twenty-four days after one prompt was sent, its secret link was posted into a chat on Feishu, the Chinese workplace app known as Lark elsewhere. The link was opened within two minutes from three desktops and three phones in Beijing and Shanghai.

The firm had disclosed only the first 8 characters of the provider's link, so whoever posted it was reading a cached copy of the full prompt.

In practice, Moore wrote, the flagged prompts were kept, passed to other companies, and read by human beings.

OpenRouter said in an [incident announcement](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) that the 125 endpoints removed from Zero Data Retention eligibility cover providers flagged by the researchers plus others cut as a precaution. Any endpoint removed during the review will require assurances and validation before its status is returned.

The gateway is adapting the researchers' testing approach so that the checks can run on an ongoing basis and is verifying network paths to identify where requests and responses may be forwarded to third parties.

The researchers are now working with about a dozen providers, and planted keys and secret links were still being accessed months after the first thefts, as of this week.

Railway, a platform company, said in October that an [intrusion it suffered](https://thehackernews.com/2026/10/railway-says-intruder-m...