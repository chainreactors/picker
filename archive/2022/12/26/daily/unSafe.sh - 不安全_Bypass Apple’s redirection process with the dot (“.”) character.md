---
title: Bypass Apple’s redirection process with the dot (“.”) character
url: https://buaq.net/go-141295.html
source: unSafe.sh - 不安全
date: 2022-12-26
fetch_date: 2025-10-04T02:30:49.154689
---

# Bypass Apple’s redirection process with the dot (“.”) character

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

Bypass Apple’s redirection process with the dot (“.”) character

Hi guys, I have been gone for a while but now I’m back and here is a new write-up post. Today, I’m g
*2022-12-25 01:12:50
Author: [infosecwriteups.com(查看原文)](/jump-141295.htm)
阅读量:40
收藏*

---

Hi guys, I have been gone for a while but now I’m back and here is a new write-up post. Today, I’m gonna show you the Open Redirection vulnerability I found at Apple’s subdomain using the dot character.

I don’t have a permission to publish this subdomain so I won’t publish it but you can think it as a forum area where users are active. So I’ll call it as “redacted” and let’s get started!

First of all, when we visit to the redacted.apple.com subdomain, there is a login screen here and logging in is quite simple.

As you can see in the picture, the *?path=* parameter is set to redirect to another page in the same subdomain in the section for choosing a nickname for users who log in for the first time.

This process will probably be redirected to “/welcome?login=true” for first time users after all prerequisites have been completed correctly.

As I guessed, the redirect was redirecting to the specified page after choosing the username and uploading the avatar. Of course I tried some payloads here primarily like https://evil.com & //evil.com etc.

Actually, what was interesting to me here was that after using the //evil.com payload, the response was /evil.com with a single ‘/’ character.

In this case, I thought the only ‘/’ appended to the end was due to my payload, and I thought of just typing evil.com

The behavior I actually expected was to be redirected to a non-existent redacted.apple.comevil.com domain, but instead I returned to “/welcome?login=true”. For most parameters it would be okay to simply navigate to evil.com in the subdomain. (?path=evil.com > x.apple.com/evil.com)

Finally an idea came to my mind and I hadn’t seen it anywhere before. I was thinking purely theoretically and was surprised to see that it was possible at Apple.

If we set the payload to .evil.com (ie ?path=.evil.com), “.” character will be appended to the end of redacted.apple.com and this making it a subdomain of evil.com.

And here is the result we expect. Adding a dot character in front of the payload means that the “/” character is missing in some cases. This makes redacted.apple.com a subdomain of evil.com

<https://support.apple.com/en-us/HT201536>

This vulnerability was fixed by team and I was added the Apple Hall of Fame.

That’s all for now. Thanks for reading this far and I hope you liked it!

You can follow me on twitter: <https://twitter.com/canmustdie>

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/bypass-apples-redirection-process-with-the-dot-character-c47d40537202?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)