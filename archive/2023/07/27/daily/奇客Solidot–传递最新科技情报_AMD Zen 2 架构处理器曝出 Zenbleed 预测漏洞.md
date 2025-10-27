---
title: AMD Zen 2 架构处理器曝出 Zenbleed 预测漏洞
url: https://www.solidot.org/story?sid=75620
source: 奇客Solidot–传递最新科技情报
date: 2023-07-27
fetch_date: 2025-10-04T11:54:58.443701
---

# AMD Zen 2 架构处理器曝出 Zenbleed 预测漏洞

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

**本文已被查看 8118 次**

## AMD Zen 2 架构处理器曝出 Zenbleed 预测漏洞

[![AMD](https://icon.solidot.org/images/topics/topicamd.png?123)](/search?tid=22 "AMD")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年07月26日 17时09分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75620&appkey=1370085986&title=AMD%20Zen%202%20%E6%9E%B6%E6%9E%84%E5%A4%84%E7%90%86%E5%99%A8%E6%9B%9D%E5%87%BA%20Zenbleed%20%E9%A2%84%E6%B5%8B%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自造星主**

Google Project Zero 安全团队的 Tavis Ormandy 披露了 AMD Zen 2 架构处理器的 Zenbleed 漏洞(CVE-2023-20593)。该漏洞影响基于 Zen 2 的消费级、工作站和服务器处理器。漏洞允许攻击者从 CPU 寄存器窃取数据。现代处理器利用预测执行机制通过预测下一步的任务加速操作，Zen 2 处理器无法从特定类型的预测错误中正确恢复， Zenbleed 能利用该漏洞窃取敏感数据。它会导致 CPU 以每秒最高 30 KB 的速度泄露数据，其中包括加密密钥、root 和用户密码等敏感信息。该漏洞能被远程利用，恶意网站可通过加载 JS 触发。好消息是目前还没有观察到漏洞利用，但随着 Zenbleed 的披露情况可能会发生改变。修复该漏洞的微码已经释出，未更新的 Linux 用户需要尽快更新。
https://lock.cmpxchg8b.com/zenbleed.html

﻿

任何有可能出错的事将会出错--墨菲定理

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