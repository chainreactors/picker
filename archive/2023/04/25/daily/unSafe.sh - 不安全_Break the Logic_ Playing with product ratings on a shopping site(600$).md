---
title: Break the Logic: Playing with product ratings on a shopping site(600$)
url: https://buaq.net/go-160302.html
source: unSafe.sh - 不安全
date: 2023-04-25
fetch_date: 2025-10-04T11:31:33.262917
---

# Break the Logic: Playing with product ratings on a shopping site(600$)

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

Break the Logic: Playing with product ratings on a shopping site(600$)

Hey! I always talk about my latest findings, this time i wanted to talk about an interesting past fi
*2023-4-24 22:10:44
Author: [infosecwriteups.com(查看原文)](/jump-160302.htm)
阅读量:19
收藏*

---

## Hey! I always talk about my latest findings, this time i wanted to talk about an interesting past finding of mine.

As it’s a private program, i’ll refer to it as “redacted”. Let me give you some information about the program before we start.

The main application was a specified beverage shopping site. So as always i took my time to learn all the features and the working of the site. There were memberships, packages and profiles for every user.

midjourney ai bot / discord

As a bug bounty hunter the most important thing you could do is to not give up on a program. Most people switch programs often because they feel like they wont find any vulnerability there. But that’s not true, you have to take your time while learning the working of the site.

So i took my time and learned all the features on the website, then i started to test specific pages and features.

While wandering around the product page, i noticed that i could rate a beverage without actually buying it. Here is the request of it:

```
POST /customer/product/product-rating.json HTTP/2
```

There were two types of rating, one of them was just a question of: “Would you buy this again?” if you chose yes it would return `"yesOrNo:5`if not then it would return `"YesOrNo:1"`. So i thought can i manipulate the ratings by trying race condition and giving a value of 1 to YesOrNo question. But that didn’t work.

As for the other rating; it was a simple star rating, you would choose how many hearts you wanted to give out of 5 and it would return it in the sliderRating.

I tried a few things, one of them was changing the sliderRating to 150. And to my surprise, it worked. It was showing “150" both on front end and in the api. Here’s the response

```
HTTP/2 200 OK
Date: Sat, 25 Jun 2022 19:54:16 GMT
Content-Type: application/json;charset=UTF-8
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Content-Security-Policy:
Expires: 0
Pragma: no-cache
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
Expect-Ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"

{"rating":{"id":113062722,"rating":150.0,"sliderRating":600.0,........}
```

As you can see, i was able to manipulate both the star rating and the yes or no question. I created a report and waited for their response. I was expecting it to be closen as informative because this could be not affecting the reputation of the ratings. But their response was positive, it was affecting the ratings and they accepted it as a business logic error. Whilst this was not a security issue, they accepted it so i gave my respect to them 😅.

If you want to contact me and ask questions, heres my socials:

[Twitter](https://twitter.com/firaterror)

[LinkedIn](https://www.linkedin.com/in/error666/)

文章来源: https://infosecwriteups.com/break-the-logic-playing-with-product-ratings-on-a-shopping-site-600-c9a87fb66a73?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)