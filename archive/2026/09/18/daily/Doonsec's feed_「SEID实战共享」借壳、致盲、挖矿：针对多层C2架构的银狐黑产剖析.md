---
title: 「SEID实战共享」借壳、致盲、挖矿：针对多层C2架构的银狐黑产剖析
url: https://mp.weixin.qq.com/s/OWOCPn9Sq94Oj7P4F82Y1A
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:54:32.242265
---

# 「SEID实战共享」借壳、致盲、挖矿：针对多层C2架构的银狐黑产剖析

# 「SEID实战共享」借壳、致盲、挖矿：针对多层C2架构的银狐黑产剖析

CACT
CACT

中资网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

*「本次分析的全部素材均来自 SEID 社区成员的主动提交与共享，感谢中煤集团、中国中化、哈电集团等企业提供的信息」*

近期，国资国企网络威胁信息共建共享平台（SEID） 陆续收到多家央企成员单位上报的同类可疑样本。经关联分析与逆向研判，确认这是一起自今年第二季度起持续活跃的大规模银狐远控+挖矿组合攻击。攻击者批量仿冒常见软件安装包（MSI/EXE），捆绑传播 Gh0stRAT 变种及基于 XMRig 的挖矿程序，技术层面融合了 BYOVD 致盲、WDAC 策略伪造、阿里云 OSS 投递、三层 C2 架构、无文件内存注入等高级攻防手法，驻留持久化设计极为缜密，清除难度极高。

现将本次攻击的完整剖析向公众披露，以供更广泛的国资国企安全团队参考布防。

**1**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk06iaVia2Dk2sGVJz4DyeVuiaWJ5aQZib68ap8kIpdkYW5azy1Yg7utIp5gJvym8pOvEog7SXibfFqjicZ7pf9fDLQK8AUGicVa9989jss/640?wx_fmt=png&from=appmsg)

***样本整体流程***

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk07tLNYXadIe2G2gYtqwm0dgpq15sgibvKiaNIutBXgddnia5AtcYBLNYAzCXc7zr0w8Ncf75LDKKqIPELdpeLDOAq3zBKr8ly5fR8/640?wx_fmt=png&from=appmsg)

样本整体执行流程可按功能划分为三个阶段：第一阶段（蓝色）为初始感染阶段，主要完成样本解包，并从远端服务器拉取后续阶段所需的恶意文件及EDR致盲组件；第二阶段（粉色）为致盲与驻留阶段，利用获取的致盲组件禁用EDR防护，随后解密Gh0stRAT Payload并以无文件落地的方式实现内存驻留；第三阶段（黄色）为挖矿执行阶段，启动挖矿程序开始恶意挖矿操作。详细流程见图1：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk06G09hnIUyHIzTHWkfd31LGZW50iclKLyB43rnabpdwuJUqKXHict6XCftLNcUxviarDM8ic9zFvo2mOUiceE7hw05S9lFAKLc24cCU/640?wx_fmt=png&from=appmsg)

**2**

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk06EkAAfYXRQPMarcaqtxSlWusQ2Issibwia6HKs36lZtBUtfNBicvSL6GiaoqYQniczygu9ibeTPbia0rprEn5aMDvmAs4MYYGNTzzcw8/640?wx_fmt=png&from=appmsg)

***细节分析及特征披露***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk07hicLJyZzDQS4cGrJNSMZyUcLSp1QgMduVznJYqSXvtNKp4GEalBsCgWlUjpw4EG1X1DySrPAJH1aNEPLQKjZw1j6pIJB0hrxo/640?wx_fmt=png&from=appmsg)

(一) 初始阶段

在初始感染阶段，攻击者通过仿造MSI或EXE格式的日语环境常见应用程序，如：NumLockLock、PpcNotif.Provider.RequiredApp（松下相关应用）及少部分国产大模型相关程序，如：豆包等，诱使相关应用程序使用者安装伪造的应用程序，进而实现传播Gh0stRAT及挖矿程序的目的。

(二) 感染阶段（投递&提权）

