---
title: IPinside: Korea’s mandatory spyware
url: https://palant.info/2023/01/25/ipinside-koreas-mandatory-spyware/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-01
fetch_date: 2025-10-04T08:21:59.691114
---

# IPinside: Korea’s mandatory spyware

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# IPinside: Koreaâs mandatory spyware

2023-01-25
 [Korea](/categories/korea/)/[Privacy](/categories/privacy/)/[Security](/categories/security/)
 14 mins
 [10 comments](/2023/01/25/ipinside-koreas-mandatory-spyware/#comments)

*Note*: This article is also available [in Korean](https://github.com/alanleedev/KoreaSecurityApps/blob/main/02_ipinside_lws_agent.md).

On our [tour of South Koreaâs so-called security applications](/2023/01/02/south-koreas-online-security-dead-end/) weâve already [took a look at TouchEn nxKey](/2023/01/09/touchen-nxkey-the-keylogging-anti-keylogger-solution/), an application meant to combat keyloggers by â¦ *checks notes* â¦ making keylogging easier. Today I want to shed some light on another application that many people in South Korea had to install on their computers: IPinside LWS Agent by Interezen.

The stated goal of the application is retrieving your ârealâ IP address to prevent online fraud. I found however that it collects way more data. And while it exposes this trove of data to any website asking politely, it doesnât look like it is all too helpful for combating actual fraud.

#### Contents

* [How does it work?](#how-does-it-work)
* [What data is it?](#what-data-is-it)
  + [wdata](#wdata)
    - [Information about running processes](#information-about-running-processes)
  + [ndata](#ndata)
  + [udata](#udata)
* [How is this data protected?](#how-is-this-data-protected)
* [And the overall security of the application?](#and-the-overall-security-of-the-application)
* [When will it be fixed?](#when-will-it-be-fixed)
* [Does IPinside actually make banking safer?](#does-ipinside-actually-make-banking-safer)

## How does it work?

Similarly to TouchEn nxKey, the IPinside LWS Agent application also communicates with websites via a local web server. When a banking website in South Korea wants to learn more about you, it will make a [JSONP request](https://en.wikipedia.org/wiki/JSONP) to `localhost:21300`. If this request fails, the banking website will deny entry and ask that you install IPinside LWS Agent first. So in South Korea running this application isnât optional.

On the other hand, if the application is present the website will receive various pieces of data in the `wdata`, `ndata` and `udata` fields. Quite a bit of data actually:

![Screenshot of a browser window with the address 127.0.0.1:21300/?t=A&value= open. The response is a jQuery callback with some data including wdata, ndata and udata fields and base64-encoded values.](/2023/01/25/ipinside-koreas-mandatory-spyware/request.png)

This data is supposed to contain your IP address. But even from the size of it, itâs obvious that it cannot be only that. In fact, there is a whole lot more data being transmitted.

## What data is it?

### wdata

Letâs start with `wdata` which is the most interesting data structure here. When decrypted, you get a considerable amount of binary data:

![A hex dump with some binary data but also obvious strings like QEMU Harddisk or Gigabit Network Connection](/2023/01/25/ipinside-koreas-mandatory-spyware/wdata.png)

As you can see from the output, I am running IPinside in a virtual machine. It even says `VirtualBox` at the end of the output, even though this particular machine is no longer running on VirtualBox.

Another obvious thing are the two hard drives of my virtual machine, one with the serial number `QM00001` and another with the serial number `abcdef`. That `F0129A45` is the serial number of the primary hard drive volume. You can also see my two network cards, both listed as `Intel(R) 82574L Gigabit Network Connection`. There is my keyboard model (Standard PS/2 Keyboard) and keyboard layout (de-de).

And if you look closely, youâll even notice the byte sequences `c0 a8 7a 01` (standing for my gatewayâs IP address 192.168.122.1), `c0 a8 7a 8c` (192.168.122.140, the local IP address of the first network card) and `c0 a8 7a 0a` (192.168.122.10, the local IP address of the second network card).

But there is way more. For example, that `65` (letter `e`) right before the hard drive information is the result of calling [GetProductInfo() function](https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo) and indicates that Iâm running Windows 10 Home. And `74` (letter `t`) before it encodes my exact Windows version.

#### Information about running processes

One piece of the data is particularly interesting. Donât you wonder where the `firefox.exe` comes from here? It indicates that the Mozilla Firefox process is running in the background. This information is transmitted despite the active application being Google Chrome.

See, websites give IPinside agent a number of parameters that determine the output produced. One such parameter is called `winRemote`. Itâs mildly obfuscated, but after removing the obfuscation you get:

> TeamViewer\_Desktop.exe|rcsemgru.exe|rcengmgru.exe|teamviewer\_Desktop.exe

So banking websites are interested in whether you are running remote access tools. If a process is detected that matches one of these strings, the match is added to the `wdata` response.

And of course this functionality isnât limited to searching for remote access tools. I replaced the `winRemote` parameter by `AGULAAAAAAtmaXJlZm94LmV4ZQA=` and got the information back whether Firefox is currently running. So this can be abused to look for any applications of interest.

And even that isnât the end of it. IPinside agent will match substrings as well! So it can tell you whether a process with `fire` in its name is currently running.

That is enough for a website to start searching your process list without knowing what these processes could be. I created a page that would start with the `.exe` suffix and do a depth-first search. The issue here was mostly IPinside response being so slow, each request taking half a second. I slightly optimized the performance by testing multiple guesses with one request and got a proof of concept page that would turn up a process name every 40-50 seconds:

![Screenshot of a page saying: âPlease wait, fetching your process listâ¦ Testing suffix oerver-svg.exe cortana.exe.â It also lists already found processes: i3gproc.exe asdsvc.exe wpmsvc.exe i3gmainsvc.exe](/2023/01/25/ipinside-koreas-mandatory-spyware/processes.png)

With sufficient time, this page could potentially enumerate every process running on the system.

### ndata

The `ndata` part of the response is much simpler. It looks like this:

> ï¿½ï¿½HDATAIP=âââ.âââ.âââ.âââï¿½ï¿½VD1NATIP=âââ.âââ.âââ.âââï¿½ï¿½VD1CLTIP=192.168.122.140ï¿½ï¿½VD2NATIP=ï¿½ï¿½VD2CLTIP=192.168.122.10ï¿½ï¿½VPN=2ï¿½ï¿½ETHTYPE=ETH1

No, I didnât mess up decoding the data. Yes, `ï¿½` is really in the response. The idea here was actually to use `â½` (reverse tilde symbol) as a separator. But since my operating system isnât Korean, the character encoding for non-Unicode applications (like IPinside LWS Agent) isnât set to EUC-KR. The application doesnât expect this and botches the conversion to UTF-8.

`âââ.âââ.âââ.âââ` on the other hand was me censoring my public IP address. The application gets it by two different means. `VD1NATIP` appears to come from my home router.

`HDATAIP` on the other hand comes from a web server. Which web server? Thatâs determined by the `host_info` parameter that the website provides to the application. It is also obfuscated, the actual value is:

> www.securetrueip.co.kr:80:/vbank\_01.jsc:\_INSIDE\_AX\_H=

Only the first two parts appear to be used, the application makes a request to `http://www.securetrueip.co.kr:80/androidagent.jsc`. One of the response headers is `RESPONSE_IP`. You guessed it: thatâs your IP address as this web server sees it.

The application use...