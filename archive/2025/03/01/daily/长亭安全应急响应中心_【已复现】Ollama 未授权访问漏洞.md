---
title: 【已复现】Ollama 未授权访问漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIwMDk1MjMyMg==&mid=2247492715&idx=1&sn=d7bae998bce7c8a9f1c6db0d49b80710&chksm=96f7fb06a1807210413176f7d16cd222ef6f5822c05c0e4303601397e050deb411274caac59c&scene=58&subscene=0#rd
source: 长亭安全应急响应中心
date: 2025-03-01
fetch_date: 2025-10-06T21:59:00.946672
---

# 【已复现】Ollama 未授权访问漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicTtnorMTPLgxiayQWhmFNFLju7qjSmS1Qs8PfbCFM1VVibMIObgUbfv7m25c8SeBREFxkwzQf2qVDvw/0?wx_fmt=jpeg)

# 【已复现】Ollama 未授权访问漏洞

长亭安全应急响应中心

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FOh11C4BDicTtnorMTPLgxiayQWhmFNFLjJ6f5zbrKoibpUJrl39cq6IpTt3KPRpucfUsVmbyYWoKS3iaPOPAlXVdw/640?wx_fmt=jpeg&from=appmsg)

Ollama 是一个开源的大语言模型（LLM）运行环境和工具集，旨在帮助开发者轻松部署、管理和使用模型（如 DeepSeek 等）。

近期互联网披露，如果 Ollama 直接暴露服务端口（默认为 11434）于公网，并且未启用身份认证机制，远程攻击者可以在未授权的情况下访问其高危接口。建议受影响的用户尽快修改相关配置或部署安全策略，以收敛安全风险。

#

**漏洞描述**

Description

**0****1**

**漏洞成因**

Ollama 默认部署时监听于 127.0.0.1，仅允许本地访问，从而在初始配置下保证了较高的安全性。然而部分用户为了方便从公网访问，会将监听地址修改为 0.0.0.0。

在这种修改之后，如果未额外配置身份认证或访问控制机制，Ollama 的管理接口就会暴露于公网，导致攻击者只需访问服务端口（默认 11434）即可调用敏感功能接口，进而读取、下载或删除私有模型文件，或滥用模型推理资源等。

此外，老版本 Ollama 的部分实现在处理用户提供的数据时缺乏严格校验，进一步加剧了漏洞影响。例如 Ollama 0.1.34 版本之前的 /api/pull 接口存在路径遍历漏洞（CVE-2024-37032），攻击者可利用特制请求覆盖服务器文件并进而执行任意代码。在缺乏认证的前提下，这类漏洞更加容易被远程利用。

## **漏洞影响**

机密数据泄露：攻击者可以未经授权下载服务器上的私有模型或敏感数据，将其窃取并外传。例如通过调用 /api/push 等接口，攻击者可以将服务器上的所有模型导出到其控制的远程服务器，从而导致核心模型资产泄露。

资源滥用与拒绝服务：由于无需认证，攻击者可以反复调用模型推理或模型拉取等接口，恶意耗用计算、存储和带宽资源。例如不断发送模型下载请求会占满磁盘空间，最终导致服务不可用（拒绝服务）。这不仅影响业务正常运行，还可能产生高额的资源消耗成本。

系统配置篡改与扩大利用：未授权接口的访问还可能被用来修改服务器的配置参数或状态。更严重的是，攻击者或可结合其他漏洞实现对服务器的进一步控制（如远程代码执行）。一旦攻击者取得对服务器的更高权限，可能导致更广泛的系统入侵和破坏。

**处置优先级：高**

**漏洞类型：**未授权访问

**漏洞危害等级：**高

**触发方式：**网络远程

**权限认证要求：**无需权限（Pre-Auth）

**系统配置要求：**需修改默认配置对公网开放

**用户交互要求：**无需用户交互

**利用成熟度：**已出现在野攻击

**修复复杂度：**低，只需调整配置或部署安全策略

**影响版本**

Affects

**02**

```
所有版本的 Ollama（在未配置认证且直接暴露公网的情况下）均受此问题影响。

注：部分相关漏洞（如前述可导致文件覆盖的漏洞）在新版 Ollama 中已获修复。官方已在 0.1.34 及之后的版本中修补了一些严重漏洞，建议用户尽快升级到新版本避免受到历史漏洞的影响。
```

**解决方案**

Solution

**03**

##

1. 限制公网访问：尽量避免直接将 Ollama 服务端口（默认 11434）暴露在公网。如无特殊需求，建议仅允许内网或通过 VPN 访问 Ollama 服务，从网络层面减少攻击面。

2. 配置网络访问控制：通过云安全组、防火墙等手段限制对 Ollama 服务端口的访问来源。仅允许可信的源 IP 地址连接 11434 端口，阻止非授权 IP 的访问请求。

3. 启用身份认证保护：如果业务需要开放 Ollama 接口供公网访问，务必为其添加认证机制。由于 Ollama 本身暂不支持开箱即用的认证，可通过反向代理实现保护。例如，使用 Nginx 做前置代理，并在代理处启用 HTTP Basic Authentication 或基于 OAuth 的认证。配置示例（需预先生成 .htpasswd 用户密码文件）：

```
location / {    proxy_pass http://localhost:11434;    auth_basic "Ollama Admin";    auth_basic_user_file /etc/nginx/conf.d/ollama.htpasswd;}
```

上述配置将所有对 Ollama 的请求转发前强制要求 Basic Auth 验证。使用其他代理服务器（如 Caddy、Apache）或接入 API Gateway 等也可以达到类似的安全加固效果。

**漏洞复现**

Reproduction

**04**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicTtnorMTPLgxiayQWhmFNFLjMiaOSNe9rYJYpVBCNrChxuZgAdoAZHGkrM9cgnybcgsnictZOwZOYL2Q/640?wx_fmt=png&from=appmsg)

**产品支持**

Support

**05**

**云图：**默认支持该产品的指纹识别，同时支持该漏洞的PoC原理检测。

**洞鉴：**预计3月7日前发布更新支持该漏洞检测。

**时间线**

Timeline

**06**

2月27日 长亭应急响应实验室复现漏洞

2月28日 长亭安全应急响应中心发布通告

**长亭应急响应服务**

全力进行产品升级

及时将风险提示预案发送给客户

检测业务是否受到此次漏洞影响

请联系长亭应急服务团队

7\*24小时，守护您的安全

第一时间找到我们：

邮箱：support@chaitin.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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