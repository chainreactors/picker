---
title: AutoJack暗藏致命攻击链路，一个网页可劫持AI Agent执行任意代码
url: https://mp.weixin.qq.com/s/tONGl_6QUSn3aS1jj0jmjg
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:17.364425
---

# AutoJack暗藏致命攻击链路，一个网页可劫持AI Agent执行任意代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1bVibib7ibm2B6aRBTsfdxGP01Tu82Wica3bToqzCc7tdyQTcpDPkj9YKSG7t9cAafInNNicaTm0Izv8OMLI9MHEPV8m6JZr2u1LXM/0?wx_fmt=jpeg)

# AutoJack暗藏致命攻击链路，一个网页可劫持AI Agent执行任意代码

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3R21mrZo9icIJaFMx9ZGPLGISYJHZeibH19KWyAMvJF2NRvZw2ibCiblvta6T23ys1u0ibW4wucypWRk1swJAX84y4F6PT0IHRVnibc/640?wx_fmt=gif)

![AutoJack攻击示意图](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX13ezXP2dEsBndIV3zJD2jBa5ticfxibtlpVZZXpoaEczt3tnZib0UBjoibsicwcWGPvX5FUnFbsbx5Va77YBZBwLPgjBKmkUFuBr9w/640?wx_fmt=jpeg)

微软研究人员披露了一个名为AutoJack的攻击链，该漏洞可将AI浏览Agent转变为远程代码执行的载体。只需诱导Agent加载攻击者网页，该页面的JavaScript就能访问本地高权限服务并在主机上执行任意进程。整个过程无需凭证验证、无需登录界面，Agent加载页面后也无需额外用户交互——攻击者仅需通过植入链接、URL字段或提示词注入等方式使Agent打开网页即可。

Part01

漏洞根源与版本影响

该漏洞存在于AutoGen Studio——微软研究院AutoGen多Agent框架的开源原型界面中。值得注意的是，并非所有安装包都会受影响，版本差异至关重要：

* 通过pip install autogenstudio安装的稳定版0.4.2.2（微软审查版本）完全不包含Model Context Protocol（MCP）路由
* 但两个预发布版本（0.4.3.dev1和0.4.3.dev2）通过PyPI分发时携带了存在漏洞的MCP WebSocket处理程序

经Hacker News验证，这两个预发布版本中的MCP WebSocket路由存在以下问题：直接执行请求中的未经验证命令。虽然常规pip安装不会获取预发布版本（需显式使用--pre参数），但已安装预发布版本的用户仍面临风险——当前PyPI尚未发布包含主分支修复代码（GitHub提交b047730）的版本。

Part02

攻击链运作原理

![漏洞版本示意](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX16EaG1S13CVvXiblvy3rB3t2BfjoyfIdoFz6ib27v4lPqTqh8gqtrydICLEBPWvTZs0TP9fvMotqqDdiaYQnu53EXLsLbsKiaLfkI/640?wx_fmt=jpeg)

AutoJack攻击利用MCP WebSocket的三重缺陷：

三者结合，使得互联网页面通过本地Agent渲染后，能以AutoGen Studio运行账户权限执行攻击者指定命令。微软PoC演示中，"网页内容摘要Agent"在访问恶意URL时会触发开发者桌面弹出calc.exe计算器程序。

Part03

修复方案与缓解措施

![攻击链示意](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3gs0RQYHIMMyEs3PUWMgW3gFpmYrEvDkIkoKMl7GDVrXFAXje7lQ6VhvlqIbM8f11bDARJO6CgbnHmDfFkc5u9qYdLibMhNalI/640?wx_fmt=jpeg)

微软已通过提交b047730（PR #7362）修复主分支代码，新版本处理程序：

* 不再从URL直接读取命令参数
* 采用一次性会话ID进行服务端参数存储
* 强制MCP路由通过标准认证流程

当前应对方案：

* 稳定版0.4.2.2用户不受影响
* 预发布版本用户需手动拉取GitHub主分支b047730后提交代码
* 在官方修复版本发布前，建议将AutoGen Studio与浏览/代码执行Agent隔离运行：
* 避免两者共存于同一localhost环境
* 必要时采用容器/虚拟机隔离
* 使用低权限账户运行AutoGen Studio

Part04

行业警示

微软指出此类模式普遍存在于Agent框架中：过度授权的本地服务、将localhost验证作为安全边界、可加载不可信页面的Agent。类似问题近期已出现在ChatGPhish（ChatGPT钓鱼向量）和Semantic Kernel RCE（CVE-2026-26030、CVE-2026-25592）中。安全实践需超越简单的localhost检查，应实施控制平面认证、进程执行白名单机制，并为Agent分配独立于开发者会话的身份标识——当Agent既能浏览开放网络又能访问特权本地服务时，localhost已不能作为可信边界。

参考来源：

AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution

https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)**### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)**

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过