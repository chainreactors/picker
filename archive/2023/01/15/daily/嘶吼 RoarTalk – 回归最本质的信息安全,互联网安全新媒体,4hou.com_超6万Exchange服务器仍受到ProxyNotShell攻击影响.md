---
title: 超6万Exchange服务器仍受到ProxyNotShell攻击影响
url: https://www.4hou.com/posts/03QL
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-15
fetch_date: 2025-10-04T03:55:46.788826
---

# 超6万Exchange服务器仍受到ProxyNotShell攻击影响

超6万Exchange服务器仍受到ProxyNotShell攻击影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 超6万Exchange服务器仍受到ProxyNotShell攻击影响

ang010ela
[新闻](https://www.4hou.com/category/news)
2023-01-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161427

收藏

导语：​超6万Exchange服务器仍未修复CVE-2022-41082远程代码执行漏洞，受到ProxyNotShell攻击的影响。

超6万Exchange服务器仍未修复CVE-2022-41082远程代码执行漏洞，受到ProxyNotShell攻击的影响。

ProxyNotShell攻击是微软Exchange服务器中的两个安全漏洞的集合，即CVE-2022-41082 和CVE-2022-41040。攻击者利用这两个漏洞可以在受害者Exchange服务器上实现权限提升、实现任意代码执行和远程代码执行。漏洞影响Exchange服务器2013、2016和 2019版本。

研究人员自2022年9月起就发现了ProxyNotShell在野攻击，微软也于2022年11月的微软补丁日发布了安全更新来修复这两个安全漏洞。

近日，Shadowserver Foundation安全研究人员发推称，根据Exchange服务器的版本信息(服务器的x\_owa\_version header)判断，仍有近7万微软Exchange服务器易受到ProxyNotShell 攻击的影响。

根据Shadowserver Foundation 1月2日发布的最新数据显示，有漏洞的Exchange服务器数量已从2022年12月中旬的83,946下降到1月2日的60,865。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672821284877045.png "1672821226178308.png")

图 受到ProxyNotShell攻击影响的Exchange 服务器

威胁情报公司GreyNoise自2022年9月开始追踪ProxyNotShell攻击活动，并提供了ProxyNotShell扫描活动的信息和与攻击相关的IP地址列表。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672821285213545.png "1672821253966072.png")

图 受ProxyNotShell攻击影响的Exchange服务器地图

为应对潜在的攻击，研究人员建议Exchange服务器用户尽快安装微软2022年11月发布的ProxyNotShell补丁。虽然微软提供了补丁，但攻击者仍然可以绕过补丁。2022年1月，Play 勒索软件攻击者就使用新的漏洞利用链来绕过ProxyNotShell URL重写缓解措施，并通过Outlook Web Access (OWA)在有漏洞的服务器上实现远程代码执行。

此外，Shodan搜索结果显示有大量未修复的Exchange服务器暴露在互联网，上千台服务器仍然受到ProxyShell 和 ProxyLogon攻击的影响。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230104/1672821283213260.png "1672821283213260.png")

图 暴露在互联网的Exchange服务器

本文翻译自：https://www.bleepingcomputer.com/news/security/over-60-000-exchange-servers-vulnerable-to-proxynotshell-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?80WftVg1)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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