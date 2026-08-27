---
title: ../../ to Admin for a $,$$$ Bounty
url: https://infosecwriteups.com/to-admin-for-a-bounty-b946f781607f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-26
fetch_date: 2026-08-27T12:12:38.945605
---

# ../../ to Admin for a $,$$$ Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fto-admin-for-a-bounty-b946f781607f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fto-admin-for-a-bounty-b946f781607f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b946f781607f---------------------------------------)

·

1. [The boring part nobody posts about](/?source=post_page-----b946f781607f---------------------------------------#5f51 "The boring part nobody posts about")
2. [Step 0: the one that answered](/?source=post_page-----b946f781607f---------------------------------------#0890 "Step 0: the one that answered")
3. [Step 1: the dumbest possible test](/?source=post_page-----b946f781607f---------------------------------------#ed8f "Step 1: the dumbest possible test")
   1. [Still 200.](/?source=post_page-----b946f781607f---------------------------------------#aa22 "Still 200.")
4. [Step 2: walking up](/?source=post_page-----b946f781607f---------------------------------------#5210 "Step 2: walking up")
5. [Step 3: the one I was building toward](/?source=post_page-----b946f781607f---------------------------------------#6b04 "Step 3: the one I was building toward")
6. [Why it actually worked](/?source=post_page-----b946f781607f---------------------------------------#1d93 "Why it actually worked")
7. [What I’d tell you to take from this](/?source=post_page-----b946f781607f---------------------------------------#b6d3 "What I’d tell you to take from this")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b946f781607f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--b946f781607f---------------------------------------)

[Ctf Writeup](https://medium.com/tag/ctf-writeup?source=post_page---header_tags--b946f781607f---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--b946f781607f---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page---header_tags--b946f781607f---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page---header_tags--b946f781607f---------------------------------------)

# **../../ to Admin for a $,$$$ Bounty**

[![Adhamkhairy](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*xv5j3MG7_VrAoW34)](https://0xsponge.medium.com/?source=post_page---byline--b946f781607f---------------------------------------)

[Adhamkhairy](https://0xsponge.medium.com/?source=post_page---byline--b946f781607f---------------------------------------)

5 min read

·

Jul 30, 2026

--

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Db946f781607f&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fto-admin-for-a-bounty-b946f781607f&source=---header_actions--b946f781607f---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

How Two Dots Made Me Admin

The target had two roles.

**Admin:** settings, user management, billing, promotion. Basically the whole application. Around **150 endpoints**.

**Viewer:** read a few resources and go home. **10 endpoints**. Guess which one my account was.

140 endpoints I wasn’t allowed to touch. That gap is not a limitation, that’s a to-do list.

## The boring part nobody posts about

So here’s what I actually did, and I want to be honest because most writeups skip this bit and jump straight to the clever payload.

I created an admin account on the second tenant, clicked through every single feature, and logged every request Burp saw. Then I took my **viewer** session cookie, dropped it into all 150 of those requests, and replayed them one by one.

That’s it. No custom tooling, no 12-stage recon pipeline. Just a viewer cookie and a lot of right-clicking.

Press enter or click to view image in full size

![]()

I know i should rename the tabs, focus on the finding mate

149 of them came back with the same thing:

```
HTTP/1.1 403 Forbidden
.........
.........
.........
.........

{"error":"Insufficient permissions"}
```

Over and over and over. At some point you stop reading the responses and start pattern-matching on the color of the status code column. Which is exactly when you miss things, so I made myself slow down and actually look at each one.

Good thing I did, because number 137 was green.

## Step 0: the one that answered

```
POST /api/admin/action HTTP/1.1
Host: app.example.com
Cookie: session=<viewer_session>
Content-Type: application/x-www-form-urlencoded

Action=ViewSettings
```

```
HTTP/1.1 200 OK
.......
.......
.......

{"success":true,"settings":{...}}
```

A viewer just read the repository settings.

That’s already a report. Broken access control, admin functionality reachable by a read-only role, write it up and get a $500 medium bug and move on.

But something about it bothered me.

Look at the request again. There’s no resource id, no object reference, no query. The entire request is a **VERB in a string**. `Action=ViewSettings`. The server takes a name and… does the thing named that?

If that were a normal `switch` statement or an allow-list, fine, whatever. But it didn't smell like a switch. It smelled like the value was being **concatenated into something**.

And things that get concatenated into paths can be walked.

## Step 1: the dumbest possible test

Before doing anything clever I wanted to know which of the two it was: allow-list or path resolution.

So I sent the most useless payload I could think of.

```
POST /api/admin/action HTTP/1.1
Cookie: session=<viewer_session>
.......
.......
.......

Action=./ViewSettings
```

```
HTTP/1.1 200 OK
.......
.......
.......

{"success":true,"settings":{...}}
```

### Still **200**.

And this is the whole finding right here, in one character.

`./ViewSettings` is **not a valid action name**. If the backend were comparing my input against a list of allowed strings, this is an instant reject, it's simply not in the list. There is no world where an allow-list accepts it.

## Get Adhamkhairy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

But `./` means "same directory, go nowhere." It's a no-op. To a **path resolver**, `./ViewSettings` and `ViewSettings` are the same place.

The server treated them as the same place.

So it’s a path. It was never an action name, it was a pat...