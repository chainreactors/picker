---
title: S3Crets_Scanner - Hunting For Secrets Uploaded To Public S3 Buckets
url: https://buaq.net/go-141186.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:46.864972
---

# S3Crets_Scanner - Hunting For Secrets Uploaded To Public S3 Buckets

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

![](https://8aqnet.cdn.bcebos.com/4669a479cb1e8e32dfe993727bc2f93b.jpg)

S3Crets\_Scanner - Hunting For Secrets Uploaded To Public S3 Buckets

S3cret Scanner tool designed to provide a complementary layer for the Amazon S3 Security B
*2022-12-23 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-141186.htm)
阅读量:54
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj9Ahc2RsjM17KYp8WaTL_xp0roZiIbE5Xbu60gjF4E2beYJy47tn2Vv8-ZtfnvtIF7_4FQ7m5Kq40bUlY2tad0NYtdGCCvwNruBw9RuVYD73dZJt9CIn7O6bE2nrOlHZyERrgHBOrb4LceULA0-i-tDJZSFx6d68AGYrvjO4QBWUNCDZOXIM8QZJzVbg=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEj9Ahc2RsjM17KYp8WaTL_xp0roZiIbE5Xbu60gjF4E2beYJy47tn2Vv8-ZtfnvtIF7_4FQ7m5Kq40bUlY2tad0NYtdGCCvwNruBw9RuVYD73dZJt9CIn7O6bE2nrOlHZyERrgHBOrb4LceULA0-i-tDJZSFx6d68AGYrvjO4QBWUNCDZOXIM8QZJzVbg)

* `S3cret Scanner` tool designed to provide a complementary layer for the [Amazon S3 Security Best Practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html "Amazon S3 Security Best Practices") by proactively hunting secrets in public S3 buckets.
* Can be executed as `scheduled task` or `On-Demand`

## Automation workflow

The [automation](https://www.kitploit.com/search/label/Automation "automation") will perform the following actions:

1. List the public buckets in the account (Set with ACL of `Public` or `objects can be public`)
2. List the textual or sensitive files (i.e. `.p12`, `.pgp` and more)
3. Download, scan (using truffleHog3) and delete the files from disk, once done evaluating, one by one.
4. The [logs](https://www.kitploit.com/search/label/Logs "logs") will be created in `logger.log` file.

---

S3Crets\_Scanner - Hunting For Secrets Uploaded To Public S3 Buckets
![S3Crets_Scanner - Hunting For Secrets Uploaded To Public S3 Buckets](https://blogger.googleusercontent.com/img/a/AVvXsEj9Ahc2RsjM17KYp8WaTL_xp0roZiIbE5Xbu60gjF4E2beYJy47tn2Vv8-ZtfnvtIF7_4FQ7m5Kq40bUlY2tad0NYtdGCCvwNruBw9RuVYD73dZJt9CIn7O6bE2nrOlHZyERrgHBOrb4LceULA0-i-tDJZSFx6d68AGYrvjO4QBWUNCDZOXIM8QZJzVbg=s72-c)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/s3cretsscanner-hunting-for-secrets.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)