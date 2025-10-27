---
title: Learn How hackers hack Databases (PART 1)
url: https://infosecwriteups.com/sql-injection-for-beginners-using-sqlmap-36e091e8a070?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-12
fetch_date: 2025-10-04T11:45:13.835640
---

# Learn How hackers hack Databases (PART 1)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F36e091e8a070&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-for-beginners-using-sqlmap-36e091e8a070&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-for-beginners-using-sqlmap-36e091e8a070&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-36e091e8a070---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-36e091e8a070---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Learn How hackers hack Databases (PART 1)

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:64:64/1*a7KPXIpCqRnq7KYHJ8PTpA.png)](https://medium.com/%40RajneeshKarya?source=post_page---byline--36e091e8a070---------------------------------------)

[Rajneesh Kumar Arya](https://medium.com/%40RajneeshKarya?source=post_page---byline--36e091e8a070---------------------------------------)

4 min read

·

Oct 9, 2022

--

Listen

Share

Press enter or click to view image in full size

![]()

Hello Learners, so let’s start with my first blog it is just based on a topic you already knew SQL injection before that let me just introduce myself I am Rajneesh K. Arya student of B.Tech CSE specializing in Cybersecurity
so let us start our blog.

SQL is the structure query language that deals with databases, SQL generated some queries at the backend of the server and grep the data from the database using this query. In SQL Injection we have to just interact with the database with our manipulated query, in other words, we have the power to control the query and we got all information we want.

So, Without going deep into the theory part let me just show you how it works. Today we are using some tools that you can download its free open sources.

> DISCLAIMER: Do not use these techniques to hack anyone try these in your own lab environment.

We are taking this <http://testphp.vulnweb.com/>a sample vulnerable website for SQL injection you can also try this too.

Press enter or click to view image in full size

![]()

This is our sample website which is having a login page but the thing is we don’t know what its username and password. So, Lets call our tool here which sqlmap.

Press enter or click to view image in full size

![]()

You can download this from [github](https://github.com/sqlmapproject/sqlmap).

we have two types of request GET and POST the basic difference is that GET request show the parameter content on the URL but POST don’t.

As you can see I changed the request method to GET and the content of the parameters are clearly visible on the URL.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

In sqlmap also we have two methods based on the request method, first of all, we see how to use sqlmap with the POST request method.
Just intercept the request using burpsuite and copy the all requested content.

Press enter or click to view image in full size

![]()

burpsuite copied request

Now, open your favorite text editor and paste that sucker on it and change the uname parameter value with an asterisk (\*) and save it with a .txt extension.

Press enter or click to view image in full size

![]()

Now, open a terminal or command prompt to start with our main step which is using sqlmap. so type the following command and wait for the result.

> python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt — dbs

Here, I use -r for the request file and — dbs for enumerating all the databases, run the command and take some coffee or tea because it takes time.

Press enter or click to view image in full size

![]()

As you can see I got juicy information about this target which is the name of the databases one is *acuart* and other is a default one *information\_schema*. To see what is inside the database we need to just use this command.

> python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt -D acuart — tables

We use -D for selecting the name of the database and — tables to enumerate all the tables present in that database and we got 8 tables.

Press enter or click to view image in full size

![]()

I am gonna selecting the users table because I am interested in that, you can choose as per your interest so now we can see how many users are there in this database and hopefully their passwords also.

> python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt -D acuart -T users — dump

I use -T to select the Table name and — dump to dump all the data present in that table. It will ask you whether you want to crack those password or not because in databases the password are store in their cipher text form not in the plain text

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

and at the end we got a CSV file of all data present in that Table. I am gonna open this CSV file because in terminal the data is not properly sorted.

Press enter or click to view image in full size

![]()

BOOM! we got all information about the user.

This is how sql injection works and in the next blog I’ll share about the GET method also till then keep learning, keep exploring and do hacking.

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----36e091e8a070---------------------------------------)

[Sql Injection](https://medium.com/tag/sql-injection?source=post_page-----36e091e8a070---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----36e091e8a070---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--36e091e8a070---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--36e091e8a070---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--36e091e8a070---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--36e091e8a070---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--36e091e8a070-----------------------...