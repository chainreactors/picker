---
title: DeepSeek AI Database Exposed: Over 1 Million Log Lines, Secret Keys Leaked
url: https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html
source: The Hacker News
date: 2025-01-31
fetch_date: 2025-10-06T20:15:28.240276
---

# DeepSeek AI Database Exposed: Over 1 Million Log Lines, Secret Keys Leaked

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

# [DeepSeek AI Database Exposed: Over 1 Million Log Lines, Secret Keys Leaked](https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html)

**Jan 30, 2025**Ravie LakshmananArtificial Intelligence / Data Privacy

[![DeepSeek AI Database](data:image/png;base64... "DeepSeek AI Database")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl0nP3wD3UGFX0Lsg7dbi7N21AxNIK6jjR_Rs9eLzwoKem-ORdABiWtAZZ9x9HeL6_B-piJKXSdbGpqMHiEeD8fPWjPg4sZmS_T194r749jQOnXRHBZ26QdiB3YhhVEQkb7pXOJ3CVGIsiL_xmV6HAk-xWfPf-SwrXUneummi59z0d8Etog5mL_hapaxZX/s790-rw-e365/deepseek.png)

Buzzy Chinese artificial intelligence (AI) startup [DeepSeek](https://thehackernews.com/2025/01/top-rated-chinese-ai-app-deepseek.html), which has had a meteoric rise in popularity in recent days, left one of its databases exposed on the internet, which could have allowed malicious actors to gain access to sensitive data.

The ClickHouse database "allows full control over database operations, including the ability to access internal data," Wiz security researcher Gal Nagli [said](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak).

The exposure also includes more than a million lines of log streams containing chat history, secret keys, backend details, and other highly sensitive information, such as API Secrets and operational metadata. DeepSeek has since plugged the security hole following attempts by the cloud security firm to contact them.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The database, hosted at oauth2callback.deepseek[.]com:9000 and dev.deepseek[.]com:9000, is said to have enabled unauthorized access to a wide range of information. The exposure, Wiz noted, allowed for complete database control and potential privilege escalation within the DeepSeek environment without requiring any authentication.

This involved leveraging ClickHouse's HTTP interface to execute arbitrary SQL queries directly via the web browser. It's currently unclear if other malicious actors seized the opportunity to access or download the data.

"The rapid adoption of AI services without corresponding security is inherently risky," Nagli said in a statement shared with The Hacker News. "While much of the attention around AI security is focused on futuristic threats, the real dangers often come from basic risks—like the accidental external exposure of databases."

"Protecting customer data must remain the top priority for security teams, and it is crucial that security teams work closely with AI engineers to safeguard data and prevent exposure."

[![DeepSeek AI Database](data:image/png;base64... "DeepSeek AI Database")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx22ZGwBnL86Z_bFArM3-pHPQzQdrmgmSeYt4AZOhe9RtTPpoG7UJEldvLKQH65nqyuwzDAUHJJdHBo7OzoQQCUowd5ApSO2jiS41jEzDSMA5GFV8hXiSGo_c-TjDDWfalUxMrZd5Flb6sSQp21LNUKYMl6DzAuEQN37JXP-m8MTVIFATM33WgNgpcyR-a/s790-rw-e365/database-2.png)

[![DeepSeek AI Database](data:image/png;base64... "DeepSeek AI Database")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5Cr48thdK1SRKZKIff5M7eLk7e7CKTq9aJr08eV35P3tHtZqKJCMprdmy_dDZ6pMeaQ3hhtHec7UQBh04sjw4mrO9kkUPi3U5XdzqZSX8QgF7XMYMcHJW4oZxflSdhItVC6MD1zN4P1XnqhBgfs2-jBTjEZDynMy07-ep5ZHGJ7BMcgJPzkBhjeFXnpzu/s790-rw-e365/databse-1.png)

DeepSeek has become the topic du jour in AI circles for its groundbreaking open-source models that claim to rival leading AI systems like OpenAI, while also being efficient and cost-effective. Its reasoning model R1 has been [hailed](https://www.bbc.com/news/articles/cd643wx888qo) as "AI's Sputnik moment."

The upstart's AI chatbot has raced to the top of the app store charts across Android and iOS in several markets, even as it has emerged as the target of "large-scale malicious attacks," prompting it to temporarily pause registrations.

In an [update](https://status.deepseek.com/incidents/666k4t024szr) posted on January 29, 2025, the company said it has identified the issue and that it's working towards implementing a fix.

At the same time, the company has also been at the receiving end of scrutiny about its privacy policies, not to mention its Chinese ties becoming a matter of [national security concern](https://www.reuters.com/technology/artificial-intelligence/white-house-evaluates-china-ai-app-deepseeks-affect-national-security-official-2025-01-28/) for the United States.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Furthermore, DeepSeek's apps [became unavailable](https://www.reuters.com/technology/deepseek-app-unavailable-apple-google-app-stores-italy-2025-01-29/) in Italy shortly after the country's data protection regulator, the Garante, requested information about its data handling practices and where it obtained its training data. It's not known if the withdrawal of the apps was in response to questions from the watchdog. A similar request has been sent by the Irish Data Protection Commission (DPC) as well.

[Bloomberg](https://www.bloomberg.com/news/articles/2025-01-29/microsoft-probing-if-deepseek-linked-group-improperly-obtained-openai-data), [Financial Times](https://www.ft.com/content/a0dfedd1-5255-4fa9-8ccc-1fe01de87ea6), and [The Wall Street Journal](https://www.wsj.com/tech/ai/openai-china-deepseek-chatgpt-probe-ce6b864e) have also reported that both OpenAI and Microsoft are probing whether DeepSeek used OpenAI's application programming interface (API) without permission to train its own models on the output of OpenAI's systems, an approach referred to as [distillation](https://en.wikipedia.org/wiki/Knowledge_distillation).

"We know that groups in [China] are actively working to use methods, including what's known as distillation, to try to replicate advanced US AI models," an OpenAI spokesperson [told](https://www.theguardian.com/technology/2025/jan/29/openai-chatgpt-deepseek-china-us-ai-models) The Guardian.

Found this article interesting? Follow us on [Google News](https://news.google.c...