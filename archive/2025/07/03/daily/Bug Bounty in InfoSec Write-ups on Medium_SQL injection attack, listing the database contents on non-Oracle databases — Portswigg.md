---
title: SQL injection attack, listing the database contents on non-Oracle databases — Portswigg
url: https://infosecwriteups.com/sql-injection-attack-listing-the-database-contents-on-non-oracle-databases-portswigg-42fae517cc6e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:51:25.500828
---

# SQL injection attack, listing the database contents on non-Oracle databases — Portswigg

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F42fae517cc6e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-attack-listing-the-database-contents-on-non-oracle-databases-portswigg-42fae517cc6e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-attack-listing-the-database-contents-on-non-oracle-databases-portswigg-42fae517cc6e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-42fae517cc6e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-42fae517cc6e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL injection attack, listing the database contents on non-Oracle databases — Portswigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--42fae517cc6e---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--42fae517cc6e---------------------------------------)

5 min read

·

Apr 10, 2025

--

Listen

Share

Hi, my fellow hackers. This is Rayofhope. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

Day 5 of posting all the PortSwigger labs, not just the solutions. I’ll break down *why* we take each step, because once the ‘why’ is clear, the ‘how’ becomes easy.

**Let’s Start:**

![]()

Before you go for this blog, make sure to read the Previous one
***Link to Fourth Blog:*** <https://arayofhope7.medium.com/sql-injection-attack-querying-the-database-type-and-version-on-mysql-and-microsoft-85081e7eef71>

> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

**The lab states that it is not an Oracle database, which means it could be either MySQL, MSSQL, or PostgreSQL.**

* In this case, it turns out to be a **PostgreSQL database**, and you’ll see why by the end of this blog.
* Since it’s a PostgreSQL database, there are a few important details we need to keep in mind.

N**ote:**

When you’re unsure about the core database, it’s a good idea to test payloads from different database types; one of them might trigger a response.

> ***Microsoft SQL Server:*** *SELECT @@version*
>
> ***PostgreSQL****: SELECT version()*
>
> ***MySQL:*** *SELECT @@version*

In PostgreSQL, "`information_schema.tables"` is commonly used to enumerate available tables within the database.

P***ostgreSQL,*** `information_schema.tables` ***includes:***

* `table_catalog` (Name of the database containing the table (always the current database)
* `table_schema` (Name of the schema containing the table, like `public`, `pg_catalog`, etc.)
* `table_name` (Name of the Table)
* `table_type` (e.g., `'BASE TABLE'`, `'VIEW'`)
* `column_name`(Name of the column)

Press enter or click to view image in full size

![]()

Here’s what the application looks like.

Press enter or click to view image in full size

![]()

Try to find the parameter

Press enter or click to view image in full size

![]()

We identified that there is a parameter called `category` With the value `gift`.

Press enter or click to view image in full size

![]()

We can see that whatever value we are providing is getting ***projected***, which probably means it is vulnerable to ***Union-based SQL injection***.

Press enter or click to view image in full size

![]()

The request was intercepted and forwarded to the Repeater tool to log and analyze the request and response times.

Press enter or click to view image in full size

![]()

Injecting a single quote (`'`) caused an ***internal server error***, indicating that the input may ***interfere with the SQL query structure***, potentially due to ***insufficient input sanitization.***

Press enter or click to view image in full size

![]()

Used `' ORDER BY 3 --` and the application responded with an internal server error, which likely means the table doesn't have 3 columns. Let's try using 2 instead.

Press enter or click to view image in full size

![]()

*And it returned a* ***200 OK response,*** *which means the query executed successfully, indicating that the table has 2 columns*

Press enter or click to view image in full size

![]()

Tried to identify the datatype, and it is a character.

Press enter or click to view image in full size

![]()

We can see that it is not a numeric type.

Press enter or click to view image in full size

![]()

*The reason for using* `table_name` *and* `information_schema.tables` *is based on the understanding that* `information_schema` *is a built-in database schema in most SQL systems (like MySQL and PostgreSQL) that stores metadata about the database structure. The* `tables`*table specifically contains information about all existing tables, and the* `table_name` *column lists their names.*

Press enter or click to view image in full size

![]()

***And we received the user table (***`users_palrcr`***) in the response, which confirms that the table exists in the database.***

Press enter or click to view image in full size

![]()

Used ***‘ union select column\_name, ‘rayofhope’ from information\_schema.columns where table\_name=’users\_palrcr’ — —*** and it returned 200 OK

Press enter or click to view image in full size

![]()

The response also revealed sensitive data, specifically a password field with the value `password_hlbiqz`

Press enter or click to view image in full size

![]()

We do get the user details.

Press enter or click to view image in full size

![]()

**Used a simple UNION query to retrieve data related to the username and password:** `' UNION SELECT username_aiyuin, password_hlbiqz FROM users_palrcr --` **and it returned a 200 OK response.**

Press enter or click to view image in full size

![]()

**In the response, we obtained the administrator username and password:** `mh7x73ezh0ymtucxc65h.`

Press enter or click to view image in full size

![]()

Using the retrieved administrator credentials, we were able to successfully log in and gain access to the administrative interface, confirming full account takeover.

## ***Boom! Lab solved. And hey, if you learned something and didn’t break your brain in the process, that’s a win-win!***

Happy Hunting — Do hit a clap and follow for the best content

![]()

**My Social:**

LinkedIn: <https://www.linkedin.com/in/ray-of-hope/>

YouTube Channel: [www.youtube.com/@arayofhope7](http://www.you...