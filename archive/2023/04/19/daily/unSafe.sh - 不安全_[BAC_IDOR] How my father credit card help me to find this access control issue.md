---
title: [BAC/IDOR] How my father credit card help me to find this access control issue
url: https://buaq.net/go-159305.html
source: unSafe.sh - 不安全
date: 2023-04-19
fetch_date: 2025-10-04T11:32:49.814747
---

# [BAC/IDOR] How my father credit card help me to find this access control issue

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

[BAC/IDOR] How my father credit card help me to find this access control issue

بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِBismillahi-r-Rahmani-r-Rahim(In the name of Allah, The Most G
*2023-4-18 23:34:16
Author: [infosecwriteups.com(查看原文)](/jump-159305.htm)
阅读量:23
收藏*

---

**بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ**

*Bismillahi*-r-Rahmani-r-*Rahim*(In the name of Allah, The Most Gracious and The Most Merciful)

I**ntroduction**

**Assalamu Alaikum**
(Peace Be Upon You)

Hi Everyone,
This is [xcoder](https://twitter.com/xcoder074)(Joy ahmed) from Bangladesh. Recently I have completed my undergradute. And this one is my first write-up about bug bounty hunting. Lately, in 2021 mid I started my bug bounty journey. So Let’s get into the bug what I have found, on the other day I will talk about my bug bounty hunting journey.

> The bug I have found on hackerone platform which is broken access control/IDOR.
> **So what is broken access control?**
> For me broken access control is like a user who doesn’t have permission to do something but he can do it without those specific permission this is called broken access control.
>
> **Like a group owner and a basic user:** group owner can invite other members but group basic user cannot invite other user.
> But if the basic user can invite other user without being an owner then it will be a access control issue.

H**ow I found this?**

I have got an invite in a private program on hackerone which name
I cannot disclose so let’s call it **example.com** and I started my testing with the main website, though the main website don’t have much more functionality. And I have created two accounts and start browsing the website as a normal user to understand the website workflow. I have tried idor,xss and other bussiness logic issue in some endpoint and nothing found.Because the website is properly secured.

And then I saw there is bank account/credit card adding options for payment and I thought that there may be some broken access control or idor issue.One problem is I don’t have any credit card, But my father does, Then I try to add my father credit card into there and it is successfully added onto there then I saw that the card id was sequential number and I am looking into the delete endpoint for IDOR/BAC issue or any discloser of card information but nothing found.

Then again I try to adding the same card and it is added successfully one more time into there and there is now two card added. Then I saw there is an options which is swap. We can swap the default payment options like if we add two payment method then we can swap the default payment options between them.One more important thing,the website is only validating the token for any type of actions so if we remove the cookies then it is okay with it.Then I use my 2nd user account **x-api-token** two swap between the card from 1st user account and it successfully swap the card. Then I was like:

So this is the bug here that means we can swap other user default payment options if they added two payment method.

Reproduction steps:

1. Create two user account in **example.com**
2. Navigate as user1 in **example.com** and add two payment methods.

3. Login as user2 in **example.com** and copy the **x-api-token** of user2 account and saved it to a notepad for future use.

4. Here is the http request for swap the default payments:

```
PUT /api/v1/users/205246/default_payment_method/52684 HTTP/2
Host: www.example.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/account/user/payments
X-Api-Token: df4487b393ed107f2efdd743aab1d8c0
Content-Type: application/json
Origin: https://www.example.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Content-Length: 0
Te: trailers
```

4. Now use burpsuite intruder in this request add user2 account **x-api-token** to bruteforce the card id=52684 & userid=205246 as there is no rate limit on this endpoint.Then it will successfully swap the default payment options of other user who added two payment options in there account.

**Reported**: June 23, 2022

**Triaged & Rewarded**: Jul 5th, 2022

They set the severity is low becasue the impact is so minimal here and with retesting they rewarded me total=**350$** for this access control issue.

Thanks everyone to read this writeup. This one is my first writeup so please share your valuable feedbacks, This will help me to rectify the errors on the next writeup.

Follow me for more write-ups and information sharing, I will be happy to share my knowledge and my DMs are always open for the genuine help seekers.

**Twitter:** <https://twitter.com/xcoder074>

**Linkedin:** <https://www.linkedin.com/in/joy-ahmed-b07986145/>

文章来源: https://infosecwriteups.com/bac-idor-how-my-father-credit-card-help-me-to-find-this-access-control-issue-7ff7c1ae463e?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)