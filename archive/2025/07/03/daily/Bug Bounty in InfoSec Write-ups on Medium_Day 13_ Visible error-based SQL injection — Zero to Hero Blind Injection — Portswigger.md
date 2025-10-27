---
title: Day 13: Visible error-based SQL injection — Zero to Hero Blind Injection — Portswigger
url: https://infosecwriteups.com/day-13-visible-error-based-sql-injection-zero-to-hero-blind-injection-portswigger-3da2241a1672?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:51:48.537063
---

# Day 13: Visible error-based SQL injection — Zero to Hero Blind Injection — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3da2241a1672&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-13-visible-error-based-sql-injection-zero-to-hero-blind-injection-portswigger-3da2241a1672&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-13-visible-error-based-sql-injection-zero-to-hero-blind-injection-portswigger-3da2241a1672&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3da2241a1672---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3da2241a1672---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Day 13: Visible error-based SQL injection — Zero to Hero Blind Injection — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--3da2241a1672---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--3da2241a1672---------------------------------------)

5 min read

·

Apr 28, 2025

--

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 13 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

Before you go for this blog, make sure to read the Previous one

**Link to Previous Blog**: [https://medium.com/@arayofhope7/day-12-blind-sql-injection-with-conditional-errors-zero-to-hero-blind-injection-portswigger-e94f9e3977a5](https://medium.com/%40arayofhope7/day-12-blind-sql-injection-with-conditional-errors-zero-to-hero-blind-injection-portswigger-e94f9e3977a5)

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

This is how the lab looks.

Press enter or click to view image in full size

![]()

*“This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.
The database contains a different table called* `users`*, with columns called* `username`*and* `password`*. To solve the lab, find a way to leak the password for the* `administrator`*user, then log in to their account.”*

Press enter or click to view image in full size

![]()

**Vulnerable Parameter**:Tracking Cookie

**End Goals:
*1.*** *Exploit SQLi* ***to*** *output the password of the administrator user
2. Log in as the administrator user.*

Press enter or click to view image in full size

![]()

*Request was intercepted and sent to the intruder.*

Press enter or click to view image in full size

![]()

*This is what the normal response looks like.*

Press enter or click to view image in full size

![]()

*As we know, the cookie parameter is vulnerable. I used a single quote (*`'`*), and it returned a* ***500 Internal Server Error****. This indicates that the single quote might be breaking the SQL query, suggesting that the query could be part of custom developer-written code.*

Press enter or click to view image in full size

![]()

*In the response, it returned an error, and the error message included the SQL query, which could be really sensitive. Let’s see how we can use it to craft a new payload.
This is what we had in the response body:* ***Unterminated string literal started at position 52 in SQL SELECT \* FROM tracking WHERE id = ‘WPq6tHyy2UpzpneU’’. Expected char***

> **The server is not properly configured to handle errors. Instead of showing a generic error message, it leaks sensitive SQL query details, exposing the backend and increasing the risk of exploitation.**

* *If you look at the SQL query revealed by the server, you’ll notice that at the end it uses double single quotes (*`''`*). In the above scenario:* `SQL SELECT * FROM tracking WHERE id = 'WPq6tHyy2UpzpneU''.`***.****This suggests that the single quote is not properly closed, and the application is trying to handle it internally by escaping the quote, possibly to prevent SQL Injection.*

Press enter or click to view image in full size

![]()

*Now, I used* `--` *and it commented out the rest of the code after the first single quote. Quick tip: you can also use* `#` ***or*** `--` ***(with a space and another dash)*** *to comment out the rest of the code.*

Press enter or click to view image in full size

![]()

*But it does create a verbose error, which could be the same way we may retrieve the administrator password.*

N**ote: —**

*The* `CAST()` *function is used to convert a syntax from one data type to another*
Like: ‘ AND CAST((SELECT 1) AS INT) — —

Press enter or click to view image in full size

![]()

*But wait, we got an error even after using ‘****AND CAST((SELECT 1) AS INT)’.***

Press enter or click to view image in full size

![]()

*But in the response, we got the solution as well. It says that ‘****the argument of AND must be of type boolean****,* ***not type integer,’*** *which clearly explains why we are getting the error.*

Press enter or click to view image in full size

![]()

*And there we go, we balanced the syntax: (WPq6tHyy2UpzpneU’ and 1=cast ((select 1) as int) — — ), and it returned a 200 OK.*

*It forces the query to return a* `true` *condition by ensuring that* `1=1` *is evaluated. Here, we used the result of* `select 1` *to an integer, making the comparison work as expected.*

Press enter or click to view image in full size

![]()

*Used* `' AND 1=CAST((SELECT username FROM users) AS INT)--`*. Let's see if the error message returned the username.*

Press enter or click to view image in full size

![]()

*There we have a verbose error, but not the username. However, we know that the syntax we are using is correct.*

Press enter or click to view image in full size

![]()

*Let’s see if the response reveals the username.*

Press enter or click to view image in full size

![]()

*It’s a generic error, likely because the query is attempting to retrieve more columns than expected, which is why the username isn’t being returned. Let’s try using* `LIMIT`*to restrict the results and see if that helps.*

Press enter or click to view image in full size

![]()

*Executed the payload* ***‘ AND 1=cast((select username FROM users LIMIT 1) as INT) — —*** *, and it...