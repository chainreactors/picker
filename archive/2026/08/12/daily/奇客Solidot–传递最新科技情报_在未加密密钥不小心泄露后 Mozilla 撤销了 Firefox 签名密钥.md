---
title: 在未加密密钥不小心泄露后 Mozilla 撤销了 Firefox 签名密钥
url: https://www.solidot.org/story?sid=85066
source: 奇客Solidot–传递最新科技情报
date: 2026-08-12
fetch_date: 2026-08-13T04:04:02.531845
---

# 在未加密密钥不小心泄露后 Mozilla 撤销了 Firefox 签名密钥

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260812)
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

**本文已被查看 2120 次**

## 在未加密密钥不小心泄露后 Mozilla 撤销了 Firefox 签名密钥

[![Mozilla](https://icon.solidot.org/images/topics/topicmozilla.png?123)](/search?tid=29 "Mozilla")
[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")

[Edwards](/~Edwards) (42866)发表于 2026年08月12日 13时41分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85066&appkey=1370085986&title=%E5%9C%A8%E6%9C%AA%E5%8A%A0%E5%AF%86%E5%AF%86%E9%92%A5%E4%B8%8D%E5%B0%8F%E5%BF%83%E6%B3%84%E9%9C%B2%E5%90%8E%20Mozilla%20%E6%92%A4%E9%94%80%E4%BA%86%20Firefox%20%E7%AD%BE%E5%90%8D%E5%AF%86%E9%92%A5%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自平行恋人**

Mozilla 披露，它的 Firefox 和 Thunderbird 签名密钥的未加密版本不小心被人递交到了一个不公开的 GitHub 代码库里，该代码库只有少数员工才能访问，而相关员工早已通过其它方式获得密钥的访问授权。尽管如此，将未加密签名私钥保留在源代码控制系统中不是好的做法，因此 Mozilla 撤销了密钥。相关密钥被用于给 Firefox 和 Thunderbird 的 Linux tarball、RPM 包以及校验和文件进行签名。Mozilla 表示，它的调查未发现密钥被未经授权第三方访问的证据。对于密钥更换，大多数 Firefox 和 Thunderbird 用户无需任何操作，但手动验证 Mozilla GPG 签名的用户需要导入新的签名密钥以及旧密钥的撤销信息。
https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/
https://www.theregister.com/security/2026/08/11/mozilla-revokes-firefox-signing-key-after-unencrypted-copy-lands-in-github/5285908

[回复](/comments?sid=85066&op=reply&type=story)

﻿

我不像你一样是一个机器人，让磁盘把我淹没，除非它们是小甜饼，并且只在嘴里。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260812)
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