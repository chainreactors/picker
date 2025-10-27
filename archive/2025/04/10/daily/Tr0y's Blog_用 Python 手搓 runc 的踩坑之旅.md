---
title: 用 Python 手搓 runc 的踩坑之旅
url: https://www.tr0y.wang/2025/04/09/%E7%94%A8Python%E6%89%8B%E6%90%93runc%E7%9A%84%E8%B8%A9%E5%9D%91%E4%B9%8B%E6%97%85/
source: Tr0y's Blog
date: 2025-04-10
fetch_date: 2025-10-06T22:06:17.109688
---

# 用 Python 手搓 runc 的踩坑之旅

[**Tr0y's Blog**](/)

* [首页](/)
* [生命线](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [摄影集](/gallery/)
* [关于](/about/)

2025年4月9日 20:35:12

636 字

4 分钟

 次

[知识输出
(16)](#collapse-77f0ee1b8a872569d52f43f678e2970f "知识输出")

[ChatGPT 指导下的 TOA 伪造之旅](/2023/12/13/fake_toa/ "ChatGPT 指导下的 TOA 伪造之旅")
[MATLAB 实现 stegsolve](/2017/06/14/MATLABstegsolve/ "MATLAB 实现 stegsolve")
[ReIPdog - 查询旁站的脚本](/2018/05/29/ReIPdog/ "ReIPdog - 查询旁站的脚本")
[WLANSniffer](/2018/01/28/WlanSniffer/ "WLANSniffer")
[parselmouth 介绍](/2024/03/04/parselmouth/ "parselmouth 介绍")
[书蜗抢座爬虫](/2017/08/09/SwSpider/ "书蜗抢座爬虫")
[伪造电子邮件以及制造电子邮件炸弹的攻防探讨](/2018/09/26/email-hacker/ "伪造电子邮件以及制造电子邮件炸弹的攻防探讨")
[利用书蜗自动续借图书](/2017/08/09/SwRenew/ "利用书蜗自动续借图书")
[模拟退火之 TSP 问题](/2017/06/02/FireTSP/ "模拟退火之 TSP 问题")
[模拟退火之函数最值](/2017/06/03/FireFunction/ "模拟退火之函数最值")
[More...](/categories/%E7%9F%A5%E8%AF%86%E8%BE%93%E5%87%BA/)

# 用 Python 手搓 runc 的踩坑之旅

本文最后更新于：3 个月前

本篇是云原生安全系列的开篇

正如 2024 年度总结里说的，今年要开启云原生安全系列，本篇是云原生安全系列的开篇。老规矩，系列开篇第一期，扯点闲话。云计算真的是一个很大的概念，这是一个很大的坑，我也不知道什么时候能填完。

![](https://rzx1szyykpugqc-1252075454.piccd.myqcloud.com/用Python手搓runc的踩坑之旅/58ec387e-9fb9-4624-ad60-e6cba6ba2c23.png!blog#width-zoom4)

我决定从容器化技术开始。说起容器，docker（准确地说是 runc）绝对是核心组件。对于 docker，我大概是在大学期间接触到的，当时毕设的课题还是一个基于 docker 的分布式安全演练靶场，那个时候主要是以使用为主，对于容器技术只有朦朦胧胧的了解。不过在那个时候，除了阿里云等几家云厂商之外，国内落地大规模容器化架构的公司还是比较少的，关于云安全的技术研究也不多。时过境迁，现在来看，容器化技术已经遍地开花，企业上云逐渐变得非常常见。

在看完容器技术的核心 3 个基础技术之后：

* [Linux 基础-Namespace](https://www.tr0y.wang/2025/03/03/linux-namespace/)
* [Linux 基础-CGroup](https://www.tr0y.wang/2025/03/07/linux-cgroup/)
* [Linux 基础-Union File System](https://www.tr0y.wang/2025/03/11/linux-unionfs/)

最近我一直在琢磨，能不能自己写一个 runc 出来？即使是一个玩具化的实现，也要比只看概念强得多。runc 是用 go 写的，golang 我不太会，反正咱们写的就是玩具，就用我最熟悉的 Python 好了。

于是就有了本篇 —— 一个基于 Python 的 runc 实现 —— 麻雀虽小，五脏俱全。同时，这也是我的第一篇付费文章（折合约 10 块钱），希望有余力的橘友们多多支持（如果条件实在是比较困难，或者觉得文章写得不好，可以找我退钱）

好了，坐稳发车啦！

本篇是付费文章，[请移步](https://mp.weixin.qq.com/s/B_dHCDdMFe2_hucKMTLhKA)

事后评事易
事前做事难
加油橘友们！

---

[知识输出](/categories/%E7%9F%A5%E8%AF%86%E8%BE%93%E5%87%BA/)

[#Python](/tags/Python/)
[#云原生安全](/tags/%E4%BA%91%E5%8E%9F%E7%94%9F%E5%AE%89%E5%85%A8/)
[#linux](/tags/linux/)
[#付费](/tags/%E4%BB%98%E8%B4%B9/)

用 Python 手搓 runc 的踩坑之旅

https://www.tr0y.wang/2025/04/09/用Python手搓runc的踩坑之旅/

作者

Tr0y

发布于

2025年4月9日

更新于

2025年4月16日

许可协议

[走近 DMA — 三角洲里的天才少年
上一篇](/2025/06/26/dma/ "走近 DMA — 三角洲里的天才少年")

[SecMap - ReDos
下一篇](/2025/03/19/SecMap-ReDos/ "SecMap - ReDos")

Please enable JavaScript to view the comments

目录

#### 搜索

×

关键词

[Hexo](https://hexo.io)  [Fluid](https://github.com/fluid-dev/hexo-theme-fluid)

总访问量
次

总访客数
人

博客在允许 JavaScript 运行的环境下浏览效果更佳