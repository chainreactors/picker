---
title: Inception瞬态执行攻击影响所有AMD Zen CPU
url: https://buaq.net/go-174820.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:50.411733
---

# Inception瞬态执行攻击影响所有AMD Zen CPU

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

![](https://8aqnet.cdn.bcebos.com/b19f5464aa6c452bbe71d4a81d60cfd9.jpg)

Inception瞬态执行攻击影响所有AMD Zen CPU

导语：​新瞬态执行攻击Inception可
*2023-8-19 11:50:0
Author: [www.4hou.com(查看原文)](/jump-174820.htm)
阅读量:29
收藏*

---

导语：​新瞬态执行攻击Inception可从所有AMD Zen CPU泄露敏感数据。

新瞬态执行攻击Inception可从所有AMD Zen CPU泄露敏感数据。

苏黎世联邦理工学院（ETH Zurich）研究人员发现一种新的瞬态执行攻击——'Inception'攻击。攻击可从攻击者控制的地址发起推测执行，引发信息泄露。漏洞CVE编号CVE-2023-20569，影响所有AMD Zen CPU。

瞬态执行攻击利用了现代处理器的推测执行特征，通过猜测接下来要执行的内容来提高CPU的性能。如果猜测正确，CPU就无需等到操作执行结束，如果猜测失败，只需要回滚并继续执行操作即可。猜测执行存在的问题是会留下痕迹，攻击者可以查看和分析这些有价值的数据用于攻击活动。

苏黎世联邦理工学院研究人员融合了'Phantom speculation' (CVE-2022-23825)和一种新的瞬态执行攻击（TTE，Training in Transient Execution）创建了更加强大的inception攻击。'Phantom speculation'允许攻击者在无错误预测源处无需任何分支就可以触发错误预测，比如在任意异或XOR指令创建推测执行周期（瞬态窗口）。TTE是一种对未来错误预测的操纵，通过注入新的预测到预测分支来创建可利用的推测执行。Inception攻击融合了以上两种概念，使得被攻击的CPU认为XOR指令是一个递归调用指令。Inception攻击会用攻击者控制的目标地址来覆写返回栈缓存，攻击者可从AMD Zen CPU运行的非特权进程泄露任意数据。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230809/1691587335438228.png "1691586950498544.png")

图 Inception攻击逻辑

Inception攻击可实现39字节/秒的数据泄露速率，泄露一个16字符的密码只需要0.5秒，泄露一个RSA密钥只需要6.5秒。Inception攻击可以绕过现有推测执行攻击的修复措施，如Spectre和瞬时控制流劫持等。

Inception攻击是针对AMD CPU的，所以是由AMD CPU的设备都受到Inception和 Phantom攻击的影响。研究人员分析发现Phantom也会影响Intel CPU，此外部分Intel CPU也受到特定TTE变种的影响。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230809/1691587337136037.png "1691586978179739.png")

图 特定TTE变种对CPU的影响

研究人员开发的PoC运行在Linux系统上，但Inception 和Phantom攻击是针对的是硬件漏洞。因此，任何受影响的CPU上运行的操作系统都会受到影响。

AMD建议使用Zen 3和Zen 4 CPU架构的用户使用µcode补丁或BIOS更新，对于Zen和Zen 2 CPU架构用户无需使用µcode补丁或BIOS更新。此外，AMD还计划发布更新的AGESA。

相关研究成果已被安全顶会Usenix security 2023录用，论文下载地址：https://comsec.ethz.ch/wp-content/files/inception\_sec23.pdf

更多参见：https://comsec.ethz.ch/research/microarch/inception/

本文翻译自：https://comsec.ethz.ch/research/microarch/inception/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?YALmdfRK)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/f36e8f61d6ad9bd924da6c739e380b82.jpg)

  Inception瞬态执行攻击影响所有AMD Zen CPU](https://www.4hou.com/posts/EXXY)
* [![](https://img.4hou.com/images/516e3c10f19d3f1a13fb3ad9d2198bc9.jpg)

  XCon2023议题 | Golang安全：探索安全稳定的Hook方法](https://www.4hou.com/posts/9ABB)
* [![](https://img.4hou.com/images/7d8495fbefc4657ce438baa8ab4da463.png)

  XCon2023议题：基于VxWorks系统的固件符号恢复方法研究](https://www.4hou.com/posts/5wxK)
* [![](https://img.4hou.com/images/eacb6e0789a93e7098ba998d7e3a0609.png)

  XCon2023议题：依托于SLSA框架的广义可信供应链安全建设实践](https://www.4hou.com/posts/WKvQ)
* [![](https://img.4hou.com/images/aa4f234ef43a40479f29880ba4db1f41.jpg)

  云计算攻击：网络攻击的新载体](https://www.4hou.com/posts/7yy1)
* [![](https://img.4hou.com/images/201810211415429849.jpg)

  Lazarus黑客以微软 IIS 服务器为目标传播恶意软件](https://www.4hou.com/posts/V2nX)

![]()

文章来源: https://www.4hou.com/posts/EXXY
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)