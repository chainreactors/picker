---
title: VulnNodeApp - A Vulnerable Node.Js Application
url: https://buaq.net/go-246761.html
source: unSafe.sh - 不安全
date: 2024-06-24
fetch_date: 2025-10-06T16:54:51.608867
---

# VulnNodeApp - A Vulnerable Node.Js Application

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

![](https://8aqnet.cdn.bcebos.com/973506ac1f214c5560545edfdae3590a.jpg)

VulnNodeApp - A Vulnerable Node.Js Application

A vulnerable application made using node.js, express server and ejs template engine. This ap
*2024-6-23 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-246761.htm)
阅读量:16
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjhkbtFHEZYZ2XWPDOmuQB510cU5uUDArQC0gsTgoippwjw8deFa6WZgTE4ubxRQ1ntloFXY__gPPWp9Ffeo7iqYqdKGeXzlNPd0VlvaX2S9wLXONtEvXzdPt2K68TYbV2m87R-CbCGQqgq6rc85_LeEeRMhCoxWPi7hImJVMsOk3YxRft3eO4kRFmtwpOw=w640-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEjhkbtFHEZYZ2XWPDOmuQB510cU5uUDArQC0gsTgoippwjw8deFa6WZgTE4ubxRQ1ntloFXY__gPPWp9Ffeo7iqYqdKGeXzlNPd0VlvaX2S9wLXONtEvXzdPt2K68TYbV2m87R-CbCGQqgq6rc85_LeEeRMhCoxWPi7hImJVMsOk3YxRft3eO4kRFmtwpOw)

A [vulnerable](https://www.kitploit.com/search/label/Vulnerable "vulnerable") application made using node.js, express server and ejs template engine. This application is meant for educational purposes only.

## Clone this repository

```
git clone https://github.com/4auvar/VulnNodeApp.git
```

## Application setup:

* Install the latest node.js version with npm.
* Open terminal/command prompt and navigate to the location of downloaded/cloned repository.
* Run command: `npm install`

## DB setup

* Install and configure latest mysql version and start the mysql service/deamon
* Login with root user in mysql and run below sql script:

```
CREATE USER 'vulnnodeapp'@'localhost' IDENTIFIED BY 'password';
create database vuln_node_app_db;
GRANT ALL PRIVILEGES ON vuln_node_app_db.* TO 'vulnnodeapp'@'localhost';
USE vuln_node_app_db;
create table users (id int AUTO_INCREMENT PRIMARY KEY, fullname varchar(255), username varchar(255),password varchar(255), email varchar(255), phone varchar(255), profilepic varchar(255));
insert into users(fullname,username,password,email,phone) values("test1","test1","test1","[email protected]","976543210");
insert into users(fullname,username,password,email,phone) values("test2","test2","test2","[email protected]","9887987541");
insert into users(fullname,username,password,email,phone) values("test3","test3","test3","[email protected]","9876987611");
insert into users(fullname,username,password,email,phone) values("test4","test4","test4","[email protected]","9123459876");
insert into users(fullname,username,password,email,phone) values("test5","test5","test   5","[email protected]","7893451230");
```

## Set basic environment variable

* User needs to set the below environment variable.
  + DATABASE\_HOST (E.g: localhost, 127.0.0.1, etc...)
  + DATABASE\_NAME (E.g: vuln\_node\_app\_db or DB name you change in above DB script)
  + DATABASE\_USER (E.g: vulnnodeapp or user name you change in above DB script)
  + DATABASE\_PASS (E.g: password or password you change in above DB script)

* Open the command prompt/terminal and navigate to the location of your repository
* Run command: `npm start`
* Access the application at http://localhost:3000

* SQL Injection
* Cross Site Scripting (XSS)
* Insecure Direct Object Reference (IDOR)
* Command Injection
* Arbitrary File Retrieval
* Regular Expression Injection
* External XML Entity Injection (XXE)
* Node js Deserialization
* Security Misconfiguration
* Insecure Session Management

* Will add new vulnerabilities such as CORS, Template Injection, etc...
* Improve application documentation

* In case of bugs in the application, feel free to create an [issues](https://github.com/4auvar/VulnNodeApp/issues "issues") on github.

* Feel free to create a pull request for any contribution.

You can reach me out at [@4auvar](https://twitter.com/4auvar "@4auvar")

VulnNodeApp - A Vulnerable Node.Js Application
![VulnNodeApp - A Vulnerable Node.Js Application](https://blogger.googleusercontent.com/img/a/AVvXsEjhkbtFHEZYZ2XWPDOmuQB510cU5uUDArQC0gsTgoippwjw8deFa6WZgTE4ubxRQ1ntloFXY__gPPWp9Ffeo7iqYqdKGeXzlNPd0VlvaX2S9wLXONtEvXzdPt2K68TYbV2m87R-CbCGQqgq6rc85_LeEeRMhCoxWPi7hImJVMsOk3YxRft3eO4kRFmtwpOw=s72-w640-c-h320)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2024/06/vulnnodeapp-vulnerable-nodejs.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)