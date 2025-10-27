---
title: Louisiana wants your ID if you're looking at adult-only websites
url: https://buaq.net/go-144859.html
source: unSafe.sh - 不安全
date: 2023-01-10
fetch_date: 2025-10-04T03:22:58.324995
---

# Louisiana wants your ID if you're looking at adult-only websites

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

Louisiana wants your ID if you're looking at adult-only websites

The state of Louisiana introduced a law on January 1, 2023, that holds
*2023-1-9 19:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-144859.htm)
阅读量:12
收藏*

---

The state of Louisiana introduced a law on January 1, 2023, that holds sites that specialize in pornographic content accountable if they do not check their visitors' ages.

A website is obliged to check whether a visitor is of the legal age required to access pornographic content if a substantial portion of its content falls into that category—meaning more than thirty-three and one-third percent of total material on a website. So, for obvious reasons, we will refer to the affected parties as porn sites in the rest of this article.

The law, known as [Act 440](https://legis.la.gov/legis/ViewDocument.aspx?d=1289498), can result in adult sites getting sued if they do not implement age verification technology. It lists a lot of reasons why explicit content can be harmful for young visitors and while we understand those reasons, we envision a lot of issues.

## Identifying information

Verifying somebody's age will almost certainly require that users provide personally identifiable information (PII) such as a credit card, ID or driver's license. So the first question is, what are the risks of trusting adult sites with this kind of PII? What happens if the stored information gets exfiltrated by a threat actor or a rogue insider? There's money, headlines, and potentially leverage, in understanding people's sexual preferences. And it's not just politicians, sports stars and celebrities at risk: I can already envision the phishing mails that claim ”Your ID was found on the servers of a porn site. Pay now or we will tell all your friends and family.”

The legislators must have had the same thought. The law says the commercial entity or third-party service that does the age verification should not retain any identifying information of the individual after access has been granted to the material. And those that retain identifying information will be liable for damages.

That's reassuring but, unfortunately, computer systems are very bad at forgetting things. Data breaches can happen to those with the best intentions and they can have all kinds of consequences. Users have no way to know if their data is beind stored or discarded, and the law won't do anything to stop [card skimmers](https://www.malwarebytes.com/blog/news/2021/11/how-to-defend-your-website-against-card-skimmers)—malware that's injected into a site to collect information as its entered into forms.

## Location, location

As in real estate, location matters a lot here. As long as Louisiana is the only state, or one of a few, with such a law, it is child’s play (pun intended) to circumvent the age verification. The IP address allocated to your computer can be used to discover with reasonable accurancy where you are in the world, to the nearest town or city. So, understanding where somebody is, and whether they should be asked their age, will probably be based on their IP address.

Such IP geolocation is not a foolproof system. Some ranges of IP addresses may occur only partially in Louisiana while the rest are located in other states or even countries. Both alse positives and false negatives are likely.

There are also several methods to mask or change an IP address deliberately, such as using a [VPN](https://www.malwarebytes.com/what-is-vpn), which can make it appear that a visitor is in a different city, or even a different country, than the one they are actually in.

Another location-related problem are the sites outside of Louisiana. Some countries are known to turn a blind eye to anything that doesn’t hurt its own population and brings in cash. They would do absolutely nothing about complaints hailing from Louisiana or any other state or country based on this or similar laws.

## UK

The UK has had plans to implement a similar law since 2016 as part of the [Digital Economy Act](https://www.gov.uk/government/collections/digital-economy-bill-2016), which demands mandatory age verification to access online pornography but was subsequently not enforced by the government.

And last year an even more far-reaching update was added to its draft [Online Safety Bill](https://www.gov.uk/guidance/a-guide-to-the-online-safety-bill). It hasn't happened yet, and it has received plenty of criticism for the reasons we have pointed out: Bad for privacy, easy to circumvent, and hard to achieve.

[Draft amendments](https://www.brookings.edu/blog/techtank/2022/12/21/u-k-government-purges-legal-but-harmful-provisions-from-its-revised-online-safety-bill/) have been made to smooth the path to getting the bill passed and the legislative process should take a couple of months, before we know how much gets implemented.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/01/attempts-to-stop-under-aged-from-accessing-adult-only-content-on-the-internet
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)