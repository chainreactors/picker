---
title: 如何让 AMD Zen CPU 总是生成 4 作为随机数
url: https://www.solidot.org/story?sid=80513
source: 奇客Solidot–传递最新科技情报
date: 2025-02-11
fetch_date: 2025-10-06T20:38:23.540831
---

# 如何让 AMD Zen CPU 总是生成 4 作为随机数

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251005)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 6875 次**

## 如何让 AMD Zen CPU 总是生成 4 作为随机数

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年02月10日 13时52分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80513&appkey=1370085986&title=%E5%A6%82%E4%BD%95%E8%AE%A9%20AMD%20Zen%20CPU%20%E6%80%BB%E6%98%AF%E7%94%9F%E6%88%90%204%20%E4%BD%9C%E4%B8%BA%E9%9A%8F%E6%9C%BA%E6%95%B0 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自红女王**

Google 研究人员披露了 AMD Zen CPU 的微码签名验证漏洞，该漏洞允许有本地管理员权限的攻击者加载恶意 CPU 微码，能根据需要改变芯片的行为，突破芯片保护措施如最新版本的 AMD Secure Encrypted Virtualization、SEV-SNP 或 Dynamic Root of Trust Measurement。Google 研究人员在演示中利用修改后的微码让 AMD Zen CPU 总是生成 4 作为随机数。4 随机数出自 XKCD 漫画。研究人员演示的概念验证攻击针对的平台包括了基于 Milan 的 Epyc 服务器芯片和基于 Phoenix 的 Ryzen 9 桌面处理器。Google 于 2024 年 9 月 25 日向 AMD 报告了漏洞。AMD 于 2024 年 12 月 17 日向其客户提供了补丁。鉴于供应链的复杂性，Google 在 131 天后才公开漏洞。
GitHub/Google AMD: Microcode Signature Verification Vulnerability
XKCD/221 Random Number

﻿

通往地狱的路，都是由善意铺成的——哈耶克

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251005)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>