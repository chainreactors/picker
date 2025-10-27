---
title: SQL injection UNION attack, retrieving data from other tables — Portswigger
url: https://infosecwriteups.com/sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-ab892f5a9527?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-01
fetch_date: 2025-10-06T23:53:10.678985
---

# SQL injection UNION attack, retrieving data from other tables — Portswigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fab892f5a9527&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-data-from-other-tables-portswigger-ab892f5a9527&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-data-from-other-tables-portswigger-ab892f5a9527&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ab892f5a9527---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ab892f5a9527---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL injection UNION attack, retrieving data from other tables — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--ab892f5a9527---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--ab892f5a9527---------------------------------------)

5 min read

·

Apr 14, 2025

--

Listen

Share

Hi, my fellow hackers. This is Rayofhope. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

Day 9 of posting all the PortSwigger labs, not just the solutions. I’ll break down *why* we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

> ***Before you go for this blog, make sure to read the Previous one******Link to Seventh Blog:*** [*https://arayofhope7.medium.com/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-01321d3953cb*](https://arayofhope7.medium.com/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-01321d3953cb)
>
> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

### **This is what the lab says.**

* This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.
* The database contains a different table called `users`, with columns called `username` and `password`.
* To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.

**In this blog, I will jump directly into the practical part. For the theory and concepts, please refer to the Day 7 blog.**

Here’s what the application looks like.

Press enter or click to view image in full size

![]()

*We have multiple categories on the site, and when I clicked on the ‘Accessories’ category, I noticed that the URL contains a category parameter with a specific value. This indicates that the application uses this parameter to dynamically retrieve data, likely from a database, which could be vulnerable to SQL injection if input validation is insufficient.*

Press enter or click to view image in full size

![]()

The `category` parameter accepts arbitrary input`ray` and reflects it in the response, indicating that the backend might be using it directly in queries. This makes it vulnerable to SQL injection testing.

Press enter or click to view image in full size

![]()

*Used a single quote (*`'`*) to identify the developer code or to break the query, and sure enough, the query broke. This means we can now confirm that the application is vulnerable to SQL injection. It appears they have not implemented proper input sanitization.*

### Let’s Intercept the data:

Press enter or click to view image in full size

![]()

***Data was intercepted and sent to the repeater.***

Press enter or click to view image in full size

![]()

***This is how the request and response look. Now, we will try to identify which parts are developer-written code and which syntax elements break or interrupt the developer-written code.***

Press enter or click to view image in full size

![]()

***Used double quotes (***`"`***) and it returned a 200 OK, which means it didn't break the query.***

Press enter or click to view image in full size

![]()

*Used single quotes (*`'`*) and it returned an error, which means it broke the query. Therefore, we can now confirm that it is interacting with the database and is vulnerable to SQL injection.*

Press enter or click to view image in full size

![]()

*Used* `' ORDER BY 3--` *and it returned an internal server error, which means the table doesn't have 3 columns. Let's try with 2 instead.*

Press enter or click to view image in full size

![]()

*Used* `' ORDER BY 2--` *and it returned 200 OK, which means the table has 2 columns. Now, we will try to identify what is the datatype.*

Press enter or click to view image in full size

![]()

Used `' UNION SELECT 1, 2--` and it returned an error, which means the columns do not have an integer data type.

Press enter or click to view image in full size

![]()

Used `' UNION SELECT 'ray', 'ray'--` and it returned 200 OK, which means the columns have a CHAR datatype.

Press enter or click to view image in full size

![]()

Used `' UNION SELECT username, password FROM users--` and it returned 200 OK. Now, you may ask why I used the `users`table—this was mentioned in the lab instructions, but in real-world scenarios, it's also a common default table. So make sure to try it.

Press enter or click to view image in full size

![]()

*Used those credentials to log in to the application, and we were able to access the account as an admin. This is how we achieved complete account takeover.*

Press enter or click to view image in full size

![]()

## Boom! Lab solved. And hey, if you learned something and didn’t break your brain in the process, that’s a win-win!

Happy Hunting — Do hit a clap and follow for the best content

![]()

**My Social:**

LinkedIn: <https://www.linkedin.com/in/ray-of-hope/>

YouTube Channel: [www.youtube.com/@arayofhope7](http://www.youtube.com/%40arayofhope7)

Twitter: <https://x.com/ray_of_hope7>

Instagram: <https://www.instagram.com/a_rayofhope7/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ab892f5a9527---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----ab892f5a9527---------------------------------------)

[Penet...