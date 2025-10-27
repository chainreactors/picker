---
title: 韩国黑客利用 WPS Office 0day 部署恶意程序
url: https://www.solidot.org/story?sid=79106
source: 奇客Solidot–传递最新科技情报
date: 2024-08-30
fetch_date: 2025-10-06T18:04:59.200908
---

# 韩国黑客利用 WPS Office 0day 部署恶意程序

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

**本文已被查看 6412 次**

## 韩国黑客利用 WPS Office 0day 部署恶意程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年08月29日 14时53分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79106&appkey=1370085986&title=%E9%9F%A9%E5%9B%BD%E9%BB%91%E5%AE%A2%E5%88%A9%E7%94%A8%20WPS%20Office%200day%20%E9%83%A8%E7%BD%B2%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自阿尔法计划**

韩国黑客组织 APT-C-60 利用了 Windows 版 WPS Office 的一个 0day 在目标设备上安装后门 SpyGlace。WPS 是金山开发的办公软件，在全球有逾 5 亿活跃用户。黑客利用的 0day 被称为 CVE-2024-7262，影响版本从 12.2.0.13110（2023 年 8 月）到 12.1.0.16412（2024 年 3 月）。金山在 3 月悄悄修复了漏洞，但没有向客户披露该漏洞正被活跃利用，促使安全公司 ESET 就该漏洞公布了一份详细报告。CVE-2024-7262 与软件如何处理自定义协议处理器的方式相关，其中 ksoqing:// 允许文档中嵌入的特制 URL 执行外部应用。APT-C-60 创建了 MHTML 文件，嵌入了隐藏在诱饵图像下的恶意超链接，引诱受害者点击图像触发漏洞。金山修复 CVE-2024-7262 的补丁并不完整，ESET 研究人员发现了第二个任意代码执行的高危漏洞 CVE-2024-7263。金山在 5 月修复了新的漏洞。为修复这两个漏洞 WPS 用户需要尽可能快的升级到 v12.2.0.17119 及以上版本。
https://www.bleepingcomputer.com/news/security/apt-c-60-hackers-exploited-wps-office-zero-day-to-deploy-spyglace-malware/
https://www.welivesecurity.com/en/eset-research/analysis-of-two-arbitrary-code-execution-vulnerabilities-affecting-wps-office/

﻿

没有人足够完美，以至可以未经别人同意就支配别人。--林肯

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