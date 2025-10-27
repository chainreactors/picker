---
title: SMB 攻击威胁模拟与防御
url: https://www.freebuf.com/articles/es/347941.html
source: FreeBuf网络安全行业门户
date: 2022-10-27
fetch_date: 2025-10-03T21:00:59.641126
---

# SMB 攻击威胁模拟与防御

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

SMB 攻击威胁模拟与防御

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

SMB 攻击威胁模拟与防御

2022-10-26 16:30:57

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# SMB 攻击威胁模拟与防御

> 大家放轻松，您的一把梭老师帮您搞定一些晦涩难懂的地方。

本文定位

* 当高级威胁组织得到初始访问之后，为了扩大战果，SMB攻击策略是他们的选择之一。
* 面向红队，事件分析师，规则优化工程师，应急响应工程师，安服工程师，office工程师等。
* 提升您的参与感，让防御设备更好的服务于您。
* 使得您提前知道整个攻击过程并运用高超的意识，预判规则的预判。

# 前置知识：介绍NTLMv2

* 为了弄清楚SMB中继，需要先理解NTMLv2

下图为windows域环境的NTLMv2认证

注意：密码散列值被中间数据流（询问+响应）代替掉了。显而易见的好处：妈妈再也不用担心，为了验证而把真正的密码（或密码哈希）发过去了

