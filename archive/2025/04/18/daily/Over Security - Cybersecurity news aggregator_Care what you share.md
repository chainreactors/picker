---
title: Care what you share
url: https://blog.talosintelligence.com/care-what-you-share/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-18
fetch_date: 2025-10-06T22:06:12.936707
---

# Care what you share

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Care what you share

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, April 17, 2025 14:01

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

As we navigate our daily routines, certain tasks become second nature to us, especially if they are integral to our professions. However, what feels instinctive to one person might be foreign to another. This disparity is akin to a skilled musician effortlessly playing a complex melody, while someone without musical training might appreciate the beauty of the music in a different way. Both may enjoy music, but they experience it from different perspectives.

Lately, I've found myself thinking about these differences in the context of online interactions, particularly with search engines. I've become increasingly frustrated with how they try to influence my buying behavior or try to “enhance” search results with AI. It's often unsuccessful, as many of you have experienced. I once looked up something for my father-in-law and got swamped for weeks after with advertisements absolutely irrelevant to me.

It's easy to overlook that when using a search engine, the exchange of knowledge is not one-sided. It's not only users who gain knowledge from indexed content, but search engines also acquire detailed insights into user behavior and preferences. You may unknowingly share sensitive information that could be stored for extended periods or shared with third parties for advertising or other purposes. I tried to get around this by shifting to privacy-focused search engines but wasn’t happy with the experience, either because of smaller or different indexes, or I was missing results in my native language.

Luckily, I came across an open-source project called [SearXNG](https://docs.searxng.org/), a “free internet metasearch engine which aggregates results from up to 229 search services. Users are neither tracked nor profiled.”

I like it for three reasons:

1. You can try one of the [public instances](https://searx.space/) and check if you like it before you go all-in.
2. You can self-host it on bare metal, in Docker or LXC, giving you even more control over your data.
3. With [Opensearch](https://docs.searxng.org/user/about.html#how-do-i-set-it-as-the-default-search-engine) it seamlessly integrates with your existing browser.

It took me a couple of days to get used to it, but I do really like it now. It’s not perfect, but it is a real timesaver. As a bonus, the search syntax for advanced use is easy to memorize:

* “:en”, “:de” or “:fr” to search in a given language
* “!social\_media” or “!news” to search just a given category

The same principle applies to the increasing number of AI and large language models (LLMs) that process your queries — they also gather information about you. There are initiatives like Perplexica on GitHub that aim to bridge the gap for AI-assisted searches, although I haven't explored them in detail. Additionally, if your interactions extend beyond simple searches to more profound inquiries, such as asking an LLM about the meaning of life, it's wise to first assess the trustworthiness of the engine or the company behind it. Care what you share.

## The one big thing

We are continuing our discussion of Talos' [2024 Year in Review](https://blog.talosintelligence.com/2024yearinreview/) report, looking at each section in detail. This week, let’s examine [ransomware](https://blog.talosintelligence.com/year-in-review-ransomware/).

### Why do I care?

Ransomware actors overwhelmingly leveraged valid accounts for initial access in 2024, with this tactic appearing in almost 70% of related cases.

Ransomware actors exploited public-facing applications nearly 20% of the time. The Known Exploited Vulnerabilities Catalog for 2024 lists 28 out of 186 Vulnerabilities as “Known to be used in Ransomware Campaigns” with CVE ID’s all the way from 2012-2024 (except for 2015).

### So now what?

These are major risks which can be mitigated by applying basic cyber hygiene principles. Please update and patch your software, and protect your credentials. Tune in next week to learn about multi-factor authentication (MFA) and identity threats, and why you need to do more than just enable MFA.

## Top security headlines of the week

* **OpenAI cuts safety tests in “reckless” AI push.** According to the article, testing has gone down from six months to just days. We all know that even with six months of testing any model, it’ll never be quite perfect. ([MSN](https://www.msn.com/en-us/news/technology/openai-cuts-safety-tests-in-reckless-ai-push/ar-AA1CJmYp?ocid=socialshare&cvid=0d9bd7ed158348b98829bf11a9c3d61c&ei=70)) Further compounding this:
* **AI-hallucinated code dependencies become new supply chain risk.** “Slopsquatting” (as a spin on typosquatting) has become a thing. Threat actors can check with one or more AI models what packages they hallucinate and upload their malicious ones to PyPI or npm. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/))
* **Windows Recall seems to be back again.** More privacy-related news. If I recall (pun intended) correctly, in May last year Microsoft introduced Recall — a feature which constantly takes screenshots, indexes them, and makes them searchable for you. After huge backslashes in the community, and the creation of tools like [TotalRecall](https://github.com/xaitax/TotalRecall), Microsoft paused the launch last June. ([BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-starts-final-windows-recall-testing-before-rollout/))
* **The 25-year-old CVE program seemed to be at risk.** MITRE warned on April 15 that...