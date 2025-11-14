---
title: NuGet平台现恶意包 暗藏破坏有效载荷
url: https://www.4hou.com/posts/VW69
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-13
fetch_date: 2025-11-14T03:12:24.350765
---

# NuGet平台现恶意包 暗藏破坏有效载荷

NuGet平台现恶意包 暗藏破坏有效载荷 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# NuGet平台现恶意包 暗藏破坏有效载荷

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10470

收藏

导语：目前这些恶意扩展的具体攻击目标与来源尚不清楚，但建议可能受影响的机构立即核查资产是否安装了上述9款包，若存在则需默认已遭入侵并采取应对措施。

NuGet平台出现多款恶意软件包，内含定于2027年至2028年激活的破坏载荷，攻击目标直指数据库部署环境与西门子S7工业控制设备。这些嵌入的恶意代码采用概率触发机制，是否激活取决于受感染设备上的一系列参数配置。

NuGet是开源包管理器及软件分发系统，开发者可通过它下载现成的.NET类库并集成到自身项目中。

Socket的研究人员在NuGet上发现9款恶意包，均以“shanhai666”为开发者名称发布，这些包表面具备合法功能，实则隐藏有害代码。

这些恶意包“有针对性地瞄准.NET应用中常用的三大数据库提供商（SQL Server、PostgreSQL、SQLite）”。其中最危险的是Sharp7Extend包——该包伪装成用于与西门子可编程逻辑控制器（PLC）进行以太网通信的合法Sharp7类库，专门针对其用户发起攻击。

Socket研究人员表示：“攻击者在可信的Sharp7名称后添加‘Extend’后缀，诱导那些搜索Sharp7扩展或增强功能的开发者下载。”

NuGet平台上“shanhai666”账号共列出12款包，其中9款包含恶意代码，具体如下：

1. SqlUnicorn.Core

2. SqlDbRepository

3. SqlLiteRepository

4. SqlUnicornCoreTest

5. SqlUnicornCore

6. SqlRepository

7. MyDbRepository

8. MCDbRepository

9. Sharp7Extend

目前，该开发者账号下已无相关包列出，但需注意的是，这些包下架时下载量已接近9500次。

**暗藏“定时炸弹”**

Socket研究人员指出，这些恶意包中99%为合法代码，营造安全可信的假象，仅嵌入20行左右的恶意载荷。

Socket在本周发布的报告中解释：“该恶意软件利用C#扩展方法，将恶意逻辑隐秘注入每一次数据库操作和PLC操作中。”

每当应用程序执行数据库查询或PLC操作时，这些扩展方法都会被触发。同时，代码会将受感染系统的当前日期与硬编码的触发日期（范围为2027年8月8日至2028年11月29日）进行比对。

![triggerdate.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251110/1762744905124827.png "1762744871328932.png")

2028年 11 月触发日期

若日期条件匹配，代码会创建“Random”类生成1至100之间的随机数，若数值大于80（触发概率20%），则调用“Process.GetCurrentProcess().Kill()”函数，立即终止宿主进程。

对于频繁调用事务或连接方法的典型PLC客户端而言，这将导致运营操作立即中断。

伪装成合法Sharp7类库（西门子S7 PLC常用的.NET通信层）的Sharp7Extend包则采用相反逻辑：在20%的情况下直接终止PLC通信，该机制将于2028年6月6日失效。

Sharp7Extend包还包含第二种破坏手段：代码尝试读取不存在的配置值，导致初始化操作必然失败。

第三种机制会为内部PLC操作创建过滤值，并设置30至90分钟的载荷执行延迟。延迟结束后，经过该过滤器的PLC写入操作有80%的概率被篡改，进而导致执行器无法接收指令、设定值无法更新、安全系统无法启动、生产参数无法修改等严重后果。

![corrupt-writes.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251110/1762744911126388.png "1762744911126388.png")

损坏 PLC 写入

Socket研究人员表示：“通过BeginTran()函数实现的随机即时进程终止，与通过ResFliter实现的延迟写入篡改相结合，构成了一套随时间演进的复杂多层攻击。”

目前这些恶意扩展的具体攻击目标与来源尚不清楚，但建议可能受影响的机构立即核查资产是否安装了上述9款包，若存在则需默认已遭入侵并采取应对措施。

对于运行Sharp7Extend包的工业环境，需核查PLC写入操作的完整性、检查安全系统日志中是否存在指令丢失或启动失败记录，并为关键操作部署写入验证机制。

文章翻译自：https://www.bleepingcomputer.com/news/security/malicious-nuget-packages-drop-disruptive-time-bombs/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8meAzzh0)

#### 你可能感兴趣的

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
* [![]()

  恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [CSTIS：关于防范Morte僵尸网络的风险提示](https://www.4hou.com/posts/kgEY)
  2025-11-14 10:10:20
* [NuGet平台现恶意包 暗藏破坏有效载荷](https://www.4hou.com/posts/VW69)
  2025-11-13 12:00:00
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/0MQG)
  2025-11-13 10:34:14
* [Balancer协议V2池遭黑客攻击 损失超1.28亿美元](https://www.4hou.com/posts/NG4K)
  2025-11-11 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

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
* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)

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