运行初始样本后，其将后续核心恶意组件释放至 C:\Users\Public\{random char} 及 C:\Windows\Temp 目录下，主要包括：具备 UAC Bypass 能力的第二阶段"白+黑"组合样本、伪装为 .jpg 图片的 TrueSight V2.0.2 内核驱动（ranchserv.jpg）以及 WDAC 策略文件（SiPolicy.p7b），为后续禁用安全工具、BYOVD 致盲及多层持久化部署做好充分准备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk06bWKyHiaETL5oiamdNbPkTaiciazAlbKk3Zdj2IfzgdibJwvPXLD4WAlYxNTXLXN1QARIicDZpBoFoZNcHSrIsFcdkLibmO2VPiaibey3I/640?wx_fmt=png&from=appmsg)

C:\Users\Public\{random char}下 “白+黑”文件启动后会进行UAC Bypass提权以获得高权限，其主要功能是写入WDAC策略，以服务的形式加载漏洞驱动，并从阿里云OSS拉取下一阶段恶意文件，写入 C:\Program Files (x86) 下。

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk04ia4bBIg3nbEnz4mfnNkkWtGrXOZrkkPEFOumjibm0uia8R0nBr9Ba4X7uwicianRmwXJ6Xr40oeldoibpsYelNyRyXpGF0pIYB6vPY/640?wx_fmt=png&from=appmsg)

其中ranchserv.jpg是非常经典的TrueSight V2.0.2 内核驱动，成功加载后可向攻击者提供内核层面的进程终止、文件读写、注册表清除及APC注入等能力，进而实现杀软及EDR等安全工具的致盲。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk04sNNfBt7FRtMH8YXkYiar206IM6vVUsnUsZp1ffE1SpA1UEkTJSWTk1uI0Ijy77EpPWKaYFbFMl07Xh9ZMLyHxIb8gDSMrY0DQ/640?wx_fmt=png&from=appmsg)

从OSS下载的文件（IgGQrZ.exe）依旧采用“白+黑”的手法，其主要功能是解密payload（Gh0stRAT）并注入内存回连攻击者C2，同时从阿里云 OSS 下载下一阶段恶意程序，写入 C:\ProgramData\{random char}，并通过注册表建立持久化。在致盲层面其通cmd.exe 执行系统致盲命令（禁用 Defender/Windows Update、删除卷影副本、修改host文件）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk06Ogp9Ot4c6eEm7oib34SzLEbGV9Wc43koueVn174Csxiciag6lDnTBxxrTtCMrlUHxhJHPHW6FibxiaSMIhAqUTGsmsd09T8iaCJuLY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk07KWoODZXvhFyKLBe8ygLYfhF3awpa2BnYsJyiaYSlyJ8aQFB646SOFUh0OMpTTBbnEXw6b4CiaE56iabtjODTAAlRpc4wEryjJdw/640?wx_fmt=png&from=appmsg)

wrf0fpGa.exe是一个基于TrueUpdate的挖矿安装程序，其会伪装成xshell安装程序，实际向远端OSS请求名为“page-404.png”的文件并将其落地于C:\ProgramData\{random char}，此外攻击者还会通过计划任务实现新落地文件的持久化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk07nNGlvk4EqcHrFwG9Jk4SjEqPlNo1CeArGQ92T8Xqyib4FgO3FkBYY8iaeny1HYTxuwwic3kM48Mc5LJCkmma1SibRGibJkBeg64no/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk05653Jo5YxcZvLwY2Lfc9yn2IaZkX13EzjDlzMh3RQQMB0gmoQq20HGEQIhZC6MO9QgAwKwrvuLibGy1m9ESvYrx7Tr5xdpERGU/640?wx_fmt=png&from=appmsg)

(三) 挖矿阶段

落地挖矿木马以变形 UPX 壳保护，脱壳重建后确认是基于 XMRig 框架的 RandomX 多币种挖矿程序，由命令行参数 1776 触发激活；其通信采用“固定密钥流 XOR 混淆（512 字节硬编码表循环）→ Base64 → TLS”三层封装连接矿池，以规避流量监测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1WldmtZwk05HW21WxYYt7Dxicje60VW68wAPqzJ8n2AicPZOiaYzt5feNEoiaaNMO0IKABicDg9FiatmfGnVTUfnazrXiawPTboCn14QpNXoaKTZME/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk06Y1AdaI16lbwSfyt6qHU1GRjTy43Ffk9zCYHS7JzjuS21ldVSK3ZCic54HeNCUrXQhZjqOuy0blkXBicQyCKDBLI6v7ib6vc8zIE/640?wx_fmt=png&from=appmsg)

