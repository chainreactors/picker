---
title: 恶意应用利用开源工具伪造签名时间戳
url: https://www.solidot.org/story?sid=75516
source: 奇客Solidot–传递最新科技情报
date: 2023-07-15
fetch_date: 2025-10-04T11:54:02.770487
---

# 恶意应用利用开源工具伪造签名时间戳

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

**本文已被查看 7576 次**

## 恶意应用利用开源工具伪造签名时间戳

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年07月14日 19时33分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75516&appkey=1370085986&title=%E6%81%B6%E6%84%8F%E5%BA%94%E7%94%A8%E5%88%A9%E7%94%A8%E5%BC%80%E6%BA%90%E5%B7%A5%E5%85%B7%E4%BC%AA%E9%80%A0%E7%AD%BE%E5%90%8D%E6%97%B6%E9%97%B4%E6%88%B3 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自致命的发动机**

思科 Talos 安全团队发表了两篇博文，披露恶意应用在利用开源工具伪造签名时间戳，而这些恶意应用主要针对中文用户。从 Windows 10 v1607 开始，微软更新了驱动签名政策，不再允许未递交到 Developer Portal 签名的新内核模式驱动，但为了保持向后兼容，使用 2015 年 7 月 29 日之前颁发的最终实体证书签名的驱动程序将继续允许将链式链与受支持的交叉签名 CA 进行关联。这个例外制造了一个漏洞，允许新编译的驱动程序使用 2015 年 7 月 29 日之前颁发或过期的未撤销证书签名。有两个开源工具 HookSignTool 和 FuckCertVerifyTimeValidity 都允许伪造签名日期。主要针对中文用户的恶意程序利用这些开源工具使用窃取的证书进行签名，其中之一是 RedDriver。RedDriver 是一种基于驱动程序的浏览器劫持程序，使用 Windows Filtering Platform (WFP) 拦截浏览器流量，它利用 HookSignTool 伪造签名时间戳，它有一个硬编码的中文浏览器进程名单，针对的明显是中文用户，名单中包含了中国流行的浏览器，如 360 浏览器和 QQ 浏览器。
https://blog.talosintelligence.com/old-certificate-new-signature/
https://blog.talosintelligence.com/undocumented-reddriver/

﻿

任何人均有其价值

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