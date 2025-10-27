---
title: How We Discovered a Stored HTML Injection in a Chatbot System ️
url: https://infosecwriteups.com/how-we-discovered-a-stored-html-injection-in-a-chatbot-system-%EF%B8%8F-6cbefe8b0718?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-28
fetch_date: 2025-10-06T23:17:54.015634
---

# How We Discovered a Stored HTML Injection in a Chatbot System ️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6cbefe8b0718&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-we-discovered-a-stored-html-injection-in-a-chatbot-system-%25EF%25B8%258F-6cbefe8b0718&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-we-discovered-a-stored-html-injection-in-a-chatbot-system-%25EF%25B8%258F-6cbefe8b0718&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6cbefe8b0718---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6cbefe8b0718---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How We Discovered a Stored HTML Injection in a Chatbot System 🕷️

[![Het Patel](https://miro.medium.com/v2/resize:fill:64:64/1*0xmi1m3lKtIdhh3vz8hFsA.jpeg)](https://hettt.medium.com/?source=post_page---byline--6cbefe8b0718---------------------------------------)

[Het Patel](https://hettt.medium.com/?source=post_page---byline--6cbefe8b0718---------------------------------------)

3 min read

·

Jun 6, 2025

--

1

Listen

Share

Press enter or click to view image in full size

![]()

*This write-up has been prepared under the guidance of* [*Amish Patel*](https://medium.com/%40cyberexpertamish)*,* [*Lay Patel*](https://medium.com/%40cynex) *at* [*Hacker4Help*](https://medium.com/%40hacker4help) *as part of our learning initiative on cybersecurity awareness.*

## 🔍 Introduction

As budding cybersecurity enthusiasts, we’re always on the lookout for vulnerable systems that can help us learn and sharpen our skills. One casual evening of testing led us — **Het Patel** and [**Kaif Shah**](https://medium.com/%40SKaif009) — to discover a **Stored HTML Injection vulnerability** in the chatbot feature of redacted[.co.in](https://pyng.co.in), an AI-driven platform that connects users with verified professional experts across various categories.

![]()

So Let’s get started **😎**

## What is Stored HTML Injection? 💥

Before we dive into the juicy details, let’s break down what **Stored HTML Injection** actually is (because not everyone speaks fluent hacker 🤓):

![]()

**Think of it like this:** Imagine you’re at a restaurant and the waiter takes your order without questioning it. You ask for “spaghetti with a side of *surprise ingredients*” and the kitchen just… makes it. No questions asked. That’s essentially what happens with stored HTML injection! 🍝

Hence, **Stored HTML Injection** occurs when user-supplied HTML content is not properly sanitized and is saved in the application’s database. When this data is later rendered on a page, the HTML is executed directly, which could lead to defacements or further security issues such as phishing or XSS (if scripts are allowed).

This can lead to:

* 🎭 Page defacements (making websites look funky)
* 🎣 Phishing attacks (tricking users)
* ⚡ XSS vulnerabilities (if scripts sneak through)

## The Setup: Where We Found It 🧪

While exploring the **AI chatbot feature** of pyng.co.in, we noticed an input field where users could send messages. At first, it seemed harmless — but our curiosity nudged us to test how it handled raw HTML.

## Payload and Execution

We entered the following simple HTML tag as our message:

```
<h1>Hello from Het & Kaif</h1>
```

To our surprise, when the chat history was loaded on page refresh or revisit, the message was rendered exactly as HTML — **not escaped**, not sanitized.
This confirmed a **stored HTML injection** — the HTML was being stored server-side and rendered client-side without any filtering.

We also tried several other payloads to confirm the injection:

```
<b style="color:red">XSS</b>
<i onclick="alert('XSS')">Click me</i>
<div style="background:red;padding:10px">Injected DIV</div>
<b style="color:red">XSS</b>
```

However, since JavaScript execution was fully disabled, despite attempting multiple payloads and bypass techniques, we were unable to achieve any successful execution.

## Screenshot of Payload Execution

![]()

## 📬 Responsible Disclosure

We followed responsible disclosure practices:

* Reported the bug to the redacted.co.in team.
* Shared steps to reproduce and suggestions to mitigate.

We did got the reply from support team:

Press enter or click to view image in full size

![]()

They were already aware of the vulnerability so they marked our report as “Duplicate Submission” 😭

## **About the Authors:**

![]()

* [**Het Patel**](https://www.linkedin.com/in/hetpatel9) — Cybersecurity Enthusiast | Bug Hunter | Coffee Addict ☕
* [**Kaif Shah**](https://www.linkedin.com/in/skaif009/) — Security Researcher | CEHv11 | CRTA | Top 4% THM | Bug Hunter

*Happy Hacking! (Ethically, of course)* 😉🔒

[Html Injection](https://medium.com/tag/html-injection?source=post_page-----6cbefe8b0718---------------------------------------)

[Xss Vulnerability](https://medium.com/tag/xss-vulnerability?source=post_page-----6cbefe8b0718---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6cbefe8b0718---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6cbefe8b0718---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6cbefe8b0718---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6cbefe8b0718---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6cbefe8b0718---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--6cbefe8b0718---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Het Patel](https://miro.medium.com/v2/resize:fill:96:96/1*0xmi1m3lKtIdhh3vz8hFsA.jpeg)](https://hettt.medium.com/?source=post_page---post_author_info--6cbefe8b0718---------------------------------------)

[...