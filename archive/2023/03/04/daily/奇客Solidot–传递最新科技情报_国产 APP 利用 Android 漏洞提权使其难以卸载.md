---
title: 国产 APP 利用 Android 漏洞提权使其难以卸载
url: https://www.solidot.org/story?sid=74293
source: 奇客Solidot–传递最新科技情报
date: 2023-03-04
fetch_date: 2025-10-04T08:39:10.077482
---

# 国产 APP 利用 Android 漏洞提权使其难以卸载

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

**本文已被查看 12475 次**

## 国产 APP 利用 Android 漏洞提权使其难以卸载

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年03月03日 20时07分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74293&appkey=1370085986&title=%E5%9B%BD%E4%BA%A7%20APP%20%E5%88%A9%E7%94%A8%20Android%20%E6%BC%8F%E6%B4%9E%E6%8F%90%E6%9D%83%E4%BD%BF%E5%85%B6%E9%9A%BE%E4%BB%A5%E5%8D%B8%E8%BD%BD%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自遥远地球之歌**

国内的一个独立安全研究机构 DarkNavy 发表文章披露，国内一家互联网巨头的 APP 利用了 Android 系统漏洞提权使其难以卸载。报道没有公开相关公司的名字，但称得上巨头也就那四五家公司。报道称，该 APP 首先利用了多个厂商 OEM 代码中的反序列化漏洞提权，提权控制手机系统之后，该 App 即开启了一系列的违规操作，绕过隐私合规监管，大肆收集用户的隐私信息（包括社交媒体账户资料、位置信息、Wi-Fi 信息、基站信息甚至路由器信息等）。之后，该 App 利用手机厂商 OEM 代码中导出的 root-path FileContentProvider， 进行 System App 和敏感系统应用文件读写；进而突破沙箱机制、绕开权限系统改写系统关键配置文件为自身保活，修改用户桌面(Launcher)配置隐藏自身或欺骗用户实现防卸载；随后，还进一步通过覆盖动态代码文件的方式劫持其他应用注入后门执行代码，进行更加隐蔽的长期驻留；甚至还实现了和间谍软件一样的遥控机制，通过远端“云控开关”控制非法行为的启动与暂停，来躲避检测。
https://mp.weixin.qq.com/s/P\_EYQxOEupqdU0BJMRqWsw

﻿

计算机没什么用。他们只会告诉你答案。--毕加索

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