**3**

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk04c3hxf3jPlicbWOzqGVdXsz0qMYTibcBicveg8boxdFNe2ZJoqlItqQp1LnyUY2mWRlStMTknReubQvmOgTr2WSficmw0vBYSYym8/640?wx_fmt=png&from=appmsg)

***部分样本 IOC和 HASH***

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk06345ib0uLs2Rsu2w4WpD9sGUZenZBOOibNkgd6twsSHYNPwmyX53RcxmvQwN79CRbCILRhE5dNKCctcrEso7a1dBC3ic31yAzXNc/640?wx_fmt=png&from=appmsg)

(一) C2基础设施：

1. gqsqoq.net

2. jnkous.net

3. lisyrf.net

4. wfmwsj.net

5. vqxvll.net

6. ufozdv.net

(二) 样本HASH：

1.2e90e3aaa76f9bd0a5b9bfc83f92bdb51a1c42b9121d3f204fbcbf2b724a0f88

2.418102029f37211691325f75980476277c2ca3d66363f6ad4bc022e660ffd72f

3.f22ca2ecd01573012ff6a187b484f68b13bef285a590ae3c5f93a2c6a83a2f3c

4.b655766fc801ed8a07db3447bf6a8ab1ae12507eab3ebd560e662b2a804e2989

5.7b7ee0af580497220c90a5db42c5202a70c0c16007515bb7fde9d3ad6e341f7b

6.a72083135eaae2b4af0b30db51b46a03d44869d60a41f55cb2cf5f33fa992503

7.fafefa1bf9ffa5342341b92ee398499149958000bb3508a14e3458841b3e8f5c

**4**

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk05quNG7V5JYXKKzpcNbC8FKIMfwDjZz1v3RAyc9LeMc0RP7swboHC10WLcDYsfgGtCdNjECmy2hgnFVFyQltT5C9Gribf071UHE/640?wx_fmt=png&from=appmsg)

***加入SEID社区***

![](https://mmbiz.qpic.cn/mmbiz_png/1WldmtZwk04WtOw5MxxvANibyVQEsrU9XEXQv6dN52BV3qP8sDHPEIaHhQRyEN7N8q6W1cPjkKmmTyxhp8XtGicx1cjWrrpWhVYicw9dVWOzIs/640?wx_fmt=png&from=appmsg)

(一) 简介

SEID是国资国企专属的国家级威胁情报共享实战平台，由国资国企在线监管安全运营中心倾力打造，集情报研判、样本分析、漏洞排查三大核心体系于一体，实时共享国资国企专属网络威胁信息，为国资国企网络安全运营工作保驾护航！

(二) 优势

SEID平台通过SD-WAN实现安全数据交互，集成沙箱设备为国资央企提供可疑样本上传和分析服务、为国资国企威胁情报共享和联防联控提供统一平台。集于国资国企在线监管安全运营中心5年积累的海量安全大数据、安全运营垂域大模型，它拥有：

最权威的国资央企威胁情报数据库：全面收集、高效整合国资央企情报资源和能力，实时汇聚来源于国资央企一线的实战威胁情报，通过国资国企网络信息安全在线监管平台验证，确保威胁情报的高鲜活性和高准确性。

高可信运营平台：通过国资国企白名单准入机制构建高可信生态，严格限定参与主体为国资国企成员，并实施文件隔离保护策略，确保共享环境安全可控。

(三) 使用注册

1.申请账号。发送邮件至service@cacts.cn，注明企业、人员、联系方式，将由专人对接跟进

2.登录平台。使用专属账号，登录SEID

3.提交信息。按照平台规范，提交网络威胁信息

4.核验计分。内容审核完成后，自动核算积分

![](https://mmbiz.qpic.cn/mmbiz_jpg/hJhLqhjYliaDueicqNHNdVjvKyKGwic9csic6RBryLvSOHLqOPz0E3J4HUKrvYGOR69ic2ECM3APB0aphOz1LhAU4ag/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hJhLqhjYliaC66tRiavPSrHJrIbk5WgeEvOHU57OHanbq6ARpicYWV3bVRy0SaQ0GUwCWp0roP4ZDMeIrkPic2N6mA/0?wx_fmt=png)

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