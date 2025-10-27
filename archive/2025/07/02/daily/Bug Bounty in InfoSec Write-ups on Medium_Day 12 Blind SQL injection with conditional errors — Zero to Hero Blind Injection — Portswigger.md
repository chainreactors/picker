---
title: Day 12 Blind SQL injection with conditional errors — Zero to Hero Blind Injection — Portswigger
url: https://infosecwriteups.com/day-12-blind-sql-injection-with-conditional-errors-zero-to-hero-blind-injection-portswigger-e94f9e3977a5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:36.323055
---

# Day 12 Blind SQL injection with conditional errors — Zero to Hero Blind Injection — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe94f9e3977a5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-12-blind-sql-injection-with-conditional-errors-zero-to-hero-blind-injection-portswigger-e94f9e3977a5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-12-blind-sql-injection-with-conditional-errors-zero-to-hero-blind-injection-portswigger-e94f9e3977a5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e94f9e3977a5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e94f9e3977a5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Day 12 Blind SQL injection with conditional errors — Zero to Hero Blind Injection — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--e94f9e3977a5---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--e94f9e3977a5---------------------------------------)

9 min read

·

Apr 22, 2025

--

1

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 12 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

Before you go for this blog, make sure to read the Previous one

**Link to First Blog**: <https://arayofhope7.medium.com/blind-sql-injection-with-conditional-responses-zero-to-hero-blind-injection-portswigger-dad0cab48d57>

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

Deadliest Virus in the world.

Press enter or click to view image in full size

![]()

**This is how the application looks:**

Press enter or click to view image in full size

![]()

*As we already know, the* `cookies` *parameter is vulnerable to Blind SQL Injection. So, let's intercept the request and explore what we can do with it.*

Press enter or click to view image in full size

![]()

Sent it to the repeater.

Press enter or click to view image in full size

![]()

*Tried injecting a single quote* ***(***`'`***),*** *and it returned a 200 OK response. However, there's no clear indication, such as a* ***true or false*** *statement, to confirm the vulnerability. It could be that the* `Pets` *parameter is the one being affected.*

Press enter or click to view image in full size

![]()

*Replaced the Tracking ID with* `rayofhope`***,*** *and it still returned a 200 OK response. However,* `rayofhope`*doesn't appear anywhere in the response, and we aren't seeing any indicators that would confirm a* ***true or false condition****.*

Press enter or click to view image in full size

![]()

*Used a* ***single quote (***`'`***)****, and it returned a* ***500 Internal Server Error****. This indicates that the single quote might be breaking the SQL query, which suggests that the query could be part of custom* ***developer-written code.***

Press enter or click to view image in full size

![]()

*There we go, this time, we didn’t get an error. We used* ***‘ and 1=1****, which is a* ***universal true condition,*** *confirming that the single quote is now properly balancing the* ***SQL query.*** *This suggests that the parameter could potentially be vulnerable to* ***Blind SQL Injection.***

Press enter or click to view image in full size

![]()

> But wait a minute, we tried `' and 1=2`, which is clearly a f**alse condition** (because, yeah, 1 is never equal to 2, not even in developer dreams). Yet, we still got a 200 OK response! No error, no change, no sign of rejection.
>
> This is where things get tricky. When both true **(**`' and 1=1`**)** and false (`' and 1=2`**)** conditions return the same response, we can't rely on visual cues or error messages. Welcome to the world of Blind SQL Injection — where the injection is happening, but the app acts like nothing’s wrong. It's like trying to read a poker face... in the dark!

Press enter or click to view image in full size

![]()

> Inputs like `'--` or `''` are valid parts of an SQL query, so the database doesn’t throw an error, the query still runs, and we get a 200 OK in response.
>
> But waiiih — we just saw that ‘’ is accepted, right? That might mean the input is being treated as part of a valid SQL string. Sooo… what if we try to concatenate something? Like ‘ || (SELECT ‘’)’

Press enter or click to view image in full size

![]()

*Oh nooo, we still got an error with* `'||(SELECT '')||'`*! Where are we messing up? Wait a sec… maybe it's not using a string concatenation operator like* `||`*. Could it be an Oracle database? 🤔 Either way, getting an error now is actually a good thing — it means we’re poking the query in the right place!*

Press enter or click to view image in full size

![]()

*There we go — we finally got a 200 OK with the payload* `' || (SELECT '' FROM dual) || '`*. And you know what that means? Yep, we’re most likely dealing with an Oracle database! Want to know why that works and how to go even deeper with Oracle SQL Injection?*

*Then you have to check out this blog:* [***SQL Injection Attack: Querying the Database Type and Version on Oracle (PortSwigger Lab)***](https://arayofhope7.medium.com/sql-injection-attack-querying-the-database-type-and-version-on-oracle-portswigger-904487db7d3d)*. Trust me — it’ll level up your injection game!*

Press enter or click to view image in full size

![]()

*We replaced* `dual`*with* `rayofhope,`*a table we know doesn’t exist, and boom, we got an error! But with*`dual`*, we get a clean* ***200 OK****. That’s the confirmation we needed: the input is being executed, the equation is balanced, and yes, it's vulnerable to* ***Blind SQL Injection.***

**What’s Next? — See Me Doin’ It! 🎥🔥**

Press enter or click to view image in full size

![]()

Why does `'||(select '' from users)||'` give an error even though the `users`table exists?

Let’s understand this way: —

*If the* `users` *table has no rows (i.e., it's empty), the query* `SELECT '' FROM users` *will return no results. This means a 200 OK response, as the query completes successfully without returning any rows.*

Press enter or click to view image in full size

![]()

*But wait,* `'||(select '' from users where row...