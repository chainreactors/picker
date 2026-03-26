---
title: PyPI 库中的 LiteLLM 遭到入侵植入恶意代码
url: https://www.solidot.org/story?sid=83865
source: 奇客Solidot–传递最新科技情报
date: 2026-03-25
fetch_date: 2026-03-26T04:30:37.876217
---

# PyPI 库中的 LiteLLM 遭到入侵植入恶意代码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260325)
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

**本文已被查看 1908 次**

## PyPI 库中的 LiteLLM 遭到入侵植入恶意代码

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年03月25日 15时27分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83865&appkey=1370085986&title=PyPI%20%E5%BA%93%E4%B8%AD%E7%9A%84%20LiteLLM%20%E9%81%AD%E5%88%B0%E5%85%A5%E4%BE%B5%E6%A4%8D%E5%85%A5%E6%81%B6%E6%84%8F%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自影舞**

LiteLLM 项目维护者账号被盗，黑客向 PyPI 软件库发布了两个嵌入恶意代码的版本 v1.82.7 和 v1.82.8。恶意代码旨在窃取凭证，包括 SSH 密钥、云服务凭证、加密钱包等。任何安装了恶意版本的用户需要立即检查是否遭到入侵。恶意文件 litellm\_init.pth 会在每次 Python 进程启动时自动执行。项目维护者称账号被盗源于刚刚爆出的 trivy 漏洞，恶意版本都已从 PyPI 上移除，所有维护者帐户都已更改。
https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/
https://github.com/BerriAI/litellm/issues/24512
https://news.ycombinator.com/item?id=47501426

[回复](/comments?sid=83865&op=reply&type=story)

﻿

所谓科学的论辩，从总体上来说则是没有多大效果的，更不用说论辩几乎总是各持己见的这个事实。——弗洛伊德

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260325)
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