![![image](https://image.3001.net/images/20221026/1666772270_6358ed2e3f3d5f193f9f0.png!small)

* 上图第3步：NTLMv2响应的计算原理如下图所示
  用户名的代表：域名，用户名 **challenge的代表：时间戳等**

![image](https://image.3001.net/images/20221026/1666772328_6358ed6814e0a3d162730.png!small)

* 现在的一切都使用 kerberos？不，NTLMv2依旧在使用。部分原因如下：

1.kerberos认证依赖于SPNs(Service Principals Names) 服务主体名称，默认情况下每当IP地址为（例子：`\\192.168.1.1`等）时，**kerberos不起作用**，认证默认**回退到NTLMv2**上面来（可以使用 GPO 调整这个默认）。

2.一些**旧软件**不支持kerberos认证或者**非windows系统**在AD域认证中相互作用。

# NTLM攻击策略：获取NTLMv2 challenge/Response

responder是这种攻击策略的实施工具之一，诱捕受害者与之连接认证，捕获NTLMv2。

它使用两个主要的多播协议进行名称解析：

NBT-NS（Netbios Name Server）

LLMNR（Link-local Multicast Name Resolution）

两协议都允许同一子网上的主机在多播地址上发请求来解析主机名（类似于 ARP 的主机名解析功能）

* 注意观察图中的关键词部分：NBT-NS,LLMNR；service文件服务器，erikvabu（不存在的主机名），domain master browser等。
* 此工具冒充应用服务器来欺骗客户端过来认证，poisoned answer带毒的多播（利用上面两协议）

划重点：客户端在DNS中找不到erikvabu主机名的解析记录，但在两多播协议中发现了erikvabu主机名的解析记录。因此将客户端在寻找erikvabu主机名解析的过程中，诱骗过来进行了NTLMv2认证与捕获。

一把梭：客户端找不到主机名，导致responder得到机会利用多播协议发送诱骗IP地址。由于找不到记录，为所欲为的kali IP对外宣称，你要的主机名是我。

![image](https://image.3001.net/images/20221026/1666772362_6358ed8a5e1f035af920b.png!small)

* 关于浏览器自动代理设置与WPAD认证

windows系统功能：联网时会使用默认浏览器自动检测代理设置。responder工具带有这种多个浏览器自动检测代理设置的功能。

responder工具会使用前面提到的两多播协议将带毒记录响应给WPAD。

所有选择解析带毒记录的主机将开始误用responder工具，作为他们的网络代理。

可以将responder工具中的 wpad 插件配置为强制 NTLM 身份验证，因此可以捕获凭据。

* 多年来有很多方法获得NTLMv2哈希，攻击者仅需要目标加载windows SSO的外部资源

使用认证后的漏扫

word文档中嵌入远程图片置于SMB共享中

文件夹共享（SCF 文件）中嵌入远程icon于SMB共享中

在web应用源码中嵌入SMB共享的图片

综上所述：这些方法，都是在尝试加载SMB中的资源通过单点登录尝试验证SMB服务器，会产生NTLMv2，由于这个原因在企业安全建设中，绝对要禁用出站 SMB

* 破解NTLMv2 哈希

https://hashcat.net/wiki/doku.php?id=example\_hashes

hashcat的5600

实施命令：hashcat -m 5600 hash.txt password\_list.txt -o cracked.txt

![image](https://image.3001.net/images/20221026/1666772388_6358eda4e08a78465a5ff.png!small)

# 威胁演练

### 模拟客户端使用文件共享资源

这里需要关注的重点当然不是windows02大小写的区别（同一回事），而是**专注于观察不存在的主机名windows03**

![image](https://image.3001.net/images/20221026/1666772411_6358edbb9b19237639f75.png!small)

![image](https://image.3001.net/images/20221026/1666772427_6358edcb77269c8eeca05.png!small)

* 我们需要windows03找不到的解析情报，并使用responder工具利用这一点。kali IP（192.168.10.55）

responder -I eth1 -v 开启带毒的多播

![image](https://image.3001.net/images/20221026/1666772444_6358eddc48cb1982a4827.png!small)

* 可以看见带毒多播的两协议和其他诱骗认证的服务

![image](https://image.3001.net/images/20221026/1666772458_6358edeae69f6d2d838e5.png!small)

* 以下错误没什么大不了，比如apache的工具显然已经在此机器上运行，所以它在抱怨

![image](https://image.3001.net/images/20221026/1666772475_6358edfb2b954a3a5f3a1.png!small)

* 客户端寻找不存在的window03记录时，responder工具利用了这一点，发布带毒的多播并声称主机名解析到我

![image](https://image.3001.net/images/20221026/1666772489_6358ee09eb4723ba25b1f.png!small)

* 可以观察到kali IP192.168.10.55，响应了windows03主机名的标准查询并将它解析到192.168.10.55，就是解析到kali本身

![image](https://image.3001.net/images/20221026/1666772505_6358ee19bc40651179322.png!small)

* 只需要在客户端诱骗去访问不存在的windows03进行认证（注意前面提过的很多方法，但此处已共享文件夹为例），我们知道什么都不真实存在（windows03是带毒回复重定向到kali，文件共享也不存在，是工具的伪装服务）。

![image](https://image.3001.net/images/20221026/1666772524_6358ee2c03ba88fb92431.png!small)

* 客户端进行网络认证，NTLMv2哈希已经到kali了。如果您在此输入user的密码，kali侧还会捕获user用户的HTLMv2哈希。

![image](https://image.3001.net/images/20221026/1666772539_6358ee3bd62ade2a16770.png!small)

* 因为什么都是假的，因此认证之后会报错，嗅觉敏感的分析师会意识到它的异常。

![image](https://image.3001.net/images/20221026/1666772552_6358ee4805bca200f6ed1.png!small)

* 将捕获的NTLMv2哈希放到hash.txt中，使用john hash.txt进行破解

![image](https://image.3001.net/images/20221026/1666772566_6358ee5651aaf7f841b32.png!small)

## 模拟客户端访问web服务器

systemctl stop apache2

responder -I eth1 -v

它没有抱怨80端口的错误了，因为占用80端口的apache2服务已被停止。

* 模拟一个http请求进行认证，responder工具捕获了哈希

![image](https://image.3001.net/images/20221026/1666772585_6358ee69eb45791e2da2d.png!small)

* 您可以观察流量，已一个包为例子。responder工具声称您未认证，需要NTLM进行认证，来捕获它。

![image](https://image.3001.net/images/20221026/1666772599_6358ee774e34eb2bfd1a0.png!small)

* 制作一些带毒的文档，让客户端去进行http，文件共享夹等出站连接“认证”服务器并捕获NTLMv2。以下是利用word嵌入远程源图片的功能点，制作的带毒文档。它加载远程图片的时候就需要您进行认证。

![image](https://image.3001.net/images/20221026/1666772617_6358ee891104253100bba.png!small)

* 涉及到word正版软件的实施。插入以下语句。192.168.32.131为kali IP。

![image](https://image.3001.net/images/20221026/1666772632_6358ee98b66533c31f8e3.png!small)

* 启动responder监听NTLMv2哈希即可。当文档被打开时，它会试图自动加载远程图片。

responder -I eth1 -v

![image](https://image.3001.net/images/20221026/1666772647_6358eea74553a5b9e7d03.png!small)

# NTLM攻击策略：SMB Relaying 中继

攻击者尝试将NTLMv2认证中继到另一个系统，以获得对该机器的未授权访问。

我夹在中间忽悠你，用你自己的车钥匙开你的锁，最后我未授权开你的车并告诉你车门没打开。

![image](https://image.3001.net/images/20221026/1666772662_6358eeb6cec520f2b3a1f.png!small)

这一样可以使用responder工具一把梭。因为此工具使用两协议的多播忽悠客户端将主机名解析于攻击者，中继又开始了。

* 使用MultiRelay脚本进行监听，实施如图。注意SMB signing为false，这表示域控没有做签名，容易受到此类攻击。

![image](https://image.3001.net/images/20221026/1666772682_6358eeca5d4d2aa6ff41e.png!small)

* 再开一个窗口进行带毒多播 responder -I eth1 -v

客户端访问不存在的windows05共享文件夹，经过带毒多播 responder工具的一顿操作，MultiRelay脚本得到认证成功的shell，它成功的访问了windows01机器。

![image](https://image.3001.net/images/20221026/1666772696_6358eed861a54a748998b.png!small)

# 安全营运

* 为了防止以诱使受害者身份验证为目的的上述攻击，建议禁用 NBT-NS 和 LLMNR，这两个设置都可以使用组策略进行配置。
* SMB 签名将防止，SMB Relaying 中继攻击。默认情况下，SMB 签名仅在 Windows 域控制器上启用。可使用组策略在需要的机器上启用它。
* 确保创建了一个实际指向公司代理服务器的 WPAD DNS 记录。或者，考虑在浏览器中禁用“自动检测代理设置”。
* 从架构的角度来看，使用私有 VLAN 等来隔离客户端也是阻碍 Responder 的有效方式。 此外，在充分了解SMB业务需求之后，阻止 SMB 与外部主机的连接。

感谢大师傅们很有耐心的阅读到了这里，我们还会再见面的，共勉！

> 参考资料：https://www.freebuf.com/articles/network/208802.html

# NTLM # RedTeam # 蓝队 # SMB共享

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

模拟客户端访问web服务器

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码...