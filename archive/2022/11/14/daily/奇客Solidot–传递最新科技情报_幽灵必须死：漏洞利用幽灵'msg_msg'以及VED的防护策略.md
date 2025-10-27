---
title: 幽灵必须死：漏洞利用幽灵'msg_msg'以及VED的防护策略
url: https://www.solidot.org/story?sid=73351
source: 奇客Solidot–传递最新科技情报
date: 2022-11-14
fetch_date: 2025-10-03T22:41:06.551359
---

# 幽灵必须死：漏洞利用幽灵'msg_msg'以及VED的防护策略

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

**本文已被查看 7041 次**

## 幽灵必须死：漏洞利用幽灵'msg\_msg'以及VED的防护策略

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[WinterIsComing](/~WinterIsComing) (31822)发表于 2022年11月13日 22时23分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73351&appkey=1370085986&title=%E5%B9%BD%E7%81%B5%E5%BF%85%E9%A1%BB%E6%AD%BB%EF%BC%9A%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%E5%B9%BD%E7%81%B5%27msg_msg%27%E4%BB%A5%E5%8F%8AVED%E7%9A%84%E9%98%B2%E6%8A%A4%E7%AD%96%E7%95%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自神秘博士：侧影**

HardenedVault 写道 *"近年来不少针对Linux系统内核的漏洞利用攻击方式都会利用一个名为msg\_msg的神奇结构体作为利用早期阶段的部署展开，比如信息泄漏的攻击场景，对于系统安全的纵深防御体系越早的检测和阻断对于防御的一方越有利，赛博堡垒（HardenedVault）的Linux内核疫苗方案VED（Vault Exploit Defense）的一个2022版本的特性可以针对这种攻击方法免疫，并测试了主流的公开的漏洞利用。VED 维护了一个 msg\_msg 的列表，计算每个 msg\_msg 内容的 hash。 使用 msgrcv() 读取或释放struct msg\_msgseg next, size\_t m\_ts 和 void \*security' 被污染的 msg\_msg 将会被 VED 探测到。但是我们的检查并没有包含 stuct list\_head m\_list`， 这意味着如果该指针被污染并被释放，VED 并不能检查出来，因为他是由 msg\_queue 来维护的。
CVE-2021-22555: Turning \x00\x00 into 10000$ - Exploring struct msg\_msg 就是这样一个例子. 但 VED 使用其他办法来进行防御。VED 添加了越界读取的检查。如果说读取目标缓存的长度和读取长度是不匹配的， VED 就能检查到污染。在漏洞利用中’size\_t m\_ts’的污染较容易达成越界读取， 并且实现 KASLR 绕过或者泄漏堆地址。VED 的检查能够有效检查到越界读取， 但是这个防御也是不完整的，精心制作的 msg 仍可能绕过。比如说， 存在 UAF/double free 漏洞的结构体，msg\_msg 结构体，需要泄漏目标结构体， 三者的长度都是一致的，仍可以绕过 VED 的检查。

这两个缓解措施均是可被绕过的，VED 目前的版本是基于 LKRG 实现的，检查的完整性与性能的平衡是需要考虑的。更加严密的 msg 是可能的，但是 kprobe 的检查点数量，计算量需要多的多。另外则是虽然这两个缓解措施均可被绕过，但是叠加两者，由于其中的检查是相互交叉的，比方说完整性检查包含的 struct msg\_msgseg \*next, size\_t m\_ts，和越界检查。这使得漏洞利用需要依赖于原代码路径来实现堆喷，和更依赖同类型的 object 之间的污染，使得 msg 的漏洞利用困难程度上升。当然这些专门的绕过对资深的内核黑客来说不会是多大的问题。VED 也在探索更加完整并且平衡性能损耗的方案。"*http://https://hardenedvault.net/blog/2022-11-13-msg\_msg-recon-mitigation-ved/

﻿

实现明天理想的唯一障碍是今天的疑虑。

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