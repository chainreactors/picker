---
title: VM2远程代码执行漏洞曝光
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552091&idx=2&sn=445cd3cc9b5c1d062ed8c6c4a99dcfc4&chksm=e915dc61de6255774a3e4eb5b6e47ebc8f30d7aaac158cde1aeb35ef18677cfd20d370b07936&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-15
fetch_date: 2025-10-03T19:59:51.148476
---

# VM2远程代码执行漏洞曝光

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyVjkqzUMOEcvHMF5iaIEWNZicfty8KvKEicRbYaPRq7wgJ51ibBHiaibl1t2Q/0?wx_fmt=jpeg)

# VM2远程代码执行漏洞曝光

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

VM2现10分漏洞，可在沙箱外运行代码。

vm2是JS沙箱库，每个月通过npm的下载量超过1600万。Oxeye安全研究人员在vm2中发现了一个非常严重的远程代码执行漏洞，漏洞CVE编号为CVE-2022-36067，CVSS评分10分，攻击者利用该漏洞可以从沙箱环境逃逸并在主机系统上运行命令。

沙箱是与操作系统其他部分隔离开来的隔离环境。开发者常用沙箱来运行或测试不安全的代码，因此从受限的环境中逃逸并在主机上执行代码是一个非常大的安全隐患。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)漏洞分析

Node.js允许应用开发者定制应用遇到错误时的调用stack。定制调用stack可以通过Error对象的“prepareStacktrace”方法来实现。也就是说错误在发生时，错误对象的stack属性会被访问，node.js会调用该方法，并提供给该方法一个字符串表示和“CallSite”对象作为参数。Node.js调用“prepareStackTrace”函数如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLymMHBfpgiaCVHFBE7ufxmuRQmtfNGjibfkxNJLk7y5rDZ9TV5xtlKUHjA/640?wx_fmt=png)

数组中的每个“CallSite”对象都表示不同的stake帧。“CallSite”对象的严格方法getThis负责返回this对象。该行为可能会引发沙箱逃逸，因为有“CallSite”对象可能会返回通过调用“getThis”方法时创建的对象。在获得沙箱外创建的“CallSite”对象后，就可能访问节点的全局对象并执行任意系统命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLy8Z51oado90iaIsPyk0rzllyP5923ntjRQRMDAIP6d9LV3a5c0URvWQA/640?wx_fmt=png)

PoC代码如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyvNmDRzQsicjmYwwfhLXlWtOB3t6ZLu14ApAZldR3QmKyAr55xzDyaNg/640?wx_fmt=png)

攻击者利用该漏洞可以绕过vm2沙箱环境，并在沙箱主机上运行shell命令。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyXXVicn0lvfkajFapJXGCHp1meaImEc8spwI5BtufTeZKpPonW9PKW7g/640?wx_fmt=png)漏洞修复

Vm2维护人员意识到覆写“prepareStackTrace”可能会引发沙箱逃逸，并尝试封装Error对象和“prepareStackTrace”方法来进行应对。Vm2已于v 3.9.11版本中修复了该漏洞。使用沙箱的用户应检查确认是否依赖vm2，并更新到最新版本。

完整技术分析参见：https://www.oxeye.io/blog/vm2-sandbreak-vulnerability-cve-2022-36067

参考及来源：https://www.bleepingcomputer.com/news/security/critical-vm2-flaw-lets-attackers-run-code-outside-the-sandbox/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLyNJ7sPbBCIiaesWxs4ZJ8iaWVZoFbL5CxwMrKjyKRbDSeGc9rRrqjCqmQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28LrEyHKKuuOsKYUaRLJcLy25nJqrS3dpqubo41iaY2uw9H4XiatorZiawBbILY6kzBGaeelXPopiccfA/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过