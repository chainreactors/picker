---
title: 【紧急预警】7-Zip假官网疯传！你下载的可能是木马！！！
url: https://mp.weixin.qq.com/s/Jyk1Wq9tHWpEBi2IrGM4Tg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:20:50.457478
---

# 【紧急预警】7-Zip假官网疯传！你下载的可能是木马！！！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zmF08GSBtAbagaM1BCdWmrfdWCljnvlf9L4HNSprKHibJkAwTNHoxuAvDiaFbA1AAsvpic6Qj7qs4n4Cl6uFbicCwDpad0SbeE7wNPbDicgsYI4k/0?wx_fmt=jpeg)

# 【紧急预警】7-Zip假官网疯传！你下载的可能是木马！！！

原创

玲珑安全
玲珑安全

玲珑安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zmF08GSBtAYmz9ibZjO5q6Tx64dLYUnZPZR8xxzazLWV09oyKicVFDDKfLib1KxKlUQu6icPQ6PgBn2aoTiaFo3obssSlMrRv8fgTVJ1icBIOUFCo/640?wx_fmt=png&from=appmsg)

近期，一场高度隐蔽的钓鱼攻击正在全网蔓延。全球知名安全厂商Malwarebytes于2026年2月9日正式发布威胁情报，一款仿冒7-Zip压缩软件的恶意安装包，正通过搜索引擎广告、YouTube装机教程、社交群组等渠道疯狂传播，让无数普通用户在毫不知情的情况下，把家用电脑变成了黑客手中的“肉鸡”。

作为装机量极高的免费开源压缩工具，7-Zip一直是用户信任的基础软件，也正因如此，它成为黑客精准攻击的目标。本次事件中，攻击者使用的域名为7zip.com，页面布局、文字介绍、下载按钮与正版官网高度一致，普通用户几乎无法通过视觉分辨。

而7-Zip官方在多次声明中强调，唯一官方地址为7-zip.org，带中间横杠，后缀为.org，从未使用过7zip.com这个域名。

![Malicious website dropping the trojanized 7-Zip](https://mmbiz.qpic.cn/mmbiz_jpg/zmF08GSBtAZo5Ma21JXkLSWUThZibaFvRwXH7uWhkTGfS6rUWee5ib2mCcQMWT8do422oh4L7Kia1P083O8XUWBLlHsomZWjO8bj7jpCWTIfxQ/640?wx_fmt=jpeg&from=appmsg)

外媒Malwarebytes官方报告：

> “The fake installer does install the legitimate 7-Zip, but alongside it, a malicious proxy module is quietly deployed.”
>
> 这个伪造的安装程序确实会安装正版7-Zip，但与此同时，一个恶意代理模块会被悄悄部署。

这正是本次攻击最狡猾的地方——捆绑正版、暗植木马。

用户安装后，解压软件可以正常使用，很难第一时间发现异常。

但在系统后台，恶意程序会自动释放文件到系统关键目录C:\Windows\SysWOW64\hero\，生成hero.exe、Uphero.exe、hero.dll等组件，以SYSTEM最高权限注册系统服务，实现开机自启，并通过netsh命令修改防火墙规则，为后台联网扫清障碍。

此外，该恶意软件还会通过WMI和Windows API收集设备硬件信息（如内存大小、CPU数量、磁盘属性和网络配置），并上报至iplogger.org，用于进一步剖析受害者环境。

外媒BleepingComputer报道：

> “The malware collects device data and communicates with a C2 server, turning infected PCs into residential proxy nodes used for credential stuffing, phishing, and fraud.”
>
> 该恶意软件会收集设备数据并与控制服务器通信，将受感染电脑变成住宅代理节点，用于撞库、网络钓鱼与欺诈活动。

简单来说，黑客并不直接偷你的文件或密码，而是借用你的家庭宽带IP，去做各种违法操作。

你的IP会被标记为恶意地址，可能导致账号封禁、网络异常，甚至面临法律关联风险。

该攻击使用Go语言编写的hero.exe作为核心代理负载，通过旋转的C2域名（如soc.hero-sms.co、neo.herosms.co等）获取配置，并在非标准端口（如1000、1002）建立出站代理连接，使用轻量级XOR编码协议（密钥0x70）进行通信。

为规避检测，它还集成虚拟机检测（针对VMware、VirtualBox等）、反调试机制、运行时API解析和进程枚举等技术。

Malwarebytes研究员表示，这是一整条黑产链条的一部分，攻击者还在用同样的手法仿冒TikTok、WhatsApp、HolaVPN、Wire VPN等热门应用，批量制作钓鱼安装包。安装包使用已吊销的Authenticode证书（来自Jozeal Network Technology Co., Limited）签名，进一步增强伪装性。

目前，微软Defender已将其识别为Trojan:Win32/Malgent!MSR，更新病毒库后可有效查杀。 Malwarebytes等专业工具也能全面检测并逆转其持久化机制。

很多受害者都是在跟着教程装机、搜索“官方下载”时中招。搜索引擎广告位、视频简介链接、论坛网盘分享，都是这类钓鱼文件的高发地带。黑客利用用户对“教程”“官方”“免费”的信任，完成低成本、高扩散的恶意投放。

多位安全研究者和媒体账号（如@Malwarebytes、@BleepingComputer）持续转发警告，强调该域名已活跃一段时间，呼吁用户立即验证来源。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zmF08GSBtAYr1Rp4opaPxmTbBVnUCzUdaLrjKtEnCj1ONZKQmqmVq3F1fTX0cHAXk0z5ANBNywk26yFm5Liao0ia1icJNUf4HOLhDA3N1a2VicQ/640?wx_fmt=png&from=appmsg)

