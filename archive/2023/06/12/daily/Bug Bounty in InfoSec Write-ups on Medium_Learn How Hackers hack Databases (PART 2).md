---
title: Learn How Hackers hack Databases (PART 2)
url: https://infosecwriteups.com/sql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-06-12
fetch_date: 2025-10-04T11:45:11.117482
---

# Learn How Hackers hack Databases (PART 2)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F53e9775b67f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-53e9775b67f5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-53e9775b67f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Learn How Hackers hack Databases (PART 2)

[![Rajneesh Kumar Arya](https://miro.medium.com/v2/resize:fill:64:64/1*a7KPXIpCqRnq7KYHJ8PTpA.png)](https://medium.com/%40RajneeshKarya?source=post_page---byline--53e9775b67f5---------------------------------------)

[Rajneesh Kumar Arya](https://medium.com/%40RajneeshKarya?source=post_page---byline--53e9775b67f5---------------------------------------)

6 min read

·

Oct 16, 2022

--

1

Listen

Share

Hello friends, I’m Rajneesh Kumar Arya back again with my new blog on SQL Injection. If you haven’t checked out [my first blog](https://medium.com/%40RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) so first take a look at that and then you can continue with this one so without further do let’s power on your system, get some coffee or tea and get jump into it.
In the previous blog, we learn how to enumerate the database of a website having a POST request method with [sqlmap](https://github.com/sqlmapproject/sqlmap) today we are going to do the same thing but with a different method so first of all we need a [sample website.](https://juice-shop.herokuapp.com/#/)

So, our sample website is having a search bar here so let’s try our technique here.

Press enter or click to view image in full size

![]()

> DISCLAIMER: Do not use these techniques to hack anyone try these in your own lab environment.

I put a random string in the search parameter and hit ENTER then it appears in the URL which means it is having GET method to request the server.

Press enter or click to view image in full size

![]()

step2 : enter “test” in search parameter

As we found our endpoint. So, to test the vulnerability of SQL injection let’s fireup our tool called [bursuite](https://portswigger.net/burp/communitydownload) and intercept the request.

Press enter or click to view image in full size

![]()

step3:intercept the request in burpsuite

Now press Ctrl + R to send the request to Repeater where we can modify the request.

Press enter or click to view image in full size

![]()

step4:Send request to the repeater

Now we need to add a ‘test’ in the search parameter and send the request.

![]()

step5:Add ‘test’ in search parameter and send the request.

![]()

Here we got the response of the sever in the response section with a 200 OK response code which means our parameter was sent to the server without any error.

From now the main games start, we need to modify the request and again send it to the server and check its behavior against this request. I’m adding a ‘ in front of our parameter value test and sending it.

![]()

step7:Modifying the request by adding a ‘ in front of test.

And we got an error with the 500 Internal Server Error response code which confirm that here is the vulnerability of SQL Injection.

> Hey, do you know the difference between a developer and Hacker? well, the developer hates the error but a hacker loves it so in this case also we got an error which is a good thing for us but not for developers.

![]()

step8:got a 500 server error

We confirmed that our sample website’s search parameter is vulnerable to SQL Injection so now we have to just exploit that vulnerability. To do this we need to call our tool sqlmap.

![]()

SQLMAP tool

Now open your terminal or command prompt and type the following command but before that copy the request from the burp suite and paste to any text editor and modify it by adding an [Asterisk](https://en.wikipedia.org/wiki/Asterisk) and save it, we had done the same step in the [previous blog](https://medium.com/%40RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) also, go and check out.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt --dbs --level 5
```

Here, I use ‘— dbs’ for enumerating database and ‘— level’ to increase the aggressiveness of the attack now hit ENTER and take some tea or coffee because it takes time and more than the previous one.

![]()

step9:enumerating database

And you can see we got database information and to know what inside database just type this command and take a coffee break.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt --tables --threads 10
```

I use ‘— tables’ to enumerating all the tables present in this database ,‘ — threads’ to increase the speed of enumeration and I got this juicy information.

Press enter or click to view image in full size

![]()

step10: got 20 tables

As you can see I got 20 Tables but I’m only interested in the ‘Users’ table. So, to see what is inside that table you need to just type this command and hit ENTER.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt  --threads 10 -T Users --columns
```

I use ‘-T’ to select the table name and ‘ — columns’ to enumerating columns and I got this information.

Press enter or click to view image in full size

![]()

step11:Enumerating columns

And again it gave me a lot of data but I’m only interested in ‘email’ and ‘password’ because I wanted to see how many users are there in this website and their password so I can log into it. So, to do so you need type this command and press ENTER.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt  --threads 10 -T Users -C email,password --dump
```

I use ‘-C’ to selecting the columns and ‘ — dump’ to dump all the data from these columns and it takes long time to dump all the emails and password so again a coffee break and you’re good to go.

Press enter or click to view image in full size

![]()

step11:Dump all the data inside the columns

![]()

We got this whole information from the columns but it is useless because you can see passwords are in encrypted form and we cannot use these to gain access to the account. So, what we can do now.

Now, I’ll show you how you can gain access to the accounts with their emails only.

![]()

So let’s hack one of the email from our list I choose ‘hariprakash0902@gmail.com’ as an email now we have to go to ...