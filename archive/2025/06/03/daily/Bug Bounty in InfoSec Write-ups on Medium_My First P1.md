---
title: My First P1
url: https://infosecwriteups.com/my-first-p1-ae9d09c02927?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-03
fetch_date: 2025-10-06T22:51:59.403389
---

# My First P1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae9d09c02927&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-p1-ae9d09c02927&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-p1-ae9d09c02927&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae9d09c02927---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae9d09c02927---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My First P1

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--ae9d09c02927---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--ae9d09c02927---------------------------------------)

3 min read

·

Apr 26, 2025

--

7

Listen

Share

Last week, I decided to get [**iScan.today**](https://iscan.today/) because I had seen so much positive feedback about it.

Press enter or click to view image in full size

![]()

iscan

As soon as my private instance was sent to me, I started testing my targets.

Press enter or click to view image in full size

![]()

Very quickly, I got a **Telegram alert** that **iScan.today** had found a **GitHub token**.
 The token was exposed in the endpoint: `scripts/reports/license-term-validation.sh`.

![]()

Curious, I tested the token using **secrets.ninja** — it was **active**.
 At first, I hesitated. The token was inside a license script — maybe it wasn’t serious? I could only use it to query public repos in Postman.

But then… my hacker instincts kicked in.

I ran:

```
curl https://api.github.com/orgs/ORG_NAME/repos
```

I started wondering: **What could an attacker do with this?**

I opened ChatGPT and asked for advice. ChatGPT suggested I check the **permissions** attached to the token.

The permissions blew my mind:

```
admin:enterprise
admin:gpg_key
admin:org
admin:org_hook
admin:public_key
admin:repo_hook
delete:packages
delete_repo
gist
notifications
repo
user
workflow
write:discussion
write:packages
```

**That’s a *lot* of permissions.**

At this point, I could have reported it immediately, but:

* I wanted to achieve **maximum impact** safely.
* I knew some programs downgrade reports if you don’t show real exploitation.

### Privilege Escalation

I tested further:

```
GET https://api.github.com/user/repos?visibility=private
```

Silently praying… and **Alhamdulillāh**, it listed two **private repositories**.

Press enter or click to view image in full size

![]()

I tried cloning. Git asked me for a **username** and **password**.

So, I went back to GitHub, found the **username** of the person who committed the file, then used the **username** and the **token** for authentication.

I successfully cloned the private repo. At this point, it was clear: **Access Granted**

Press enter or click to view image in full size

![]()

I quickly drafted my report and submitted it to the private BBP program (invite-only). Surprisingly, it was mistakenly **closed as Non-Reproducible** because of this message.

Press enter or click to view image in full size

![]()

I made a request. They **reopened** it and directed me to submit it to their **VDP program** instead.:}

I submitted it to the VDP. Within a short time, it was **triaged**, **P1**, and **accepted**!

Alhamdulillāh, it became my **first P1 on Bugcrowd**! The submission is now **resolved**.

Press enter or click to view image in full size

![]()

### Key Lessons

* When you find a token but don’t know its impact: Ask **ChatGPT** or any AI assistant. Let it **boost your workflow**, not replace you.
* Always think of the **maximum safe impact** you can show without causing damage.
* Tools like **iScan.today** by

  [Arshad Kazmi](https://medium.com/u/c136fd4fc73c?source=post_page---user_mention--ae9d09c02927---------------------------------------)

   are game-changers — highly recommended!

> I stand in solidarity with Palestine, praying for justice and peace.

[Github](https://medium.com/tag/github?source=post_page-----ae9d09c02927---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ae9d09c02927---------------------------------------)

[Genocide](https://medium.com/tag/genocide?source=post_page-----ae9d09c02927---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----ae9d09c02927---------------------------------------)

[Recon](https://medium.com/tag/recon?source=post_page-----ae9d09c02927---------------------------------------)

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ae9d09c02927---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ae9d09c02927---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ae9d09c02927---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ae9d09c02927---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ae9d09c02927---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![callgh0st](https://miro.medium.com/v2/resize:fill:96:96/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---post_author_info--ae9d09c02927---------------------------------------)

[![callgh0st](https://miro.medium.com/v2/resize:fill:128:128/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---post_author_info--ae9d09c02927---------------------------------------)

[## Written by callgh0st](https://call...