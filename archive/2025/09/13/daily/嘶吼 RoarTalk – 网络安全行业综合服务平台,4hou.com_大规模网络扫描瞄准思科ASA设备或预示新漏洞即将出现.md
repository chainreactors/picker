---
title: 大规模网络扫描瞄准思科ASA设备或预示新漏洞即将出现
url: https://www.4hou.com/posts/0MKX
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-13
fetch_date: 2025-10-02T20:05:26.388356
---

# 大规模网络扫描瞄准思科ASA设备或预示新漏洞即将出现

大规模网络扫描瞄准思科ASA设备或预示新漏洞即将出现 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 大规模网络扫描瞄准思科ASA设备或预示新漏洞即将出现

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43629

收藏

导语：据显示，8月末出现两次显著的扫描高峰，多达2.5万个独立IP地址对ASA登录入口及思科IOS的Telnet/SSH服务进行探测。

近期出现大规模针对思科ASA设备的网络扫描活动，网络安全研究人员就此发出警示，称此类活动可能预示这些产品即将曝出新漏洞。

网络安全公司GreyNoise记录显示，8月末出现两次显著的扫描高峰，多达2.5万个独立IP地址对ASA登录入口及思科IOS的Telnet/SSH服务进行探测。

2025年8月26日的第二波扫描中，80%的流量来自一个巴西僵尸网络，涉及约1.7万个IP地址。两次扫描活动中，威胁者使用的用户代理均与Chrome浏览器相似且存在重叠，表明其可能源自同一源头。

![greypsikes.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757487834382471.jpg "1757487834382471.jpg")

扫描活动主要针对美国，英国和德国也未能幸免。

GreyNoise此前曾指出，在80%的案例中，此类侦察活动都发生在被扫描产品的新漏洞披露之前。从数据上看，思科产品的这种相关性较其他厂商更弱，但扫描高峰的相关信息仍能帮助防御者加强监控并采取主动防御措施。

这些扫描活动通常是对已修复漏洞的失败利用尝试，但也可能是攻击者为利用新漏洞而进行的资产枚举与网络测绘。

**报告证实扫描活动升级**

系统管理员“NadSec – Rat5ak”此前发布的另一份报告显示，类似扫描活动始于7月31日，初期为低强度的 opportunistic 扫描，8月中旬逐渐升级，并于8月28日达到顶峰。

Rat5ak观察到，20小时内思科ASA端点遭遇了20万次访问，且每个IP的流量均稳定在1万次左右，呈现出高度自动化的特征。

![mousespike.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757487923118012.jpg "1757487923118012.jpg")

该管理员称，这些活动来自三个自治系统编号（ASN），分别是Nybula、Cheapy-Host和Global Connectivity Solutions LLP。

**安全建议**

研究人员建议系统管理员采取以下措施：

1.  为思科ASA设备安装最新安全更新，修复已知漏洞；

2.  对所有ASA远程登录强制启用多因素认证（MFA）；

3.  避免将/+CSCOE+/logon.html页面、WebVPN、Telnet或SSH服务直接暴露在公网；

4.  若确需外部访问，应使用VPN集中器、反向代理或访问网关加强访问控制；

5.  利用GreyNoise和Rat5ak报告中共享的扫描活动指标，主动拦截此类尝试，或对远离本组织业务区域的IP实施地理封锁与速率限制。

文章翻译自：https://www.bleepingcomputer.com/news/security/surge-in-networks-scans-targeting-cisco-asa-devices-raise-concerns/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?y1rCopi7)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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