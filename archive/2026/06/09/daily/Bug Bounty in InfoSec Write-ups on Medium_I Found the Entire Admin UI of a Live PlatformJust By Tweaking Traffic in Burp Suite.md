---
title: I Found the Entire Admin UI of a Live PlatformJust By Tweaking Traffic in Burp Suite
url: https://infosecwriteups.com/i-found-the-entire-admin-ui-of-a-live-platformjust-by-tweaking-traffic-in-burp-suite-c788db767598?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-09
fetch_date: 2026-06-10T06:15:29.242922
---

# I Found the Entire Admin UI of a Live PlatformJust By Tweaking Traffic in Burp Suite

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-the-entire-admin-ui-of-a-live-platformjust-by-tweaking-traffic-in-burp-suite-c788db767598&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-the-entire-admin-ui-of-a-live-platformjust-by-tweaking-traffic-in-burp-suite-c788db767598&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c788db767598---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c788db767598---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# **I Found the Entire Admin UI of a Live PlatformJust By Tweaking Traffic in Burp Suite**

[![ReFang](https://miro.medium.com/v2/resize:fill:64:64/1*8wLqK__BuQSYLLy1Wzn4mg.png)](https://medium.com/%40refang?source=post_page---byline--c788db767598---------------------------------------)

[ReFang](https://medium.com/%40refang?source=post_page---byline--c788db767598---------------------------------------)

5 min read

·

21 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc788db767598&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-found-the-entire-admin-ui-of-a-live-platformjust-by-tweaking-traffic-in-burp-suite-c788db767598&source=---header_actions--c788db767598---------------------post_audio_button------------------)

Share

Hey, I’m Hamza Hashim. On socials I am known as refang. I write about real bugs I find out in the wild. Not CTF challenges, not labs. Real, live, running software

This one is about a bug I found in the an internship program portal REDACTED.org, a programme I was actually enrolled in as an intern. I was poking around during normal use when I noticed something interesting. This article covers just one finding from a broader report I submitted to them.

**Background**

So I was enrolled in an internship programme. where interns log in, submit reports, and progress through stages. There are also graders and admins who manage things behind the scenes. Role-based access control (RBAC) is in place or at least, it’s supposed to be.

When I logged in as a Stage 0 intern, I had the most basic role on the platform. I shouldn’t be seeing anything admin-related.

**What is Burp Suite’s Match and Replace?**

Before I explain the bug, let me explain the tool.

Burp Suite is a web proxy it sits between your browser and the server and lets you see and modify all the traffic going back and forth. One of its features is called **Match and Replace**. It does exactly what it sounds like: every time a specific word appears in the traffic, replace it with another word automatically.

Think of it like Find & Replace in Word but working on live web traffic, invisibly, in real time.

**The Setup**

I set up a few Match and Replace rules in Burp.
The idea was simple:
when the server sends back traffic that says my role is `INTERN`, I wanted to see what the app would render if it thought I was a `GRADER` or `SUPER_ADMIN` instead.

So I made rules like:

* Replace `"role":"INTERN"` → `"role":"Grader"`
* Replace `"INTERN"` → `"Grader"` in relevant response contexts

**Rule 1: For Request Header**

Press enter or click to view image in full size

![]()

**Rule 2: For Request Body**

Press enter or click to view image in full size

![]()

**Rule 3:For Response**

Press enter or click to view image in full size

![]()

**Rule 4: For Response Body**

Press enter or click to view image in full size

![]()

With these rules active, I logged in through Burp’s proxy. The browser received the modified responses thinking I was a super admin and rendered the UI accordingly.

## Get ReFang’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

**What Happened**

The entire admin and grader interface appeared. Navigation items, menu entries, dashboard links, operational controls all of it rendered for me as a regular intern account.

Features I could now *see* included things like grading tools, user management panels, and operations dashboards. The full map of admin functionality was laid out in front of me.

Press enter or click to view image in full size

![]()

**But Here’s the Catch**

When I actually clicked any of those buttons or tried to use any of those features, I got 404s and errors. Every actual action hit the server and failed. The server-side was doing its own auth checks and rejecting my intern token properly.

So to be clear, **I could not actually do anything admin-level.** The data APIs were protected. This is the key difference from other UI-exposure bugs I’ve reported before, in one [previous writeup](https://medium.com/bugbountywriteup/i-became-admin-on-a-ctf-platform-c26cb49546a5), on a CTF platform, I was able to fully become admin and perform privileged actions. Here, the backend held the line.

What wasn’t protected was the *rendering* of the UI itself. The frontend was trusting the role in the response to decide what to show, and Burp let me lie about that role.

**Why This Still Matters**

You might think: if nothing actually works, who cares?

Here’s why it matters:

1. **Full attack surface enumeration.** An attacker doesn’t need to fuzz or guess admin routes. The UI just hands them a complete, labelled map of everything the admin can do. Every feature, every endpoint, every control. That’s free recon.
2. **Defense in depth is broken.** Security isn’t supposed to rely on a single layer. If the backend is the only thing enforcing access control, you’ve lost one of your layers. The frontend should *also* not reveal privileged UI to unprivileged users.
3. **It’s a one-rule Burp change.** The barrier to doing this is extremely low. Anyone with Burp Suite — which is free — and basic curiosity can reproduce this in a few minutes.

**The Fix**

The right fix here is straightforward: role-based rendering decisions should happen server-side, not client-side.

In a Next.js app (which REDACTED.org appears to use), this means checking the user’s actual session role in a server component or middleware before rendering privileged navigation or UI elements. The client should never receive markup for features it isn’t authorized to use — regardless of what the JWT or response payload says.

Don’t just hide buttons. Don’t render them at all.

**Disclosure**

I discovered this while using the platform as an enrolled intern. All testing was done on my own authenticated session. No data was mod...