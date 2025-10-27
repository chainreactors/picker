---
title: SSRF That Allowed Us to Access Whole Infra Web Services and Many More
url: https://buaq.net/go-151580.html
source: unSafe.sh - 不安全
date: 2023-03-02
fetch_date: 2025-10-04T08:25:24.554845
---

# SSRF That Allowed Us to Access Whole Infra Web Services and Many More

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

SSRF That Allowed Us to Access Whole Infra Web Services and Many More

Hi this is Basavaraj back again with another writeup on SSRF.This Writeup/Report/Bug will collaborat
*2023-3-1 22:15:18
Author: [infosecwriteups.com(查看原文)](/jump-151580.htm)
阅读量:17
收藏*

---

Hi this is [Basavaraj](https://twitter.com/basu_banakar) back again with another writeup on SSRF.

This Writeup/Report/Bug will collaborated with my dost i.e [Lohith Gowda](https://twitter.com/lohigowda_in)

IC : Cobalt

> **What is SSRF?**
>
> SSRF stands for Server-Side Request Forgery, which is a type of security vulnerability that allows an attacker to send unauthorized requests from a vulnerable server to other internal systems, potentially exposing sensitive information or executing malicious actions.

**What can be achieved using SSRF?**

Basically we can **takeover the whole company** in some cases(In this case too.)!

> An SSRF vulnerability occurs when a server makes HTTP or other types of requests to other internal systems or resources on behalf of an attacker, using the vulnerable server’s network privileges. This can lead to unauthorized access to sensitive information, such as private network data, or to other types of exploitation, such as triggering denial-of-service attacks or even executing code on vulnerable systems.

We will try to keep this writeup as beginner friendly, So lets jump in directly into the topic.

This is an private program, And most of us(Indians) have used this application which has 50M user base.

We have an target called **redacted.com** and while browsing whole application as an normal user, We found that the one of the **POST** request is being made to example : **/api/v1/json** with request body parameter **path** and contain some json url as a value.

Initial Request

We removed the whole path value and replaced the value with my burp collaborator URL and here we confirmed the **full read SSRF** with call back on my burp collab listener.

Full read SSRF is present(But want to confirm by exploiting)

We got to know that web server is running on AWS, and I replaced the value with 169.254.169.254(aws metadata url) and I got the 403 response(Which is from cloudflare waf) and we got the confidence that we can bypass this, because the response is not from the server side (It is from waf).

403 from cloudflare

And we explored some of the bypass techniques and many of them worked. and finally chosen one i.e converting the 169.254.169.254 to decimal value and the final URL will be <http://2852039166> and by using this URL we successfully bypassed WAF.

Waf bypass via decimal encoding

Now accessed user data by hitting — /latest/user-data

accessed user-data

Now accessed the IAM credentials by appending metadata paths.

IAM Credentials

Now Imported IAM credentials to AWS-CLI and executed the command i.e **aws ec2 describe-instances (**When you run this command, it sends a request to the AWS EC2 service to retrieve information about the instances specified in the command. This information can include details such as the instance ID, state, public IP address, instance type, and more.**)** and saved the output in **out.txt**

Extracting ec2 instance information

Now we created an bash script that takes the **out.txt** file and extract the IPv4 addresses from it, remove the duplicate IPv4’s and displays the output.

extracting IP’s and remove duplicate IP’s(i.e repeated)

Now we will run the script and count the number of IP’s which we have extracted i.e.

Totally 3774 internal+public facing IPv4's

Now its time to use burp intruder(You can use any) to bruteforce all of these internal IP’s using our vulnerable endpoint and host.

Payload position

Paste the list of IP’s i.e 3774 and start attack

Payloads

Now we got access to **200+ internal web services** by bruteforcing the IP’s

Successfully Accessed 200+ internal hosts

> **We could have takeover the whole company via bruteforcing the internal IP’s with ports and that will be 225**(internal hosts)**\*65535**(ports) **= 14745375(Requests), but we didn’t performed that.**

And here are some sample screenshots, That describes what we got access for

Some status manager

Some employee PII in internal host html response(Includes name, phone, email, auth tokens etc..)

Employee PII

Some internal login panels, Dashboards etc…

internal login panel

Internal dashboard

And that’s from our side, If you have any doubts regarding SSRF, you can ask in comments.

Bounty : Still pending and discussion going on.

If you like our contribution towards Infosec, do follow us on:

Twitter : [Basavaraj](https://twitter.com/basu_banakar) and [Lohith](https://twitter.com/lohigowda_in)

LinkedIn: [Basavaraj](https://www.linkedin.com/in/basubanakar/) and [Lohith](https://www.linkedin.com/in/lohigowda/)

Instagram : [Basavaraj](https://www.instagram.com/basu_banakar/) and [Lohith](https://www.instagram.com/lohigowda.in/)

文章来源: https://infosecwriteups.com/ssrf-that-allowed-us-to-access-whole-infra-web-services-and-many-more-3424f8efa0e4?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)