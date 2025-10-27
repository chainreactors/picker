---
title: 超过84000个Roundcube网络邮件安装受到RCE漏洞影响
url: https://www.4hou.com/posts/XPBA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-19
fetch_date: 2025-10-06T22:51:44.882281
---

# 超过84000个Roundcube网络邮件安装受到RCE漏洞影响

超过84000个Roundcube网络邮件安装受到RCE漏洞影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 超过84000个Roundcube网络邮件安装受到RCE漏洞影响

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-06-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)49166

收藏

导语：目前尚不清楚该漏洞是否被用于实际的攻击，以及规模有多大，但安全研究员建议人们应立即采取行动。

最新发现，超过84000个Roundcube网络邮件安装容易受到CVE-2025-49113的攻击，CVE-2025-49113是一个严重的远程代码执行（RCE）漏洞，可公开利用。

该漏洞影响了Roundcube的1.1.0到1.6.10版本，跨越了十年，在安全研究员Kirill Firsov发现并报告后，于2025年6月1日被修补。

该错误源于未处理的$\_GET['\_from']输入，当会话键以感叹号开始时，会启用PHP对象反序列化和会话损坏。

补丁发布后不久，黑客对其进行了逆向工程，开发了一个有效的漏洞，并在地下论坛上出售。尽管利用CVE-2025-49113需要身份验证，但攻击者声称可以通过CSRF、日志抓取或暴力强制获取有效凭据。目前Firsov在他的博客上分享了有关该漏洞的技术细节，以帮助防御很可能发生的主动利用尝试。

**大规模的曝光**

Roundcube广泛用于共享主机（GoDaddy, Hostinger， OVH）以及政府，教育和技术部门，在线可见实例超过120万。

威胁监测平台Shadowserver基金会报告称，截至2025年6月8日，其互联网扫描返回了84925个易受CVE-2025-49113攻击的Roundcube实例。

这些案例中的大多数发生在美国（19500）、印度（15500）、德国（13600）、法国（3600）、加拿大（3500）和英国（2400）。

考虑到高风险的利用和潜在的数据盗窃，这些实例的暴露是一个重大的网络安全风险。建议系统管理员尽快更新到解决CVE-2025-49113的1.6.11和1.5.10版本。

目前尚不清楚该漏洞是否被用于实际的攻击，以及规模有多大，但安全研究员建议人们应立即采取行动。如果无法升级，建议限制对webmail的访问，关闭文件上传，添加CSRF保护，阻止有风险的PHP函数，并监控漏洞利用指标。

文章翻译自：https://www.bleepingcomputer.com/news/security/over-84-000-roundcube-instances-vulnerable-to-actively-exploited-flaw/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uyIlxEJo)

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