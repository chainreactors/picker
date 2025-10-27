---
title: 【安全圈】CL-UNK-0979 利用 Ivanti Connect Secure 中的零日漏洞获取网络访问权限
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067480&idx=4&sn=8dc7094933166fceeb2e467f38e23545&chksm=f36e7ad8c419f3ce413fdcd09b7fbf2c3828fe34b5aca8c6a3b0d570a1f213c166b9943c4be8&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-20
fetch_date: 2025-10-06T20:09:25.962056
---

# 【安全圈】CL-UNK-0979 利用 Ivanti Connect Secure 中的零日漏洞获取网络访问权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaPe1B66JiaecZicwXgaw8TlGRdYO0BMjBvwFlAySnyAD2ph8GGS108edibEpCib8TD0lg1CjWxtJb0Ag/0?wx_fmt=jpeg)

# 【安全圈】CL-UNK-0979 利用 Ivanti Connect Secure 中的零日漏洞获取网络访问权限

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaPe1B66JiaecZicwXgaw8TlGQ4tFy5Z321BibUdsoYbkpTFfQicyUE0G2zY8o5U3MXtdlLfaJqTTLFqw/640?wx_fmt=other&from=appmsg)

Palo Alto Networks 发布了一份详细的威胁简报，介绍了 Ivanti 产品中的两个严重漏洞 CVE-2025-0282 和 CVE-2025-0283。这些漏洞影响 Ivanti 的 Connect Secure、Policy Secure 和 ZTA 网关设备，这些设备广泛用于实现远程网络连接。

CVE-2025-0282 是 Ivanti Connect Secure 22.7R2.5 之前版本、Policy Secure 22.7R1.2 之前版本以及 ZTA 网关 22.7R2.3 之前版本中的一个基于堆栈的缓冲区溢出漏洞。该漏洞允许未经身份验证的攻击者通过向存在漏洞的设备发送特制请求来实现远程代码执行 (RCE)。该漏洞被评为严重，CVSS 评分为 9.0。

同时，CVE-2025-0283 也是一个基于堆栈的缓冲区溢出漏洞，它使本地经过身份验证的攻击者能够在受影响的设备上提升其权限。尽管该漏洞的严重性评级为高（CVSS 评分为 7.0），但迄今为止尚未发现有人主动利用该漏洞。

多家网络安全组织记录了 CVE-2025-0282 的利用情况，包括 Mandiant、Watchtowr Labs 和 Palo Alto Networks。据观察，攻击者利用此零日漏洞渗透内部网络。Palo Alto Networks详细说明：“我们的遥测显示，2024 年 12 月下旬，一名威胁行为者可能利用了面向公众的 Ivanti Connect Secure (ICS) VPN 设备中的 CVE-2025-0282 零日预身份验证远程代码执行漏洞。”

该活动集群被追踪为CL-UNK-0979，涉及四个阶段的攻击：

1. 初始访问：攻击者通过利用暴露的 Ivanti 设备上的 CVE-2025-0282 获取进入权限。
2. 凭证收集和横向移动：名为 ldap.pl 的自定义 Perl 脚本用于收集凭证，这些凭证随后用于受害者网络内基于 RDP 的横向移动。
3. 防御逃避：日志文件被系统地删除，受感染设备上的/var/cores等目录 被清除，以阻碍法医调查。
4. 持久性：像 SPAWNSNAIL 这样的后门和自定义恶意软件工具可以建立对目标系统的持久访问权限。

攻击工具和技术

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaPe1B66JiaecZicwXgaw8TlGVIoRMCGOLdkb50eu9N3zGObYUa4BiamPZajjo0T32rkQ4foWzItgoFQ/640?wx_fmt=other&from=appmsg)

攻击中使用的 Perl 脚本 ldap.pl 的内容 | 来源：Palo Alto Networks

* 自定义 Perl 脚本：脚本ldap.pl用于从 Ivanti 设备中提取和解密凭据。
* 内存转储工具：利用 Visual Studio 的 MSBuild.exe，使用名为package.dll的工具来收集 LSASS 内存中的凭证。
* DLL 侧加载： deelevator64.dll和vixDiskLib.dll等恶意 DLL使攻击者能够将后门侧加载到系统中。

攻击者使用了多个命令和控制 (C2) 服务器，包括：

* 168.100.8[.]144
* 193.149.180[.]128

vixDiskLib.dll 和 deelevator64.dll 等文件工件与横向移动和持久性有关。

Ivanti 已发布针对这些漏洞的补丁，并建议立即更新所有受影响的系统。他们的建议强调了应用补丁的重要性，特别是对于一直是主要目标的 Connect Secure 设备。Ivanti 还鼓励使用其完整性检查工具 (ICT) 来监控可疑活动。

来源：https://securityonline.info/cl-unk-0979-exploit-zero-day-flaw-in-ivanti-connect-secure-to-gain-access-to-networks/

***END***

阅读推荐

[【安全圈】高危！rsync被爆出多个安全漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=1&sn=7e41cdf5b76e20186089903f7171a588&scene=21#wechat_redirect)

[【安全圈】国家互联网应急中心通报两起美方对我国网络攻击事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=2&sn=1eeea145994ab308cf3f78f1ca987a19&scene=21#wechat_redirect)

[【安全圈】网络安全态势研判分析报告 （2024年12月）](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=3&sn=86d02f407c0e151d308f83282274bf31&scene=21#wechat_redirect)

[【安全圈】支付宝P0级重大事故：整整5分钟所有订单打8折，官方回应：不向用户追款](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=1&sn=c8e7e9e9cc66acce28dbc15174a86f30&scene=21#wechat_redirect)

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