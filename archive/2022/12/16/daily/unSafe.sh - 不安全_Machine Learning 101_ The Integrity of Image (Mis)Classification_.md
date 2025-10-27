---
title: Machine Learning 101: The Integrity of Image (Mis)Classification?
url: https://buaq.net/go-140170.html
source: unSafe.sh - 不安全
date: 2022-12-16
fetch_date: 2025-10-04T01:38:56.122972
---

# Machine Learning 101: The Integrity of Image (Mis)Classification?

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

![](https://8aqnet.cdn.bcebos.com/c97b9bbea22338ec75c76d5acc9fe668.jpg)

Machine Learning 101: The Integrity of Image (Mis)Classification?

Professor Ron Rivest observed the close relationship between cryptogra
*2022-12-15 22:9:25
Author: [research.nccgroup.com(查看原文)](/jump-140170.htm)
阅读量:18
收藏*

---

![](https://i0.wp.com/photos.smugmug.com/Jump/i-xqFcQDm/0/1d111de6/L/helmet3-L.jpg?w=1100&ssl=1)

Professor Ron Rivest observed the close relationship between cryptography and machine learning at the [ASIACRYPT conference back in 1991](https://people.csail.mit.edu/rivest/pubs.html#Riv91). Cross-fertilization of common notions, such as integrity, privacy, confidentiality and authenticity, have only grown in the following three decades as these fields have become more central to our everyday lives.

This blog post is the first in a series related to machine learning, and highlights a realistic weakness in the integrity of image classification systems. As a running example, the post will demonstrate how images that are correctly recognized as containing a stop signal are minimally perturbed into derived images which are then incorrectly classified into another category. Consider the impact of self-driving cars that [incorrectly recognize stop signals](https://www.washingtonpost.com/technology/2022/02/02/tesla-phantom-braking/), or the potential consequences of [client-side media scanning](https://www.theregister.com/2021/10/15/clientside_side_scanning/) incorrectly flagging problematic content.

This is an executable blog post that you can run yourself by [loading the Gist `.ipynb` file](https://gist.github.com/eschorn1/f587ccf5b33db405f0e416865bdeff39) into any Jupyter-based notebook system, or you can just continue browsing it below.

Sorry, something went wrong. [Reload?](https://gist.github.com/eschorn1/f587ccf5b33db405f0e416865bdeff39.json)

Sorry, we cannot display this file.

Sorry, this file is invalid so it cannot be displayed.

**Published**
December 15, 2022

## Post navigation

文章来源: https://research.nccgroup.com/2022/12/15/machine-learning-101-the-integrity-of-image-misclassification/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)