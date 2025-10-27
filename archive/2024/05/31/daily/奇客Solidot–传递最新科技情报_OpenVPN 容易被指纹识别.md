---
title: OpenVPN 容易被指纹识别
url: https://www.solidot.org/story?sid=78306
source: 奇客Solidot–传递最新科技情报
date: 2024-05-31
fetch_date: 2025-10-06T16:51:00.632626
---

# OpenVPN 容易被指纹识别

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

**本文已被查看 6557 次**

## OpenVPN 容易被指纹识别

[![审查](https://icon.solidot.org/images/topics/topicCensorship.png?123)](/search?tid=120 "审查")

[Wilson](/~Wilson) (42865)发表于 2024年05月30日 14时23分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78306&appkey=1370085986&title=OpenVPN%20%E5%AE%B9%E6%98%93%E8%A2%AB%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自被掩埋的巨人**

ISP、广告商和政府日益破坏、操纵和监视网络流量，VPN 的普及率因此大幅增长。为了应对 VPN 的流行，ISP 和政府都在设法跟踪和阻止 VPN 流量，以确保网络流量的可见性和对其的控制。方滨兴形容这一情况为“永恒之战”。印度和俄罗斯最近也都以国家网络安全的理由禁止使用 VPN。OpenVPN 是最流行的 VPN 协议，研究人员在 CACM 期刊（《美国计算机学会通讯》）上发表论文，分析了 OpenVPN 的指纹识别能力，寻求回答两个疑问：(1) ISP 和政府能否实时识别 OpenVPN 流量？(2) 能否不会因误报而造成附带损害？他们模仿了防火长城的架构，与一家地区 ISP 合作，通过镜像流量识别其中的 VPN 连接。结果显示，OpenVPN 非常容易被指纹识别，即使使用了混淆层加密 OpenVPN 流量也无法隐藏指纹。研究人员称，绝大多数 OpenVPN 流量和服务容易遭到被动过滤和主动探测。top10vpn.com 排名前 10 的 VPN 服务有 8 家使用了某种形式的混淆服务，但由于加密不足和数据包长度混淆不足，所有这些流量都能被标记为可疑流量。研究人员建议 VPN 服务商采用更有弹性和标准化的混淆方法。
https://cacm.acm.org/research/openvpn-is-open-to-vpn-fingerprinting/

﻿

谁能最恰当地评价一个人，他的敌人还是他自己？

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