---
title: Cloudflare将本周大规模服务中断事件归咎于数据库问题
url: https://www.4hou.com/posts/MX3B
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-21
fetch_date: 2025-11-22T03:06:58.879825
---

# Cloudflare将本周大规模服务中断事件归咎于数据库问题

Cloudflare将本周大规模服务中断事件归咎于数据库问题 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
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

# Cloudflare将本周大规模服务中断事件归咎于数据库问题

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10583

收藏

导语：Cloudflare遭遇六年最严重服务中断 数据库权限变更引发全球网络连锁故障。

本周，Cloudflare发生六年来最严重的服务中断事件。数据库访问控制权限变更触发其全球网络连锁故障，导致大量网站及在线平台近6小时无法访问。

Cloudflare全球网络是一套分布式基础设施，服务器与数据中心遍布120多个国家，提供内容分发、安全防护及性能优化服务。该网络已与全球超1.3万个网络建立连接，包括所有主流互联网服务提供商（ISP）、云服务商及企业网络。

公司首席执行官Matthew Prince在故障缓解后发布的事后分析报告中表示，此次服务中断并非由网络攻击导致。故障源于某一数据库系统的权限变更——这一变更导致数据库向“机器人管理系统”使用的“特征文件”中输出多条重复条目。

一项常规的数据库权限更新，致使Cloudflare的机器人管理系统生成了包含重复条目的超大配置文件。该文件超出系统内置大小限制，导致网络流量路由过程中相关软件崩溃。

权限变更后，数据库查询返回了重复的列元数据，使特征文件中的条目从约60个翻倍至200多个，突破了系统为防止内存无限制占用而硬编码设定的200个特征上限。

![Cloudflare 5xx error HTTP status codes.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251120/1763624228289262.jpg "1763623973376053.jpg")

5xx 错误 HTTP 状态码在故障期间

每五分钟系统会生成一次配置文件——结果可能正常也可能存在故障，具体取决于哪些集群节点已完成更新，这导致网络在正常运行与故障状态之间反复波动。

此外，当超大文件在网络设备间传播时，机器人管理模块的Rust代码触发系统崩溃并返回5xx错误，进而导致负责流量处理的核心代理系统宕机。

随后，Cloudflare工程师定位故障根源并将问题文件替换为早期版本后，核心流量恢复正常。不久后，所有系统完全恢复运行。此次中断影响了Cloudflare的核心CDN、安全服务、Turnstile验证服务、Workers KV存储服务、控制台访问、邮件安全及身份认证服务。

Matthew Prince表示“鉴于Cloudflare在互联网生态系统中的重要性，任何系统中断都是不可接受的。”

此次中断事件是Cloudflare自2019年以来最严重的一次服务中断。以往也曾出现过控制台无法访问、新功能暂时不可用等情况，但过去六年多来，从未发生过导致大部分核心流量无法通过我们网络的中断事件。

今年6月，Cloudflare曾缓解过另一起大规模中断事件，当时导致多个地区的零信任WARP连接出现问题、身份认证服务故障，还影响了谷歌云基础设施。

10月，亚马逊也处理了一起由重大DNS故障引发的中断事件，该故障导致数百万使用其亚马逊网络服务（AWS）云计算平台的网站连接中断。

文章来源自：https://www.bleepingcomputer.com/news/technology/cloudflare-blames-this-weeks-massive-outage-on-database-issues/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?REckWDbH)

#### 你可能感兴趣的

* [![]()

  Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
* [![]()

  公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)
* [![]()

  Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
* [![]()

  Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)
* [![]()

  捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)
* [![]()

  AI-Slop勒索软件测试版潜入VS Code应用市场](https://www.4hou.com/posts/ZgjE)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
  2025-11-21 12:01:00
* [公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)
  2025-11-21 10:13:24
* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
  2025-11-19 12:00:00
* [Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)
  2025-11-19 11:03:05

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)

  胡金鱼
* [公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)

  胡金鱼
* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)

  胡金鱼
* [Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)

  胡金鱼
* [捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)

  胡金鱼
* [AI-Slop勒索软件测试版潜入VS Code应用市场](https://www.4hou.com/posts/ZgjE)

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