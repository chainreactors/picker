---
title: California Tax Refund Mobile Phish
url: https://garwarner.blogspot.com/2025/09/california-tax-refund-mobile-phish.html
source: CyberCrime & Doing Time
date: 2025-09-04
fetch_date: 2025-10-02T19:38:53.340921
---

# California Tax Refund Mobile Phish

# [CyberCrime & Doing Time](https://garwarner.blogspot.com/)

A Blog about Cyber Crime and related Justice issues

## Wednesday, September 03, 2025

### [California Tax Refund Mobile Phish](https://garwarner.blogspot.com/2025/09/california-tax-refund-mobile-phish.html)

A new round of mobile phish is imitating the State of California's "Franchise Tax Board" in a round of phishing sites that are gaining prominence in the past few days. I visited ftb.ca-gov-sg[.]top/notice from a burner phone to see how the scheme works (the page doesn't load from the Windows browsers I tested.)

After harvesting all of my private information, the site informs me that I had a $1050 refund available. The phish claims that "Bank Routing" is unavailable due to "system maintenance" and offers the option to send my refund via my Credit Card if I just provide the card number, expiration date, and CVV.

|  |  |  |
| --- | --- | --- |
|  | [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0H1U9bPGL9IadXHNLF9NFkeIF90ANtpsDSRoCRtQ-U8AJqqQBsS8koZpP3ZUGdu0CToCYDPZiUxEgM8MRLvSyw3qmATVTzA-cWIWy2DQDFB4v7kHdkOKZcUL2W2Q4j1Oc4Qwxage95lrXZXsMUM1IHQKWye1Q32dyHFeVDbx5idNq4VSbjnF-v4c4PRjQMA/w150-h400/CA.1.jpg)![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3Rsroc4C01NgBYnD55BZL_KLoTmtPNcH2tOwdlDnYRi_OOw9vfZhCszeloe9m3jXCUTS1Q9-tS2J7bMtjCa5_POarK9hpf7dVUGfYydjSCTv4w8o5rjuAx6RpXlZBN1FNXBKcVGwIjTwKsLGoboRnUgxJsH1HuXEEPS1sgqlv_espJeI3RgajFUbACK0XYA/w138-h400/CA.2.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3Rsroc4C01NgBYnD55BZL_KLoTmtPNcH2tOwdlDnYRi_OOw9vfZhCszeloe9m3jXCUTS1Q9-tS2J7bMtjCa5_POarK9hpf7dVUGfYydjSCTv4w8o5rjuAx6RpXlZBN1FNXBKcVGwIjTwKsLGoboRnUgxJsH1HuXEEPS1sgqlv_espJeI3RgajFUbACK0XYA/s1280/CA.2.jpg) | [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhtrPWh55XZH4JGTPl8n2vZqruMdNpcBZkUIb3Pjtc_8FiBV5QyIcvPhAgLe5jlZQOsu4B8YBjb2Rg9wsB8sRHsO9H-_x2HAyj_TOR430WpZ6E0c410yMSVWc6HZUYfyYMqsMuknE8Vns3lVLgGnGA4mCkitOfMG5tnidzwqnLahPQVKqKFnESmLOOvCnQyQ/w139-h400/CA.3.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhtrPWh55XZH4JGTPl8n2vZqruMdNpcBZkUIb3Pjtc_8FiBV5QyIcvPhAgLe5jlZQOsu4B8YBjb2Rg9wsB8sRHsO9H-_x2HAyj_TOR430WpZ6E0c410yMSVWc6HZUYfyYMqsMuknE8Vns3lVLgGnGA4mCkitOfMG5tnidzwqnLahPQVKqKFnESmLOOvCnQyQ/s1280/CA.3.jpg) |

urlscan.io shows at least 300 domains have been observed, all using a hostname pattern that starts with "ftb.cagov" or "ftb.ca-gov" following by some random characters and using TLDs ".cfd" or ".cc"

Most of the observed domains were registered at Dominet (HK) Limited, and likely all are hosted at TENCENT, though most are having their location protected by the reverse proxy service at CloudFlare. (All of the non-CloudFlare ones are on TenCent).

Some recent example hostnames are:

* ftb.cagov-ac[.]cfd
* ftb.cagov-bd[.]cfd
* ftb.cagov-ch[.]cfd
* ftb.ca-gov-ci[.]cfd
* ftb.cagov-ckt[.]cc
* ftb.cagov-ga[.]cc
* ftb.ca-gov-gd[.]cfd
* ftb.cagov-gi[.]cc
* ftb.cagov-go[.]cc
* ftb.cagov-idr[.]cc
* ftb.cagov-nb[.]cfd
* ftb.cagov-ork[.]cc
* ftb.ca-gov-pf[.]cfd
* ftb.cagov-rld[.]cc
* ftb.cagov-tes[.]cc
* ftb.cagov-tuf[.]cc
* ftb.cagov-tug[.]cc
* ftb.cagov-tum[.]cc
* ftb.cagov-vkd[.]cc
* ftb.cagov-whe[.]cc
* ftb.cagov-wht[.]cc
* ftb.cagov-whu[.]cc
* ftb.cagov-why[.]cc
* ftb.ca-gov-yg[.]cfd
* ftb.cagov-ytk[.]cc

