---
title: SQL injection UNION attack, retrieving multiple values in a single column — PortSwigger
url: https://infosecwriteups.com/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-65d850e9cc8e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-01
fetch_date: 2025-10-06T23:53:27.959873
---

# SQL injection UNION attack, retrieving multiple values in a single column — PortSwigger

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F65d850e9cc8e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-65d850e9cc8e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-65d850e9cc8e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-65d850e9cc8e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-65d850e9cc8e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SQL injection UNION attack, retrieving multiple values in a single column — PortSwigger

[![RayofHope](https://miro.medium.com/v2/resize:fill:64:64/1*pb6R-58-0JIs9DggdPv4MA.jpeg)](https://arayofhope7.medium.com/?source=post_page---byline--65d850e9cc8e---------------------------------------)

[RayofHope](https://arayofhope7.medium.com/?source=post_page---byline--65d850e9cc8e---------------------------------------)

5 min read

·

Apr 19, 2025

--

Listen

Share

Hi, my fellow hackers. This is Rayofhope. I have over 5 years of experience and am currently working as a consultant with a Big 4 firm.

Day 9 of posting all the PortSwigger labs, not just the solutions. I’ll break down *why* we take each step, because once the ***‘why’ is clear, the ‘how’ becomes easy.***

**Let’s Start:**

![]()

> ***Before you go for this blog, make sure to read the Previous one******Link to Seventh Blog:*** [https://medium.com/@arayofhope7/sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data-portswigger-12342def10ec](https://medium.com/%40arayofhope7/sql-injection-vulnerability-in-where-clause-allowing-retrieval-of-hidden-data-portswigger-12342def10ec)
>
> **Video Walkthrough** — You can watch the video or read the blog, totally up to you. But if you ask me, start with the video, then read the blog to connect all the dots.

## This is what the lab says.

* This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application’s response so you can use a UNION attack to retrieve data from other tables.
* The database contains a different table called `users`, with columns called `username` and `password`.
* To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the `administrator` user.’

Note:

* A single table in a database can contain ***multiple columns***, and each of these columns can have a ***different data type*** based on the kind of ***information it is designed to store***.

Press enter or click to view image in full size

![]()

Here’s what the application looks like.

Press enter or click to view image in full size

![]()

We have multiple categories on the site, and when I clicked on the ‘***Lifestyle***’ category, I noticed that the URL contains a category parameter with a specific value. This indicates that the application uses this parameter to dynamically retrieve data, likely from a database, which could be vulnerable to SQL injection if input validation is insufficient.

Press enter or click to view image in full size

![]()

*The category parameter accepts arbitrary input* ***rayofhope*** *and reflects it in the response, indicating that the backend might be using it directly in queries. This makes it vulnerable to SQL injection testing.*

Press enter or click to view image in full size

![]()

## Let’s Intercept the data:

Press enter or click to view image in full size

![]()

The data was intercepted and sent to the repeater, and this is what the response looks like.

Press enter or click to view image in full size

![]()

*Since we have a parameter with the value* ***‘rayofhope’,*** *we will try to figure out the underlying code written by the developer by injecting a single quote* ***(‘)*** *to see if it breaks the query.*

Press enter or click to view image in full size

![]()

*And it throws an internal server error, which indicates that the application is vulnerable to SQL Injection. We also get an idea of how the query is structured. Now, we’ll try to figure out how many columns the query has.*

Press enter or click to view image in full size

![]()

“Used `' ORDER BY 2 --` and it returned a 200 OK response, which indicates that the query executed successfully and the table has at least 2 columns. Let’s see if it has 3 columns or not.

Press enter or click to view image in full size

![]()

*When we used* `ORDER BY 3`***,*** *it threw an error, which confirms that the table has only 2 columns. Now, the next step is to identify the data types of these columns.*

Press enter or click to view image in full size

![]()

*We used* `' UNION SELECT 1, 2 --` *and it returned an error, which means that not all columns accept integer data types.*

Press enter or click to view image in full size

![]()

*It’s not even accepting a* `CHAR` *data type, so it's possible that the table has one column with an* ***integer data type*** *and the other with a string* ***(CHAR or VARCHAR)*** *data type. Let’s try using one integer and one* ***string value*** *to test this.*

Press enter or click to view image in full size

![]()

*It returned a 200 OK response, which confirms that the first column is of integer type and the second column is of string type. Now that we know the second column is a string type, we will attempt to retrieve the user and password details from this column.*

Press enter or click to view image in full size

![]()

*There we go! I tried using* `' UNION SELECT 1, username FROM users --` *and received a 200 OK response.*

Press enter or click to view image in full size

![]()

*From the response body, we can clearly see that the usernames have been successfully retrieved. Let’s see if we can get password as well.*

Press enter or click to view image in full size

![]()

*And we’ve also successfully retrieved the passwords from the response.*

***Now let’s see if we can retrieve both the username and password in a single query.***

Press enter or click to view image in full size

![]()

*By using the CONCAT statement with* ***’ UNION SELECT 1, username || password from users — —*** *, we were able to retrieve both the* ***username*** *and* ***password*** *in a single response.*

Note: To use the `CONCAT` statement, it's important to first identify the type of database being used, as the syntax varies ac...