---
title: 网安原创文章推荐【2026/5/3】
url: https://mp.weixin.qq.com/s/zDm6Pas4gW10k9nVUHimcw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:56:28.848989
---

# 网安原创文章推荐【2026/5/3】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJADSFr5IPqLGW13XNFZCouS4e4CsuIXQZ32b1sTKTasXlwvKTloEoVT4tZed0APXYJmHhHR6YQNlEN0IeLrsevoAcyFcs9wIibT0/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/5/3】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-05-03 微信公众号精选安全技术文章总览

> 洞见网安 2026-05-03

---

### 0x1 [Shiro 550 RememberMe 反序列化漏洞](https://mp.weixin.qq.com/s?__biz=MzY4MTAzNzk5NQ==&mid=2247485359&idx=1&sn=507729f961872ab2e999aef46d65e20e&scene=21#wechat_redirect "Shiro 550 RememberMe 反序列化漏洞")

> 成渝Sec 2026-05-03 12:33:44

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIDTblJYD4ATLDibxISicLjeibicPUbRtn0EDMicvcGYINssVwNlRoHibNCjI1fRNzeZKbgSGFdRwpSY0sy2Rz8aUiczAmK8NX8ubpCxp8/640?wx_fmt=jpeg)

本文详细分析了Shiro框架中的550 RememberMe反序列化漏洞。该漏洞是由于Shiro框架在使用默认密钥对不安全的Java反序列化数据进行加解密时，攻击者可以伪造恶意rememberMe字段，从而触发任意命令执行。文章首先介绍了Shiro框架的基本功能和RememberMe功能的实现原理，接着阐述了Shiro-550和Shiro-721两个漏洞的区别，主要在于密钥的管理方式不同。Shiro-550的密钥是硬编码在代码中，易于攻击者爆破，而Shiro-721的密钥是随机生成的，利用难度更高。文章还详细描述了Shiro 550反序列化漏洞的攻击原理、攻击流程和核心关键点，并提供了漏洞复现的步骤和利用工具。最后，文章总结了漏洞的根本原因和防范措施，提醒用户注意修改默认密钥和加强代码的安全性。

Java安全漏洞

反序列化漏洞

Shiro框架

身份验证

加密

会话管理

漏洞利用

安全框架

---

### 0x2 [Linux 内核史诗级本地提权漏洞 全网深度复现、原理完整分析( CVE-2026-31431)](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247498786&idx=2&sn=a403933b0d29861cecaf29c74156925b&scene=21#wechat_redirect "Linux 内核史诗级本地提权漏洞 全网深度复现、原理完整分析( CVE-2026-31431)")

> 渗透安全HackTwo 2026-05-03 10:45:19

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibrevicNauKAUMdWxM9DCDMFE46EQydCx4vvEAjevmxk1O99jWAQjaE1ZRReWdjMb1Cn7VBj6UEIpkCOq1nw0QBGN70caXuVroLXk2WjJESQY/640?wx_fmt=jpeg)

本文详细分析了Linux内核史诗级本地提权漏洞CVE-2026-31431，该漏洞被命名为"Copy Fail"，由韩国安全研究团队Theori在2026年4月29日公开披露。该漏洞源于2017年引入的一个原地优化，导致所有基于该版本构建的内核均受影响。漏洞利用门槛极低，只需一个本地普通用户账号和732字节的Python脚本即可实现提权。该漏洞允许攻击者在共享内核的云环境、K8s集群、CI/CD流水线中突破隔离，获取宿主机root权限。文章深入分析了漏洞的原理，包括内核子系统的交汇点、AEAD算法模板的优化以及攻击数据流。受影响的内核版本和发行版也被列出，同时提供了漏洞复现的步骤和修复建议。

Linux内核安全

本地提权漏洞

内存破坏漏洞

AI辅助代码审计

云安全

容器安全

漏洞复现

安全补丁

漏洞利用

---

### 0x3 [JAVA框架与组件 FastJSON 漏洞分析](https://mp.weixin.qq.com/s?__biz=MzY4MTAzNzk5NQ==&mid=2247485315&idx=1&sn=cb45472eba57f0fd95dea814a5fe1f57&scene=21#wechat_redirect "JAVA框架与组件 FastJSON 漏洞分析")

> 成渝Sec 2026-05-03 10:30:52

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIDjZ5FchXRx6bej4XyjWpPg4IH3GaiaRlDcS9icZhtPxgzmItEJyoYtWSUALeHTmZpfYiaOCz0jOqtcGoczbr1ribVV0obvwGeNhmw/640?wx_fmt=jpeg)

