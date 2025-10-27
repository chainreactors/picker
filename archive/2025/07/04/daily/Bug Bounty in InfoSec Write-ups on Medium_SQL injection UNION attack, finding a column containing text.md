---
title: SQL injection UNION attack, finding a column containing text
url: https://infosecwriteups.com/sql-injection-union-attack-finding-a-column-containing-text-8bb9f92b6430?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-04
fetch_date: 2025-10-06T23:50:31.658364
---

# SQL injection UNION attack, finding a column containing text

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8bb9f92b6430&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-finding-a-column-containing-text-8bb9f92b6430&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-finding-a-column-containing-text-8bb9f92b6430&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8bb9f92b6430---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8bb9f92b6430---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL injection UNION attack, finding a column containing text

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--8bb9f92b6430---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--8bb9f92b6430---------------------------------------)

4 min read

·

Apr 13, 2025

--

Listen

Share

Hi, my fellow hackers. This is Rayofhope. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

Day 8 of posting all the PortSwigger labs, not just the solutions. I’ll break down *why* we take each step, because once the ‘why’ is clear, the ‘how’ becomes easy.

**Let’s Start:**

![]()

> **Before you go for this blog, make sure to read the Previous one**
> **Link to Seventh Blog:** <https://arayofhope7.medium.com/sql-injection-union-attack-determining-the-number-of-columns-returned-by-the-query-01321d3953cb>
>
> V***ideo Walkthrough*** *— You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.*

## This is what the lab says.

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a [previous lab](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns). The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

* **In this blog, I will jump directly into the practical part. For the theory and concepts, please refer to the Day 7 blog.**

Here’s what the application looks like.

Press enter or click to view image in full size

![]()

*We have multiple categories on the site, and when I clicked on the ‘Gift’ category, I noticed that the URL contains a category parameter with a specific value. This indicates that the application uses this parameter to dynamically retrieve data, likely from a database. which could be vulnerable to SQL injection if input validation is insufficient.*

Press enter or click to view image in full size

![]()

The `category` parameter accepts arbitrary input`rayofhope` and reflects it in the response, indicating that the backend might be using it directly in queries. This makes it vulnerable to SQL injection testing.

Press enter or click to view image in full size

![]()

*Used a single quote (*`'`*) to identify the developer code or to break the query, and sure enough, the query broke. This means we can now confirm that the application is vulnerable to SQL injection. It appears they have not implemented proper input sanitization.*

Press enter or click to view image in full size

![]()

*I tried* `' ORDER BY 2 --` *and it got projected, which means the application likely has more than two columns in the query result.*

Press enter or click to view image in full size

![]()

*I tried* `' ORDER BY 4 --` *and it returned an error, which means the query likely has three columns. Now that we know there are three columns, we need to identify the data type and retrieve 2ibKWe.*

Press enter or click to view image in full size

![]()

*Used* `' UNION SELECT 1, 2, 3 --` *and it returned an error, which means the application doesn't have all columns with integer data types.*

Press enter or click to view image in full size

![]()

*Used* `' UNION SELECT 'ray', 'ray', 'ray'--` *and it returned an error, which means the application doesn't have all columns with CHAR data types.*

Note:

Now, it could be that the table has both `CHAR` and an integer data types, but how can we identify them? We will use a NULL column.

Press enter or click to view image in full size

![]()

And it returned 200 OK, now we have to retrieve the string: ‘2ibKWe’

Press enter or click to view image in full size

![]()

Used `' UNION SELECT NULL, NULL, '2ibKWe' --` and it returned an error, which means the third column is not a string and does not accept '2ibKWe'.

Press enter or click to view image in full size

![]()

Used `' UNION SELECT NULL, '2ibKWe', NULL--` and it returned 200 OK, which means the second column is a string and does accept '2ibKWe'.

## Boom! Lab solved. And hey, if you learned something and didn’t break your brain in the process, that’s a win-win!

Happy Hunting — Do hit a clap and follow for the best content

![]()

**My Social:**

LinkedIn: <https://www.linkedin.com/in/ray-of-hope/>

YouTube Channel: [www.youtube.com/@arayofhope7](http://www.youtube.com/%40arayofhope7)

Twitter: <https://x.com/ray_of_hope7>

Instagram: <https://www.instagram.com/a_rayofhope7/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8bb9f92b6430---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----8bb9f92b6430---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----8bb9f92b6430---------------------------------------)

[Web Penetration Testing](https://medium.com/tag/web-penetration-testing?source=post_page-----8bb9f92b6430---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----8bb9f92b6430---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0...