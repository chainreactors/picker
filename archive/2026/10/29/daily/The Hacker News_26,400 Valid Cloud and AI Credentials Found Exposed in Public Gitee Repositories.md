---
title: 26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories
url: https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html
source: The Hacker News
date: 2026-10-29
fetch_date: 2026-10-30T07:56:33.887945
---

# 26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [26,400 Valid Cloud and AI Credentials Found Exposed in Public Gitee Repositories](https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html)

**Swati Khandelwal**Oct 29, 2026Cloud Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwVszv5076OudfiraNA4yh_XuzZZof-jYaklwUgiY700oPMvBHQfKHx-8yLNwhF9NVXahFRvWwU7c0mPCsIG-GUo45Fi_LT6ecZMsaRUfaLIL6eK16qeku1PO5aMTQRV0VKJh-pjKG4rC-RyajCGjL4R_A5W6YPsps4B4-GhEbstuAN7AnelVJPwIFK5W-/s1700-nu-rw-lo-l85-e365/gite.jpg)

26,400 credentials that developers left in public code on **Gitee**, a Chinese code-hosting service, still worked when a researcher tested them. Anyone who copied one from that code could have used it.

Independent researcher **Ben Zimmermann** found them by scanning 7.25 million public Gitee repositories and [reported the results](https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets) on October 28. Most were keys for cloud and AI services, led by 9,473 Alibaba Cloud AccessKey pairs.

Zimmermann sent the vendors with the most exposed keys a list of their credentials, but he did not contact the developers who leaked them. When he published, he had not confirmed that any of the reported credentials had been revoked. So anyone who has pushed a key to a public Gitee repository cannot assume it has been revoked.

The scan ran for about a month, but Zimmermann did not provide the dates, so it is unclear how long ago the credentials were tested. He also did not say whether anyone else had used them.

He ran two secret scanners, [TruffleHog](https://github.com/trufflesecurity/trufflehog) and [Kingfisher](https://github.com/mongodb/kingfisher), over every repository. Both tried each credential against the service that issued it and kept only those that worked, he wrote.

The scanners read each repository's full commit history. A key that a developer later removed from the code could still be found and counted there.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

The 26,400 figure counts each credential once, regardless of how many repositories it appeared in. By commit date, 12,242 of the credentials came from 2025, nearly half the total. Some dated to the late 2000s.

### What Was Exposed

After the Alibaba Cloud keys, the largest groups were 3,805 YouTube API keys, 3,170 DeepSeek keys, 1,489 keys for Zhipu's BigModel AI platform, and 1,348 OpenAI keys. Smaller numbers were found for GitHub, AWS, Google Cloud and Google's Gemini.

One of the credentials was "an active organization-admin credential for a major enterprise AI platform," Zimmermann wrote. He did not name the platform or say what the credential could reach.

What a working key lets someone do depends on the service. OpenAI says that a compromised key allows another person to use the account's quota without the owner's consent. That can cause "data loss, unexpected charges," a used-up monthly quota, and interrupted API access.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEga096EUb7qYUKJFGjrS1qU6VeOHLnnXj5gB6QDaHBmu02_5NIj1dlmNXFSDZt3eUmJOhLXMjERhXoies74Bp_y1EG-rKxaQOwQJg5XiVOm2wwDlopXk6iE86JNjE0WePWESyPfbVfdmVQ3QqgbVVunXJTeJTkjvVY02WcZ3UZEj4ML8-Np5jnpIaZgxbU/s1700-nu-rw-lo-l85-e365/1.png)

A YouTube API key is a Google Cloud API key that identifies a project, [Google says](https://developers.google.com/youtube/registering_an_application). Without API restrictions, such a key can be used with every API that accepts Google Cloud keys.

### What to Do If You Committed Keys

Treat any key that has ever been in a public Gitee repository as exposed, and revoke it at the provider. Deleting a key from the code or rewriting the repository's history [does not revoke it](https://trufflesecurity.com/blog/why-exposed-credentials-stay-live-for-years), as noted by TruffleHog's maker, Truffle Security.

* **Alibaba Cloud:** create a new AccessKey pair, switch your apps to it, then disable and delete the old pair. Check for unexpected charges and for resources created or deleted that you did not need, Alibaba Cloud's [leak response plan](https://help.aliyun.com/en/ram/user-guide/solution-to-accesskey-leakage) says. ActionTrail shows the key's API calls for the last 90 days, but data operations in services such as OSS and SLS have to be checked in each service's own logs.
* **Google and YouTube API keys:** [rotate the key](https://docs.cloud.google.com/docs/authentication/api-keys), which creates a new key with the same restrictions, update your apps to use it, then delete the old key. Add API restrictions so the key works only with the APIs you need.
* **OpenAI:** rotate the key immediately from the API Keys page, [as OpenAI advises](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety), and set spend limits to help limit charges from a leaked key.

### Two Scanners, Different Results

MongoDB makes Kingfisher, and Zimmermann's post was developed with its Kingfisher team.

In this scan, TruffleHog found 12,737 credentials that worked, and Kingfisher found 14,664, but only 1,001 were found by both. Each tool alone found about half of the total.

TruffleHog found almost all of the Alibaba Cloud keys. Kingfisher found all 1,489 BigModel keys, because TruffleHog has no detector for Zhipu's keys, Zimmermann wrote.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Teams that rely on a single scanner should verify its detectors against the services they use.

### Gitee and Other Code Hosts

China's Ministry of Industry and Information Technology [chose Gitee in 2020](https://blog.gitee.com/2020/08/17/gitee-gxb/) as the base for a national open-source code-hosting platform.

Gitee's public API is limited, and a [2021 attempt](https://chinggg.github.io/post/git-leaks/) to study leaked cr...