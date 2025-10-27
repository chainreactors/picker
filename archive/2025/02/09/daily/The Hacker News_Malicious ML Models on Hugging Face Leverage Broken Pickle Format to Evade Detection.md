---
title: Malicious ML Models on Hugging Face Leverage Broken Pickle Format to Evade Detection
url: https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html
source: The Hacker News
date: 2025-02-09
fetch_date: 2025-10-06T20:37:58.651840
---

# Malicious ML Models on Hugging Face Leverage Broken Pickle Format to Evade Detection

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

# [Malicious ML Models on Hugging Face Leverage Broken Pickle Format to Evade Detection](https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html)

**Feb 08, 2025**Ravie LakshmananArtificial Intelligence / Supply Chain Security

[![Malicious ML Models](data:image/png;base64... "Malicious ML Models")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiy9HRla2vCXTJvnM3vT93AmKbjqs9stovOJ537UUG3Uq_M-ZPX2Yd45EZH9mCfek0Mi11XBLVV5yZjxpHBmvUnWkaYjlRlG9ASGHpXTwjd40LkrKauR0WuaaH62q7x9en4RowtY8zBugXEBETIiT_PLPlhK8Czmz_V79IcsE5QCEE521sWAu16DrtsMn8R/s790-rw-e365/hugging-face-malware.png)

Cybersecurity researchers have uncovered two malicious machine learning (ML) models on Hugging Face that leveraged an unusual technique of "broken" pickle files to evade detection.

"The pickle files extracted from the mentioned PyTorch archives revealed the malicious Python content at the beginning of the file," ReversingLabs researcher Karlo Zanki [said](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face) in a report shared with The Hacker News. "In both cases, the malicious payload was a typical platform-aware reverse shell that connects to a hard-coded IP address."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The approach has been dubbed nullifAI, as it involves clearcut attempts to [sidestep existing safeguards](https://checkmarx.com/blog/free-hugs-what-to-be-wary-of-in-hugging-face-part-4/) put in place to identify malicious models. The Hugging Face repositories have been listed below -

* glockr1/ballr7
* who-r-u0000/0000000000000000000000000000000000000

It's believed that the models are more of a proof-of-concept (PoC) than an active supply chain attack scenario.

The pickle serialization format, used commonly for distributing ML models, has been [repeatedly found](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html) to be a security risk, as it offers ways to execute arbitrary code as soon as they are loaded and deserialized.

[![Malicious ML Models](data:image/png;base64... "Malicious ML Models")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhOkjwZiNh4b2foWpp2iLABOWeXkHhZNTnCg4lwPGL4869tsQ8cCg81ZX9_QEi-u91o6XPxSPwhKdwLflJZGYNKu-Sksm7QJrNgoQgszGNHHRyPSg4KC8jwwU55_7l1fwLRr2A5z_4ZZ1Mw-76S6OSKMDuzkfpsZ_5QZAybVNAEVCHNukOX07jOi3VeqTj/s790-rw-e365/code.png)

The two models detected by the cybersecurity company are stored in the PyTorch format, which is nothing but a compressed pickle file. While PyTorch uses the ZIP format for compression by default, the identified models have been found to be compressed using the 7z format.

Consequently, this behavior made it possible for the models to fly under the radar and avoid getting flagged as malicious by Picklescan, a tool used by Hugging Face to detect suspicious Pickle files.

"An interesting thing about this Pickle file is that the object serialization — the purpose of the Pickle file — breaks shortly after the malicious payload is executed, resulting in the failure of the object's decompilation," Zanki said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Further analysis has revealed that such broken pickle files can still be partially deserialized owing to the discrepancy between Picklescan and how deserialization works, causing the malicious code to be executed despite the tool throwing an error message. The open-source utility has since been [updated](https://github.com/mmaitre314/picklescan) to rectify this bug.

"The explanation for this behavior is that the object deserialization is performed on Pickle files sequentially," Zanki noted.

"Pickle opcodes are executed as they are encountered, and until all opcodes are executed or a broken instruction is encountered. In the case of the discovered model, since the malicious payload is inserted at the beginning of the Pickle stream, execution of the model wouldn't be detected as unsafe by Hugging Face's existing security scanning tools."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data security](https://thehackernews.com/search/label/data%20security)[machine learning](https://thehackernews.com/search/label/machine%20learning)[malware analysis](https://thehackernews.com/search/label/malware%20analysis)[Open Source](https://thehackernews.com/search/label/Open%20Source)[PyTorch](https://thehackernews.com/search/label/PyTorch)[Supply Chain Security](https://thehackernews.com/search/label/Supply%20Chain%20Security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[...