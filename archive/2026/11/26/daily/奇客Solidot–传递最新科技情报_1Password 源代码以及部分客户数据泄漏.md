---
title: 1Password 源代码以及部分客户数据泄漏
url: https://www.solidot.org/story?sid=85995
source: 奇客Solidot–传递最新科技情报
date: 2026-11-26
fetch_date: 2026-11-27T10:16:32.097024
---

# 1Password 源代码以及部分客户数据泄漏

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261126)
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

**本文已被查看 3476 次**

## 1Password 源代码以及部分客户数据泄漏

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年11月26日 15时15分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85995&appkey=1370085986&title=1Password%20%E6%BA%90%E4%BB%A3%E7%A0%81%E4%BB%A5%E5%8F%8A%E9%83%A8%E5%88%86%E5%AE%A2%E6%88%B7%E6%95%B0%E6%8D%AE%E6%B3%84%E6%BC%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自夏日永别**

密码管理器 1Password 披露了一起安全事件：2026 年 11 月 19 日黑客入侵了该公司一名员工的企业 GitHub 账户，访问了源代码，向后端服务推送恶意代码，下载了客户相关的管理数据。泄漏的数据包括了客户姓名和电子邮件地址；账户及用户标识符、账户创建时间和最后登录时间；公钥（本身就是公开的），Secure Remote Password 协议参数；邀请、配置及账户恢复邮件链接中的令牌，以及其它非机密账户元数据。1Password 称，黑客拷贝了私有库的源代码，访问了其 CI/CD 系统。源代码不包含任何用户机密信息，CI/CD 系统中包含了与基础设施相关的机密信息，它已对所有可能已泄露的凭据进行了轮换，向邮件令牌泄漏的用户发出了警告。1Password 称用户的密码库、主密码，以及私钥和账号恢复密钥都未受到影响。
https://1password.com/blog/update-on-nov-2026-security-incident

[回复](/comments?sid=85995&op=reply&type=story)

﻿

罗马帝国灭亡的其中一个主要原因是他们没有0 - 这样他们就没法给自己的C程序指明成功退出的路--Robert Firth

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261126)
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