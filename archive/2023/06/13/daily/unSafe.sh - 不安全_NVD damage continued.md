---
title: NVD damage continued
url: https://buaq.net/go-168409.html
source: unSafe.sh - 不安全
date: 2023-06-13
fetch_date: 2025-10-04T11:44:28.921941
---

# NVD damage continued

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

![](https://8aqnet.cdn.bcebos.com/d6056309a02ace6b9d01876803f40c0a.jpg)

NVD damage continued

There is something about having your product installed in over twenty billion instances all over
*2023-6-12 20:35:17
Author: [daniel.haxx.se(查看原文)](/jump-168409.htm)
阅读量:26
收藏*

---

There is something about having your product installed in over **twenty billion instances** all over the world and even [out of the globe](https://daniel.haxx.se/blog/2021/04/19/mars-2020-helicopter-contributor/). In my case it helps me remain focused on and committed to working on the security aspects of curl. Ideally, we will never have our [heartbleed](https://en.wikipedia.org/wiki/Heartbleed) moment.

Security is also a generally growing concern in the world around us and Open Source security perhaps especially so. This is one reason why [NVD making things up](https://daniel.haxx.se/blog/2023/03/06/nvd-makes-up-vulnerability-severity-levels/) is such a big problem.

The National Vulnerability Database (NVD) has a global presence. They host and share information about security vulnerabilities. If you search for a CVE Id using your favorite search engine, it is likely that the first result you get is a link to NVD’s page with information about that specific CVE. They take it upon themselves to educate the world about security issues. A job that certainly is needed but also one that puts a responsibility and requirement on them to be accurate. When they get things wrong. they help distributing misinformation. Misinformation makes people potentially draw the wrong conclusions or act in wrong, incomplete or exaggerated ways.

## Low or Medium severity issues

There are well-known, recognized and reputable Open Source projects who by policy never issue CVEs for security vulnerabilities they rank severity low or medium. (I will not identify such projects here because it is not the point of this post.)

Such a policy successfully avoids the risk that NVD will greatly inflate their issues since they can already only be high or critical. But is it helping the users and the ecosystem at large?

In the curl project we have a policy which makes us register a CVE for every single reported or self-detected problem that can have a security impact. Either at will or by mistake. This includes a fair amount of low and medium issues. The amount of low and medium issues as a total of all issues increases over time as we keep finding issues, but the really bad ones are less frequently reported.

As we have all data recorded and stored, we can visualize this development over time. Below is a graph showing the curl vulnerability and severity level trends since 2010.

[![](https://daniel.haxx.se/blog/wp-content/uploads/2023/06/Screenshot-2023-06-09-at-14-55-06-Screenshot.png)](https://daniel.haxx.se/blog/wp-content/uploads/2023/06/Screenshot-2023-06-09-at-14-55-06-Screenshot.png)

Severity distribution in reported curl vulnerabilities since 2010

Out of the 145 published curl security vulnerabilities so far, 28% have been rated severity high or critical while 104 of them were set low or medium by the curl security team.

I think this trend is easy to explain. It is because of two separate developments:

1. We as a project have matured and have learned over time how to test better, write code better to minimize risk and we have existed for a while to have a series of truly bad flaws already found (and fixed). We make less serious bugs these days.
2. Since 2010, lots of more people look for security problems and these days we are much better better at identifying problems as security related and we have better tools, while for a few years ago the same problem would just have become “a bug fix”.

## Deciding severity

When a security problem is reported to curl, the curl security team and the reporter collaborate. First to make sure we understand the full width of the problem and its security impact. What can happen and what is required for that badness to trigger? Further, we assess what the likeliness that this can be done on purpose or by mistake and how common those situations and required configurations might be. We know curl, we know the code but we also often go back and double-check exactly what the documentation says and promises to better assess what users should be expected to know and do, and what is not expected from them etc. And we re-read the involved code again and again.

curl is currently a little over 160,000 lines of feature packed C code (excluding blank lines). It might not always be straight forward to a casual observer exactly how everything is glued together even if we try to also [document internals](https://everything.curl.dev/internals) to help you find deeper knowledge.

I think it is fair to say that it requires a certain amount of experience and time spent with the code to be able to fully understand a curl security issue and what impact it might have. I believe it is difficult or next to impossible for someone without knowledge about how it works to just casually read our security advisories and try to second-guess our assessments and instead make your own.

Yet this is exactly what NVD does. They don’t even ask us for help or for clarifications of anything. They think they can assess the severity of our problems without knowing curl nor fully understanding the reported issues.

## A case to prove my point

In March 2023 we published a security advisory for the problem commonly referred to as [CVE-2023-27536](https://curl.se/docs/CVE-2023-27536.html).

This is *potentially* a security problem, probably never hurts anyone and is in fact quite unlikely to ever cause a problem. But it *might*. So after deliberating we accepted it and ranked it **severity low**.

Bear with me here. I’ll spend two paragraphs revealing some details from the internal libcurl engine:

The problem is of a kind we have had several times in the past: curl has a connection pool and when a user makes a subsequent request which this particular option modified (compared to how it was when the previous connection was setup) it would wrongly reuse the first connection thinking they had the exact same properties.

The second would then accidentally get the wrong rights because it was setup differently. Still, the first connection would need the correct credentials and everything and so would the second one, it would just differ depending on what “GSSAPI delegation” that is allowed.

## NVD ranks this

The person or team at NVD whose job it is to make up stuff for security vulnerabilities ranked this as **CRITICAL 9.8**. Almost as bad as it gets apparently. 10 is the max as you might recall.

When realizing this, at the end of May, I first fell off my chair in shock by this insanity, but after a quick recovery I emailed them (again) and complained (yet again) on setting this severity for \*27536. I used the word “ridiculous” in my email to describe their actions. Why and who benefits from them scaremongering the world like this? It makes no sense. On the contrary, this is bad for everyone.

As a reaction to my complaint, someone at NVD went back and agreed to revise the CVSS string they had set and suddenly it was “only” ranked **HIGH 7.2**. I say “someone” because they never communicate with names and never sign the emails which whomever I talk to. They are just “NVD”.

I objected to their new CVSS string as well. **It is just not a high severity security problem!**

In my new argument I changed two particular details in the CVSS string (compared to the one they insisted was good) and presented arguments for that. For your pleasure, I include my exact word...