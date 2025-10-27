---
title: 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击
url: https://www.4hou.com/posts/MXX1
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-12
fetch_date: 2025-10-06T20:33:21.061353
---

# 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击

新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型 Aquabotv3 勒索软件利用 Mitel 命令注入漏洞发起攻击

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-02-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)75411

收藏

导语：这是一个中等严重的漏洞，它允许具有管理员特权的身份验证的攻击者，由于启动过程中的参数消毒不足而进行参数注射攻击，从而导致任意命令执行。

一种基于“Mirai”的僵尸网络恶意软件“Aquabot”的新变种已被发现正在积极利用 Mitel SIP 电话中的命令注入漏洞 CVE-2024-41710。

这项活动是由Akamai的安全情报和响应小组（SIRT）发现的，报告说这是属于其雷达的Aquabot的第三种变体。恶意软件系列是在2023年引入的，第二版增加了持久机制。第三个变体“ aquabotv3”引入了一个系统，该系统检测终止信号并将信息发送到命令和控制服务器（C2）服务器。

AquaboTV3报告阻断尝试的机制对于僵尸网络来说不同寻常，并且可能已添加以使其运营商更好地进行监控。

![kill.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250205/1738748975187129.png "1738748706751284.png")

报告过程阻断C2的尝试

**针对Mitel手机**

CVE-2024-41710是影响Mitel 6800系列，6900系列和6900W系列SIP电话的指挥注射漏洞，通常用于公司办公室，企业，政府机构，医院，医院，教育机构，教育机构，酒店和金融机构。

这是一个中等严重的漏洞，它允许具有管理员特权的身份验证的攻击者，由于启动过程中的参数消毒不足而进行参数注射攻击，从而导致任意命令执行。

Mitel于2024年7月17日发布了有关此漏洞的修复程序和安全咨询，敦促用户进行升级。两周后，安全研究员Kyle Burns在Github上发表了概念验证（POC）。

AquaboTV3在攻击中使用该POC利用CVE-2024-41710，是利用此漏洞的第一个记录案例。研究人员解释说：“ Akamai Sirt在2025年1月初，通过全球蜜罐网络使用有效载荷几乎与POC相同，检测到针对这种脆弱性的利用尝试。”

攻击需要身份验证的事实表明，恶意软件僵尸网络使用蛮力来获得初始访问。

攻击者制作的HTTP POST请求针对脆弱的端点8021xSupport.html，负责Mitel SIP电话中的802.1X身份验证设置。该应用程序不当处理用户输入，允许将畸形的数据插入手机的本地配置（/nvdata/etc/local.cfg）。

通过注入线路结束字符（％dt→％0D），攻击者可以操纵设备启动过程中如何解析配置文件以从其服务器中执行远程壳脚本（BIN.SH）。

该脚本下载并安装了定义的体系结构（X86，ARM，MIPS等）的Aquabot有效载荷，使用“ CHMOD 777”设置其执行权限，然后清理任何痕迹。

**Aquabotv3活性**

一旦确保了持久性，Aquabotv3将通过TCP连接到其C2，以接收说明、攻击命令，更新或其他有效负载。

接下来，它尝试使用MITEL Exploit，CVE-2018-17532（TP-Link），CVE-2023-26801（IOT固件RCE），CVE-2022-31137（Web App RCE），Linksys E E linksys e，尝试使用MITEL Exploit（TP-Link），CVE-2018-17532（TP-Link）（TP-Link）（TP-Link）（TP-Link）（TP-Link），Linksys E - 系列RCE，Hadoop纱和CVE-2018-10562 / CVE-2018-10561（Dasan Router Router Bugs）。该恶意软件还试图违反强制默认或弱SSH/TELNET凭据，以扩展到同一网络上固定较差的设备。

AquaboTV3的目标是将设备纳入其分配拒绝服务（DDOS）群，并使用它们执行TCP SYN，TCP ACK，UDP，GRE IP和应用程序层攻击。

Akamai在其报告底部列出了与 Aquabotv3 相关的入侵指标（IoC），以及用于检测该恶意软件的 Snort 和 YARA 规则。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-aquabotv3-botnet-malware-targets-mitel-command-injection-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?gEuuDyLY)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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