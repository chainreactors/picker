---
title: Bcrypt 准备说再见
url: https://buaq.net/go-165952.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:08.806284
---

# Bcrypt 准备说再见

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

Bcrypt 准备说再见

流行密码哈希算法 Bcrypt 已走过了四分之一世纪。它的长寿要归功于其开源可用性和技术特征。Bcrypt 的共同发明人 Niels Provos 希望在庆祝其下一个重要生日前 Bcryp
*2023-5-26 22:12:4
Author: [www.solidot.org(查看原文)](/jump-165952.htm)
阅读量:23
收藏*

---

流行密码哈希算法 Bcrypt 已走过了四分之一世纪。它的长寿要归功于其开源可用性和技术特征。Bcrypt 的共同发明人 Niels Provos 希望在庆祝其下一个重要生日前 Bcrypt 将不再流行。bcrypt 最早是随 OpenBSD 2.1 在 1997 年发布的，当时美国还对加密算法实施出口禁令，而 Provos 在德国长大在德国生活期间参与开发了 Bcrypt。它的迅速流行被认为是开源、不受出口限制的约束、任何人都可以用不同的语言实现该算法等因素的结果。Provos 与斯坦福大学系统安全教授 David Mazieres 共同开发了 bcrypt，当时他在 MIT 学习，通过开源社区相识，都参与了 OpenBSD 项目。bcrypt 相比其它哈希算法的创新是它包含了一个安全参数，可以随时间的推移而进行调整，以需要更多的算力去破解 bcrypt 哈希，因此 bcrypt 哈希在 25 年后计算资源无比丰富的情况下仍然难以破解。但可并行计算的专用硬件的出现让 bcrypt 算法面临淘汰。下一代哈希算法需要限制并行攻击的能力，比如需要大量的内存。

https://www.wired.com/story/bcrypt-password-hashing-25-years/

文章来源: https://www.solidot.org/story?sid=75070
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)