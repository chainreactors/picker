---
title: 黑客的新后门程序利用了 MQTT 协议
url: https://www.solidot.org/story?sid=74296
source: 奇客Solidot–传递最新科技情报
date: 2023-03-04
fetch_date: 2025-10-04T08:39:09.228745
---

# 黑客的新后门程序利用了 MQTT 协议

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

**本文已被查看 6846 次**

## 黑客的新后门程序利用了 MQTT 协议

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年03月03日 23时17分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74296&appkey=1370085986&title=%E9%BB%91%E5%AE%A2%E7%9A%84%E6%96%B0%E5%90%8E%E9%97%A8%E7%A8%8B%E5%BA%8F%E5%88%A9%E7%94%A8%E4%BA%86%20MQTT%20%E5%8D%8F%E8%AE%AE "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自月球人**

安全公司 ESET 报告，黑客组织 Mustang Panda aka TA416 和 Bronze President 部署了一种新的后门程序 MQsTTang。恶意程序主要通过钓鱼邮件传播，通过一个 GitHub 软件库下载负荷，它会在注册表增加一个启动时运行的注册表项去实现持久存在。为了躲避监测它利用了 MQTT 协议去进行指令通信。MQsTTang 还会检查主机上是否存在调试器或监控工具，如果有发现，它会相应的改变行为。
https://www.welivesecurity.com/2023/03/02/mqsttang-mustang-panda-latest-backdoor-treads-new-ground-qt-mqtt/

﻿

在这个世界上我只确定一件事。那就是人确定的事情越少越好。--毛姆

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