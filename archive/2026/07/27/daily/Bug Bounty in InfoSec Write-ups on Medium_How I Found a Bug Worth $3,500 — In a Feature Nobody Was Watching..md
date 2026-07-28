---
title: How I Found a Bug Worth $3,500 — In a Feature Nobody Was Watching.
url: https://infosecwriteups.com/how-i-found-a-bug-worth-3-500-in-a-feature-nobody-was-watching-6773df9fce72?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-27
fetch_date: 2026-07-28T04:58:46.751102
---

# How I Found a Bug Worth $3,500 — In a Feature Nobody Was Watching.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-bug-worth-3-500-in-a-feature-nobody-was-watching-6773df9fce72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-bug-worth-3-500-in-a-feature-nobody-was-watching-6773df9fce72&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6773df9fce72---------------------------------------)

·

1. [The Setup — Where Nobody Looks](/?source=post_page-----6773df9fce72---------------------------------------#553a "The Setup — Where Nobody Looks")
2. [Target Recon — It’s About the Questions You Ask](/?source=post_page-----6773df9fce72---------------------------------------#9fce "Target Recon — It’s About the Questions You Ask")
3. [🐛 Bug #1 — The Size Field That Lied](/?source=post_page-----6773df9fce72---------------------------------------#2889 "🐛 Bug #1 — The Size Field That Lied")
4. [Classification](/?source=post_page-----6773df9fce72---------------------------------------#0972 "Classification")
5. [💀 Bug #2 — The XSS That Waited for an Admin](/?source=post_page-----6773df9fce72---------------------------------------#d7a7 "💀 Bug #2 — The XSS That Waited for an Admin")
6. [Classification](/?source=post_page-----6773df9fce72---------------------------------------#fbc9 "Classification")
7. [⛓️ The Chain — From “Boring Upload” to Admin Takeover](/?source=post_page-----6773df9fce72---------------------------------------#d0c1 "⛓️ The Chain — From “Boring Upload” to Admin Takeover")
8. [💵 Where the $3,500 Comes From](/?source=post_page-----6773df9fce72---------------------------------------#3eb1 "💵 Where the $3,500 Comes From")
9. [📝 What I Learned — And What You Should Take Away](/?source=post_page-----6773df9fce72---------------------------------------#df1c "📝 What I Learned — And What You Should Take Away")
10. [1. Metadata is attack surface.](/?source=post_page-----6773df9fce72---------------------------------------#0563 "1. Metadata is attack surface.")
11. [2. Severity is about the victim, not the vulnerability.](/?source=post_page-----6773df9fce72---------------------------------------#06fb "2. Severity is about the victim, not the vulnerability.")
12. [3. “Boring” features age badly.](/?source=post_page-----6773df9fce72---------------------------------------#62ec "3. “Boring” features age badly.")
13. [4. Think in chains, not singles.](/?source=post_page-----6773df9fce72---------------------------------------#2161 "4. Think in chains, not singles.")
14. [🛡️ Responsible Disclosure](/?source=post_page-----6773df9fce72---------------------------------------#fcd8 "🛡️ Responsible Disclosure")
15. [About the Author](/?source=post_page-----6773df9fce72---------------------------------------#8a0a "About the Author")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6773df9fce72---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Found a Bug Worth $3,500 — In a Feature Nobody Was Watching.

[![Vishw Bhatt](https://miro.medium.com/v2/resize:fill:64:64/1*vFKPWnO-GHZyRfoV1tYAAw.png)](https://medium.com/%40Vishw04?source=post_page---byline--6773df9fce72---------------------------------------)

[Vishw Bhatt](https://medium.com/%40Vishw04?source=post_page---byline--6773df9fce72---------------------------------------)

7 min read

·

3 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6773df9fce72&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-a-bug-worth-3-500-in-a-feature-nobody-was-watching-6773df9fce72&source=---header_actions--6773df9fce72---------------------post_audio_button------------------)

Share

A storage-exhaustion flaw. A stored XSS that waited for an admin. Both hiding in the same “boring” file upload form that hadn’t been touched in years.

Press enter or click to view image in full size

![]()

*What happens when nobody stress-tests the upload form for three years.*

A file upload form. Zero server-side validation. A spoofed size field. A filename that executed code in an admin’s browser three days after I uploaded it.

## The Setup — Where Nobody Looks

This wasn’t some flashy HackerOne program with a public leaderboard and a hall of fame. It’s a private one 😉.

It was a B2B SaaS platform — the kind of internal business tool that handles users’ images and map data out of it.

Just a login page, a dashboard, and a bunch of forms, **well tested before, but no one thought what if it could be landing in the admin’s pocket.**

> *If you want to find bugs that matter, look where nobody else is looking. The flashy features get all the attention. The boring ones get all the vulnerabilities.*

The program already had 1000+ reports and some of them disclosed around the image upload feature only.

**That’s usually where the good bugs live.**

Press enter or click to view image in full size

![]()

*Every pentester knows: the boring stuff is where the gold is 🏆*

## Target Recon — It’s About the Questions You Ask

Nothing exotic here. Standard black-box approach. But the difference between finding nothing and finding two chained bugs comes down to **what questions you ask**:

→ Map every feature that touches user-supplied files

→ Note anything that accepts **metadata** alongside the file — filename, declared size, MIME type

→ Ask the question most testers skip: ***who eventually consumes this data, and in what context?***

That last question is the one that actually matters.

Most testers stop at *“does the upload work?”*

**The real question is: “Who could open this file later — and what do they trust about it?”**

That single question turned a “meh” upload form into a two-bug chain worth writing about. Let me show you how.

## 🐛 Bug #1 — The Size Field That Lied

The upload form enforced a file size limit — **on paper.**

But here’s the thing: the limit was checked against a **client-supplied metadata field**, not the actual bytes landing in storage.

Read that again.

So there were two requests in the image upload feature that were there:

1. **The Main File Upload:**

* A simple POST request to /upload-user-profile-image with the usual file upload request.
* Every other file type was blocked.
* Only JPG and PNG
* Everything bigger than 15 MB gets blocked.
* Fully secure, and most of us were done here, including me, but then after some time, when I was testing BAC, I revisited that feature and found out about the second request.

2. The Metadata Endpoint

* A metadata request going just after the upload request: POST /upload-...