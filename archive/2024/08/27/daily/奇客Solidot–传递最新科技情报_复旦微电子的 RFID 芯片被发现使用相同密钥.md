---
title: 复旦微电子的 RFID 芯片被发现使用相同密钥
url: https://www.solidot.org/story?sid=79077
source: 奇客Solidot–传递最新科技情报
date: 2024-08-27
fetch_date: 2025-10-06T18:06:01.576759
---

# 复旦微电子的 RFID 芯片被发现使用相同密钥

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

**本文已被查看 6007 次**

## 复旦微电子的 RFID 芯片被发现使用相同密钥

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年08月26日 19时13分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79077&appkey=1370085986&title=%E5%A4%8D%E6%97%A6%E5%BE%AE%E7%94%B5%E5%AD%90%E7%9A%84%20RFID%20%E8%8A%AF%E7%89%87%E8%A2%AB%E5%8F%91%E7%8E%B0%E4%BD%BF%E7%94%A8%E7%9B%B8%E5%90%8C%E5%AF%86%E9%92%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自人性分解**

法国安全服务公司 Quarkslab 的研究员 Philippe Teuwen 发现，复旦微电子集团制造的非接触式读卡器芯片使用了相同的密钥，允许在数分钟内克隆 RFID 智能卡，打开世界各地的房门。复旦微电子在 2020 年发布了用于门锁钥匙、小额支付、会员卡的 FM11RF08S，它使用了被称为“静态加密随机数（static encrypted nonce）”的方法，研究人员设计了一种攻击方法，如果 FM11RF08S 密钥在至少三张卡上重复使用，就能破解它。进一步研究发现，FM11RF08S 存在一个硬件后门——也就是所有卡使用的相同密钥。Teuwen 发现上一代的 FM11RF08 存在相似的后门但使用了不同的密钥，该密钥被发现被 FM11RF08、FM11RF32、FM1208-10，以及 NXP 和 Infineon 的部分卡使用。Quarkslab 督促世界各地的酒店检查其房卡使用的芯片，评估安全风险。
https://eprint.iacr.org/2024/1275.pdf
https://www.fmsh.com/7e67a741-a1ed-718d-15e3-83bdb6ecf4fa/

﻿

没有人足够完美，以至可以未经别人同意就支配别人。--林肯

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