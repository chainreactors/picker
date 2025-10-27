---
title: The curl fragment trick
url: https://buaq.net/go-141183.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:45.776253
---

# The curl fragment trick

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

![](https://8aqnet.cdn.bcebos.com/904c0934426d4ce662d4dd2ec8df634d.jpg)

The curl fragment trick

curl supports globbing in the sense that you can provide ranges or list
*2022-12-23 21:44:33
Author: [daniel.haxx.se(查看原文)](/jump-141183.htm)
阅读量:30
收藏*

---

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/08/daniel-books-wide.jpg)

curl supports *globbing* in the sense that you can provide ranges or lists in the URL that will make curl iterate, loop, over all the different variations and do a separate transfer for each.

For example, get ten images in a numeric range:

```
curl https://example.com/image[1-10].jpg -O
```

Or get them when named after some weekdays:

```
curl https://example.com/{Monday,Tuesday,Friday}.jpg -O
```

## Naming the output

The examples above use `-O` which makes curl use the same name for the destination file as is used the effective URL. Convenient, but not always what you want.

curl also allows you to refer to the number or name from the range or list and use that when naming your output files, which helps you do better globbing.

For example, maybe the file name part of the URL is actually the same and you iterate over another difference in the URL. Like this:

```
curl https://example.com/{Monday,Tuesday,Friday}/image -o #1.jpg
```

The `#1` part in the example is a reference back to the first list/range, as you can do multiple ones and even using mixed types and you can then use multiple #-references in the same command line. To illustrate, here is a simple example using two iterators to download three hundred images:

```
curl https://{red,blue,green}.example.com/image[1-100].jpg -o "#2-#1-stored.jpg"
```

There is actually no upper limit to how many transfers you can do like this with curl, other than that the numeric ranges only deal with up to 64 bit numbers.

## Hundreds? Maybe go parallel

If you actually do come up with a command line that needs to transfer several hundred or more resources, then maybe consider adding `-Z, --parallel` to the mix so that curl performs many transfers simultaneously, in parallel. This can drastically reduce the total time needed for completing the task.

curl runs up to 50 transfers in parallel by default when this option is used, but you can also tweak this amount with `--parallel-max`.

## A fragment trick

Okay, so now we finally arrive at the fragment and *the trick* mentioned in the title.

If you want to do several repeated transfers but not actually change the URL then the examples above do not satisfy you as they change the URL for every new transfer.

A neat trick is then to add a fragment part to the URL you use, and then do the globbing there. The fragment is the rightmost part of a URL that starts with a `#`-character and continues to the end of the URL.

A fragment can always be added to a URL, but the fragment is never actually transmitted over the network so the remote server is not aware of it.

Get *the same* URL ten times, saved in different target files:

```
curl https://example.com/index.html#[1-10] -o #1.html
```

If you rather name the outputs according some scheme, you can of course just list them in the glob:

```
curl https://example.com/index.html#{mercury,venus,earth,mars} -o #1.html
```

## Maybe slower

In cases where you transfer the same URL many times, chances are you want to do this because the content changes at some interval. Perhaps you then do not want them all to be done as fast as possible as then the contents may not have updated.

To help you pace the transfers to get the same thing over and over in a more controlled manner, curl offers `[--rate](https://daniel.haxx.se/blog/2022/05/23/curl-offers-repeated-transfers-at-slower-pace/)`. With this you can tell curl to not do it faster than N transfers per given period.

If the URL contents update every 5 minutes, then doing the transfer 12 times per hour seems suitable. Let’s do it 2016 times to have the operation run non-stop for a week:

```
curl "https://example.com/index.html#[1-2016]" --rate 12/h -O
```

## tech, open source and networking

文章来源: https://daniel.haxx.se/blog/2022/12/23/the-curl-fragment-trick/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)