---
title: 超6万Exchange服务器仍受到ProxyNotShell攻击影响
url: https://buaq.net/go-145499.html
source: unSafe.sh - 不安全
date: 2023-01-15
fetch_date: 2025-10-04T03:56:03.292890
---

# 超6万Exchange服务器仍受到ProxyNotShell攻击影响

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/6d8ad1c4f9efb4d2f7a44d17ed170d51.jpg)

超6万Exchange服务器仍受到ProxyNotShell攻击影响

导语：​超6万Exchange服务器仍未修
*2023-1-14 12:0:0
Author: [www.4hou.com(查看原文)](/jump-145499.htm)
阅读量:17
收藏*

---

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

![](https://www.4hou.com/captcha/flat?KKDY6DWN)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/1673227598146450.jpeg)

  俄罗斯Turla黑客劫持老旧的恶意软件基础设施部署新的后门](https://www.4hou.com/posts/DE4K)
* [![](https://img.4hou.com/images/微信截图_20230113142433.png)

  超6万Exchange服务器仍受到ProxyNotShell攻击影响](https://www.4hou.com/posts/03QL)
* [![](https://img.4hou.com/images/微信截图_20230112100638.png)

  《2022年嘶吼电子季刊Q4》发布](https://www.4hou.com/posts/03GL)
* [![](https://img.4hou.com/images/微信截图_20230113095510.png)

  勒索软件谈判的注意事项](https://www.4hou.com/posts/wgW8)
* [![](https://img.4hou.com/images/633e451b8e9f092db1445e6b_1024.jpg)

  在谷歌和苹果商店中发现了近300个恶意的贷款应用程序](https://www.4hou.com/posts/DEjk)
* [![](https://img.4hou.com/images/微信截图_20230111174407.png)

  国内学者提出新算法可破解RSA-2048，引发外国学者争议](https://www.4hou.com/posts/AO4l)

![]()

文章来源: https://www.4hou.com/posts/03QL
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)