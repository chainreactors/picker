---
title: ChatGPT leaks bits of users' chat history
url: https://www.malwarebytes.com/blog/news/2023/03/chatgpt-reveals-chat-history-of-other-users
source: Over Security - Cybersecurity news aggregator
date: 2023-03-27
fetch_date: 2025-10-04T10:46:57.776215
---

# ChatGPT leaks bits of users' chat history

[ ]

[![ThreatDown Powered by Malwarebytes](https://www.threatdown.com/wp-content/themes/mbc/images/logo-header-threatdown-horizontal.svg)](https://www.threatdown.com/)

SUPPORT

* [Nebula support](https://support.threatdown.com/hc/en-us/)
* [OneView support](https://support.threatdown.com/hc/en-us/p/oneview)

SIGN IN

* [Nebula sign in](https://cloud.threatdown.com/auth/login)
* [OneView sign in](https://oneview.threatdown.com/)
* [Partner Portal sign in](https://partners.malwarebytes.com/English/)

[ ]

## Products

< Products

* ## Products
* [Endpoint Detection & Response (EDR)](/products/endpoint-detection-and-response/)
* [Endpoint Protection](/products/endpoint-protection/)
* [Vulnerability Assessment](/products/vulnerability-assessment/)
* [Patch Management](/products/patch-management/)
* [Application Block](/products/application-block/)
* [DNS Filtering](/products/dns-filtering/)
* [Mobile Security](/products/mobile-security/)
* [Email Security](/products/email-security/)

* ## Services
* [Managed Detection & Response (MDR)](/products/managed-detection-and-response/)
* [Managed Threat Hunting](/products/managed-threat-hunting/)
* [Premium Support](/products/premium-support/)

* ## Features
* [Browser Phishing Protection](/products/browser-phishing-protection/)
* [Firewall Management](/products/firewall-management/)
* [Security Advisor](/products/security-advisor/)

* ## Platforms
* [Nebula](/products/nebula/)
* Manage your organization’s endpoint security in a single-tenant console

  [Nebula customer sign in >](https://cloud.threatdown.com/auth/login)
* [OneView](/products/oneview/)
* Provides MSPs centralized visibility and management capabilities across customer sites

  [OneView customer sign in >](https://oneview.threatdown.com/auth/login)

[ ]

## Partners

< Partners

* [Explore Partnerships](/partner-program/)
* Review program benefits, innovative technology, channel first mentality
* [Managed Service Providers](/partner-program/msp/)
* Everything MSPs need to run their business seamlessly

* [Technology Partners](/technology-integrations/)
* Explore our technology integrations
* [Resellers](/partner-program/partner-reseller/)
* Build growth, profitability, and customer loyalty

* ![](https://www.threatdown.com/wp-content/uploads/2023/11/px-center.png?w=356)
* Retain and grow your business with tools, education, and support in the partner experience center.

  [Sign in to PXC >](https://partners.threatdown.com/English/%20)

[ ]

## Resources

< Resources

* [Threat Center](/threat-center/)
* Learn about the latest threat news
* [Reports](/threat-center/reports/)
* [Threat Detections](/threat-detections/)
* [Executive POV](/threat-center/executive-pov/)
* [Glossary](/glossary/)
* [Blog](/blog/)

* [Resource Center](/resources/)
* Learn more about ThreatDown
* [ThreatDown News](/press/)
* [Case Studies](/resources/categories/case-studies/)
* [Reviews](/resources/categories/products/)
* [Cybersecurity Tips & Tricks](/resources/categories/cybersecurity-tips-tricks/)
* [Webinars](/resources/categories/webinars/)
* [About Us](/about-us/)

* ![2025 State of Ransomware: Inside a record-breaking year of ransomware attacks](https://www.threatdown.com/wp-content/uploads/2025/08/2025-state-of-ransomware.png?w=1246)
* Discover a record-breaking year of attacks where ransomware became decentralized and unpredictable, spreading further than ever before.

  [Download now >](https://www.threatdown.com/dl-state-of-ransomware-2025/)

[Pricing](/pricing/)

[ ]

## Why ThreatDown

< Why ThreatDown

* ## Why ThreatDown
* [About Us](/about-us/)
* [ThreatDown vs. Competition](/vs/)
* [Case Studies](/resources/categories/case-studies/)

* ![](https://www.threatdown.com/wp-content/uploads/2025/04/product-of-the-year-nav.png?w=712)
* ThreatDown named Product of the Year by MRG Effitas.

  [Learn more >](https://www.threatdown.com/blog/product-of-the-year/)

[Get a quote](/custom-quote/)

[Buy now](/pricing/)

[Home](/)
>
[Blog](/blog/)

![](https://www.threatdown.com/wp-content/uploads/2024/04/Chat_GPT_Leaks.png?w=1024)

[Breaches](https://www.threatdown.com/blog/category/breaches/)

## ChatGPT leaks bits of users’ chat history

March 24, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

New gadgets and software come with new bugs, especially if they’re rushed. We can see this very clearly in the race between tech giants to push large language models (LLMs) like ChatGPT and its competitors out the door. In the most recently revealed LLM bug, ChatGPT allowed some users to see the titles of other users’ conversations.

LLMs are huge deep-neural-networks, which are trained on the input of billions of pages of written material.

In the words of ChatGPT itself:

> “The training process involves exposing the model to vast amounts of text data, such as books, articles, and websites. During training, the model adjusts its internal parameters to minimize the difference between the text it generates and the text in the training data. This allows the model to learn patterns and relationships in language, and to generate new text that is similar in style and content to the text it was trained on.”

We have written before about tricking LLMs in to behaving in ways they aren’t supposed to. We call that [jailbreaking](https://www.threatdown.com/blog/jailbreaking-chatgpt-and-other-large-language-models-while-we-can/). And I’d say that’s fine. It’s all part of what could be seen as a beta-testing phase for these complex new tools. And as long as we report the ways in which we are able to exceed the limitations of the model and give the developers a chance to tighten things up, we’re working together to make the models better.

But, when a model spills information about other users we stumble into an area that should have been sealed off already.

To understand better what has happened, it is necessary to have some basic working knowledge about how these models work. To improve the quality of the responses they get, users can organize the conversations they have with the LLM into a type of thread, so that the model, and the user, can look back and see what ground they have covered and what they are working on.

With ChatGPT, each conversation with the chatbot is stored in the user’s chat history bar where it can be revisited later. This gives the user an opportunity to work on several subjects and keep them organized and separate.

![](https://www.threatdown.com/wp-content/uploads/2024/04/easset_upload_file88459_262527_e.webp?w=260)

Showing this history to other users would, at the very least, be annoying and unacceptable, because it could be embarrassing or even give away sensitive information.

![](https://www.threatdown.com/wp-content/uploads/2024/04/easset_upload_file79585_262527_e.webp?w=260)

Nevertheless, this is exactly what happened. At some point, users started noticing items in their history that weren’t their own.

Although OpenAI reassured users that others could not access the actual chats, users were understandably worried about their privacy.

According to [an OpenAI spokesperson on Reddit](https://www.reddit.com/r/ChatGPT/comments/11yw746/chatgpt_security_update_from_sam_altman/) the underlying bug was in an open source library.

![](https://www.threatdown.com/wp-content/uploads/2024/04/easset_upload_file85049_262527_e.webp?w=637)

OpenAI CEO Sam Altman said the company feels “awful”, but the “significant” error has now been fixed.

## Things to remember

Giant, interactive LLMs like ChatGPT are still in the early stages of development and, despite what some want us to believe, they are neither the answer to everything nor the end of the world. At this point they are just very limited search engines that rephrase what they found about the subject you asked about, unlike an “old-fashioned” search engine that shows you possible sources of information and you can decide which ones are trustworthy and which ones aren’t.

When ...