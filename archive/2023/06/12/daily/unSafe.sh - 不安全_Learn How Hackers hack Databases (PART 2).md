---
title: Learn How Hackers hack Databases (PART 2)
url: https://buaq.net/go-168246.html
source: unSafe.sh - 不安全
date: 2023-06-12
fetch_date: 2025-10-04T11:44:39.901894
---

# Learn How Hackers hack Databases (PART 2)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Learn How Hackers hack Databases (PART 2)

Hello friends, I’m Rajneesh Kumar Arya back again with my new blog on SQL Injection. If you haven’t
*2023-6-11 20:56:51
Author: [infosecwriteups.com(查看原文)](/jump-168246.htm)
阅读量:26
收藏*

---

Hello friends, I’m Rajneesh Kumar Arya back again with my new blog on SQL Injection. If you haven’t checked out [my first blog](https://medium.com/%40RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) so first take a look at that and then you can continue with this one so without further do let’s power on your system, get some coffee or tea and get jump into it.

So, our sample website is having a search bar here so let’s try our technique here.

> DISCLAIMER: Do not use these techniques to hack anyone try these in your own lab environment.

I put a random string in the search parameter and hit ENTER then it appears in the URL which means it is having GET method to request the server.

step2 : enter “test” in search parameter

As we found our endpoint. So, to test the vulnerability of SQL injection let’s fireup our tool called [bursuite](https://portswigger.net/burp/communitydownload) and intercept the request.

step3:intercept the request in burpsuite

Now press Ctrl + R to send the request to Repeater where we can modify the request.

step4:Send request to the repeater

Now we need to add a ‘test’ in the search parameter and send the request.

step5:Add ‘test’ in search parameter and send the request.

Here we got the response of the sever in the response section with a 200 OK response code which means our parameter was sent to the server without any error.

From now the main games start, we need to modify the request and again send it to the server and check its behavior against this request. I’m adding a ‘ in front of our parameter value test and sending it.

step7:Modifying the request by adding a ‘ in front of test.

And we got an error with the 500 Internal Server Error response code which confirm that here is the vulnerability of SQL Injection.

> Hey, do you know the difference between a developer and Hacker? well, the developer hates the error but a hacker loves it so in this case also we got an error which is a good thing for us but not for developers.

step8:got a 500 server error

We confirmed that our sample website’s search parameter is vulnerable to SQL Injection so now we have to just exploit that vulnerability. To do this we need to call our tool sqlmap.

SQLMAP tool

Now open your terminal or command prompt and type the following command but before that copy the request from the burp suite and paste to any text editor and modify it by adding an [Asterisk](https://en.wikipedia.org/wiki/Asterisk) and save it, we had done the same step in the [previous blog](https://medium.com/%40RajneeshKarya/sql-injection-for-beginners-using-sqlmap-36e091e8a070) also, go and check out.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt --dbs --level 5
```

Here, I use ‘— dbs’ for enumerating database and ‘— level’ to increase the aggressiveness of the attack now hit ENTER and take some tea or coffee because it takes time and more than the previous one.

step9:enumerating database

And you can see we got database information and to know what inside database just type this command and take a coffee break.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt --tables --threads 10
```

I use ‘— tables’ to enumerating all the tables present in this database ,‘ — threads’ to increase the speed of enumeration and I got this juicy information.

step10: got 20 tables

As you can see I got 20 Tables but I’m only interested in the ‘Users’ table. So, to see what is inside that table you need to just type this command and hit ENTER.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt  --threads 10 -T Users --columns
```

I use ‘-T’ to select the table name and ‘ — columns’ to enumerating columns and I got this information.

step11:Enumerating columns

And again it gave me a lot of data but I’m only interested in ‘email’ and ‘password’ because I wanted to see how many users are there in this website and their password so I can log into it. So, to do so you need type this command and press ENTER.

```
python3 sqlmap.py -r /home/kairaj5456/Desktop/request.txt  --threads 10 -T Users -C email,password --dump
```

I use ‘-C’ to selecting the columns and ‘ — dump’ to dump all the data from these columns and it takes long time to dump all the emails and password so again a coffee break and you’re good to go.

step11:Dump all the data inside the columns

We got this whole information from the columns but it is useless because you can see passwords are in encrypted form and we cannot use these to gain access to the account. So, what we can do now.

Now, I’ll show you how you can gain access to the accounts with their emails only.

So let’s hack one of the email from our list I choose ‘[[email protected]](/cdn-cgi/l/email-protection#9df5fceff4edeffcf6fceef5ada4adafddfaf0fcf4f1b3fef2f0)’ as an email now we have to go to login page of this website.

step12:Login page

And enter the email in the email parameter and anything in the password section and you can login to that account. Its seems like a joke that how we can login into someones account by putting anything in the password but the reality is its possible and I’m gonna show how it works.

```
'UNION SELECT * FROM Users WHERE email='[email protected]'--
```

So, copy the above thing and paste into the email parameter and type anything in the password parameter and press Login…….

BOOM! we are in….we hack the username and get access to his account.

To Understand whats happened here you should have a little knowledge about SQL Query but don’t worry I’ll explain you.

So, basically I use **SELECT** for Select the data and I use ‘**\***’ astrisk after that which means select all the data.

**FROM** is used to navigate the Table name which is Users if you remember.

**WHERE** is used to check whether this input email is present in our database or not and at the end this is the main thing the two dashes “ — “ which comment down all the other query including password query and if you know comments are not executable and that’s why the server did not check the password query and only check the email query and if you not put two dashes at the end you are not able to log in.

This is how you can hack account using SQL Injection and WAIT!!! I have challenge for you hack [this website](http://testfire.net/) and try to login.

Till then keep learning, keep exploring and do HACKING.

文章来源: https://infosecwriteups.com/sql-injection-for-beginners-using-sqlmap-part-2-53e9775b67f5?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)