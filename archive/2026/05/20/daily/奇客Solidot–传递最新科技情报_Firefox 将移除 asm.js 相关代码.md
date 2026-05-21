---
title: Firefox 将移除 asm.js 相关代码
url: https://www.solidot.org/story?sid=84356
source: 奇客Solidot–传递最新科技情报
date: 2026-05-20
fetch_date: 2026-05-21T06:03:06.181035
---

# Firefox 将移除 asm.js 相关代码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260520)
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

**本文已被查看 1709 次**

## Firefox 将移除 asm.js 相关代码

[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")

[Edwards](/~Edwards) (42866)发表于 2026年05月20日 23时39分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84356&appkey=1370085986&title=Firefox%20%E5%B0%86%E7%A7%BB%E9%99%A4%20asm.js%20%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自快乐基因**

Mozilla 宣布 Firefox 未来将移除 asm.js 相关代码，因为它早有了后继者 WebAssembly，同时维护两者耗费时间且增加攻击面。asm.js 是 Mozilla 对 NaCl 和 PNaCl 的回应：通过选择一个严格静态的 JavaScript 子集获得类似 NaCl/PNaCl 的性能，同时代码又能直接运行在 Web 内容中。asm.js 于 2013 年随 Firefox 22 发布，获得了巨大的成功，证明只使用 Web 技术就能在 Web 上以接近原生的速度运行代码，它为 WebAssembly 的诞生铺平了道路，WebAssembly 在 2019 年成为 W3C 标准。Mozilla 从 Firefox 148 开始 JS 引擎 SpiderMonkey 默认禁用 asm.js 优化，未来版本将完全移除相关代码，使用 asm.js 的网站不会受到影响，开发者建议想要继续使用 asm.js 发布内容的网站重编译到 WebAssembly，它的执行速度更快，二进制文件更小。
https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html

[回复](/comments?sid=84356&op=reply&type=story)

﻿

与魔鬼战斗的人，应当小心自己不要成为魔鬼。当你远远凝视深渊时，深渊也在凝视你。——尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260520)
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