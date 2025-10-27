---
title: Smishing: The new year is here — and so are new scams
url: https://buaq.net/go-144319.html
source: unSafe.sh - 不安全
date: 2023-01-06
fetch_date: 2025-10-04T03:08:25.478072
---

# Smishing: The new year is here — and so are new scams

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

![](https://8aqnet.cdn.bcebos.com/ef4b7fc4a7c86a89d81377d6b3ea229f.jpg)

Smishing: The new year is here — and so are new scams

The day after we found out about this scam, Spain’s national police force arrested 17 people that ha
*2023-1-5 21:20:27
Author: [blog.avast.com(查看原文)](/jump-144319.htm)
阅读量:23
收藏*

---

The day after we found out about this scam, Spain’s national police force arrested 17 people that had been running a smishing fraud scheme and had stolen 145,000 euros from 170 victims.

[Smishing](https://blog.avast.com/irs-smishing-attacks?_ga=2.32000702.1825018133.1672924380-307544329.1672924380) has become an increasingly popular attack method among cybercriminals – and they’re getting better at using it.

Today, it’s not just customers of big financial institutions that are being targeted, and messages with spelling mistakes or in the [wrong language](https://blog.avast.com/tech-support-scammer-language-avast?_ga=2.32000702.1825018133.1672924380-307544329.1672924380) that allowed users to notice something was off are getting harder to spot. Nowadays, we’re seeing nearly-perfect language and fake websites used by scammers that are almost impossible to say whether we are looking at a fake message or a real one at first glance.

An example of one of our team’s latest catches is a small regional bank in Spain called [Laboral Kutxa](https://www.laboralkutxa.com/). The day after we found out about this case, Spain’s national police force arrested 17 people that had been running a smishing fraud scheme and had stolen 145,000 euros from 170 victims. There’s a [press release](https://www.policia.es/_es/comunicacion_prensa_detalle.php?ID=15161) (in Spanish) available with further details about the case.

## **A step-by-step look at the smishing scam**

In this smishing scam, an initial message to the bank’s customers arrives via SMS using perfect Spanish:

![](https://lh3.googleusercontent.com/a8EqC0G1FB3ytHBLxB1N3A7TLIswasPUx2KzG-Bx94B984tkozwBDnRWiQxikyZbcQvAUnOrkLkxxo_YTw_exPnBWzwNOU_8g0St9mSruVPECSsDT-TwA52o9oz_a8icOrmZN1iIyKIJhOS3Fk44n9_p3Z2ORp3jNlqrWP_YznZLBQfZZ4Pfjbnff7DFAQ)

It translates to “Purchase accepted for the amount of 500 euros. If it wasn’t you, follow the steps in this link to cancel it”.

The link starts with ‘http**s**’, which may lead users to believe that it is real. Years ago, one of the things that many people examined when doing online transactions was whether or not they had a secure connection – at that time, it was widely believed that the ‘s’ in ‘https’ means ‘secure’. Now, the majority of web connections are “secure” in the sense that the traffic from our browsers is [encrypted](https://www.avast.com/c-encryption?_ga=2.32000702.1825018133.1672924380-307544329.1672924380), but this doesn’t mean that we’re safe.

When clicking on the link shown in the SMS above, the victim is taken to the bank’s login page, which mimics (almost perfectly) the real one.

Below, the top screenshot is a look at the phishing website, while the one on the bottom is the bank’s genuine website.

![](https://lh4.googleusercontent.com/vN9J-JOIcpfBUsW9pYX9DeW4cC2Yja6Z1Pg2dH5kEWh1G7rdhAHbZ-xm4u9xiAzaYPJaSqBkm-X_Q4OaRQQMHPAAfx2ZG4jbmfFDJaRcj8iwdJ5JD70eTZrWn9VBJwu8uRWAPPrj6L3cWAQIpGN4lL608kPvmFlg3ovlsGG27bJm30YHTs6eAMNDiAJN8A)                                    ![](https://lh3.googleusercontent.com/Q-Sbp0T5O5txnjHhzrCritLFptPHcuP4ZlAtk87AvnpUE40f-FAScvNZhlrmcqPKeW2b_M9rgQcxWPu2gQjPQCfNculb_mhqvoiU9bj5MGuT5o6_Qc9WCrOwfzR8EgNetg3ZF-PAPcvCMTBu-wguWDRl5ITf8QJ2wMHt02UBboqVCtYxDuf2jYcVarOEYw)

As I mentioned before, cybercriminals are getting better at these kinds of malicious techniques, and it’s clear to see their skills when comparing these two screenshots. Given its level of sophistication, most customers won’t realize that they’re on a phishing site.

The unlucky folks who fall for the scam will be asked for their mobile phone number:

![](https://lh5.googleusercontent.com/FL9tlbj81aAD4-tlU6-thVPLKodE_1fc5qd9RewBUtiJwyVV1NgQHvpkXDzEb0_swNHy_n1wmCAGkXdgGYSTt8nv45kkI65qVsBcXnTh9nOZ5fuCW0TjUdXlFOsrwU-xHH5dKIU8DY0V_Y8FX1VQeEOsZOhAeblVtmXNAbaoF3srfMo3gV35Q4hNMZvghw)

Afterwards, they’re asked to input an SMS code that they’ll receive:

![](https://lh4.googleusercontent.com/RgrOHH9ZXovU7vYVvyw0Mo7Ibel9Emy8UstnTfomXTKTa8ZufkMnlTl7f41Pl6qGSKgHqhHq8nu-wbbqiP0DCFvap6imLtHZQjiz_YDiISCc2Ail5UeZV7qJNbn2RBbltyw9tGQx0nq6G1LhVIlHKefIQ2NKP2PMbmkqoy3Sqa-BWpTvjeek77DFOL8H4A)

Of course, anyone who gets to this point in the smishing scam can be certain that their account is compromised.

With the arrival of easy-to-use AI tools, the sophistication of these types of smishing attacks will only get better. For that reason, it’s crucial that we take the steps necessary to prepare ourselves and know what to look for.

Here are a couple rules of thumb to keep in mind:

1. Never ever click on a link you receive via SMS. It doesn’t matter how urgent the topic is  – in fact, more urgent messages are more likely to be scams.
2. Install [reliable antivirus software](https://www.avast.com/index?_ga=2.32000702.1825018133.1672924380-307544329.1672924380) on your devices that can detect and block [phishing](https://www.avast.com/c-phishing?_ga=2.32000702.1825018133.1672924380-307544329.1672924380) sites.

文章来源: https://blog.avast.com/new-year-smishing
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)