There have been 190 domains observed by URLScan that included the pattern "\*.cagov-xx.cc" with the first round imitating California's DMV from June 23rd to June 25th. The "FTB" pattern began August 19th with ftb.cagov-ge[.]cc/notice and continuing with 143 more reported domains, including 32 domains reported today. The "cagov-XX.cfd" pattern began on August 31st and has been seen using 31 domains. "ca-gov-XX.cfd" also began August 31st and has used 58 domains so far, all hosted at TENCENT.

Searching by IP address using ZETAlytics ZoneCruncher, we find at least 105 domains hosted on four TenCent IP addresses:

41 domains hosted on 170.106.140[.]181
38 domains hosted on 43.153.19[.]10
14 domains hosted on 49.51.188[.]94
12 domains hosted on 43.130.56[.]94

Posted by
Gary Warner

at
[1:50 PM](https://garwarner.blogspot.com/2025/09/california-tax-refund-mobile-phish.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=35783026&postID=125693898198029159&from=pencil "Edit Post")

#### No comments:

#### Post a Comment

Trying a new setting. After turning on comments, I got about 20-30 comments per day that were all link spam. Sorry to require login, but the spam was too much.

[Newer Post](https://garwarner.blogspot.com/2025/09/chinese-guarantee-syndicates-and-fruit.html "Newer Post")

[Older Post](https://garwarner.blogspot.com/2025/08/chinese-sms-spammers-go-mobile.html "Older Post")
[Home](https://garwarner.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://garwarner.blogspot.com/feeds/125693898198029159/comments/default)

## GarWarner

* [Gary Warner](https://www.blogger.com/profile/10822366940133384061)
* [Heather McCalley](https://www.blogger.com/profile/06969346551823881101)
* [MalwareSecrets](https://www.blogger.com/profile/11459838476063107050)

## Subscribe To

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fgarwarner.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fgarwarner.blogspot.com%2Ffeeds%2Fposts%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://garwarner.blogspot.com/feeds/posts/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Posts

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)
![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

[![](https://resources.blogblog.com/img/widgets/subscribe-netvibes.png)](https://www.netvibes.com/subscribe.php?url=https%3A%2F%2Fgarwarner.blogspot.com%2Ffeeds%2F125693898198029159%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/widgets/subscribe-yahoo.png)](https://add.my.yahoo.com/content?url=https%3A%2F%2Fgarwarner.blogspot.com%2Ffeeds%2F125693898198029159%2Fcomments%2Fdefault)
[![](https://resources.blogblog.com/img/icon_feed12.png)
Atom](https://garwarner.blogspot.com/feeds/125693898198029159/comments/default)

![](https://resources.blogblog.com/img/widgets/arrow_dropdown.gif)

![](https://resources.blogblog.com/img/icon_feed12.png)
Comments

## Blog Archive

* ▼
  [2025](https://garwarner.blogspot.com/2025/)
  (12)
  + ▼
    [September](https://garwarner.blogspot.com/2025/09/)
    (8)
    - [New Smish: New York Department of Revenue](https://garwarner.blogspot.com/2025/09/new-smish-new-york-department-of-revenue.html)
    - [SMS Pools and what the US Secret Service Really Fo...](https://garwarner.blogspot.com/2025/09/sms-pools-and-what-us-secret-service.html)
    - [Postal Thief Arrested in Oregon](https://garwarner.blogspot.com/2025/09/postal-thief-arrested-in-oregon.html)
    - [Microsoft DCU's Takedown of RaccoonO365](https://garwarner.blogspot.com/2025/09/microsoft-dcus-takedown-of-raccoono365.html)
    - [Indian Call Center Scammers partner with Chinese M...](https://garwarner.blogspot.com/2025/09/indian-call-center-scammers-partner.html)
    - [Attorney Generals go after Bitcoin ATMs for suppor...](https://garwarner.blogspot.com/2025/09/attorney-generals-go-after-bitcoin-atms.html)
    - [Chinese Guarantee Syndicates and the Fruit Machine](https://garwarner.blogspot.com/2025/09/chinese-guarantee-syndicates-and-fruit.html)
    - [California Tax Refund Mobile Phish](https://garwarner.blogspot.com/2025/09/california-tax-refund-mobile-phish.html)
  + ►
    [August](https://garwarner.b...