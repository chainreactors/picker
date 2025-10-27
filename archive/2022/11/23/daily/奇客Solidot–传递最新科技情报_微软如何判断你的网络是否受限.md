---
title: 微软如何判断你的网络是否受限
url: https://www.solidot.org/story?sid=73443
source: 奇客Solidot–传递最新科技情报
date: 2022-11-23
fetch_date: 2025-10-03T23:30:08.406411
---

# 微软如何判断你的网络是否受限

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

**本文已被查看 7841 次**

## 微软如何判断你的网络是否受限

[![Windows](https://icon.solidot.org/images/topics/topicwindows.png?123)](/search?tid=33 "Windows")

[WinterIsComing](/~WinterIsComing) (31822)发表于 2022年11月22日 15时29分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73443&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E5%A6%82%E4%BD%95%E5%88%A4%E6%96%AD%E4%BD%A0%E7%9A%84%E7%BD%91%E7%BB%9C%E6%98%AF%E5%90%A6%E5%8F%97%E9%99%90 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自西塔甘达**

微软是如何判断你的网络是否受限？微软资深软件工程师、《The Old New Thing》作者 Raymond Chen 解释说，根据你的 Windows 版本而定，系统会尝试从一个专门的 Web 服务器上下载文件，可能是 http://www.msftncsi.com/ncsi.txt 或 http://www.msftconnecttest.com/connecttest.txt，如果下载成功而且包含正确的内容，Windows 会认为你拥有完整的互联网接入。如果出错了，根据错误它会认为能访问受限制或无互联网接入。
https://devblogs.microsoft.com/oldnewthing/20221115-00/?p=107399

﻿

一个人能够洋洋得意地随著军乐队在四列纵队里行进，单凭这一点就足以使我对他轻视。他所以长了一个大脑，只是出于误会；单单一根脊髓就可满足他的全部需要了。文明国家的这种罪恶的渊薮，应当尽快加以消灭。由命令而产生的勇敢行为，毫无意义的暴行，以及在爱国主义名义下一切可恶的胡闹，所有这些都使我深恶痛绝。——爱因斯坦

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