---
title: RCE Writeups
url: https://buaq.net/go-152047.html
source: unSafe.sh - 不安全
date: 2023-03-06
fetch_date: 2025-10-04T08:44:53.816485
---

# RCE Writeups

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

RCE Writeups

Hello my friends, in this write-up, I will explain how I found four P1 and two P2 bugs and showed mu
*2023-3-5 15:31:36
Author: [infosecwriteups.com(查看原文)](/jump-152047.htm)
阅读量:46
收藏*

---

Hello my friends, in this write-up, I will explain how I found four P1 and two P2 bugs and showed multiple attack scenarios.

Usually, the first thing I do to get started on wide-scope programs is to find the ASNs and CIDRs of the company, through which I can reach the IPs belonging to the company. Having the company’s IPs can be very helpful in the next stages of the hunt. For example, when we reach a website that uses a CDN, we can use these IPs to find the origin IP of the website or get the PTR records of each IP. If it is active, we can access the domains served on the IP (something like a reversed A record). Or we can do a port scan and work on the IP, but we have to verify that the service on the IP belongs to the company itself. At this stage, if we contact the security team, they can help us.

Well, in the first step, I searched for the name of the company on <https://bgpview.io> and the company’s ASNs were listed for me. The next step was to find the live IPs in the ASNs, which can be done manually with this command:

```
whois -h whois.radb.net -- '-i origin AS123' | grep -Eo "([0-9.]+){4}/[0-9]+" | uniq | mapcidr -silent | httpx
```

In the first step of this command, it obtains the information of the ASN’s owner and extracts the CIDRs from the `whois` command output using the `grep` command. It then removes any duplicates and passes the result to [mapcidr](https://github.com/projectdiscovery/mapcidr) for mapping and IP conversion. The final step in the pipeline is to perform service discovery using `httpx`. You can also specify ports for `httpx`.

The easiest way to do this flow is to use Shodan with this search query:

```
asn:AS123
```

It follows almost the same flow for us, but the CLI method is much more complete because it’s possible that a service has gone live for a new IP and Shodan hasn’t yet found it (hasn’t yet sent a request to it).

NOTE: *Shodan ASN search is not available for Free accounts and you must have a membership account.*

Well, I got help from Shodan here, and it found about 200 IPs for me, and among them, I chose a page that was similar to the admin panel for hunting.

Well, the target I chose was an admin login page, which, after checking Wappalyzer, I noticed was written in PHP.

The first thing that came to my mind was to test SQLi on the login page but didn’t work.

In the next step, since our target had a document root, I started to fuzz for directories and files using [FFUF](https://github.com/ffuf/ffuf).

After a few minutes, I got a `401` response code on this route:

```
http://target.com/Config/
```

I requested this page in the browser and tested `admin:admin` on the login page, and boom, it worked! 💥

When protecting such an important place with such a user and password, I concluded that this system must work properly and that the whole table will probably be found.

After checking the target again, I found several other folders like `js`, `css`, `images`, and `data`. However, there was nothing interesting in them until I saw a `rar` file in the `images` folder that caught my attention.

I found a `.doc` file inside. It was a recipe in Chinese so that the admin can use it to change the logo and photos of the site.

Do you see that changelogo.php file? The first thing I did was sending a request to it in the browser and the whole response came, but didn’t saw anything in the response. I checked that again in the render tab (in my Burp proxy) to see the page and saw that the page was not loaded.

When I tested it in the browser, I saw that I was redirected to index.php. But when I checked the request in burp I noticed this code in response:

When I tested it in the browser, I saw that I was redirected to index.php. But when I checked the request in burp I noticed this code in response:

As you can see, we have a file upload here. In the next step, I uploaded a `gif` file (to see how the server behaves), which was allowed for uploading. Finally, I noticed that it was in the `images` folder without requiring access at all.

I tried to upload a shell but didn’t work :( I couldn’t upload any other files except `.png`, `.gif` and I messed up here. In the last part of my test, I tried some payloads for testing RCE, SQL, SSTI, … in the *filename:*

```
filename="PAYLOADS.ext"
```

As the application was written in PHP, SQL Injection usually works there. I started with SQL injection payloads, but it didn’t work. After that, I tested some RCE payloads and boom! it worked 🙂

```
filename="test||sleep 30 ||.gif"
```

In the last step, I searched for the title of this panel among all the IPs that I found during the Recon stage. In the same IP range, I found another panel with the exact same specifications, and it also had the same vulnerability :)

I report all of them immediately and after a few hours, my reports got triaged.

Thanks for reading.

Twitter: [@omidxrz](https://twitter.com/omidxrz)

文章来源: https://infosecwriteups.com/command-injection-by-changing-the-logo-2d730887ab6c?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)