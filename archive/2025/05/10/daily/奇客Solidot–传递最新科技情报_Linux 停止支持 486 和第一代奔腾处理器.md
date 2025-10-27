---
title: Linux 停止支持 486 和第一代奔腾处理器
url: https://www.solidot.org/story?sid=81251
source: 奇客Solidot–传递最新科技情报
date: 2025-05-10
fetch_date: 2025-10-06T22:29:55.868299
---

# Linux 停止支持 486 和第一代奔腾处理器

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

**本文已被查看 26064 次**

## Linux 停止支持 486 和第一代奔腾处理器

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")

[Wilson](/~Wilson) (42865)发表于 2025年05月09日 23时50分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81251&appkey=1370085986&title=Linux%20%E5%81%9C%E6%AD%A2%E6%94%AF%E6%8C%81%20486%20%E5%92%8C%E7%AC%AC%E4%B8%80%E4%BB%A3%E5%A5%94%E8%85%BE%E5%A4%84%E7%90%86%E5%99%A8%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自千与千寻**

即将发布的 Linux 6.15 将停止支持有 36 年历史的 486 以及第一代奔腾处理器。微软早在 2001 年发布 Windows XP 后就停止了对 486 的支持。Linux 作者 Linus Torvalds 在内核邮件列表上表示是时候放弃支持 i486 了，不值得在 i486 上浪费开发精力。资深内核开发者 Ingo Molnar 解释说，为了支持已经很少有人使用的旧 x86-32 架构，内核开发者花费了很多力气去实现兼容性。这种兼容性粘合常常会带来需要大量精力解决的问题，这些时间本可以做其它事情。Linux 是在 2012 年停止支持 386。未来对 x86 CPU 的支持最低将是 P5 微架构的奔腾处理器。
修正：
风之影 写道：*Intel 80486处理器发布于1989年。486处理器缺少CX8（CMPXCHG8B）指令和TSC（时间戳计数器），为了支持486处理器，操作系统必须包含模拟CX8和TSC的逻辑，这带来了额外的维护工作。Linus Torvalds在2022年曾提议停止支持486处理器，但被投票否决了。近期，Linus Torvalds再次提议放弃对486处理器的支持，随后，内核老将Ingo Molnar提交了一组补丁，移除了对缺少CX8和TSC功能的CPU的支持。受影响的处理器除486以外，还包括部分早期的586处理器，如AMD K5和Elan系列、Cyrix的5x86/6x86/6x86MX、IDT的WinChip系列等。早在2012年的Linux 3.8中，就是Ingo Molnar编写的补丁终止了支持386处理器。

386和486处理器可用于嵌入式系统、工业电脑和航天领域，二者持续生产到了2007年才停产，但若停止支持486处理器的补丁获准通过，并不会对此产生影响，这是因为嵌入式系统使用的486处理器（如Intel Quark）支持CX8和TSC，而更原始的486处理器则搭载旧版Linux。

Windows操作系统早在2001年的Windows XP就因为要求CX8而停止支持486处理器。*
ZDNet: Linux drops support for 486 and early Pentium processors - 20 years after Microsoft

﻿

如果你想走到高处，就要使用自己的两条腿！不要让别人把你抬到高处；不要坐在别人的背上和头上。 --尼采·F.W.

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