Fastjson是一个由阿里巴巴开发的Java语言编写的开源JSON库，主要用于将Java对象转换为JSON字符串，以及将JSON字符串转换回Java对象。Fastjson的一个特色功能是AutoType，它能够在反序列化时指定类型，从而方便后续的开发操作。然而，AutoType功能也存在安全漏洞，攻击者可以利用该功能执行恶意代码。Fastjson漏洞的利用原理主要是通过AutoType功能，当Fastjson解析JSON时，遇到@type会尝试实例化指定的类。攻击者可以构造特定的payload，利用AutoType功能加载并执行远程恶意类，实现远程代码执行（RCE）。Fastjson漏洞的发现可以通过DNSLog外带记录，如果Fastjson有DNSLog外带记录，就证明了目标存在Fastjson漏洞。Fastjson漏洞的利用步骤包括拦截用户请求，修改请求体，插入{"@type":"恶意类",...}，发送后，若服务端触发DNSLog或执行了命令，则证明存在漏洞。攻击者可以通过抓包篡改业务中存储的JSON字符串，插入@type指定反序列化类，比如JdbcRowSetImpl连接恶意RMI服务，或使用InetAddress进行DNSLog探测。如果后端使用存在漏洞的Fastjson版本解析，就会加载远程类并执行恶意代码，最终造成服务器沦陷。Fastjson漏洞的核心在于其AutoType功能，攻击面的核心在于如果后端在解析这些数据时没有对@type字段进行过滤，攻击者就可以通过抓包改包，在JSON数据中插入恶意的@type指向反序列化利用链。

---

### 0x4 [Windows XML事件日志（EVTX）解析](https://mp.weixin.qq.com/s?__biz=MzIwMjUyNDM0OA==&mid=2247486272&idx=1&sn=f761c9980f0e3596aaaab20cd6feb427&scene=21#wechat_redirect "Windows XML事件日志（EVTX）解析")

> ListSec 2026-05-03 10:08:32

![](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDymY09avDFrXTRoKlalEnx1FH1h60W22KQZjz34n2MwpfGe8VibOibU1wbw7j6iaX8Q5RypGSpIrM3Z1624KErbVaUKO0mW18UZ7ZU/640?wx_fmt=jpeg)

本文详细介绍了Windows系统下的XML事件日志（EVTX）的解析方法。首先介绍了EVTX日志的存放位置和主要类型，如应用程序、安全、系统日志等。接着讲解了如何使用Windows自带的事件查看器查看日志，并通过示例展示了如何查看特定事件ID的日志内容。文章进一步介绍了使用evtx\_dump工具解析EVTX日志，包括如何将日志转换为XML或JSON格式，以及如何使用fd工具配合evtx\_dump进行批量处理。此外，还介绍了EvtxECmd工具的使用方法，包括如何将其输出内容至JSON文件，以及如何使用jq工具提取特定字段。最后，文章还提到了如何使用EvtxECmd和jq工具提取日志中的EventID和相关描述。

Windows系统安全

日志分析

事件响应

安全审计

工具使用

JSON格式处理

---

### 0x5 [linux史诗级安全漏洞copyfail cve-2026-31431，及修复方案](https://mp.weixin.qq.com/s?__biz=MzAxNjY1NjU5Mw==&mid=2247497621&idx=1&sn=54729bca4526aad8823ec727f2f7823b&scene=21#wechat_redirect "linux史诗级安全漏洞copyfail cve-2026-31431，及修复方案")

> 运维星火燎原 2026-05-03 00:01:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6ynCILojBKoMzHzXY6U0QkLXOkFia7ibYsaUL1yrL6RTAQvZ3P03ljOdqkSs8eU42aeXKIjCYTzBBdnbQAberA2P3QaRic5RacaCuk3jYpicLms/640?wx_fmt=jpeg)

本文详细介绍了Linux史诗级安全漏洞CopyFail（CVE-2026-31431）的漏洞核心、原理、影响范围以及修复方案。CopyFail漏洞允许普通用户通过篡改只读系统文件页缓存，实现本地提权至root用户。该漏洞由于2017年内核优化引入，影响了所有4.14及以上版本的Linux内核，包括Ubuntu、RHEL、CentOS等多个主流发行版。文章解释了漏洞的触发原理，指出攻击者可以通过特定的系统调用和加密接口篡改关键程序，实现提权。同时，文章提供了官方补丁的升级命令和临时缓解措施，包括禁用相关模块和配置seccomp策略。此外，还提供了容器逃逸的风险提示和自查命令，以及一键自查和加固脚本，帮助用户检测和修复该漏洞。

Linux安全漏洞

内核漏洞

提权攻击

容器安全

安全修复

安全风险

安全自查

---

> 本站文章为人工采集，目的是为了方便更好的提供免费聚合服务，如有侵权请告知。具体请在留言告知，我们将清除对此公众号的监控，并清空相关文章。所有内容，均摘自于互联网，不得以任何方式将其用于商业目的。由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，本站以及文章作者不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

洞见网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

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