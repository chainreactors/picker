---
title: How I Made Over $10,000 Just by Chaining Multiple IDORs in a Single Web App (All from the Share…
url: https://infosecwriteups.com/how-i-made-over-10-000-just-by-chaining-multiple-idors-in-a-single-web-app-all-from-the-share-4d425a15aa37?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:37.972856
---

# How I Made Over $10,000 Just by Chaining Multiple IDORs in a Single Web App (All from the Share…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-made-over-10-000-just-by-chaining-multiple-idors-in-a-single-web-app-all-from-the-share-4d425a15aa37&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-made-over-10-000-just-by-chaining-multiple-idors-in-a-single-web-app-all-from-the-share-4d425a15aa37&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4d425a15aa37---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4d425a15aa37---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--4d425a15aa37---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page---header_tags--4d425a15aa37---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page---header_tags--4d425a15aa37---------------------------------------)

[Idor Vulnerability](https://medium.com/tag/idor-vulnerability?source=post_page---header_tags--4d425a15aa37---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page---header_tags--4d425a15aa37---------------------------------------)

# How I Made Over $10,000 Just by Chaining Multiple IDORs in a Single Web App (All from the Share Function)

[![Ferdus Alam](https://miro.medium.com/v2/resize:fill:64:64/1*1elJ9t5-1mJxohOO488yDA@2x.jpeg)](https://medium.com/%40ferdusalam0?source=post_page---byline--4d425a15aa37---------------------------------------)

[Ferdus Alam](https://medium.com/%40ferdusalam0?source=post_page---byline--4d425a15aa37---------------------------------------)

3 min read

·

Oct 19, 2025

--

10

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D4d425a15aa37&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-made-over-10-000-just-by-chaining-multiple-idors-in-a-single-web-app-all-from-the-share-4d425a15aa37&source=---header_actions--4d425a15aa37---------------------post_audio_button------------------)

Share

Hey folks 👋
 I’m **Ferdus**, a security researcher and bug hunter. I used to hunt mostly on **Bugcrowd** under the handle **bebe**, and now I’m more active on **HackerOne** with the username **hackmebebe1**.

Press enter or click to view image in full size

![]()

This writeup is for **beginners and non-technical hunters** who think you need complex skills to earn good bounties. Trust me, you don’t. I made **over $10,000** just by focusing on **one feature** — the **share function** — and finding multiple **IDOR vulnerabilities** that exposed **PII of over 7M users** on a major SaaS project management platform (name redacted).

**Why I Focused on One Target**

Instead of jumping between dozens of programs, I picked **one app** and spent time understanding how it works — features, roles, permissions, how share and access logic works, etc.

Once I found **one IDOR**, I used a simple rule:

**“If one feature is vulnerable, similar features might be too.”**

**The First IDOR — The Breakthrough**

* In this app, users can **share tasks** with other members.
* I shared a task normally, then **intercepted the request in Burp Suite**.
* The JSON body looked like this:

{

“user\_id”: “173535”

}

* I changed the user\_id to a **random ID that didn’t belong to my workspace**.
* Boom — the response leaked **PII data of that user** (name, email, etc.).

I reported it and got **$500 bounty** in just a few days.

**The Real Jackpot — Repeat the Same Logic Everywhere**

## Get Ferdus Alam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

After the first bounty, I got curious. The app had multiple share-like features:

✅ Share **Tasks**
 ✅ Share **Documents**
 ✅ Share **Lists**
 ✅ Share **Folders**
 ✅ Share **Goals**
 ✅ Share **Spaces**

I repeated the same trick on all of them. **Most were vulnerable**.

Some endpoints didn’t accept POST?
 ➡️ I tried **PUT instead of POST** — and it worked.

Some endpoints used “user”?
 ➡️ I tried “users” and “user\_ids” too — and one of those parameters got accepted.

This simple parameter mutation + ID tampering combo earned me **more than $10k across multiple reports** — all on the same platform.

**Key Takeaway for Beginners**

You don’t need advanced exploitation or RCE to earn bounties.

**Just understand the app deeply and test similar areas again and again.**

* Found one IDOR?
   ➡️ Search for **similar endpoints**.
* Saw “user\_id”?
   ➡️ Try “users”, “user”, “assignee\_id”, etc.
* POST blocked?
   ➡️ Try **PUT, PATCH, DELETE**.
* Don’t rely only on UI.
   ➡️ **Replay raw requests** with modified IDs.

**Final Words**

This hunting method is perfect for **beginners with patience**.
 Most people give up after one report. I did the opposite — **I doubled down**.

**One feature. Many variations. Many payouts.**

If you want, I can publish a **checklist for hunting IDORs in SaaS web apps** — just let me know and I’ll drop it in the next writeup.

Thanks for reading,

Happy Hacking!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---footer_tags--4d425a15aa37---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page---footer_tags--4d425a15aa37---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page---footer_tags--4d425a15aa37---------------------------------------)

[Idor Vulnerability](https://medium.com/tag/idor-vulnerability?source=post_page---footer_tags--4d425a15aa37---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page---footer_tags--4d425a15aa37---------------------------------------)

--

--

10

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d425a15aa37---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4d425a15aa37---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4d425a15aa37---------------------------------------)

[88K followers](/followers?source=...