关键指标（IOCs）参考

为帮助用户和技术人员快速识别，以下是部分已知指标（基于Malwarebytes和BleepingComputer报告）：

恶意域名：7zip.com、soc.hero-sms.co、neo.herosms.co、flux.smshero.co 等（完整列表可查Malwarebytes报告）

文件路径：C:\Windows\SysWOW64\hero\Uphero.exe、hero.exe、hero.dll

文件哈希（SHA-256）：

* Uphero.exe: e7291095de78484039fdc82106d191bf41b7469811c4e31b4228227911d25027
* hero.exe: b7a7013b951c3cea178ece3363e3dd06626b9b98ee27ebfd7c161d0bbcfbd894
* hero.dll: 3544ffefb2a38bf4faf6181aa4374f4c186d3c2a7b9b059244b65dce8d5688d9

![](https://mmbiz.qpic.cn/mmbiz_gif/5HAz5Dg8SOkjmyVTZjk9tbp3SiaRXaRbWz9K95rrjzicHcdPgfMN3MumibokNDcCrXM8HSkXyeJfY6wJPxd52uJFw/640?from=appmsg)

10秒快速自检

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZqWFntqbxCPciaouYfYKARbr4A6lYXfMp6zb2RYlTWMRxITibhicCy6ib7S6qqZlPzbWicSplPAoyqJAhWTsIjkptpw/640?from=appmsg)

1.你的7-Zip是否从7-zip.org下载？

2.查看文件夹C:\Windows\SysWOW64\hero\是否存在？

3.系统服务中是否出现Helper Service或Uphero服务？

4.杀毒是否报毒Trojan:Win32/Malgent!MSR？

满足任意一条，说明你的电脑可能已被控制。立即行动！

欢迎转发给身边常用电脑、经常下载软件的朋友，让更多人避开这波高仿钓鱼陷阱。

