---
title: STRIPE Live Key Exposed:: Bounty: $1000
url: https://buaq.net/go-139387.html
source: unSafe.sh - 不安全
date: 2022-12-10
fetch_date: 2025-10-04T01:05:30.085857
---

# STRIPE Live Key Exposed:: Bounty: $1000

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

STRIPE Live Key Exposed:: Bounty: $1000

Hey Hunters,I have found a sensitive stripe live token leaking on a private program.[let’s say redac
*2022-12-9 19:56:42
Author: [infosecwriteups.com(查看原文)](/jump-139387.htm)
阅读量:15
收藏*

---

Hey Hunters,

I have found a sensitive stripe live token leaking on a private program.[let’s say redacted.com]

I collected all the subdomains using tools like Subfinder and Amass. After that, I filtered the live subdomains using httprobe. Found a subdomain admin.redacted.com which redirects the user/admin to google OAuth.

Your browser can execute JavaScript, which can, in turn, change the document; in this case, it redirects to google OAuth. After this, I used curl for admin.redacted.com to get the plain original output and nothing else.

Leaking stripe live token

Now I have a leaking stripe live token, but the token’s validity needs to be checked.

After checking the [Keyhacks](https://github.com/streaak/keyhacks) and the [Stripe API Documentation](https://stripe.com/docs/api). I was able to get a bunch of information, including:

**Balance:** It retrieves the current balance in the Stripe account.

> curl <https://api.stripe.com/v1/balance> -u sk\_live\_<Secret-Key>:

Balance in the Stripe Account

**Customers:** It retrieves the customer’s data and tracks payments. Including the Customer’s Name, Email, IP used, and many more.

> curl <https://api.stripe.com/v1/customers> -u sk\_live\_<Secret-Key>:

Multiple customer’s data and upcoming payments

**Charges:** It retrieves charges and card information. One such card details are also attached below. Stripe only gives you the last four digits.

> curl <https://api.stripe.com/v1/charges> -u sk\_live\_<Secret-Key>:

Card Details

**Files:** Retrieves Files that the admin uploads. Files generally have invoices, disputes, events, balances, bank accounts, tokens, charges, and more.

> curl <https://api.stripe.com/v1/files> -u sk\_live\_<Secret-Key>:

Files retrieved

Companies and other end users Sensitive Information Disclosure.

Reported — 21st August

Rewarded and Fixed — 30th August

**Let's connect:** <https://www.linkedin.com/in/vipul-sahu-a7a420174/>

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/stripe-live-key-exposed-bounty-1000-dc670f2c5d9c?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)