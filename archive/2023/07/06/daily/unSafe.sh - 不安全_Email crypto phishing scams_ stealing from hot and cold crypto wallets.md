---
title: Email crypto phishing scams: stealing from hot and cold crypto wallets
url: https://buaq.net/go-171284.html
source: unSafe.sh - 不安全
date: 2023-07-06
fetch_date: 2025-10-04T11:51:33.187275
---

# Email crypto phishing scams: stealing from hot and cold crypto wallets

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

![](https://8aqnet.cdn.bcebos.com/0ac5f8e9834566aba5b8bc55a4c94b3b.jpg)

Email crypto phishing scams: stealing from hot and cold crypto wallets

The higher the global popularity of cryptocurrencies and the more new ways of storing
*2023-7-5 18:0:9
Author: [securelist.com(查看原文)](/jump-171284.htm)
阅读量:34
收藏*

---

The higher the global popularity of cryptocurrencies and the more new ways of storing them, the wider the arsenal of tools used by malicious actors who are after digital money. Scammers tailor the complexity of technology they use and the thoroughness of their efforts to imitate legitimate websites to how well the target is protected and how large the amount is that they can steal if successful. This story covers two fundamentally different methods of email attacks on the two most popular ways of storing cryptocurrency: hot and cold wallets.

## Hot wallets and attempts at hacking them

A hot wallet is a cryptocurrency wallet with permanent access to the internet. This is essentially any online service that provides cryptocurrency storage, ranging from crypto exchanges to specialized apps.

Hot wallets are a highly popular crypto storage option. This can be explained by the simplicity of creating one (registering with a wallet service is all you need to do) and the ease of withdrawing and converting funds. The popularity and simplicity of hot wallets makes them cybercriminals’ main target. However, for this reason, and due to the fact that hot wallets are always online, they are rarely used for storing large amounts. Hence, cybercriminals have little motivation to invest heavily into phishing campaigns, and so, techniques used in email attacks on hot wallets are hardly ever original or complex. In fact, they look rather primitive and target mostly unsophisticated users.

A typical phishing scam aimed at a hot wallet user works as follows: hackers send email messages addressed as coming from a well-known crypto exchange and requesting the user to confirm a transaction or verify their wallet again.

[![Sample phishing email that targets Coinbase users](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164051/Phishing_targeting_hot_and_cold_cryptowallets_01-1024x285.jpeg)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164051/Phishing_targeting_hot_and_cold_cryptowallets_01.jpeg)

Sample phishing email that targets Coinbase users

After the user clicks the link, they are redirected to a page where they are asked to enter their seed phrase. A seed phrase (recovery phrase) is a sequence of 12 (less commonly 24) words for recovering access to a crypto wallet. This is essentially the main password for the wallet. The seed phrase can be used for gaining or recovering access to the user’s account and making any transactions. The seed phrase cannot be changed or recovered: by misplacing it, the user risks losing access to their wallet for good, and by giving it to scammers, permanently compromising their account.

[![Seed phrase entry page](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164123/Phishing_targeting_hot_and_cold_cryptowallets_02-1024x557.jpeg)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164123/Phishing_targeting_hot_and_cold_cryptowallets_02.jpeg)

Seed phrase entry page

If the user enters the seed phrase on a fake web page, scammers get full access to the wallet and the ability to siphon all of the funds to their own addresses.

Fairly simple and devoid of software or social engineering tricks, scams like these typically target non-technical users. A seed phrase entry form usually has a stripped-down look: just an input field and a crypto exchange logo.

## Phishing scams that target cold wallets

A cold wallet (cold storage) is a wallet without a permanent connection to the internet, like a dedicated device or even just a private key written on a slip of paper. Hardware storage is the most common type of cold wallets. As these devices are offline most of the time, and remote access is impossible, users tend to store significantly larger amounts on these. That said, it would be erroneous to believe that a hardware wallet cannot be compromised without stealing it, or at least, getting physical access to it. As is the case with hot wallets, scammers use social engineering techniques to get to users’ funds. We spotted an email campaign recently that was specifically aimed at the owners of hardware cold wallets.

This type of attack starts as a crypto email campaign: the user gets an email, addressed as being from the Ripple cryptocurrency exchange and offering to join a giveaway of XRP tokens, the platform’s internal cryptocurrency.

[![Phishing email pretending to be from Ripple cryptocurrency exchange](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164155/Phishing_targeting_hot_and_cold_cryptowallets_03-1024x595.jpeg)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164155/Phishing_targeting_hot_and_cold_cryptowallets_03.jpeg)

***Phishing letter pretending to be from the Ripple cryptocurrency exchange***

If the user clicks the link, they are presented with a blog page featuring a post that explains the rules of the “giveaway”. The post contains a direct link to “registration”.

[![Fake Ripple blog](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164223/Phishing_targeting_hot_and_cold_cryptowallets_04.jpeg)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30164223/Phishing_targeting_hot_and_cold_cryptowallets_04.jpeg)

***Fake Ripple blog***

Already at this point, the scam shows a few differences from mass attacks on hot wallets: instead of sending the user a link to a phishing page, the scammers used a more sophisticated immersion trick with a blog post. They also went so far as meticulously copying the design of the Ripple website and registering a domain name that was nearly identical to the exchange’s official domain. This is called a [Punycode](https://encyclopedia.kaspersky.com/glossary/punycode/?utm_source=securelist&utm_medium=blog&utm_campaign=termin-explanation) phishing attack. At first glance, the second-level domain is identical to the original one, but a closer look will reveal that the letter “r” has been replaced with a Unicode character that uses a [cedilla](https://en.wikipedia.org/wiki/Cedilla):

`https://app[.]xn--ipple-4bb[.]net -> https://app[.]ŗipple[.]net/`

Also, the scam site is hosted in the .net top-level domain, rather than .com, where the official Ripple website is located. This may not raise any red flags with the victim, though, as both domains are widely used by legitimate organizations.

After the user follows the link from the “blog” to the fake Ripple page, they are offered to connect to the WebSocket address wss://s2.ripple.com.

[![Connection to the WebSocket address](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30165501/Phishing_targeting_hot_and_cold_cryptowallets_05.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30165501/Phishing_targeting_hot_and_cold_cryptowallets_05.png)

Connection to the WebSocket address

Next, the user is offered to enter the address of their XRP account.

[![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30165541/Phishing_targeting_hot_and_cold_cryptowallets_06.jpeg)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/30165541/Phishing_targeting_hot_and_cold_cryptowallets_06.jpeg)

***Ente...