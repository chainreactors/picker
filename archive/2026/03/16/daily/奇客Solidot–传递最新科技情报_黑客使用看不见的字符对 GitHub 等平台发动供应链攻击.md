---
title: 黑客使用看不见的字符对 GitHub 等平台发动供应链攻击
url: https://www.solidot.org/story?sid=83776
source: 奇客Solidot–传递最新科技情报
date: 2026-03-16
fetch_date: 2026-03-17T04:15:53.410889
---

# 黑客使用看不见的字符对 GitHub 等平台发动供应链攻击

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260316)
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

**本文已被查看 1852 次**

## 黑客使用看不见的字符对 GitHub 等平台发动供应链攻击

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年03月16日 13时48分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83776&appkey=1370085986&title=%E9%BB%91%E5%AE%A2%E4%BD%BF%E7%94%A8%E7%9C%8B%E4%B8%8D%E8%A7%81%E7%9A%84%E5%AD%97%E7%AC%A6%E5%AF%B9%20GitHub%20%E7%AD%89%E5%B9%B3%E5%8F%B0%E5%8F%91%E5%8A%A8%E4%BE%9B%E5%BA%94%E9%93%BE%E6%94%BB%E5%87%BB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自外星人**

安全公司 Aikido Security 的研究人员报告了对 GitHub 等平台发动的新供应链攻击。攻击者使用不可见的 Unicode 字符上传了 151 个恶意包，这些字符在编辑器等界面对人眼不可见，但能被机器阅读，并能执行其恶意指令。安全研究人员将该组织命名为 Glassworm，认为攻击者使用大模型生成了不同项目的软件包。不可见字符使用 Public Use Areas(aka Public Use Access)渲染，是 Unicode 标准中用于定义表情符号、旗帜等特殊字符的私有字符代码点。当输入计算机时，这些代码点的输出对人类完全不可见，只能看到空白或空行，但对 JavaScript 解释器而言，这些代码点会被转换为可执行代码。
https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode
https://arstechnica.com/security/2026/03/supply-chain-attack-using-invisible-code-hits-github-and-other-repositories/

[回复](/comments?sid=83776&op=reply&type=story)

﻿

我并不同意你的观点，但是我誓死捍卫你说话的权利——伏尔泰

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260316)
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