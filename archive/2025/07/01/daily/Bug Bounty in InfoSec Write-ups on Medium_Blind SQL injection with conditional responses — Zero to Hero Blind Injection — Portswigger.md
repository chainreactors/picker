---
title: Blind SQL injection with conditional responses — Zero to Hero Blind Injection — Portswigger
url: https://infosecwriteups.com/blind-sql-injection-with-conditional-responses-zero-to-hero-blind-injection-portswigger-dad0cab48d57?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-01
fetch_date: 2025-10-06T23:53:34.260210
---

# Blind SQL injection with conditional responses — Zero to Hero Blind Injection — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdad0cab48d57&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblind-sql-injection-with-conditional-responses-zero-to-hero-blind-injection-portswigger-dad0cab48d57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fblind-sql-injection-with-conditional-responses-zero-to-hero-blind-injection-portswigger-dad0cab48d57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dad0cab48d57---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dad0cab48d57---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Blind SQL injection with conditional responses — Zero to Hero Blind Injection — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--dad0cab48d57---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--dad0cab48d57---------------------------------------)

9 min read

·

Apr 19, 2025

--

Listen

Share

Hi, my fellow hackers. This is **Rayofhope**. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

It’s Day 11 of posting all the PortSwigger labs, not just the solutions. I’ll break down ***why*** we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

Before you go for this blog, make sure to read the Previous one

**Link to First Blog**: [https://medium.com/@arayofhope7/sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data-portswigger-12342def10ec](https://medium.com/%40arayofhope7/sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data-portswigger-12342def10ec)

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

* We covered the basics of SQL in the first blog, which I recommend you read. In this post, we’ll dive into the concept of Blind SQL Injection.

W**hat is Boolean:** —

Boolean in terms of programming simply means **True** or **False**. Or we can say, while performing blind injections, we are asking the server to respond to us as either true or false.

W**hat is Blind Injection: —**

Blind Injections or Blind SQL Injections. As the name suggests, these injections are used where we are successfully able to fetch critical data, but somehow the extracted data is not visible on the website, which may be attributed to how the website is built.

W**hat is Blind Boolean SQL Injection: —**

Blind SQL Boolean Injection is a type of SQL Injection attack where the attacker can’t directly see the results of their query. Instead, they rely on the application’s responses to determine whether their queries are **true** or **false.**

Press enter or click to view image in full size

![]()

H**ow to Identify Blind SQL Injection:**

> **Find a injection point: —** Identify a part of the application that interacts with a database (like a form field, URL parameter, or cookies)
>
> **Craft a Simple SQL Injection: —** Test Start with input that doesn’t break the query, such as adding a single quote C) to see if the application reacts with an error. **Like:- ‘OR ‘1’=’1**
>
> **Send a Boolean-based Query: —** Use a condition that is always true and one that is always false to see if the response changes.
> **True: ‘ OR 1=1 — —
> False ‘ OR 1=2 — —**
>
> **Observe Differences in Responses: — If the response to a true condition (like 1=1) is different from the false condition (like 1=2), there is a potential Blind Boolean-based SQL Injection**

![]()

Well, well, well! We now know what Blind SQL-based Injection is. Therefore, we will go ahead and perform the exploitation, and at the end of the write-up, I’m gonna cover the mitigations too.

This is how the application looks:

Press enter or click to view image in full size

![]()

*The*`category` *parameter accepts arbitrary input*`rayofhope` *and reflects it in the response, indicating that the backend might be using it directly in queries. This makes it vulnerable to SQL injection testing.*

Press enter or click to view image in full size

![]()

*Let’s intercept the request and see if it’s vulnerable. Time to put on our pentester hats and test if this target sings when we ask the right questions.*

Press enter or click to view image in full size

![]()

*The request was intercepted and sent to Intruder for further fuzzing and analysis. Let’s see how it holds up under pressure.*

Press enter or click to view image in full size

![]()

*Now that we have an entry point and we know it’s interacting with the database, we’ll try to identify what the developer has written in the backend by providing some SQL syntax. Let’s reverse-engineer their logic one payload at a time.*

Press enter or click to view image in full size

![]()

*Tried a single quote* ***(***`'`***)*** *and it returned* ***200 OK****, which means it's not breaking the developer's code or the underlying SQL query. Looks like the input is being handled… but let’s dig deeper.*

Press enter or click to view image in full size

![]()

*Used a double quote* ***(***`"`***)*** *and it's still returning* ***200 OK****, which means this too isn't breaking or unbalancing the query. Looks like the backend is staying calm, for now. Let’s push it a bit more.*

Press enter or click to view image in full size

![]()

*Even single quote close braces* ***(***`')`***)*** *or double quote close braces* ***(***`")`***)*** *are still returning* ***200 OK****. So, we might be wrong here, time to shift gears and try some Blind SQL Injection payloads. We know that the* ***cookies*** *parameter is vulnerable to the attack — let’s try to enumerate this further and see what valuable intel we can extract.*

Press enter or click to view image in full size

![]()

*We can see that the response contains* ***“Welcome back”****, which could be a clue indicating a successful condition. Let’s use this as our baseline for crafting blind SQL payloads.*

Press enter or click to view image in full size

![]()

*Added* `"Q"` *in the cookie parameter, and it returned* ***200 OK****, but the word* ***"Welcome"*** *is missing in the response. This indicates it could potentially be vulnerable to a* ***Blind SQL Boolean*** *attack. Time to test this theory with some crafted payloads.*

Press enter or cl...