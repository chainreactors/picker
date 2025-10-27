---
title: 恶意程序将家用路由器变成黑客组织的代理服务器
url: https://www.solidot.org/story?sid=74987
source: 奇客Solidot–传递最新科技情报
date: 2023-05-18
fetch_date: 2025-10-04T11:40:04.579077
---

# 恶意程序将家用路由器变成黑客组织的代理服务器

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

**本文已被查看 7821 次**

## 恶意程序将家用路由器变成黑客组织的代理服务器

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年05月17日 23时46分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74987&appkey=1370085986&title=%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F%E5%B0%86%E5%AE%B6%E7%94%A8%E8%B7%AF%E7%94%B1%E5%99%A8%E5%8F%98%E6%88%90%E9%BB%91%E5%AE%A2%E7%BB%84%E7%BB%87%E7%9A%84%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自计算群星**

安全公司 Check Point Research 报告了一种伪装成 TP-Link 路由器固件的恶意程序，包含了完整的后门功能，允许攻击者和被感染设备建立通信和文件传输，远程发送指令，上传、下载和删除文件。恶意程序的主要目的被认为是充当代理掩盖通信来源。Check Point Research 发现其指令控制基础设施由 APT 组织 Mustang Panda 控制。Check Point 推荐路由器用户检查是否连接域名 m.cremessage[.com]，管理面板中是否有修改过的升级固件，是否存在 /vat/udhcp.cnf、/var/udhcp 和 .remote\_shell.log 等文件。如果存在那么路由器很可能被感染了。TP-Link 尚未对此报告发表评论。
https://research.checkpoint.com/2023/the-dragon-who-sold-his-camaro-analyzing-custom-router-implant/

﻿

工欲善其事，必先利其器。居是邦，事其大夫之贤者，友其士之仁者。

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