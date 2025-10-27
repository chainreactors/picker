---
title: Quickly see differences between Zone Versions with Version Comparisons
url: https://buaq.net/go-172088.html
source: unSafe.sh - 不安全
date: 2023-07-15
fetch_date: 2025-10-04T11:51:22.237929
---

# Quickly see differences between Zone Versions with Version Comparisons

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

![](https://8aqnet.cdn.bcebos.com/9c95c0862e531e8599ecf2d121395d29.jpg)

Quickly see differences between Zone Versions with Version Comparisons

Loading...
*2023-7-14 21:0:50
Author: [blog.cloudflare.com(查看原文)](/jump-172088.htm)
阅读量:19
收藏*

---

Loading...

* [![Garrett Galow](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2018/04/14729279_10207227100946205_2625241094472568444_n.jpg)](https://blog.cloudflare.com/author/garrett/)

![Quickly see differences between Zone Versions with Version Comparisons](https://blog.cloudflare.com/content/images/2023/07/image3-21-1.png)

On the week of July 10, 2023, we launched a new capability for Zone Versioning - Version Comparisons. With Version Comparisons, you can quickly get a side by side glance of what changes were made between two versions. This makes it easier to evaluate that a new version of your zone’s configuration is correct before deploying to production.

![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-11-at-10.09.10-PM.png)

### A quick recap about Zone Versioning

[Zone Versioning](https://developers.cloudflare.com/version-management/) was launched at the start of 2023 to all Cloudflare Enterprise customers and allows you to create and manage independent versions of your zone configuration. This enables you to safely configure a set of configuration changes and progressively roll out those changes together to predefined environments of traffic. Having the ability to carefully test changes in a test or staging environment before deploying them to production, can help catch configuration issues before they can have a large impact on your zone’s traffic. See the [general availability announcement blog](https://blog.cloudflare.com/zone-versioning-ga/) for a deeper dive on the overall capability.

### Why we built Version Comparisons

[Diff](https://en.wikipedia.org/wiki/Diff) is a well known and often used tool by many software developers to quickly understand the difference between two files. While originally just a command line utility it is now ubiquitous across the software world. Most commonly used in code reviews, software developers use ‘diffs’ to ensure they can validate the set of changes they intend to make to a codebase and to allow others to easily review their code by focusing on what changed. One of the drawbacks of graphical user interfaces (GUIs) for managing configurations is since they aren’t ‘files’, tools like diff don’t work for them. This was true with Zone Versioning, as to try and understand what had changed between two versions you would need to manually inspect each version and the various sections of the dashboard across both versions. This is quite tedious and error-prone, so it can reduce the safety that versioning can provide.

With Version Comparisons, we are bringing the same capabilities of diff but without the need for using a command line to allow customers to compare two versions side by side. This makes the process of understanding which configurations of your zone changed between two versions easy, quick and painless. By pointing out which config has changed, you can have greater confidence that deploying a new version of your configuration will not create any surprises. Let’s now look at how to use Version Comparisons in the Cloudflare Dashboard.

### Using Version Comparisons

After navigating to a zone that has Zone Versioning enabled, select ‘Version Management’ in the left-hand navigation. For help getting started with Zone Versioning, see our [dev docs](https://developers.cloudflare.com/version-management/).

![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-11-at-10.06.53-PM.png)

After selecting the ‘Version Management’ tab you will notice a third option - ‘Comparisons’. Selecting that will prompt you to select two versions to compare. Select the two version you want to compare and then select ‘Compare’

![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-11-at-10.10.26-PM.png)

After a few seconds, the page will update automatically with a comparison on a per-product basis. The lower numbered version will always be presented on the left and the top will show you which environments the versions are assigned to so that you can ensure you are comparing the right versions. A common use case would be to compare the versions in staging and production to verify the changes before promoting the staging version to production.

Any products with changes will have ‘changes detected’ noted next to them. Selecting one will open up the diff of that product across both versions.

![](https://blog.cloudflare.com/content/images/2023/07/Screenshot-2023-07-11-at-10.09.10-PM--1-.png)

Changes will be highlighted for new additions and removals for that service. Based on the comparison, you can then decide if more changes are necessary or if that new version is ready to be rolled out.

### Try out Version Comparisons today

Versions comparisons are available to all customers using Zone Versioning! If you are a Cloudflare Enterprise customer, to get started using Zone Versioning and Version Comparisons, check out our [dev docs](https://developers.cloudflare.com/version-management/).

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate any
[website
or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/),
[ward off DDoS
attacks](https://www.cloudflare.com/ddos/), keep
[hackers at
bay](https://www.cloudflare.com/application-security/),
and can help you on
[your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://1.1.1.1/) from any device to get started with
our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a
new career direction, check out [our open
positions](https://cloudflare.com/careers).

[Zone Versioning](https://blog.cloudflare.com/tag/zone-versioning/)
[Product News](https://blog.cloudflare.com/tag/product-news/)

文章来源: http://blog.cloudflare.com/quickly-see-differences-between-zone-versions-with-version-comparisons/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)