---
title: 查找网站真实 IP 的方法
url: https://mp.weixin.qq.com/s?__biz=MzA3Mjc1MTkwOA==&mid=2650554098&idx=1&sn=363063f75a9d079aff56a0f665817046&chksm=871110b9b06699af8d510a2449cef000827434e372cc51c470a3d0893277fecc209756eaf5ae&scene=58&subscene=0#rd
source: 情报分析师
date: 2024-08-17
fetch_date: 2025-10-06T18:06:21.462695
---

# 查找网站真实 IP 的方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mkvak7WiccmVoiaYHiaicsyP5ImuZPy0OB92SWqTGe2ibW1ZdcicWpXxxKAmr5NdrUiaWmeia1thBtbqxJvgOQ4hrBWf2A/0?wx_fmt=jpeg)

# 查找网站真实 IP 的方法

原创

DMT

情报分析师

**首先，我们来认识下最寻常的真实ip隐藏的方法“CDN”。**

内容分发网络(content delivery network或content distribution network，缩写作CDN)指一种通过互联网互相连接的电脑网络系统，利用最靠近每位用户的服务器，更快、更可靠地将音乐、图片、视频、应用程序及其他文件发送给用户，来提供高性能、可扩展性及低成本的网络内容传递给用户。

CDN节点会在多个地点，不同的网络上摆放。这些节点之间会动态的互相传输内容，对用户的下载行为最优化，并借此减少内容供应者所需要的带宽成本，改善用户的下载速度，提高系统的稳定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mkvak7WiccmVoiaYHiaicsyP5ImuZPy0OB92yzHaKGGFCufaW2uvTysIWHGusB1EgLXPGwRElnowkWKXmeVpsrgQhQ/640?wx_fmt=png&from=appmsg)

**运用一些命令查看，比如：ping、nslookup、ipconfig 这类方法需要打开windows的dos运行界面**

![](https://mmbiz.qpic.cn/mmbiz_jpg/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBHKUexrjNLjemGVgB18HOrCKyIOOibClKjDYkiajaoice1Ay58j0aSvJmQ/640?wx_fmt=jpeg)

用nslookup命令查询想要查的域名，若是有多个ip就是用了cdn，多半不是真实IP；如图：

![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYB7KBg5GKMp50Lj3r1kswqRc2pdiaVmUOrCNCLVEePjib9HXhoMqQPRhsQ/640?wx_fmt=png)

其他方法类似

用ping命令输入：

ping www.baidu.com

用ipconfig命令输入：

ipconfig www.baidu.com

**可以从多个地点ping他们想要确认的域名，若返回的是不同的ip，那么服务器确定使用了cdn，返回的ip也不是服务器的真实ip；**

常用的网址有justping:

http://itools.com/tool/just-ping

![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBQAxEfhpmbY5AMX7FMDmtFGG0EF5jg9GobLSboiaEdS0bY27fBaFZqtQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

1、子域名查找法

因为cdn和反向代理是需要成本的，有的网站只在比较常用的域名使用cdn或反向代理，有的时候一些测试子域名和新的子域名都没来得及加入cdn和反向代理，所以有时候是通过查找子域名来查找网站的真实IP。

下面介绍些常用的子域名查找的方法和工具：

**微步在线**

**（https://x.threatbook.cn/）**

上文提到的微步在线功能强大，黑客只需输入要查找的域名(如baidu.com)，点击子域名选项就可以查找它的子域名了，但是免费用户每月只有5次免费查询机会。如图：

![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBhTccsXrRfZ0VV4woVFOCNGmv9XxFwnwZoOCm6EnMSpzzQoKDyFwbbg/640?wx_fmt=png)

**Dnsdb查询法**

**（https://dnsdb.io/zh-cn/）**

黑客只需输入baidu.com type:A就能收集百度的子域名和ip了，如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYB40karZG8jYcibwTcdOOYdSymIoTj8JqkPdO9lZT5p0pvVlnnX99SOrg/640?wx_fmt=jpeg)

**Google 搜索**

Google site:baidu.com -www就能查看除www外的子域名，如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBmHBOGMKtzhYKNhiaHjNF9EzVTicdnfcGIhibTYPmZIeBPsc4jj7QH4f9w/640?wx_fmt=jpeg)

各种子域名扫描器

这里，主要为大家推荐子域名挖掘机和lijiejie的subdomainbrute，网址如下

https://github.com/lijiejie/subDomainsBrute

子域名挖掘机仅需输入域名即可基于字典挖掘它的子域名，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBLKNoEbIiabjRsKwJiarHWJuDJnFFUec5Ad7TJb8FfyCXxAI5S6mpwOoQ/640?wx_fmt=png)

Subdomainbrute以windows为例，黑客仅需打开cmd进入它所在的目录输入

Pythonsubdomainbrute.py baidu.com --full即可收集百度的子域名，如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBj1g7V8CKjeicAWPHDGtAmCjpawgGTTyemtoibRDCbg2S4z24XJ2wHv1Q/640?wx_fmt=jpeg)

总结一下，收集子域名后尝试以解析ip不在cdn上的ip解析主站，真实ip成功被获取到。

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

IP历史记录解析查询法

有的网站是后来才加入CDN的，所以只需查询它的解析历史即可获取真实ip，这里就简单介绍几个网站：

dnsdb.ionetcraft

http://toolbar.netcraft.com/

Viewdns

http://viewdns.info/

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

网站漏洞查找法

通过网站的信息泄露如phpinfo泄露，github信息泄露，命令执行等漏洞获取真实ip。

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

网站订阅邮件法

