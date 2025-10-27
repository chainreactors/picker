---
title: How I Found AWS API Keys using “Trufflehog” and Validated them using “enumerate-iam” tool
url: https://buaq.net/go-145655.html
source: unSafe.sh - 不安全
date: 2023-01-16
fetch_date: 2025-10-04T03:58:36.864979
---

# How I Found AWS API Keys using “Trufflehog” and Validated them using “enumerate-iam” tool

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

How I Found AWS API Keys using “Trufflehog” and Validated them using “enumerate-iam” tool

*2023-1-15 23:51:2
Author: [infosecwriteups.com(查看原文)](/jump-145655.htm)
阅读量:24
收藏*

---

Hello Guys..!!

Happy New Year 2023 to all my followers 🥳

Hope you are doing well

Today we will discuss about how I Found AWS API Keys and how to Validate them.

**Note-1:** For Privacy reasons, I am not going to reveal the target domain on which I have found the API keys.

**Note-2:** This Article is only for demonstration and education purpose.

Let’s Start without wasting any more time.

I started Bug hunting somewhere after the summer in 2022 due to my interest in it.

So, As a beginner, I have searched on Google for the “best browser extensions for bug bounty hunters” due to my curiosity and the less knowledge I have on bug hunting.

I found various results as shown below.

**Image Source: Google**

I opened the first article which I got in the above results. I have provided the link for the article below.

Link: <https://www.p1boom.com/2022/02/top25-browser-extensions-for-hacker.html>

It’s one of the best articles I found on Google and they provided all the links for the popular extensions including for both Chrome and Firefox.

So, After going through the article, I have installed all the extensions mentioned there.

In the end of that article, you will find a bonus chrome extension named “Trufflehog”.

Extension Link: <https://chrome.google.com/webstore/detail/trufflehog/bafhdnhjnlcdbjcdcnafhdcphhnfnhjc/>

Initially, I thought this is a normal extension like any other extension.

Note: But when I see back now, I can confidently say that I found various vulnerabilities and other sensitive data like Directory Listing, .git exposure, API keys, Sensitive WordPress directories, Passwords and many others in my bug bounty journey using this Extension.

You don’t need to click on this extension or open any source code to find any sensitive data.

This Extension crawls all the links from the source code of a website we visit to find any sensitive data.

Kudos to the Founder [Dylan](https://twitter.com/InsecureNature) for this Amazing Extension 🙏

You can read the below articles to know more about this extension

Reference:

So, Let’s Jump to the main topic

I opened a random target on my browser where this extension is installed.

I got a Pop-up saying that this website contains AWS API keys as shown below.

Most of the time, it will show the exposed key and the path where it is present.

You can also copy the path and leaked key from the Pop-up box,

So, I went to the path and searched for the leaked key where I found the AWS Access key and Secret key as shown below.

It was a shock for me as most of the time both the keys won’t be present on a website in plain text and I was wondering how to use these keys as I am not aware of the process of how to use those keys.

So, I asked one of my friends who told me about this tool called “enumerate-iam” for testing the leaked API keys to validate them.

I have provided the git link of the tool in the below section

Link: <https://github.com/andresriancho/enumerate-iam>

So I have tested the leaked keys using the above tool where I only found some basic info as shown below.

**enumerate-iam results**

Note: There is no guarantee that the Leaked keys will be Valid and give more info at all times. I was fortunate to get some basic info which is of no use to increase the impact on the target.

But still, you can see that the exposed API keys are validated and gave some basic info about the AWS account as shown in the above picture.

So, That’s it for today guys

Thank you guys for Reading this Post - Happy Hunting 🐞

If you like this post, don’t forget to give me a clap 👏

**Credits:** To all Bug Bounty Hunters and Authors who developed the tools I used in this article.

**Support me:** If you like to support me, buy me a cup of [**Coffee**](https://www.buymeacoffee.com/satyakayala)☕

**Follow me:** [Satya Prakash](https://medium.com/u/8f987881b66a?source=post_page-----cd6ba7c86d09--------------------------------) | [LinkedIn](https://www.linkedin.com/in/0xkayala/) | [Twitter](https://twitter.com/0xKayala)

文章来源: https://infosecwriteups.com/how-i-found-aws-api-keys-using-trufflehog-and-validated-them-using-enumerate-iam-tool-cd6ba7c86d09?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)