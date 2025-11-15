---
title: CSTIS：关于防范Morte僵尸网络的风险提示
url: https://www.4hou.com/posts/kgEY
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-14
fetch_date: 2025-11-15T03:07:28.812795
---

# CSTIS：关于防范Morte僵尸网络的风险提示

CSTIS：关于防范Morte僵尸网络的风险提示 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# CSTIS：关于防范Morte僵尸网络的风险提示

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-11-14 10:10:20

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9545

收藏

导语：Morte僵尸网络是一种依赖“加载器即服务（LaaS）”模式运作的网络安全威胁，已活跃至少6个月。

近日，工业和信息化部网络安全威胁和漏洞信息共享平台（CSTIS）监测发现Morte僵尸网络持续活跃，其主要攻击目标为SOHO路由器、物联网（IoT）设备及Oracle WebLogic、WordPress、vBulletin等企业应用，可能导致数据泄露、系统受控、业务中断等风险。

Morte僵尸网络是一种依赖“加载器即服务（LaaS）”模式运作的网络安全威胁，已活跃至少6个月。该僵尸网络主要通过三种方式入侵目标：一是Web界面命令注入，攻击者滥用ntp、syslog、hostname等未过滤的POST参数，执行wget/curl | sh等恶意shell命令；二是暴力破解或凭证喷洒设备默认凭证（如admin:admin）；三是利用已知漏洞，包括CVE-2019-16759（vBulletin预认证RCE）、CVE-2019-17574（WordPress Popup Maker插件漏洞）等。入侵目标系统后，攻击者首先释放小型shell脚本作为dropper（投放器，一种轻量隐蔽的恶意脚本或程序，作为初始跳板秘密部署后续恶意载荷），随后安装跨架构原生二进制文件（如morte.x86、morte.x86\_64），借助BusyBox工具实现多平台的兼容性，同时利用计划任务、进程注入等技术实现对目标系统的长久控制，最终部署加密货币挖矿模块（如基于JSON-RPC协议的eth\_getWork），劫持设备CPU/GPU资源进行加密货币挖矿。此外，Morte支持HTTP C2轮询，在数十个IP间轮换基础设施以逃避追踪，攻击者可借此执行DDoS攻击、数据窃取、转售被攻陷设备访问权至黑市或进一步横向渗透扩大威胁。

建议相关单位和用户立即组织排查，修复相关设备及应用的安全漏洞，禁用默认登录凭证，关闭不必要的路由器诊断页面，更新防病毒软件，实施全盘病毒查杀，并可通过定期备份数据等措施，防范网络攻击风险。

文章来源自：网络安全威胁和漏洞信息共享平台

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?78QvZaDB)

#### 你可能感兴趣的

* [![]()

  GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)
* [![]()

  CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)
* [![]()

  NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)
* [![]()

  Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)
* [![]()

  TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)
  2025-11-14 12:00:00
* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)
  2025-11-14 10:10:20
* [NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)
  2025-11-13 12:00:00
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)
  2025-11-13 10:34:14

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [GlassWorm恶意软件卷土重来 三款新VSCode扩展下载量超万次](https://www.4hou.com/posts/YZg9)

  胡金鱼
* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)

  胡金鱼
* [NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)

  胡金鱼
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)

  胡金鱼
* [Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)

  胡金鱼
* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)