**培训咨询/报名二维码![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()**

**ID：linglongsec![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()![]()**

**![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1AoMVy0Knkpa9SdaxqHZUVp2Viar37MowzsqI5bpBAiarLxRqhHroxM0EsOTTmt2XKr2BGAjkZm5DZIpooF3RjdQ/640?wx_fmt=jpeg)![]()**

**报喜专栏总览**

**https://www.ifhsec.com/list.html**

**SRC漏洞挖掘培训**

**学员每一期的收获、我们每一期的进步**

*[玲珑安全第一期SRC漏洞挖掘培训](http://mp.weixin.qq.com/s?__biz=MzI4NTYwMzc5OQ==&mid=2247486139&idx=1&sn=11eb92b27684e41a86d26673ec4747f1&chksm=ebe8e803dc9f6115e18384bd62789bf5c5d1ad7de522faf92ebb52893a8cef4631a0f1459112&scene=21#wechat_redirect)*

*[玲珑安全第二期SRC漏洞挖掘培训](http://mp.weixin.qq.com/s?__biz=MzI4NTYwMzc5OQ==&mid=2247491250&idx=1&sn=0a1a522f09c42654a3eb2f314dfedffa&chksm=ebe8fc0adc9f751c60b0fa5c4c15bbc7947de1b50cbb8ecae11b51882a12612323d761e66f1a&scene=21#wechat_redirect)*

*[玲珑安全第三期SRC漏洞挖掘培训](http://mp.weixin.qq.com/s?__biz=MzI4NTYwMzc5OQ==&mid=2247493447&idx=1&sn=04e4dfd799d0f22f5adfb1a50032d221&chksm=ebeb05ffdc9c8ce9a3d2916634a4fe3480685bf599150c2e128e20faeae4d2ddd0f12f96b630&scene=21&token=1651477231&lang=zh_CN#wechat_redirect)*

*[玲珑安全第四期SRC漏洞挖掘培训](http://mp.weixin.qq.com/s?__biz=MzI4NTYwMzc5OQ==&mid=2247496609&idx=1&sn=db3ba684b8bf0f3c5991a30d1b899f29&chksm=ebeb1119dc9c980f7a598d7ae47d8060d984f2d6181e835c936b813f782dbb9d31dfdfb2c3f2&scene=21#wechat_redirect)*

*[玲珑安全第五期SRC漏洞挖掘培训](https://mp.weixin.qq.com/s?__biz=MzI4NTYwMzc5OQ==&mid=2247499310&idx=1&sn=e9665007697fbf72d31075cab2123923&scene=21#wechat_redirect)*

*[玲珑安全第六期SRC漏洞挖掘培训](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247486842&idx=1&sn=e2839892a4c331387be5a704bf28bb61&scene=21#wechat_redirect)*

[玲珑安全第七期SRC漏洞挖掘培训](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487217&idx=1&sn=42305c92cd949eaac54098830a25e9ef&scene=21#wechat_redirect)

**玲珑安全B站公开课**

免费课程观看/日常消息更新/学员赏金报喜

*https://space.bilibili.com/602205041*

**玲珑安全QQ群**

*191400300*

**往期文章直达**

关注公众号 各种优质好文速递

[吓哭了！天才黑客觉醒！Claude 4.6挖出500个高危0day](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487364&idx=1&sn=cc44c40962ac818505f649b1b82a1d4b&scene=21#wechat_redirect)

[紧急预警！CTF神器ToolsFx老版本暗藏涉黄陷阱](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487323&idx=1&sn=3d29866e13562d1d8e03aaa6ab24ef17&scene=21#wechat_redirect)

[谁在裸奔？1750万Ins用户数据泄露事件](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487314&idx=1&sn=a6e349da6ddf2796f3ab07e11c8876d7&scene=21#wechat_redirect)

[Grok助推AI“脱衣”技术走向主流](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487306&idx=1&sn=b2593a6650b6cfd37399c8ef05c93b51&scene=21#wechat_redirect)

[脆弱的锁：SAML 认证的新型绕过方式](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487298&idx=1&sn=bf20953a4367a6831a7ba2882b426ecf&scene=21#wechat_redirect)

[快手至暗一小时-当公域流量入口被劫持，平台的主权究竟掌握在谁手中？](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487290&idx=1&sn=23a9c0cf59864ae9b05568af11cb56ce&scene=21#wechat_redirect)

[离职当晚他敲下一行代码，不仅赔了600万，还把自己送进监狱](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487268&idx=1&sn=292b979a7274d8d608ada13f4499b9b9&scene=21#wechat_redirect)

[揭秘Cookie前缀保护失效的真实成因与攻击技巧](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487263&idx=1&sn=7e609baa7958a4efe32c8a6c14918a21&scene=21#wechat_redirect)

[从 Lyft 费用导出到本地/内网文件泄露的实战案例](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487258&idx=1&sn=028ed582b4247cf1490f44721566a01a&scene=21#wechat_redirect)

[CSPT 漏洞原理、利用与实战浅析](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487253&idx=1&sn=f41dc0b3a9fabff2714c6fd86ccb9226&scene=21#wechat_redirect)

[雅虎商业平台密码重置漏洞分析与利用](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487226&idx=1&sn=c23aeefbdbbbad583c10ceb7814af719&scene=21#wechat_redirect)

[利用 Python 中不安全的文件解压实现代码执行](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487116&idx=1&sn=44b6d13d27c87a4df88bd30b425f6f21&scene=21#wechat_redirect)

[Facebook 服务器上的远程代码执行](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487101&idx=1&sn=eee3fcb277c3acf137f88490aa62bfee&scene=21#wechat_redirect)

[挖掘特斯拉Model 3上价值1w美元的漏洞](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487079&idx=1&sn=0984778c1477c705ac5a212a760fff88&scene=21#wechat_redirect)

[入侵Chess.com并获取5000万客户记录](https://mp.weixin.qq.com/s?__biz=Mzg4NjY3OTQ3NA==&mid=2247487068...