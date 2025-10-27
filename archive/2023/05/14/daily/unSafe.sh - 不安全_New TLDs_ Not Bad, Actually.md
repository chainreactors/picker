---
title: New TLDs: Not Bad, Actually
url: https://buaq.net/go-163222.html
source: unSafe.sh - 不安全
date: 2023-05-14
fetch_date: 2025-10-04T11:37:20.990927
---

# New TLDs: Not Bad, Actually

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

![](https://8aqnet.cdn.bcebos.com/e62247f073abd5ca1933810137bd9119.jpg)

New TLDs: Not Bad, Actually

The Top Level Domain (TLD) is the rightmost label in a fully-qualified domain name:The m
*2023-5-13 22:50:54
Author: [textslashplain.com(查看原文)](/jump-163222.htm)
阅读量:31
收藏*

---

The `Top Level Domain (TLD)` is the rightmost label in a fully-qualified domain name:

[![](https://textplain.files.wordpress.com/2023/05/image-2.png?w=765)](https://textplain.files.wordpress.com/2023/05/image-2.png)

The most common label you’ll see is `com`, but you may be surprised to learn that there are [1479 registered TLDs](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) today. This list can be subdivided into categories:

* **Generic TLDs ([gTLD](https://en.wikipedia.org/wiki/Generic_top-level_domain))** like `.com`
* **Country Code TLDs ([ccTLDs](https://en.wikipedia.org/wiki/Country_code_top-level_domain))** like `.uk`, each of which is controlled by specific countries
* **Sponsored TLDs ([sTLDs](https://en.wikipedia.org/wiki/Sponsored_top-level_domain))** like `.museum` which are designed to represent a particular community
* … and a few of [more esoteric types](https://en.wikipedia.org/wiki/Generic_top-level_domain#Types)

Some TLD owners will rent domain names under the TLD to any buyer (e.g. anyone can register a `.com` site), while others impose restrictions:

* a ccTLD might require that a registrant have citizenship or a business nexus within their country to register a domain in their namespace; e.g. to get a domain with the `.ie` ccTLD, you have to [prove Irish citizenship](https://www.weare.ie/document-requirements/)
* a sTLD may require that the registrant meet some other criteria; e.g. to register within the `[.bank](https://www.register.bank/)` TLD, you must hold an active banking license and meet other criteria

### ZIP and MOV

Recently, there’s been some *excitement* about the relatively-new `.ZIP` and `.MOV` top-level domains.

Why?

Because the characters `.zip` and `.mov` also represent longstanding [file extensions](https://textslashplain.com/2023/04/05/file-types/) used to represent ZIP Archives and video files, respectively.

The argument goes that introducing `.zip` and `.mov` TLDs means that there’s now ambiguity: if a human or code encounters the string `"example.zip"`, is that just a file’s name, or a bare hostname?

Alert readers might immediately note: *“Hey, that’s also true of `.com`, the most popular TLD– [COM files](https://en.wikipedia.org/wiki/COM_file) have existed since the 1970s!*” That’s true, as far as it goes, but it is fair to say that `.com` files are rarely seen by users anymore: on Windows, `.com` has mostly been supplanted by `.exe` except in some exotic situations.

Thanks to the popularity of the TLD, most people hearing *dotcom* are going to think “website” not “application”.

Okay, so what’s the badness that could result?

### Automatic Hyperlinking

In poking the Twitter community, the top threat that folks have identified is concern about **automatic hyperlinkers**: If an author types a filename string into an email, or their blog editor, or Twitter, etc, it might be misinterpreted as a URL and automatically converted into one. Subsequently, readers might see the automatically-generated link, and click it under the belief that the author intended to include it as a URL.

This isn’t a purely new concern– for instance, folks talking about the `ASP.NET` platform encounter this issue all the time, but that’s a fairly constrained scenario, and the `https://asp.net` website is already owned by the developers of ASP.NET, so there’s no harm.

In contrast, what if I sent an email to my family saying, “*hey, check out VacationPhotos.zip*” with a ZIP file of that name attached to my email. My email editor might automatically turn my text, `VacationPhotos.zip`, into a link to `https://VacationPhotos.zip/`.

I concede that this is absolutely possible, however, it does not seem terribly exciting as an attack vector, and I remain unconvinced that normal humans routinely type filename extensions in this sort of communication.

Having said that, I would agree that it *probably* makes sense to exclude `.mov` and `.zip` from automatic hyperlinkers. Many (if not most) such hyperlinkers do not automatically link any string that contains any of the 1479 of the current TLDs, and I don’t think introducing autolinking for these two should be a priority for them either.

(As an aside, if I was talking to an author of an automatic hyperlinker library, my *primary* concern would be the fact that almost all such libraries convert `example.com` into a non-secure reference to `http://example.com` instead of a secure `https://example.com` URL.)

### User Confusion

Another argument goes that URLs are already exceedingly confusing, and by introducing a popular file extension as a TLD, they might become more so.

I do not find this argument compelling.

URLs are already [incredibly subtle](https://www.usenix.org/conference/enigma2019/presentation/stark), and relying on users to mentally parse them correctly is a losing game. There’s no requirement that a URL contain a filename at all. Even before the introduction of the `ZIP` TLD, it was already possible to include the characters “`.zip`” in the Scheme, UserInfo, Hostname, Path, Filename, QueryString, and Fragment components of a URL. The fact that a fully-qualified hostname can now *end* with this string does not seem very interesting.

### General Skepticism

Finally, there’s a general skepticism around the introduction of new TLDs, with pundits proclaiming that they simply represent an unnecessary “money grab” on the part of ICANN (because the fees to get an official TLD are significant).

*“Why do we even need these?”* pundits protest, sometimes making an argument that boils down to “*`.com` ought to be enough for anybody*.”

This does not feel like a compelling argument for a number of reasons:

1. COM was intended for “commercial entities”, and many domain owners are not commercial at all
2. COM is written in English, a language not spoken by many of the world’s population
3. The legacy COM/NET/ORG namespace is very crowded, and name collisions are common. For example, one of my favorite image editors is `Paint.Net`, but that domain name was, until recently, owned by a paint manufacturer. Now it’s “parked” while the owner tries to sell it for likely thousands of dollars.

Other pundits make a slightly more constrained argument: “*Fine, new gTLDs are* generally *okay, but these two* specifically *seem unnecessarily confusing.*” That’s a reasonable conversation to have.

Some pundits argue *“Hey, domains under these new TLDs are often disproportionately malicious”*, pointing at `.xyz` as an example.

That tracks, insofar as the biggest companies *tend* to stick to the most common TLDs. However, the vast majority of malicious registrations under non-`.COM` TLDs don’t happen because getting a domain in a newer TLD is “easier” or subject to fewer checks or anything of that sort. If anything, new TLDs are likely to have *more stringent* registration requirements than a legacy TLD.

### New TLDs Represent New, More Secure Opportunities

One very cool thing about the introduction of a new TLD is that it gives the registrar the ability to introduce new requirements of the registrants without the fear of breaking legacy usage.

In particular, a common case is [HSTS Preloading](https://textslashplain.com/2017/12/05/strict-transport-security-for-dev/): a TLD owner can add the TLD to the browser’s HSTS preload list, such that every link to every URL with...