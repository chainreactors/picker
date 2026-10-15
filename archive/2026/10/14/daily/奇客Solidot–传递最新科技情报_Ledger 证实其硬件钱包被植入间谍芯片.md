---
title: Ledger 证实其硬件钱包被植入间谍芯片
url: https://www.solidot.org/story?sid=85604
source: 奇客Solidot–传递最新科技情报
date: 2026-10-14
fetch_date: 2026-10-15T06:44:17.178404
---

# Ledger 证实其硬件钱包被植入间谍芯片

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261014)
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

**本文已被查看 2841 次**

## Ledger 证实其硬件钱包被植入间谍芯片

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")
[![比特币](https://icon.solidot.org/images/topics/topicBitcoin.png?123)](/search?tid=149 "比特币")

[Edwards](/~Edwards) (42866)发表于 2026年10月14日 14时12分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85604&appkey=1370085986&title=Ledger%20%E8%AF%81%E5%AE%9E%E5%85%B6%E7%A1%AC%E4%BB%B6%E9%92%B1%E5%8C%85%E8%A2%AB%E6%A4%8D%E5%85%A5%E9%97%B4%E8%B0%8D%E8%8A%AF%E7%89%87 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自魔法集成**

提供硬件和软件钱包的 Ledger 公司证实由 CryptoBilis 经销的部分硬件钱包被植入间谍芯片，导致客户钱包里的加密货币被盗，它已经要求 CryptoBilis 停止销售硬件钱包。CryptoBilis 是一家总部位于马来西亚、业务遍及东南亚的大型硬件钱包零售商。CryptoBilis 经销的部分被篡改 Ledger X 钱包售价仅是原型号的一半，Tibane Labs 的安全研究人员对其进行的分析发现，原装电池被替换为体积更小的电池，以腾出空间安装恶意电路。该电池同时为间谍芯片和 Ledger X 供电。恶意电路是一颗基于 Arm Cortex-M4 架构、配备 128 KB 闪存以及采用 UFQFPN32 封装的 ST STM32G431KBU6 芯片，位于电池和天线下方。攻击者在微控制器单元（MCU）旁边安装了一个微型 eSIM，使用一个屏蔽式 LTE 模块发送信号。Tibane Labs 还发现攻击者使用了多个版本，第二种篡改的硬件钱包使用了原装电池供电，间谍芯片安装在 OLED 显示屏下方原本用于放置泡沫衬垫的空间内。攻击者利用间谍芯片通过 OCR 技术读取硬件钱包屏幕上显示的字体，在受害者设置过程中窃取密钥。
https://www.tibane.net/research/ledger-nano-x-implant

[回复](/comments?sid=85604&op=reply&type=story)

﻿

任何人均有其价值

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261014)
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