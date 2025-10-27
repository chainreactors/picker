---
title: 祛魅 SMPC 和它的威胁模型
url: https://www.solidot.org/story?sid=74114
source: 奇客Solidot–传递最新科技情报
date: 2023-02-14
fetch_date: 2025-10-04T06:31:56.761557
---

# 祛魅 SMPC 和它的威胁模型

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251003)
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

**本文已被查看 5720 次**

## 祛魅 SMPC 和它的威胁模型

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年02月13日 13时28分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74114&appkey=1370085986&title=%E7%A5%9B%E9%AD%85%20SMPC%20%E5%92%8C%E5%AE%83%E7%9A%84%E5%A8%81%E8%83%81%E6%A8%A1%E5%9E%8B "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自美丽新世界**

Shawn the R0ck 写道：*安全多方计算（Secure multi-party computation，简称MPC或者SMPC）起源于 A. Shamir, R. Rivet and L. Adleman 在1979年对于秘密分割问题的研究，其后姚期智（Andrew Yao）于 1982 年提出百万富翁问题和于 1986 年正式提出的 Garbled Circuit Protocol,成为了今天意义上多方计算的基础，Web3.0 的兴起让业界关注使用多方计算解决资产管理和跨链等场景的问题，SMPC 在多台计算节点之间分配签名过程，每台计算机都拥有一份代表密钥份额的私有数据，它们共同合作以分布式方式签署交易以降低单点失败的风险，但实际情况是这样吗？HardenedVault 的 Vault Labs 近期针对 SMPC 中安全假设，Oblivious transfer，同态加密，零知识证明，Shamir 秘密分割，Feldman-VSS，Paillier算法，EdDSA以及MPC-CMP等SMPC的主要特性进行了分析，以此为基础得出以下结论：1）建立合理威胁模型的前提是SMPC实现本身遵循密码学最佳实践。2）有一些厂商宣称的SMPC方案是去中心化的，但实际上是基于特权设置不仅会导致单点失败风险，而且可以让攻击者具备制造假签名的能力，用户需要仔细确认技术参数。3）即使没有特权节点，SMPC也并不能一劳永逸的解决单点失败风险的问题，因为系统安全问题依旧存在。4）没有银弹，高度依赖TEE（可信执行环境）并不是理性的选择，魔鬼在细节中。*
https://hardenedvault.net/blog/2023-02-02-smpc/
https://github.com/hardenedvault/bootkit-samples

﻿

在b进位制中，以数n起头的数出现的机率为logb(n + 1) − logb(n)--本福特定律

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251003)
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