---
title: Claude Code for VS Code 官方扩展被植入后门
url: https://www.solidot.org/story?sid=85756
source: 奇客Solidot–传递最新科技情报
date: 2026-10-30
fetch_date: 2026-10-31T07:46:59.517009
---

# Claude Code for VS Code 官方扩展被植入后门

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261030)
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

**本文已被查看 3079 次**

## Claude Code for VS Code 官方扩展被植入后门

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年10月30日 21时43分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85756&appkey=1370085986&title=Claude%20Code%20for%20VS%20Code%20%E5%AE%98%E6%96%B9%E6%89%A9%E5%B1%95%E8%A2%AB%E6%A4%8D%E5%85%A5%E5%90%8E%E9%97%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自人猿泰山之地心营救**

安全研究人员在 Cursor Marketplace 的 Claude Code for VS Code 官方扩展中发现了后门，该恶意版本已经撤下，攻击者也关闭了其服务器。Cursor 已发布安全公告，但 Claude Code 开发商 Anthropic 尚未做出任何声明。受影响的版本是 Anthropic.claude-code 2.1.313，共上线了大约 11 小时，受影响用户估计有 5,000 名，该扩展会试图植入一个持久 SSH 后门。恶意扩展会：收集主机和用户信息：主机名、用户名、操作系统、架构、主目录路径、环境变量名称、工作目录、已配置的 Git 邮箱以及公网 IP。尝试将攻击者控制的 SSH 键添加到 authorized\_keys，启用本地 SSH 服务，并建立反向 SSH 隧道。由于恶意代码存在 bug，除非 Cursor 是以管理员权限启动的 (这种情况极为罕见) ，否则这一步会失败。尝试通过 LaunchAgent (macOS) 或计划任务 (Windows，该任务会尝试以 SYSTEM 身份运行，并以启动脚本作为回退) 使反向 SSH 隧道长期生效。后台脚本大约每 60 秒重试一次建立隧道。通过 HTTP POST 将主机详情和后门状态上报至 8099 端口上的 /beacon。如果用户是在 2026 年 10 月 29 日太平洋时间凌晨 2:27 至下午 1:35 之间，从 Cursor VS Code 扩展市场安装了 Anthropic.claude-code 2.1.313 或更新到该版本，那么需要检查下系统。
https://phorion.io/blog/offical-claude-code-vsx-compromise/
https://cursor.com/cn/blog/claude-code-extension-security-notice

[回复](/comments?sid=85756&op=reply&type=story)

﻿

自由的保证是什么?是对自己不再感到羞耻。——尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261030)
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