黑客可以通过网站订阅邮件的功能，让网站给自己发邮件，查看邮件的源代码即可获取网站真实ip。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mkvak7WiccmVoiaYHiaicsyP5ImuZPy0OB92FwlyxHjPicI1a28RKkZceXmlbzEHoMyvCMrSKS5vrAIMKmkhhA4pVhg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

理想zmap法

首先从 apnic 网络信息中心获取ip段，然后使用Zmap的 banner-grab 对扫描出来 80 端口开放的主机进行banner抓取，最后在 http-req中的Host写我们需要寻找的域名，然后确认是否有相应的服务器响应。

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

网络空间引擎搜索法

常见的有以前的钟馗之眼，

shodan(https://www.shodan.io/)，

fofa搜索(https://fofa.so/)。

以fofa为例，只需输入：title:“网站的title关键字”或者body：“网站的body特征”就可以找出fofa收录的有这些关键字的ip域名，很多时候能获取网站的真实ip。

![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBUKEC4KFFRRDiadmnepiap2R4oj6Pa73tAD7vNwo1M5wxAkJNubnVWcnQ/640?wx_fmt=png)**shodan**

**![](https://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUaYaJPeI55yOeiceO4gZCYBdVYLIJPF7hVNUjUCHUZJUEP4aH8MF0ibhDsvIY3l5ArTmsibIhKXlS1w/640?wx_fmt=png)fofa**

![](https://mmbiz.qpic.cn/mmbiz_png/pUe6UvWIpQibslEJA5ibG0svswbu0Ix1yXiavkjrZ8PzugicXhkj13uB6AXqLvrJsSDTpOtqMBj0x5nGy18EKibfymg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/cKj9jFic1XzzfDoia2FUbibFCIVEEvLicDZJN2IMXyQhg4rVwegKr4YKuIQRc5Xge6dYNFkFycQltejBdCUDAbgWicg/640)

F5 LTM解码法

当服务器使用F5 LTM做负载均衡时，通过对set-cookie关键字的解码真实ip也可被获取，例如：

SetCookie:BIGipServerpool\_8.29\_8030=487098378.24095.0000，先把第一小节的十进制数即487098378取出来，然后将其转为十六进制数1d08880a，接着从后至前，以此取四位数出来，也就是0a.88.08.1d，最后依次把他们转为十进制数10.136.8.29，也就是最后的真实ip。

通过以上的方法，被获取到的ip可能是真实的ip、亦可能是真实ip的同c段ip，还需要要对其进行相关测试，如与域名的绑定测试等，最后才能确认它是不是最终ip。

识别下方二维码

立即加入

**知识星球**

**知识分享平台**

开启全球情报探索之旅

**洞察世界**

**一手掌握全球情报动态！**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mkvak7WiccmWYCrTGvaicO4rgCqUrP2ZShcyryic3xe2jAZVbCa1zQ0B6xxDnqNYDDGf0cuJtknXPgSsYsY2N3htg/640?wx_fmt=jpeg&from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mkvak7WiccmVWq6l2ibia7nxDgQJcFhsAPbxMNozb8fiaV28Kox7kR8EgVyszuVhjqMTLZjtW9YpnsR9NB5OEciadMg/640?wx_fmt=jpeg)

10款用于查询IP地址的工具网站](https://mp.weixin.qq.com/s?__biz=MzA3Mjc1MTkwOA==&mid=2650546559&idx=1&sn=cee27b6264447c6c1ec8f465a6b4679d&chksm=87110f34b0668622645756960efb87bfef67cfdc597872e9ec783b36a497297e8354146bc5de&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mkvak7WiccmVnX8DibvKJNsysKWMQqsd3YDxIbm78P38AibUxcOvNMrUn3Z40adeeLOQYkyUkAeerKBUPGiaLnob9A/640?wx_fmt=jpeg)

你真的会查看IP地址吗？](https://mp.weixin.qq.com/s?__biz=MzA3Mjc1MTkwOA==&mid=2650531925&idx=2&sn=f2ea531021df7baf26db1fcbef4ef482&chksm=8716c61eb0614f089dbb51e7c35b63df133d6c1d8b0c34cd6e3e37874654241583de7327b5ac&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Mkvak7WiccmXCdcSNpbSLEvkl4NcLW84RgpWrtFpLC6qMGBaI4eM56LkbMv7BPwGo2Pbat52dYf1dNiclztrjJTg/640?wx_fmt=jpeg)

安欣警官通过IP地址可以定位到莽村附近吗？](https://mp.weixin.qq.com/s?__biz=MzA3Mjc1MTkwOA==&mid=2650525325&idx=1&sn=6aff4e7bca9ffdf6ac63135d7c73a7d4&chksm=8716e0c6b06169d0e43f2fec2d5c8653bd2eadefdbffe87a79bc6af4c415cda28c35ac924aeb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/71FNwicgZ35ficgEDvKAHRI8AicGibuGDoWpibaULL3iaZyruWzukYEBueSGuO4ZnfDDRAnD3rGGRU03JWw6DT55sAZw/640?wx_fmt=jpeg)

用链接查看对方IP（包括机型、系统版本等信息）](https://mp.weixin.qq.com/s?__biz=MzA3Mjc1MTkwOA==&mid=2650499348&idx=3&sn=aabbfb4fde94de7ab80d4a5768770531&chksm=8716475fb061ce49b5a836fefbd45a2a438ecc1bc82b53a8e8fd5bfeea1ab55ff08876d3d64b&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Mkvak7WiccmUO5dhXictxTG5ooia6EeoxUEWwpdMstx1ibGcNTPKQKdW4lNVR4j8qr8uuWMBNGaGiaRMR0wKXP4hxAw/0?wx_fmt=png)

情报分析师...