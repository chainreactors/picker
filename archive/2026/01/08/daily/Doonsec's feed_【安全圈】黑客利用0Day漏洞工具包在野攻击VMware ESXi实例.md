---
title: 【安全圈】黑客利用0Day漏洞工具包在野攻击VMware ESXi实例
url: https://mp.weixin.qq.com/s/8XdsB9mCjaoxjL9PtZzYag
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:40.204267
---

# 【安全圈】黑客利用0Day漏洞工具包在野攻击VMware ESXi实例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaagd6b1vg9wuP9ibiaVZiaLjryOhZpngRhcVvxBvaNKQGOPNGzC7thsWLV3GCulXbzRn8I82AdsGtcA/0?wx_fmt=jpeg)

# 【安全圈】黑客利用0Day漏洞工具包在野攻击VMware ESXi实例

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaagd6b1vg9wuP9ibiaVZiaLjrvHo50Q5ZM4qMxLMxeGiaCsK3UibtaZGrm5PVNgoOHLsmG095kicTZSedQ/640?wx_fmt=jpeg&from=appmsg)

网络安全公司Huntress发现黑客正在利用一个0Day漏洞工具包攻击VMware ESXi实例，该工具包通过串联多个漏洞实现虚拟机逃逸。攻击者最初通过被入侵的SonicWall VPN获得初始访问权限。

## **攻击过程分析**

威胁行为者首先通过SonicWall VPN获得立足点，随后利用被入侵的域管理员账户进行横向移动，先后攻陷备份域控制器和主域控制器。在主域控制器上，攻击者部署了Advanced Port Scanner和ShareFinder等侦察工具，使用WinRAR暂存数据，并修改Windows防火墙规则以阻止外部出站流量，同时允许内部横向移动。

在部署漏洞工具包约20分钟后，攻击者开始执行ESXi漏洞利用程序，Huntress在勒索软件部署前成功阻止了攻击。

## **MAESTRO漏洞工具包技术细节**

Huntress将该工具包命名为MAESTRO，其工作原理包括：

* 使用devcon.exe禁用VMware VMCI驱动程序
* 通过KDU加载未签名驱动程序以绕过驱动程序签名强制（DSE）
* 执行核心逃逸操作

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaagd6b1vg9wuP9ibiaVZiaLjrZJ9lShfrDtuAMttUp6Hzic045Kjic8ElXUibianXXVz5x9zgrFHD0s6e8g/640?wx_fmt=jpeg&from=appmsg)工具包截图（来源：Huntress）

MyDriver.sys驱动程序通过VMware Guest SDK查询ESXi版本，从支持ESXi 5.1至8.0共155个构建版本的数据表中选择偏移量，通过HGFS（CVE-2025-22226）泄露VMX基址，通过VMCI（CVE-2025-22224）破坏内存，并部署用于沙箱逃逸的shellcode（CVE-2025-22225）。

| CVE编号 | CVSS评分 | 漏洞描述 |
| --- | --- | --- |
| CVE-2025-22226 | 7.1 | HGFS越界读取导致VMX内存泄露 |
| CVE-2025-22224 | 9.3 | 任意写入漏洞导致从VMX沙箱逃逸至内核 |
| CVE-2025-22225 | 8.2 | 任意写入漏洞导致从VMX沙箱逃逸至内核 |

Shellcode会部署名为VSOCKpuppet的后门程序，该后门劫持ESXi的inetd服务（端口21）以获取root权限，并使用VSOCK进行隐蔽的虚拟机-宿主机通信，这种通信方式对网络监控工具不可见。

## **攻击溯源与防御建议**

PDB路径显示该工具包在简体中文环境中开发，如"全版本逃逸--交付"的路径名称，时间戳为2024年2月，比Broadcom在2025年3月4日发布的VMSA-2025-0004安全公告早了一年多。2023年11月的client.exe PDB表明该工具采用模块化设计，被篡改的VMware驱动程序引用了"XLab"。Huntress高度确信攻击者来自中文环境，基于资源文件和0Day漏洞获取能力。

防御建议：

* 及时为ESXi打补丁，已停止支持的版本无法获得修复
* 使用"lsof -a"命令监控ESXi主机的VSOCK进程
* 警惕KDU等BYOD加载器
* 加强VPN安全防护
* 防火墙规则变更和未签名驱动程序都是系统被入侵的信号
* VSOCK后门可绕过入侵检测系统（IDS）

此次事件凸显了虚拟机监控程序面临的持续威胁，攻击者通过驱动程序恢复和配置清理保持隐蔽性。随着针对ESXi的勒索软件攻击增加，企业必须加强虚拟化环境的安全防护。

***END***

阅读推荐

[【安全圈】美军进攻委内瑞拉前当地电信公司BGP路由发生异常 流量被引导至不安全的路线](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=1&sn=10d365f3aeaa11a32edd4b32ab718cbd&scene=21#wechat_redirect)

[【安全圈】两款Chrome扩展窃取90万用户与ChatGPT的对话记录](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=2&sn=340af758cdc973198fef16ee90d05a49&scene=21#wechat_redirect)

[【安全圈】0Day漏洞Chronomaly可获取Linux内核root权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=3&sn=dea95a9fbe14ba2f6a20a39754e7f77a&scene=21#wechat_redirect)

[【安全圈】D-Link 多款老旧 DSL 网关路由器被曝命令注入 0day，已遭野外利用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073601&idx=4&sn=9c7154506dafe5b5720c6a61411d4662&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过