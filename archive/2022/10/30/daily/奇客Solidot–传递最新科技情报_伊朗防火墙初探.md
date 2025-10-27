---
title: 伊朗防火墙初探
url: https://www.solidot.org/story?sid=73208
source: 奇客Solidot–传递最新科技情报
date: 2022-10-30
fetch_date: 2025-10-03T21:19:41.110764
---

# 伊朗防火墙初探

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251002)
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

**本文已被查看 6915 次**

## 伊朗防火墙初探

[![审查](https://icon.solidot.org/images/topics/topicCensorship.png?123)](/search?tid=120 "审查")

[WinterIsComing](/~WinterIsComing) (31822)发表于 2022年10月29日 15时10分 星期六 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73208&appkey=1370085986&title=%E4%BC%8A%E6%9C%97%E9%98%B2%E7%81%AB%E5%A2%99%E5%88%9D%E6%8E%A2 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自记忆**

过去一个多月伊朗采用了物理断网和防火墙等手段限制网民访问互联网。物理断网比较罕见，基本没有办法绕过，但防火墙则有很多方法可以应对。对其防火墙的观察也可以了解其审查策略。伊朗政府在所有的出入境国际对等点都部署了 DPI（深度包检测），本地电信运营商有自己的防火墙，但大部分都是静态的，存在配置问题，只有小部分使用了 DPI。防火墙会将所有列入黑名单的域名解析到 IP 地址 10.0.34.35；它会持续扫描 Socks5 代理等服务；它很少完全屏蔽 IP 地址，而是通过丢弃 syn-ack 让 TCP 握手无法完成。伊朗政府是从下午四点到晚上 12 点之间限制访问互联网，众多的代理服务如 Tor 和 Wireguard/OpenVpn 都被屏蔽，DPI 会基于 TLS 的明文 SNI 执行封锁，在传输 1k-4k 之后所有出境流量会被屏蔽，
Cloudflare、Google Play 和 App Store 都被屏蔽，Docker 部分屏蔽，部分 ISP 采用了白名单制度屏蔽了其它所有网站。

参考：https://blog.thc.org/the-iran-firewall-a-preliminary-report

﻿

喜爱孤独者，非神即兽。--亚里士多德

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251002)
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