---
title: Gary Benson: The other AWS IAM SSO problem
url: https://buaq.net/go-148436.html
source: unSafe.sh - 不安全
date: 2023-02-08
fetch_date: 2025-10-04T05:55:42.014666
---

# Gary Benson: The other AWS IAM SSO problem

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

Gary Benson: The other AWS IAM SSO problem

AWS, GotchasTuesday 7th February 2023Tuesday 7t
*2023-2-7 22:46:48
Author: [gbenson.net(查看原文)](/jump-148436.htm)
阅读量:30
收藏*

---

[AWS](https://gbenson.net/category/aws/), [Gotchas](https://gbenson.net/category/gotchas/)

Tuesday 7th February 2023Tuesday 7th February 2023
1 Minute

The other thing you’ll run into using IAM users in AWS CLI is that a lot of things don’t support SSO sessions anyway. If you [configure an IAM user with an SSO session name](https://gbenson.net/aws-cli-with-iam-users/ "Using AWS CLI with IAM users") as recommended you’ll get errors like this:

```
$ eb init -p python-3.8 eb-flask-app
ERROR: InvalidConfigError - The profile "default" is configured to use SSO but is missing required configuration: sso_start_url, sso_region
```

and this:

```
$ terraform apply
| Error: configuring Terraform AWS Provider: loading configuration: profile "default" is configured to use SSO but is missing required configuration: sso_region, sso_start_url
```

You can fix these by configuring without an SSO session:

```
$ aws configure sso
SSO session name (Recommended):
WARNING: Configuring using legacy format (e.g. without an SSO session).
Consider re-running "configure sso" command and providing a session name.
SSO start URL [None]: https://whatever.awsapps.com/start
SSO region [None]: us-east-1
 ...
```

You can also fix them by just editing your `~/.aws/config`, and copying the `sso_start_url` and `sso_region` keys from the `[sso-session ...]` section into the relevant user’s section, but that might be a hack too far!

![](https://secure.gravatar.com/avatar/3f08bcb5e425b3d8db2285b9793d1523?s=80&d=mm&r=g)

## Published by gbenson

I make things ðŸŒ± he/him [View all posts by gbenson](https://gbenson.net/author/admin/)

**Published**
Tuesday 7th February 2023Tuesday 7th February 2023

## Post navigation

文章来源: https://gbenson.net/sessionless-aws-iam-sso/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)