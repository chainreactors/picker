---
title: DC-Sonar - Analyzing AD Domains For Security Risks Related To User Accounts
url: https://buaq.net/go-146691.html
source: unSafe.sh - 不安全
date: 2023-01-26
fetch_date: 2025-10-04T04:50:00.734171
---

# DC-Sonar - Analyzing AD Domains For Security Risks Related To User Accounts

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

![](https://8aqnet.cdn.bcebos.com/5782952824f88d0be6c3206d8f0f0e66.jpg)

DC-Sonar - Analyzing AD Domains For Security Risks Related To User Accounts

Repositories The project consists of repositories: dc-sonar-frontend dc-sonar-user-laye
*2023-1-25 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146691.htm)
阅读量:29
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh4T_TaJ_WITYbBqoWyvHgSUq1IW13NIF2MOl8t3_g3AYj44B1G_tS0PsJ6EHo9flgZui2dSIwMo4neB9Yw-CYFF4tjSyIiM_QMS8CNUqMqEKZFYSJmFevxnYASeRjNI4XGVJNjRxe6xR7LQnWXBqCwJFmlYKW0wS3wcbSALpKIRivwH4bRmRj5_I2fVA=w640-h314)](https://blogger.googleusercontent.com/img/a/AVvXsEh4T_TaJ_WITYbBqoWyvHgSUq1IW13NIF2MOl8t3_g3AYj44B1G_tS0PsJ6EHo9flgZui2dSIwMo4neB9Yw-CYFF4tjSyIiM_QMS8CNUqMqEKZFYSJmFevxnYASeRjNI4XGVJNjRxe6xR7LQnWXBqCwJFmlYKW0wS3wcbSALpKIRivwH4bRmRj5_I2fVA)

## Repositories

The project consists of repositories:

* [dc-sonar-frontend](https://github.com/ST1LLY/dc-sonar-frontend "dc-sonar-frontend")
* [dc-sonar-user-layer](https://github.com/ST1LLY/dc-sonar-user-layer "dc-sonar-user-layer")
* [dc-sonar-workers-layer](https://github.com/ST1LLY/dc-sonar-workers-layer "dc-sonar-workers-layer")
* [ntlm-scrutinizer](https://github.com/ST1LLY/ntlm-scrutinizer "ntlm-scrutinizer")

## Disclaimer

It's only for education purposes.

Avoid using it on the production [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") (AD) domain.

Neither contributor incur any responsibility for any using it.

## Social media

Check out our Red Team community [Telegram channel](https://t.me/RedTeambro "Telegram channel")

## Description

### Architecture

For the visual descriptions, open the [diagram files](https://github.com/ST1LLY/dc-sonar/tree/main/diagrams "diagram files") using the [diagrams.net](https://www.diagrams.net/ "diagrams.net") tool.

The app consists of:

* The [dc-sonar-frontend](https://github.com/ST1LLY/dc-sonar-frontend "dc-sonar-frontend") is the fronted part of the user web interface bases on:
  + [Angular](https://angular.io/ "Angular")
  + [Angular Material](https://material.angular.io/ "Angular Material")
* The [dc-sonar-user-layer](https://github.com/ST1LLY/dc-sonar-user-layer "dc-sonar-user-layer") is the backend part of the web app bases on:
  + [Python 3.10](https://www.python.org/downloads/ "Python 3.10")
  + [Django](https://www.djangoproject.com/ "Django")
  + [Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/queries/ "Django ORM")
  + [Django REST framework](https://www.django-rest-framework.org/ "Django REST framework")
  + [Celery](https://docs.celeryq.dev/en/latest/changelog.html "Celery")
  + [RabbitMQ](https://www.rabbitmq.com/ "RabbitMQ")
  + [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")
* The [dc-sonar-workers-layer](https://github.com/ST1LLY/dc-sonar-workers-layer "dc-sonar-workers-layer") is the logic layer that performs and runs analyzing processes which base on:
  + [Python 3.10](https://www.python.org/downloads/ "Python 3.10")
  + [SQLAlchemy](https://www.sqlalchemy.org/ "SQLAlchemy")
  + [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html "Alembic")
  + [APScheduler](https://apscheduler.readthedocs.io/en/3.x/ "APScheduler")
  + [RabbitMQ](https://www.rabbitmq.com/ "RabbitMQ")
  + [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")
* The [ntlm-scrutinizer](https://github.com/ST1LLY/ntlm-scrutinizer "ntlm-scrutinizer") is the NTLM hashes performer with REST API based on:

+ [Python 3.10](https://www.python.org/downloads/ "Python 3.10")
+ [FastAPI](https://fastapi.tiangolo.com/ "FastAPI")
+ [hashcat](https://github.com/hashcat/hashcat "hashcat")
+ [impacket](https://github.com/SecureAuthCorp/impacket "impacket")

### Functionallity

The DC Sonar Community provides functionality for analyzing AD domains for security risks related to accounts:

* Register analyzing AD domain in the app

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEhXzvzknvxOkjETMZb5CVQKjcW4rRvucd6rZuyZFWprOZdSJ_avODLB6cUrzJuz09rEkjSyPnMvvR6Ou4LGGHfoGfrFFnJL_naOZdvxQOff5-JauGFhJW7G1SEA7QX8pFGfPWNUcVKI-MXYto7ZXGiIoXRSXdy4fP-KGqotD5L7cS0TodpFdDF-OyLhiA=w640-h312)](https://blogger.googleusercontent.com/img/a/AVvXsEhXzvzknvxOkjETMZb5CVQKjcW4rRvucd6rZuyZFWprOZdSJ_avODLB6cUrzJuz09rEkjSyPnMvvR6Ou4LGGHfoGfrFFnJL_naOZdvxQOff5-JauGFhJW7G1SEA7QX8pFGfPWNUcVKI-MXYto7ZXGiIoXRSXdy4fP-KGqotD5L7cS0TodpFdDF-OyLhiA)
* See the statuses of domain analyzing processes

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEgP4NXGAyhO8DpjhUUZUlnk6j0gNt6TWWY-gmzHEFN7PNS8ODXNyY4z8fQAlcHqxPq8Gflbhp8VJ2jDfKHr9Fv3NAqLBIUsHNTC_Xu11245GCZRj7i9U5Uy6ysbWwgpK-sSv_ebv5KMP4bfTzbgJORVsdWPpggIM5LK9Rw5K2XrWGP1IxykswZa6E4HBw=w640-h314)](https://blogger.googleusercontent.com/img/a/AVvXsEgP4NXGAyhO8DpjhUUZUlnk6j0gNt6TWWY-gmzHEFN7PNS8ODXNyY4z8fQAlcHqxPq8Gflbhp8VJ2jDfKHr9Fv3NAqLBIUsHNTC_Xu11245GCZRj7i9U5Uy6ysbWwgpK-sSv_ebv5KMP4bfTzbgJORVsdWPpggIM5LK9Rw5K2XrWGP1IxykswZa6E4HBw)
* Dump and brute NTLM hashes from set AD domains to list accounts with weak and vulnerable passwords

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEjRcvrxN-Vi3hTAI4YMwnhvgR9Rvewfdn0xMERYM06l6pCA8lBWE4R_yRxnGETx4ArwjKiJNn-U9w4HXxRhYCda2ole6tzkJG5eYnxuqpOcgLpU9dCsAHpIkmhrILe2ZwN2MaCEI0vCwbwXoOblxahJ8o35uo7s9NUydA0iB1EJueJ-bSACts8Q5c8exw=w640-h312)](https://blogger.googleusercontent.com/img/a/AVvXsEjRcvrxN-Vi3hTAI4YMwnhvgR9Rvewfdn0xMERYM06l6pCA8lBWE4R_yRxnGETx4ArwjKiJNn-U9w4HXxRhYCda2ole6tzkJG5eYnxuqpOcgLpU9dCsAHpIkmhrILe2ZwN2MaCEI0vCwbwXoOblxahJ8o35uo7s9NUydA0iB1EJueJ-bSACts8Q5c8exw)
* Analyze AD domain accounts to list ones with never expire passwords

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEi6Ko0k4HFPyBSElT6uuhTAWDxAweR-xGQUyK_IZwvNVeDVihweI_ypx-e7mTktyhD255M9w6LIIVk2EoZU8dByL8Sg9j9KJTNvbnywxajA-ri0NWYxHdaUN8iJum-xzUb3fSGqiolM8ueHZtm5ko-DBGfcbZpvXjZiNDgnnzCpFHOnDstQA9ru-VPaPA=w640-h314)](https://blogger.googleusercontent.com/img/a/AVvXsEi6Ko0k4HFPyBSElT6uuhTAWDxAweR-xGQUyK_IZwvNVeDVihweI_ypx-e7mTktyhD255M9w6LIIVk2EoZU8dByL8Sg9j9KJTNvbnywxajA-ri0NWYxHdaUN8iJum-xzUb3fSGqiolM8ueHZtm5ko-DBGfcbZpvXjZiNDgnnzCpFHOnDstQA9ru-VPaPA)
* Analyze AD domain accounts by their NTLM password hashes to determine accounts and domains where passwords repeat

  [![](https://blogger.googleusercontent.com/img/a/AVvXsEh4T_TaJ_WITYbBqoWyvHgSUq1IW13NIF2MOl8t3_g3AYj44B1G_tS0PsJ6EHo9flgZui2dSIwMo4neB9Yw-CYFF4tjSyIiM_QMS8CNUqMqEKZFYSJmFevxnYASeRjNI4XGVJNjRxe6xR7LQnWXBqCwJFmlYKW0wS3wcbSALpKIRivwH4bRmRj5_I2fVA=w640-h314)](https://blogger.googleusercontent.com/img/a/AVvXsEh4T_TaJ_WITYbBqoWyvHgSUq1IW13NIF2MOl8t3_g3AYj44B1G_tS0PsJ6EHo9flgZui2dSIwMo4neB9Yw-CYFF4tjSyIiM_QMS8CNUqMqEKZFYSJmFevxnYASeRjNI4XGVJNjRxe6xR7LQnWXBqCwJFmlYKW0wS3wcbSALpKIRivwH4bRmRj5_I2fVA)

## Installation

### Docker

In progress ...

### Manually using dpkg

It is assumed that you have a clean [Ubuntu Server 22.04](https://ubuntu.com/download/server "Ubuntu Server 22.04") and account with the username "user".

The app will install to `/home/user/dc-sonar`.

The next releases maybe will have a more flexible installation.

Download dc\_sonar\_NNNN.N.NN-N\_amd64.tar.gz from the [last distributive](https://github.com/ST1LLY/dc-sonar/releases "last distributive") to the server.

Create a folder for extracting files:

```
mkdir dc_sonar_NNNN.N.NN-N_amd64
```

Extract the downloaded archive:

```
tar -xvf dc_sonar_NNNN.N.NN-N_amd64.tar.gz -C dc_sonar_NNNN.N.NN-N_amd64
```

Go to the folder with the extracted files:

```
cd dc_sonar_NNNN.N.NN-N_amd64/
```

Install PostgreSQL:

```
sudo bash install_postgresql.sh
```

Install RabbitMQ:

```
sudo bash install_rabbitmq.sh
```

Install dependencies...