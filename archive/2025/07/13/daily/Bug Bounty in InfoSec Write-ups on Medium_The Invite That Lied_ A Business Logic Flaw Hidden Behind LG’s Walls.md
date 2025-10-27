---
title: The Invite That Lied: A Business Logic Flaw Hidden Behind LG’s Walls
url: https://infosecwriteups.com/the-invite-that-lied-a-business-logic-flaw-hidden-behind-lgs-walls-a49cca506294?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-13
fetch_date: 2025-10-06T23:27:35.265073
---

# The Invite That Lied: A Business Logic Flaw Hidden Behind LG’s Walls

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa49cca506294&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-invite-that-lied-a-business-logic-flaw-hidden-behind-lgs-walls-a49cca506294&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-invite-that-lied-a-business-logic-flaw-hidden-behind-lgs-walls-a49cca506294&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a49cca506294---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a49cca506294---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# A Business Logic Flaw That Could Have Cost LG Millions …

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--a49cca506294---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--a49cca506294---------------------------------------)

4 min read

·

Jul 12, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

I wasn’t chasing a bounty this time.
 This time, the thrill was different — I wanted to earn a **Letter of Appreciation** from LG.

Not a bug bounty. Not a write-up trophy. Just a clean, solid find. Something they’d remember.

Because when you’re dealing with a brand like LG — where polish meets production — **you know there’s more beneath the surface**.

So, I did what I do best: opened my recon toolkit, fired up some intuition, and started hunting for cracks in the logic.

## 🕵️ Step One: Recon at Scale

My recon game started with a weapon I absolutely love: **ShrewdEye**.

It pulls out subdomains like magic — raw, downloadable, no UI fluff.

```
wget https://shrewdeye.app/domains/<domain_name>.txt
```

The file dropped, and with it came **hundreds of subdomains** — some dormant, some suspicious, and a few… *just alive enough* to be dangerous.

I filtered down the list for targets with `200 OK` responses.

And then I saw it.

A subdomain I won’t name here (*you know the drill*), but let’s just call it:

`xyz.redacted.lg.com`

It wasn’t just alive.
 It was buzzing — login flows, invitation systems, beta-looking dashboards just like every other normal web-app

The kind of place where real bugs hide in **real logic**.

## 🔁 The Feature That Felt Too Predictable

I headed straight for the **“Invite via Email”** flow.

At first glance, it was clean.

You send an invite → The user gets an email → They register.

Nice and boring.

So I started testing for **rate limiting**, **race conditions**, and all the usual suspects. I was even hammering requests just to see if it cracked.

Nothing explosive happened.

No duplicate invites.
 No crazy invite flooding.
 No race-based privilege escalations.

Honestly? It was getting dull.

So I leaned back and thought:

> *“Let’s do something stupid. Let’s check if the system is even linking the invitation email to the registered account.”*

**Basic stuff. Almost boring.**
 But that’s the thing about boring checks — **they often reveal the most absurd bugs**.

And this one? It wasn’t just a bug.

It was a glitch in reality.

[## 🕵️‍♂️💻 “I Didn’t Plan to Find a P1… But My Script Had Other Plans 🧠💣”

### 🎬 It all started with a YouTube video…

infosecwriteups.com](/%EF%B8%8F-%EF%B8%8F-i-didnt-plan-to-find-a-p1-but-my-script-had-other-plans-77691a46985b?source=post_page-----a49cca506294---------------------------------------)

## 👁️‍🗨️ The Check That Shouldn’t Have Mattered

I sent an invite to `testvictim@gmail.com`.

The email came through.
 I clicked the invite link.
 Registration page opened.

At this point, I wasn’t expecting much. Just wanted to see **whether an account gets created only if the person is just invited without being registered !**

(If you’re into bug hunting, and haven’t ever asked this question, *note it down*. Seriously.)

Then I noticed something weird:

The email field wasn’t locked. It was editable.

Surely that was just a frontend thing, right?

So I typed in `attacker@gmail.com` instead.
 Typed a password. Hit submit.

And it… **worked**.

The system happily created an account for `attacker@gmail.com`.

No warnings. No validation errors. No logs I could see.

But here’s the real kicker:

> ***In the admin dashboard, the system said that `` had accepted the invitation.***

Read that again.

* The **real invited user**? No account. Never signed up.
* The **attacker**? Full access, brand-new account.
* The **system**? Totally unaware anything was wrong

[## 💥 CVE-2025–0133 Made Easy — Find Vulnerable Assets in 2 Minutes

### You don’t need fancy tools. You just need good eyes and the right search queries. Here’s how I easily find real…

infosecwriteups.com](/cve-2025-0133-made-easy-find-vulnerable-assets-in-2-minutes-140a9ba8e2da?source=post_page-----a49cca506294---------------------------------------)

## 💥 The Ghost Account Problem

This wasn’t just a small validation mistake.

It was a **fundamental logic flaw**.

The backend wasn’t binding the invitation token to the original email.
 It just accepted *anyone* who had the link.

Worse — **it marked the wrong person as registered**.

That means:

* Analytics are broken.
* Referral logs are fake.
* Trust assumptions are completely shattered.

It *looked* like the invite was used.
 It *looked* like the right person signed up.

But no one knew the real user never even touched it.

If you’re a dev or security analyst reading this, **note this bug down**:

> *🔴* “Invited email address can be altered during registration. Account is created under a different email, but the original invite is falsely marked accepted.”

[## 💥 From Innocent Messages to Total Takeover: How I Hacked a Professional Network! 💻🔓

### Let me take you on an exciting journey of how I uncovered a massive security flaw in a professional networking…

lordofheaven1234.medium.co](https://lordofheaven1234.medium.com/from-innocent-messages-to-total-takeover-how-i-hacked-a-professional-network-2033537d5d6a?source=post_page-----a49cca506294---------------------------------------)

## 🔚 Conclusion: The Invite That Lied

This wasn’t a zero-day.
 There was no shell, no script injection, no bypass chain.

But it was **just as dangerous**.

An editable input field — seemingly harmless — let me impersonate users, skew business data, and expose the entire invitation logic as **fake trust**.

If I hadn’t checked that boring detail…
 If I had skipped the “sanity test”...