---
title: WhatsApp Launches Private Processing to Enable AI Features While Protecting Message Privacy
url: https://thehackernews.com/2025/04/whatsapp-launches-private-processing-to.html
source: The Hacker News
date: 2025-04-30
fetch_date: 2025-10-06T22:07:25.531848
---

# WhatsApp Launches Private Processing to Enable AI Features While Protecting Message Privacy

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

# [WhatsApp Launches Private Processing to Enable AI Features While Protecting Message Privacy](https://thehackernews.com/2025/04/whatsapp-launches-private-processing-to.html)

**Apr 29, 2025**Ravie LakshmananArtificial Intelligence / Data Protection

[![WhatsApp Launches Private Processing](data:image/png;base64... "WhatsApp Launches Private Processing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfcw2wP2oQTe0N7dyUblwsIYeitRdkPuOatf036QBHIlqWdDWBjTAfyUE159EbMqw4xEMSoDTN5B1ZPnqSW_ykKvSHrvBAJqtg3vj72nZqAxKbh_xQ4j4EQR0DjI9Rp88Hj6AsHkRQ_LE_5Bzi1tmrxHtEpN226qSKrlGZWw-ozxch51BJml48zd8ApGWZ/s790-rw-e365/whatsapp.jpg)

Popular messaging app WhatsApp on Tuesday unveiled a new technology called Private Processing to enable artificial intelligence (AI) capabilities in a privacy-preserving manner.

"Private Processing will allow users to leverage powerful optional AI features – like summarizing unread messages or editing help – while preserving WhatsApp's core privacy promise," the Meta-owned service said in a statement [shared](https://engineering.fb.com/2025/04/29/security/building-private-processing-for-ai-tools-on-whatsapp/) with The Hacker News.

With the introduction of the latest feature, the idea is to facilitate the use of AI features while still keeping users' messages private. It's expected to be made available in the coming weeks.

The capability, in a nutshell, allows users to initiate a request to process messages using AI within a secure environment called the confidential virtual machine (CVM) such that no other party, including Meta and WhatsApp, can access them.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Confidential processing is one of the three tenets that underpin the feature, the others being -

* Enforceable guarantees, which cause the system to fail or become publicly discoverable when attempts to modify confidential processing guarantees are detected
* Verifiable transparency, which allows users and independent researchers to audit the behavior of the system
* Non-targetability, which prevents a particular user from being targeted without breaching the whole security architecture
* Stateless processing and forward security, which ensures that messages are not retained once the messages are processed so that an attacker cannot recover historical requests or responses

The system is designed as follows: Private Processing obtains anonymous credentials to verify that future requests are coming from a legitimate WhatsApp client and then proceeds to establish an Oblivious HTTP ([OHTTP](https://thehackernews.com/2024/03/google-introduces-enhanced-real-time.html)) connection between the user's device and a Meta gateway via a third-party relay that also hides the source IP address from Meta and WhatsApp.

A secure application session is subsequently established between the user's device and the Trusted Execution Environment (TEE), following which an encrypted request is made to the Private Processing system using an ephemeral key.

This also means that the request cannot be decrypted by anyone other than the TEE or the user's device from which the request (e.g., message summarization) is sent.

The data is processed in CVM and the results are sent back to the user's device in an encrypted format using a key that's accessible only on the device and the Private Processing server.

Meta has also acknowledged the various threat vectors that could expose the system to potential attacks via compromised insiders, supply chain risks, and malicious end users, but emphasised it has adopted a defense-in-depth approach to minimize the attack surface.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Furthermore, the company has pledged to publish a third-party log of CVM binary digests and CVM binary images to help external researchers "analyze, replicate, and report instances where they believe logs could leak user data."

The development comes as Meta [released](https://about.fb.com/news/2025/04/introducing-meta-ai-app-new-way-access-ai-assistant/) a dedicated Meta AI app built with Llama 4 that comes with a "social" Discover feed to share and explore prompts and even remix them.

Private Processing, in some ways, mirrors Apple's approach to confidential AI processing called Private Cloud Compute ([PCC](https://thehackernews.com/2024/06/apple-integrates-openais-chatgpt-into.html)), which also routes PCC requests through an OHTTP relay and processes them in a sandboxed environment.

Late last year, the iPhone maker [publicly made available](https://thehackernews.com/2024/10/apple-opens-pcc-source-code-for.html) its PCC Virtual Research Environment (VRE) to allow the research community to inspect and verify the privacy and security guarantees of the system.

*(The story was updated after publication to make it clear that compromised insiders, supply chain risks, and malicious end users are examples of potential threat scenarios and not a weak link as previously stated.)*

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity]...