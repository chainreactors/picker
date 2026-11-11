---
title: 30 years of Internet transfers with curl
url: https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/
source: daniel.haxx.se
date: 2026-11-10
fetch_date: 2026-11-11T08:34:07.768124
---

# 30 years of Internet transfers with curl

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2026/10/curl-tshirt-back-lightblue.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# 30 years of Internet transfers with curl

[November 11, 2026](https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [Leave a comment](https://daniel.haxx.se/blog/2026/11/11/30-years-of-internet-transfers-with-curl/#respond)

Thirty years ago, on November 11, 1996 the young Brazilian student Rafael Sagula posted the source code for his tiny HTTP download tool online. That was *httpget* 0.1: a little over 100 lines of C code. Bare bones source code with almost no error checks and limited functionality.

## **httpget**

When I found the source code of that initial httpget release just days after Rafael put it online, I had no idea how HTTP worked. The *language* to speak over the network to ask for resources. Okay, I already knew we call it *protocol* but not a lot more. I also had never heard of neither httpget nor Rafael before. I imagine that I found httpget by searching on Altavista since this was before Google, but I can’t recall the details.

Seeing the simplicity of this code it was not difficult to immediately spot the fundamental basics of the protocol. I presume maybe in the same vain how countless others in decades to follow also have thought of it when seeing the details for the first time. Much later I would come to understand that to be *an illusion* of simplicity, but in those early days I was more amazed and fascinated. I already enjoyed doing network programming and HTTP reasoned with me at once.

httpget 0.1 was almost completely without error checks and it used plain IPv4 addresses; no hostnames or URLs.

I, still a naive and enthusiastic developer with an Open Source mindset (even though that term would not be established until 15-16 months later), addressed some immediate bugs I ran into and added name resolving to the tool. I made diffs and emailed patches over to Rafael; the standard way we exchanged code changes back then. I knew about [RCS](https://en.wikipedia.org/wiki/Revision_Control_System) and [CVS](https://en.wikipedia.org/wiki/Concurrent_Versions_System) for version control, but the use of these tools was spotty. It would actually take until September 1999 until I adopted CVS fully for the curl project. We later switched to using git in 2010.

## **Internet in 1996**

The average internet connection speed of a normal household in Sweden, where I lived and I still live, in 1996 was 30 kbps. 30 kilobit per second. This was before v90 came and bumped the modems up to 56 kilobits. Ordinary mortals connected to the internet using modems over their single phone lines. Today, the average Swedish connection speed is 200 megabits/second.

Thirty years ago there were just 36 million global Internet users and 250,000 websites. Compared to the 6 or 7 billion users and 1 billion websites of today.

We used simpler protocols and while encrypted protocols like SSL existed, they were not used a lot and only for a few rare sites.

**Computers in 1996**

In November 1996, my main home computer was still an Amiga 3000 powered by a 25Mhz 68030 CPU but in early 1997 I upgraded to a faster and more modern machine: an Intel Pentium 120Mhz. I ran Windows 95 on this thing, and its prime use was to run an X server so that I could connect to my work computers and pop up X11 terminals at home. I built the first versions of httpget remotely on SunOS, Solaris and Dell Unix – because they happened to be what we had running at work.

I installed and tested Linux for the first time at work in 1997. I got our first public web servers up and of course I made sure curl worked fine on it. I did not switch to Linux on my home machine until 2000 when I also updated to an Intel Pentium III 733 Mhz box.

## **What I needed to download**

In 1996 I was working as a software developer doing embedded systems and Unix development in C, for a small Swedish company called Frontec Railway Systems. While working there, I came to learn about and enjoy [IRC](https://en.wikipedia.org/wiki/IRC), and in my spare time a few friends and I developed an [IRC bot](https://en.wikipedia.org/wiki/IRC_bot) we called [Dancer](https://github.com/bagder/dancer-416). Spare time developing a TCP client written in C.

As the IRC bot slowly grew more capable, I wanted to use its extension capability and provide a currency translation service for the participants in the *channel* (the IRC term for a chat room*)*. In an international channel like ours, we frequently discussed the price of things and having the bot able to quickly explain how much a hundred German Marks equaled in US Dollars could be a useful service.

My currency service needed to update currency rates maybe once per day so that it could use decently accurate rates. I found an HTTP page listing a bunch of currency rates and the *httpget* tool for doing the downloads, and then the bot could offer up-to-date currency rate translations. All was good.

## **Development**

I discovered computers and programming as a teenager on a Commodore 64. I got hooked immediately. I first learned Basic and moved on to 6510 assembler pretty quickly. In the late 1980s me and my friends had demo groups where we would write cool demos (and some game attempts) in assembler (under the group name *Horizon*). I established my habit of spending spare time on programming back then.

In the early 1990s I moved over to Amiga, started writing a text editor, got my first job at IBM where I truly got into a lot of C and Unix for the first time. Together with some friends we ran a BBS (*The Holy Grail*), for which we eventually would write our own BBS software; me and my brother Björn. I learned Motorola 68000 assembler on the Amiga. I wrote 8086 assembler on PC.

I never attended university. I got my first computer job at IBM when I was twenty. I then thought I would take the uni route later, but I never did. I remain uneducated.

In the early 1990s I discovered both the Internet and the world of freely available source code and I was hooked.

## **Maintainer**

Rafael was not terribly keen on dealing with my patches for httpget. I believe he mostly just put his code out without any particular desire to do anything more with it. Instead I became the httpget maintainer and kept polishing it. My main project was Dancer, the IRC bot. httpget was just a side-project to make sure the currency service kept working fine.

## **Gopher and rename**

At some point I fell over a gopher site that provided many more currency rates than the HTTP page I was scraping at the time so of course I had to add support for that as well to the download tool. With gopher support added, it was not just http anymore and the name of the tool was no longer accurate. It became *urlget*. A third listing was found that provided rates over FTP and, yes, I added support for that protocol as well.

## **Community**

Already from the start I made the source code available under a free license, continuing what Rafel kicked off. He hosted the first releases, but during 1997 I took over and hosted the tarballs on the website I set up and administrated for work. I told my friends and the news about the tool slowly spread. I started getting bug reports from users and occasionally someone sent me patches to fix problems or add features.

This was a time of many Unix flavors and as I wanted widest possible use and adoption, I knew that I needed help and assistance from f...