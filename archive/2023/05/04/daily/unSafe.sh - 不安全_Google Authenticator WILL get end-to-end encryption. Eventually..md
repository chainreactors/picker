---
title: Google Authenticator WILL get end-to-end encryption. Eventually.
url: https://buaq.net/go-161565.html
source: unSafe.sh - 不安全
date: 2023-05-04
fetch_date: 2025-10-04T11:38:41.347187
---

# Google Authenticator WILL get end-to-end encryption. Eventually.

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

Google Authenticator WILL get end-to-end encryption. Eventually.

Following criticism, Google has decided to bring end-to-end encryption
*2023-5-3 20:15:0
Author: [www.malwarebytes.com(查看原文)](/jump-161565.htm)
阅读量:20
收藏*

---

Following criticism, Google has decided to bring end-to-end encryption (E2EE) to its Google Authenticator cloud backups. The search giant recently introduced a feature that allows users back up two-factor authentication ([2FA](https://www.malwarebytes.com/blog/news/2017/01/understanding-the-basics-of-two-factor-authentication)) tokens to the cloud, but the lack of encryption caused some commentators to warn people off using it.

Google Authenticator is an authenticator app used to generate access codes, called one-time passwords (OTPs). These OTPs are only valid for a short period and are generated on demand. They serve as an additional form of authentication by proving that you have access to the device generating the OTP. Google Authenticator is one of the most well-known authenticators. Although it's made by Google it's not limited to Google’s own services, but can also be used with Facebook, Twitter, Instagram, and many more.

On April 24, 2023, Google [announced](https://security.googleblog.com/2023/04/google-authenticator-now-supports.html) an update across both iOS and Android, which added the ability to safely backup the secrets used to generate OTPs to your Google Account. This allows users to create a backup which they can use if their device is lost, stolen, or damaged. Since OTPs in Google Authenticator were previously only stored on a single device, a loss of that device locked you out of any service where you used it to log in.

Shortly after the new feature was rolled out, Mysk’s security researchers [advised](https://twitter.com/mysk_co/status/1651021165727477763) against turning on the new feature. They analyzed the network traffic that occurs when the app syncs the secrets, and found out that the traffic was not end-to-end encrypted. This would mean that in case of a data breach or if someone obtains access to your Google Account, all of your OTP secrets would be compromised, and they would be able to generate OTPs as if they were you.

The likelihood of someone stealing the secret seeds from Google’s servers is relatively small, but since it is better to be safe than sorry and one problem less is always good to have, users asked Google to add a passphrase to protect the secrets. This would introduce an extra safeguard that makes them accessible only to their owner.

Google’s primary objection to this method was that it heightens the risk of users getting completely locked out of their own data. Meaning that if you lost your device and the passphrase, you would lose all access to your accounts.

[Google Group Product Manager Christiaan Brand tweeted](https://twitter.com/christiaanbrand/status/1651279598309744640) that end-to-end encryption (E2EE) will be made available for Google Authenticator down the line, but they are rolling out this feature carefully.

> (2/4) We encrypt data in transit, and at rest, across our products, including in Google Authenticator. E2EE is a powerful feature that provides extra protections, but at the cost of enabling users to get locked out of their own data without recovery.
>
> — Christiaan Brand (@christiaanbrand) [April 26, 2023](https://twitter.com/christiaanbrand/status/1651279648519774209?ref_src=twsrc%5Etfw)

According to Google, the option to use the app offline will remain an alternative for those who prefer to manage their backup strategy themselves. But, if you want to try the new Authenticator with Google Account synchronization, simply update the app and follow the prompts.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/05/google-will-eventually-add-end-to-end-encryption-to-google-authenticator
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)