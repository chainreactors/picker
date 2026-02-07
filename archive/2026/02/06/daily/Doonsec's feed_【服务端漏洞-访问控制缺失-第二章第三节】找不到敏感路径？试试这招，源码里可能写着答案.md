---
title: 【服务端漏洞-访问控制缺失-第二章第三节】找不到敏感路径？试试这招，源码里可能写着答案
url: https://mp.weixin.qq.com/s/z1iLbcemPe7n9yr9qcVl1w
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:03:29.252033
---

# 【服务端漏洞-访问控制缺失-第二章第三节】找不到敏感路径？试试这招，源码里可能写着答案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGFIRO0GPQ3egmMcHx9x7heht7xzSosA867TXhiabKlEGJicf5YibQ9e78icbF5m2GoVia56FeERDeiajWVquKicR9JG7wlpJxsOTqcVqA/0?wx_fmt=jpeg)

# 【服务端漏洞-访问控制缺失-第二章第三节】找不到敏感路径？试试这招，源码里可能写着答案

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

上一节[【服务端漏洞-访问控制缺失-第二章第二节】别找了，高危漏洞有时就藏在最显眼的地方](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797878&idx=1&sn=20e404cd7640867d43ffc148c1dcf3d1&scene=21#wechat_redirect)中，我们了解了一些配置文件可能泄露一些路径，且这有可能是系统有访问控制权限缺失的突破点。但如果这些常见的robots.txt中，没有泄露什么可用路径，我们又该如何继续呢？

今天这边就继续给大家分享另外一个访问控制权限缺失的突破点，这就是网站源码

查看源码，是我们在做漏洞挖掘的基础操作，这个动作做好了，会有意想不到的效果。

比如以下这个实例中，访问该系统的robots.txt 文件，是返回无法找到的，说明系统没在这类文件中泄露什么有用信息。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHonjh9tiadBqpicpUJW84TutLJMEqu3nDqSm7D3mNTvctDicw8ppjsTtRvqJvc67nQoG0cYwLKF69kmU0xkhdMNicJEc7TRoJh6nA/640?wx_fmt=png&from=appmsg)

此时，我们就可以转到网站系统的根目录，直接按 Ctrl+u 对当前系统的源码进行查看，看是否有发现。

通过阅读该系统的源码内容，发现系统中存在这样一个逻辑，就是告知了系统，如果当前登录的是管理员，就会跳转到目录 /admin-uw0ce9

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGFNOImksEubd94Qq7ADbVW6sFEy0qbM1g2FFcvsaEdGXAnjyMyHrWDibt5WdcVtsWsXQ54Zw8wrrgRFgqDMRKIfJEpgWLiciazYBg/640?wx_fmt=png&from=appmsg)

虽然这是系统逻辑要求，需要是管理员的时候才会跳转到这个路径，但我们是不能忽视用非管理员的身份去查看这个目录的动作的。这不，一试一个准，研发人员太大意了，没限制好该路径的访问权限，而且还把这个路径给泄露出来了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGF4FlmrJ9GYOsTBLEvyKeFW48FF8XTU5UEC6pd4upX3WicBobxj2HNdNKQJEC7KyQnvt9snpOJXGDLdicaO985aQZcClwXWlpSlg/640?wx_fmt=png&from=appmsg)

关于访问控制权限缺失的另一种路径发现、挖掘方式，今天就分享到这了。后续这边还会继续分享有关服务端的更多漏洞原理、利用、挖掘方式，感兴趣的可以点点关注。

觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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